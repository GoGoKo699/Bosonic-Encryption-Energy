#!/usr/bin/env python3
"""Finite, reproducible checks for the analytic results in ../science/.

Inputs to the loss channel have exact finite support, so its finite Kraus
calculation has no output-truncation error. No amplifier is simulated.
These checks do not constitute proofs or optimize over all input states.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np


SEED = 9231
TOL = 2e-11


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def trace_distance(left, right):
    difference = left - right
    hermitian = (difference + difference.conj().T) / 2
    return float(np.abs(np.linalg.eigvalsh(hermitian)).sum() / 2)


def projector(vector):
    return np.outer(vector, vector.conj())


def reference_marginal(rho, d, r):
    return np.trace(rho.reshape(d, r, d, r), axis1=0, axis2=2)


def mean_energy(rho, d, r):
    return float(np.dot(np.repeat(np.arange(d), r), rho.diagonal().real))


def pure_loss_kraus(d, eta):
    operators = []
    for lost in range(d):
        operator = np.zeros((d, d), complex)
        for n in range(lost, d):
            operator[n - lost, n] = math.sqrt(
                math.comb(n, lost) * (1 - eta) ** lost * eta ** (n - lost)
            )
        operators.append(operator)
    return operators


def apply_loss(rho, operators, d, r):
    """Apply each sparse Kraus operator on A, preserving both R indices."""
    tensor = rho.reshape(d, r, d, r)
    output = np.zeros_like(tensor)
    for lost, operator in enumerate(operators):
        amplitude = operator[np.arange(d - lost), np.arange(lost, d)]
        output[: d - lost, :, : d - lost, :] += (
            amplitude[:, None, None, None]
            * tensor[lost:, :, lost:, :]
            * amplitude[None, None, :, None]
        )
    return output.reshape(d * r, d * r)


def apply_loss_dense(rho, operators, r):
    """Separate dense implementation, used to check the sparse action."""
    output = np.zeros_like(rho)
    for operator in operators:
        joint = np.kron(operator, np.eye(r))
        output += joint @ rho @ joint.conj().T
    return output


def phase_average(rho, phases, probabilities, d, r):
    output = np.zeros_like(rho)
    for phase, probability in zip(phases, probabilities):
        diagonal = np.repeat(np.exp(1j * phase * np.arange(d)), r)
        output += probability * diagonal[:, None] * rho * diagonal.conj()[None, :]
    return output


def loss_inputs(rng, d, r):
    cases = []
    for name, n in [("vacuum", 0), ("highest-supported-number", d - 1)]:
        vector = np.zeros(d * r, complex)
        vector[n * r] = 1
        cases.append((name, projector(vector)))
    for n in [1, 2, 3, 8, 15]:
        for weight in [1e-6, 0.05, 0.5]:
            for entangled in [False, True]:
                vector = np.zeros(d * r, complex)
                vector[0] = math.sqrt(1 - weight)
                vector[n * r + int(entangled)] = math.sqrt(weight)
                label = f"vacuum-{n}; weight={weight}; entangled={entangled}"
                cases.append((label, projector(vector)))
    random_states = []
    for index in range(12):
        vector = rng.normal(size=d * r) + 1j * rng.normal(size=d * r)
        vector *= np.repeat(np.exp(-np.arange(d) / (1 + index / 3)), r)
        vector /= np.linalg.norm(vector)
        random_states.append(projector(vector))
        cases.append((f"random-purification-{index}", random_states[-1]))
    for index in range(4):
        mixed = sum(
            weight * random_states[3 * index + offset]
            for offset, weight in enumerate([0.2, 0.3, 0.5])
        )
        cases.append((f"mixed-joint-state-{index}", mixed))
    return cases


def check_loss_and_phase(rng):
    d, r = 16, 3
    etas = [0.001, 0.01, 0.1, 0.5, 0.9]
    laws = [
        ("no-phase", [0], [1], False),
        ("antipodal", [0, np.pi], [0.5, 0.5], True),
        ("three-equispaced", [0, 2 * np.pi / 3, 4 * np.pi / 3], [1 / 3] * 3, True),
        ("five-point-zero-m1", [0, 2 * np.pi / 3, 4 * np.pi / 3, np.pi / 2, 3 * np.pi / 2], [0.2] * 5, True),
    ]
    binary_parameters = [
        ("biased-0.55", 0.55, 0),
        ("biased-0.8", 0.8, 0),
        ("angle-error-0.02", 0.5, 0.02),
        ("angle-error-0.4", 0.5, 0.4),
        ("combined-error", 0.63, -0.23),
    ]
    for name, probability, angle in binary_parameters:
        laws.append((name, [0, np.pi + angle], [probability, 1 - probability], False))

    binary_identity_error = 0.0
    for _, probability, angle in binary_parameters:
        moment = probability + (1 - probability) * np.exp(1j * (np.pi + angle))
        expected = (2 * probability - 1) ** 2 + 4 * probability * (1 - probability) * math.sin(angle / 2) ** 2
        binary_identity_error = max(binary_identity_error, abs(abs(moment) ** 2 - expected))
    require(binary_identity_error < TOL, "P3 binary first-moment identity")

    operators_by_eta = {eta: pure_loss_kraus(d, eta) for eta in etas}
    completeness_error = max(
        float(np.max(np.abs(sum(k.conj().T @ k for k in operators) - np.eye(d))))
        for operators in operators_by_eta.values()
    )
    require(completeness_error < TOL, "loss Kraus completeness")

    cases = loss_inputs(rng, d, r)
    max_trace_error = max_reference_error = max_energy_error = 0.0
    max_dense_error = max_bound_excess = 0.0
    dense_comparisons = 0
    law_reports = []
    for law_name, phases, probabilities, zero_moment in laws:
        require(abs(sum(probabilities) - 1) < TOL, "phase probabilities normalize")
        moment = sum(p * np.exp(1j * theta) for p, theta in zip(probabilities, phases))
        if zero_moment:
            require(abs(moment) < 2e-15, f"{law_name} has zero first moment")
        moment_magnitude = 0.0 if zero_moment else abs(moment)
        max_ratio = 0.0
        worst = None
        nontrivial_bounds = 0
        for case_index, (name, rho) in enumerate(cases):
            energy = mean_energy(rho, d, r)
            reference = reference_marginal(rho, d, r)
            ideal = np.zeros_like(rho)
            ideal[:r, :r] = reference
            averaged = phase_average(rho, phases, probabilities, d, r)
            for eta in etas:
                operators = operators_by_eta[eta]
                output = apply_loss(averaged, operators, d, r)
                if case_index in [0, 17, len(cases) - 1] and law_name in ["antipodal", "combined-error"]:
                    dense = apply_loss_dense(averaged, operators, r)
                    max_dense_error = max(max_dense_error, float(np.max(np.abs(output - dense))))
                    dense_comparisons += 1
                actual = trace_distance(output, ideal)
                raw_bound = eta * energy + moment_magnitude * math.sqrt(eta * energy)
                raw_bound += eta * math.sqrt(energy * (energy + 1) / (2 * (1 - eta)))
                bound = min(1.0, raw_bound)
                nontrivial_bounds += int(raw_bound < 1)
                require(actual <= bound + TOL, f"loss/P3 bound: {name}, {law_name}, eta={eta}")
                max_bound_excess = max(max_bound_excess, actual - bound)
                if raw_bound > 0 and actual / raw_bound > max_ratio:
                    max_ratio = actual / raw_bound
                    worst = {"input": name, "eta": eta, "energy": energy, "distance": actual, "uncapped_bound": raw_bound}
                max_trace_error = max(max_trace_error, abs(complex(np.trace(output)) - 1))
                max_reference_error = max(max_reference_error, float(np.max(np.abs(reference_marginal(output, d, r) - reference))))
                max_energy_error = max(max_energy_error, abs(mean_energy(output, d, r) - eta * energy))
        law_reports.append({"name": law_name, "abs_m1": float(abs(moment)), "zero_m1": zero_moment,
                            "cases": len(cases) * len(etas), "uncapped_bound_below_one_cases": nontrivial_bounds,
                            "max_distance_to_uncapped_bound_ratio": max_ratio, "worst_ratio_case": worst})
    require(max(max_trace_error, max_reference_error, max_energy_error, max_dense_error) < TOL, "loss structural identities")
    return {"status": "passed", "input_support_levels": d, "reference_dimension": r,
            "input_states": len(cases), "phase_laws": len(laws), "transmissivities": etas,
            "bound_cases": len(cases) * len(laws) * len(etas), "dense_cross_checks": dense_comparisons,
            "kraus_completeness_max_abs_error": completeness_error, "dense_action_max_abs_error": max_dense_error,
            "trace_max_abs_error": max_trace_error, "reference_max_abs_error": max_reference_error,
            "output_energy_max_abs_error": max_energy_error, "max_bound_excess": max_bound_excess,
            "binary_moment_identity_max_abs_error": binary_identity_error, "laws": law_reports}


def cutoff_inputs(rng, d, dimension, r):
    cases = []
    vector = np.zeros(dimension * r, complex)
    vector[0] = 1
    cases.append(("vacuum", projector(vector)))
    vector = np.zeros(dimension * r, complex)
    for n in range(d):
        vector[n * r + n] = 1 / math.sqrt(d)
    cases.append(("low-block-maximally-entangled", projector(vector)))
    vector = np.zeros(dimension * r, complex)
    vector[(dimension - 1) * r] = 1
    cases.append(("tail-number-state", projector(vector)))
    for weight in [1e-4, 0.25, 0.9]:
        for entangled in [False, True]:
            vector = np.zeros(dimension * r, complex)
            vector[0] = math.sqrt(1 - weight)
            vector[(dimension - 1) * r + (d if entangled else 0)] = math.sqrt(weight)
            cases.append((f"low-high; weight={weight}; entangled={entangled}", projector(vector)))
    for index in range(2):
        vector = rng.normal(size=dimension * r) + 1j * rng.normal(size=dimension * r)
        vector /= np.linalg.norm(vector)
        cases.append((f"random-joint-{index}", projector(vector)))
    cases.append(("mixed-joint", 0.4 * cases[1][1] + 0.6 * cases[-1][1]))
    return cases


def cutoff_unitaries(d, dimension):
    shift = np.roll(np.eye(d, dtype=complex), 1, axis=0)
    clock = np.diag(np.exp(2j * np.pi * np.arange(d) / d))
    unitaries = []
    for a in range(d):
        for b in range(d):
            weyl = np.linalg.matrix_power(shift, a) @ np.linalg.matrix_power(clock, b)
            for sign in [-1, 1]:
                unitary = sign * np.eye(dimension, dtype=complex)
                unitary[:d, :d] = weyl
                unitaries.append(unitary)
    return unitaries


def check_cutoff_cipher(rng):
    reports = []
    inverse_checks = bound_attainment_checks = 0
    max_unitarity_error = max_inverse_error = max_channel_error = 0.0
    max_distance_error = max_energy_error = max_reference_error = 0.0
    for d in [2, 3, 4]:
        dimension, r = d + 3, d + 1
        unitaries = cutoff_unitaries(d, dimension)
        joint_unitaries = [np.kron(unitary, np.eye(r)) for unitary in unitaries]
        for unitary in unitaries:
            max_unitarity_error = max(max_unitarity_error, float(np.max(np.abs(unitary.conj().T @ unitary - np.eye(dimension)))))
        cases = cutoff_inputs(rng, d, dimension, r)
        low_projector = np.diag(np.r_[np.ones(d), np.zeros(dimension - d)])
        replacer = low_projector / d
        for name, rho in cases:
            average = np.zeros_like(rho)
            for joint in joint_unitaries:
                encrypted = joint @ rho @ joint.conj().T
                recovered = joint.conj().T @ encrypted @ joint
                max_inverse_error = max(max_inverse_error, float(np.max(np.abs(recovered - rho))))
                inverse_checks += 1
                average += encrypted / len(joint_unitaries)
            reference = reference_marginal(rho, dimension, r)
            low = np.zeros_like(rho)
            low[: d * r, : d * r] = rho[: d * r, : d * r]
            high = np.zeros_like(rho)
            high[d * r :, d * r :] = rho[d * r :, d * r :]
            analytic = np.kron(replacer, reference_marginal(low, dimension, r)) + high
            tail_weight = float(np.trace(high).real)
            expected_energy = (d - 1) * (1 - tail_weight) / 2 + mean_energy(high, dimension, r)
            distance = trace_distance(average, np.kron(replacer, reference))
            max_channel_error = max(max_channel_error, float(np.max(np.abs(average - analytic))))
            max_distance_error = max(max_distance_error, abs(distance - tail_weight))
            max_energy_error = max(max_energy_error, abs(mean_energy(average, dimension, r) - expected_energy))
            max_reference_error = max(max_reference_error, float(np.max(np.abs(reference_marginal(average, dimension, r) - reference))))
            if name == "vacuum":
                require(abs(mean_energy(average, dimension, r) - (d - 1) / 2) < TOL, "C1 vacuum energy")
        for energy_budget in [1e-4, d / 5, float(d), 2.0 * d]:
            q = min(1.0, energy_budget / d)
            vector = np.zeros(dimension * r, complex)
            vector[0] = math.sqrt(1 - q)
            vector[d * r + d] = math.sqrt(q)
            rho = projector(vector)
            average = sum(joint @ rho @ joint.conj().T for joint in joint_unitaries) / len(joint_unitaries)
            distance = trace_distance(average, np.kron(replacer, reference_marginal(rho, dimension, r)))
            require(mean_energy(rho, dimension, r) <= energy_budget + TOL, "C1 attaining input energy")
            require(abs(distance - q) < TOL, "C1 fixed-replacer error attainment")
            bound_attainment_checks += 1
        reports.append({"cutoff_d": d, "physical_support_levels": dimension, "reference_dimension": r,
                        "keys": len(unitaries), "joint_input_states": len(cases)})
    errors = [max_unitarity_error, max_inverse_error, max_channel_error, max_distance_error, max_energy_error, max_reference_error]
    require(max(errors) < TOL, "C1 identities")
    return {"status": "passed", "dimensions": reports, "averaged_channel_cases": sum(row["joint_input_states"] for row in reports),
            "keyed_inverse_cases": inverse_checks, "fixed_replacer_bound_attainment_cases": bound_attainment_checks,
            "unitarity_max_abs_error": max_unitarity_error, "keyed_inverse_max_abs_error": max_inverse_error,
            "averaged_channel_max_abs_error": max_channel_error, "T_equals_tail_weight_max_abs_error": max_distance_error,
            "averaged_energy_max_abs_error": max_energy_error, "reference_max_abs_error": max_reference_error}


def positive(value):
    return max(F(0), value)


def b_direct(d, delta):
    return sum((positive(1 - delta - F(m, d)) for m in range(1, d + 1)), F(0))


def b_closed(d, delta):
    if delta >= 1:
        return F(0)
    a = 1 - delta
    ell = (d * a).__floor__()
    return ell * a - F(ell * (ell + 1), 2 * d)


def check_rational_constants():
    tiny = F(1, 10**9)
    dimensions = list(range(1, 33)) + [63, 64, 65, 127, 128, 129, 257]
    sum_cases = 0
    for d in dimensions:
        deltas = {F(0), F(1, 10), F(1, 3), F(1, 2), F(2, 3), F(9, 10), F(1), 1 + tiny}
        for j in {0, 1, d // 3, d // 2, d - 1, d}:
            for shift in [-tiny / d, F(0), tiny / d]:
                delta = 1 - F(j, d) + shift
                if delta >= 0:
                    deltas.add(delta)
        previous = None
        for delta in sorted(deltas):
            direct = b_direct(d, delta)
            require(direct == b_closed(d, delta), f"B_d exact sum, d={d}, delta={delta}")
            if delta <= 1:
                a = 1 - delta
                fractional = d * a - (d * a).__floor__()
                polynomial = (d * a * a - a) / 2
                require(direct == polynomial + fractional * (1 - fractional) / (2 * d), "B_d fractional-part identity")
                require(direct >= positive(polynomial), "B_d polynomial lower bound")
            if previous is not None:
                require(direct <= previous, "B_d monotonicity")
            previous = direct
            sum_cases += 1

    e2_parameter_cases = 0
    for d in [2, 3, 4, 7, 16, 31, 128]:
        threshold = F(d - 1, 4)
        for energy in [F(1, 10**6), threshold * (1 - tiny), threshold, threshold * (1 + tiny), F(100)]:
            for epsilon in [F(1, 10**8), F(1, 6), F(1, 2)]:
                p = min(F(1, 2), 2 * energy / (d - 1))
                delta = epsilon / p
                require(p * F(d - 1, 2) <= energy, "E2 flagged energy")
                require(delta == max(2 * epsilon, epsilon * (d - 1) / (2 * energy)), "E2 delta identity")
                require(b_direct(d, delta) == b_closed(d, delta), "E2 finite-parameter B_d")
                e2_parameter_cases += 1

    ratios = [F(1, 1000), F(1), F(3, 2) - tiny, F(3, 2), F(3, 2) + tiny,
              F(9, 4) - tiny, F(9, 4), F(9, 4) + tiny, F(3) - tiny, F(3), F(3) + tiny, F(10), F(201, 2), F(1000)]
    e2_corollary_cases = 0
    for epsilon in [F(1, 10**6), F(1, 1000), F(1, 100), F(1, 6) - tiny, F(1, 6)]:
        for ratio in ratios:
            energy = ratio * epsilon
            target = positive(4 * energy / (27 * epsilon) - F(1, 3))
            if ratio < F(3, 2):
                require(target == 0, "E2 small-ratio branch")
            else:
                d = (2 * energy / (3 * epsilon)).__floor__() + 1
                p = min(F(1, 2), 2 * energy / (d - 1))
                delta = epsilon / p
                require(delta <= F(1, 3), "E2 chosen-d delta")
                require(b_direct(d, delta) >= target, "E2 4/27 corollary")
            e2_corollary_cases += 1

    robust_cases = 0
    for total_error in [F(1, 10**9), F(1, 10000), F(1, 100), F(1, 8) - tiny, F(1, 8)]:
        for ratio in [F(1, 1000), F(1), F(2) - tiny, F(2), F(2) + tiny, F(4) - tiny, F(4), F(4) + tiny, F(10), F(1000)]:
            for secrecy_fraction in [F(0), tiny, F(1, 1000), F(1, 4), F(1, 2), F(3, 4), 1 - tiny, F(1)]:
                energy = ratio * total_error
                epsilon = secrecy_fraction * total_error
                gamma = (1 - secrecy_fraction) * total_error
                target = positive(energy / (16 * total_error) - F(1, 4))
                if ratio < 2:
                    require(target == 0, "E2R small-ratio branch")
                else:
                    d = (energy / (2 * total_error)).__floor__() + 1
                    p = min(F(1, 2), 2 * energy / (d - 1))
                    require(p >= 4 * total_error, "E2R p >= 4s")
                    # Exact rational certificate for epsilon/p + sqrt(gamma/p) <= 1/2.
                    remainder = F(1, 2) - epsilon / p
                    require(remainder >= 0 and gamma / p <= remainder**2, "E2R square-root bound")
                    require(b_direct(d, F(1, 2)) >= target, "E2R 1/16 corollary")
                robust_cases += 1

    key_cases = 0
    for epsilon in [F(1, 10**6), F(1, 100), F(1, 2) - tiny, F(1, 2)]:
        for ratio in [F(1, 1000), 1 - tiny, F(1), 1 + tiny, F(2), F(10), F(1000)]:
            if ratio >= 1:
                energy = ratio * epsilon
                d = ratio.__floor__() + 1
                r = min(F(1), 2 * energy / (d - 1))
                delta = epsilon / r
                require(delta <= F(1, 2), "K1 chosen-d delta")
                require(d**2 * (1 - delta)**2 >= ratio**2 / 4, "K1 1/4 corollary")
            else:
                require(ratio**2 / 4 < 1, "K1 trivial alphabet branch")
            key_cases += 1
    return {"status": "passed", "arithmetic": "exact fractions; square roots bounded by nonnegative rational squares",
            "B_d_cases": sum_cases, "largest_B_d_dimension": max(dimensions),
            "E2_parameter_cases": e2_parameter_cases, "E2_corollary_cases": e2_corollary_cases,
            "E2R_corollary_cases": robust_cases, "K1_corollary_cases": key_cases,
            "near_boundary_offset": str(tiny), "E2_epsilon_upper_boundary": "1/6", "E2R_total_error_upper_boundary": "1/8"}


def integrated_homodyne_tv(noise_variance, hermite_order, legendre_order, window=12.0):
    """Convolve actual oscillator wavefunction densities; no closed TV formula.

    Gauss-Hermite integrates the input coordinate x with exp(-x^2) weight.
    Gauss-Legendre integrates both halves of the output window in q/sqrt(V+1/2).
    The signed density difference is convolved directly to limit cancellation.
    """
    x, weights_x = np.polynomial.hermite.hermgauss(hermite_order)
    # The common exp(-x^2/2) factor is absorbed into Hermite's weight.
    phi0_scaled = np.full_like(x, np.pi ** (-0.25))
    phi1_scaled = math.sqrt(2) * x * phi0_scaled
    plus_scaled = (phi0_scaled + phi1_scaled) ** 2 / 2
    minus_scaled = (phi0_scaled - phi1_scaled) ** 2 / 2
    difference_scaled = plus_scaled - minus_scaled
    input_norm_error = max(abs(float(weights_x @ plus_scaled) - 1), abs(float(weights_x @ minus_scaled) - 1))

    nodes, weights = np.polynomial.legendre.leggauss(legendre_order)
    positive_y = window * (nodes + 1) / 2
    output_y = np.r_[-positive_y, positive_y]
    output_weights = np.r_[weights, weights] * window / 2
    scale = math.sqrt(noise_variance + 0.5)
    q = scale * output_y
    kernel = np.exp(-((q[:, None] - x[None, :]) ** 2) / (2 * noise_variance))
    kernel /= math.sqrt(2 * math.pi * noise_variance)
    difference = kernel @ (weights_x * difference_scaled)
    plus = kernel @ (weights_x * plus_scaled)
    minus = kernel @ (weights_x * minus_scaled)
    tv = float(scale * np.dot(output_weights, abs(difference)) / 2)
    output_norm_error = max(abs(float(scale * (output_weights @ plus)) - 1), abs(float(scale * (output_weights @ minus)) - 1))
    return tv, input_norm_error, output_norm_error


def check_homodyne_discrepancy():
    rows = []
    for sigma in [1.0, 10.0, 30.0, 100.0]:
        variance = 2 * sigma**2
        coarse, input_error, coarse_norm_error = integrated_homodyne_tv(variance, 32, 96)
        fine, fine_input_error, fine_norm_error = integrated_homodyne_tv(variance, 64, 192)
        analytic_witness = 1 / math.sqrt(math.pi * (variance + 0.5))
        printed_n1_bound = (0.25 + 0.5 * (1 + 1 / (2 * sigma**2)) + 8) / sigma**2
        require(abs(fine - coarse) < TOL, "homodyne integration convergence")
        require(abs(fine - analytic_witness) < TOL, "integrated homodyne witness vs closed formula")
        require(max(input_error, fine_input_error, coarse_norm_error, fine_norm_error) < TOL, "homodyne density normalization")
        rows.append({"sigma": sigma, "V": variance, "integrated_homodyne_TV": fine,
                     "closed_form_homodyne_TV": analytic_witness, "coarse_fine_abs_difference": abs(fine - coarse),
                     "fine_closed_form_abs_difference": abs(fine - analytic_witness),
                     "input_normalization_max_abs_error": max(input_error, fine_input_error),
                     "output_normalization_max_abs_error": max(coarse_norm_error, fine_norm_error),
                     "printed_n1_bound": printed_n1_bound, "witness_to_printed_bound_ratio": fine / printed_n1_bound,
                     "witness_exceeds_printed_bound": fine > printed_n1_bound + TOL})
    require(rows[-1]["witness_exceeds_printed_bound"], "published-bound discrepancy witness at sigma=100")
    return {"status": "passed", "meaning": "the independently integrated measurement witness exceeds the printed bound at large sigma",
            "source": "https://doi.org/10.1103/PhysRevResearch.2.013332", "source_version": "published Theorem 1, Eq. (21), n=1; arXiv:1902.10972v2 Theorem 2",
            "input_states": "(|0> +/- |1>)/sqrt(2)", "input_mean_photon_number": 0.5,
            "quadrature": "Q=(a+a^dagger)/sqrt(2)", "variance_convention": "V=2*sigma^2",
            "coarse_orders": {"Hermite": 32, "Legendre_per_half_window": 96},
            "fine_orders": {"Hermite": 64, "Legendre_per_half_window": 192},
            "integration_window_in_units_sqrt_V_plus_half": [-12, 12], "cases": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    started = time.perf_counter()
    report = {"status": "running", "generated_utc": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": sys.version, "numpy": np.__version__, "platform": platform.platform()},
              "seed": SEED, "absolute_tolerance": TOL,
              "scope": "Finite examples and exact rational checks only. No optimization over all states, no infinite-dimensional proof, and no truncated-amplifier simulation.",
              "checks": {}}
    rng = np.random.default_rng(SEED)
    checks = [("loss_and_phase", lambda: check_loss_and_phase(rng)),
              ("cutoff_cipher", lambda: check_cutoff_cipher(rng)),
              ("rational_constants", check_rational_constants),
              ("homodyne_discrepancy", check_homodyne_discrepancy)]
    failed = False
    for name, operation in checks:
        try:
            report["checks"][name] = operation()
            print(f"PASS {name}", flush=True)
        except Exception as error:
            failed = True
            report["checks"][name] = {"status": "failed", "error_type": type(error).__name__, "error": str(error)}
            print(f"FAIL {name}: {error}", flush=True)
    report["status"] = "failed" if failed else "passed"
    report["elapsed_seconds"] = time.perf_counter() - started
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"{report['status'].upper()}: {len(checks)} groups; report: {args.output}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
