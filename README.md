# Bosonic Encryption Energy

**How much energy must an encrypted quantum state carry?** For a single oscillator, a bound on the plaintext's mean photon number still permits rare, arbitrarily energetic components. Hiding the whole state—including correlations with a reference—while keeping it exactly recoverable imposes a quantitative cost on the ciphertext.

This repository proves matching scaling laws for that cost and the size of a finite classical key. It also identifies when a simple secret phase rotation improves Gaussian-displacement encryption.

## Main results

Let $`E>0`$ bound the input mean photon number and let $`\varepsilon`$ be the allowed secrecy error in half the energy-constrained diamond distance from a fixed replacement channel. Plaintext and ciphertext each occupy one oscillator with the same fixed, nondegenerate number spectrum. The key is independent of the message, and decryption is exact.

| Question | Result | Proof |
|---|---|---|
| How much ciphertext energy is unavoidable? | Even encrypting vacuum costs $`C_{\rm vac}=\Omega(E/\varepsilon)`$. A finite-key construction attains $`O(E/\varepsilon)`$. | [Energy cost](science/energy_cost.md), [construction C1](science/finite_key.md) |
| How large must a finite key alphabet be? | $`M=\Theta((E/\varepsilon)^2)`$, or $`2\log_2(E/\varepsilon)+O(1)`$ uniform fixed-length bits, with matching orders attained by the same construction. | [Finite-key encryption](science/finite_key.md) |
| What does displacement alone cost? | Gaussian displacement requires added mean photon number $`V=\Theta(E/\varepsilon^2)`$ in the small-error regime. | [Gaussian benchmark G1](science/gaussian_encryption.md) |
| When does a secret phase improve that exponent? | For a fixed independent phase law $`\mu`$, the error is $`\Theta(V^{-1})`$ exactly when $`\int e^{i\theta}d\mu(\theta)=0`$; otherwise it is $`\Theta(V^{-1/2})`$, at fixed $`E>0`$. | [Phase criterion P1](science/phase_criterion.md) |
| How much extra phase randomness suffices? | One fair parity bit is optimal among discrete phase laws with zero first Fourier moment. Its phase bias and angle tolerance are quantified. | [G3](science/gaussian_encryption.md), [P2–P3](science/phase_criterion.md) |

The resource laws concern small secrecy error and large $`E/\varepsilon`$; they determine scaling, not optimal leading constants. The optical construction has a continuous displacement key. Its additional phase bit is distinct from the finite-key construction.

### Explicit bounds

Every exactly recoverable scheme obeys

```math
C_{\rm vac}\ge
\max\left\{0,\frac{4E}{27\varepsilon}-\frac13\right\},
\qquad 0<\varepsilon\le\frac16.
```

Randomizing the first $`d`$ Fock levels and independently their relative phase to the tail gives

```math
\delta_E(\mathcal C_d;\pi_d)=\min\{1,E/d\},\qquad
M=2d^2,\qquad
C_{\rm vac}=\frac{d-1}{2},\qquad
C_{\max}(E)=E+\frac{d-1}{2}.
```

A Gaussian displacement of added mean photon number $`V`$, preceded by a fair secret parity rotation, satisfies

```math
\delta_E(\mathcal N_V\circ\Phi_2;\tau_V)
\le\min\left\{1,\frac{E}{V+1}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}.
```

Here $`\pi_d`$ is uniform on the first $`d`$ levels and $`\tau_V`$ is thermal with mean photon number $`V`$. All guarantees include arbitrary quantum reference systems. For $`E\ge1`$, the parity bound is uniformly $`O(E/V)`$; for very small $`E`$, its $`\sqrt E/V`$ term is physically necessary.

## Read the scientific account

The chapters form a connected account, with one authoritative location for each proof.

1. **[Model and question](science/model.md):** the message family, reference-aware secrecy, exact recovery, and charged resources.
2. **[Energy cost](science/energy_cost.md):** reversible encoders, spectral spreading, rare flagged messages, the universal converse, and a scoped extension to imperfect recovery.
3. **[Finite-key encryption](science/finite_key.md):** an exact full-oscillator construction and the matching key-cardinality converse.
4. **[Gaussian encryption](science/gaussian_encryption.md):** the displacement benchmark, full phase averaging, and a one-bit optical construction.
5. **[Phase criterion](science/phase_criterion.md):** the necessary-and-sufficient first-moment condition, minimum phase entropy, and sensitivity to imperfect controls.
6. **[Physical interpretation](science/interpretation.md):** the common mechanism, worked resource examples, and boundaries of the conclusions.
7. **[Displacement-rate comparison](science/displacement_comparison.md):** an explicit homodyne witness testing a published finite-cutoff Gaussian-displacement bound.

For attribution and comparison, read [Related work](references/RELATED_WORK.md) and the [BibTeX bibliography](references/references.bib). Standard channel identities, quantum one-time pads, and finite-dimensional quantum Shannon bounds are distinguished from the energy-constrained reductions and phase-rate results established here. Combining secret rotations and displacements is an existing optical idea; the new claim is not the first use of those controls.

## Reproduce the checks

The analytic proofs do not rely on numerical truncation. The [verification suite](verification/README.md) independently checks finite Weyl averages, selected entangled inputs under exact loss Kraus maps, finite-parameter constants, and the homodyne comparison.

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The suite records a compact result summary and its actual numerical environment. Finite matrix examples support formula and implementation checks; they are not a substitute for the proofs on the full oscillator.

## Scope

The charged resource is mean ciphertext excitation at a fixed carrier frequency. It is not a bound on dissipated heat or total device work. All transmitted degrees of freedom are included in the single-oscillator model; extra modes, side registers, or a different spectrum require different accounting.

The finite-key construction uses ideal Fock-block unitaries. The simpler optical construction uses continuous Gaussian controls and does not establish a finite-precision implementation with the same guarantee. The results concern single-use encryption and do not by themselves establish authentication, key-reuse security, or loss tolerance.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
