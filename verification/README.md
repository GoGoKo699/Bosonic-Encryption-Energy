# Reproducible verification

This suite checks finite examples and the arithmetic of the stated constants. The proofs in [the science chapters](../science/model.md) carry the infinite-dimensional and arbitrary-reference claims. The numerical calculations are deliberately limited to operations whose treatment of the selected inputs is exact, apart from floating-point arithmetic.

## Run

From the repository root, using Python 3.11 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The script exits with status zero only if every group passes. It writes a compact report to [results.json](results.json), including the actual Python, NumPy, and platform versions. To preserve that file while rerunning:

```bash
python verification/run_all.py --output /tmp/bosonic-encryption-results.json
```

The only third-party dependency is NumPy, pinned to version 2.3.5. Random input states use NumPy's default generator with seed 9231. Floating-point comparisons use absolute tolerance $`2\times10^{-11}`$. The report retains group counts, largest discrepancies, and representative worst cases; it does not list every input-output pair. Timestamps and elapsed time change between runs, and last digits of numerical results may depend on the platform.

## What is checked

| Group | Checks | Scope |
| --- | --- | --- |
| Loss and phase laws | 2,160 reference-aware bound comparisons; 30 independent dense-versus-sparse Kraus comparisons | 48 joint input states, 9 phase laws, 5 transmissivities |
| Cutoff cipher C1 | 36 averaged-channel checks; 696 keyed inversions; 12 fixed-replacer bound-attainment checks | All $`2d^2`$ keys for $`d=2,3,4`$ |
| Exact arithmetic | 830 $`B_d`$ evaluations; 105 E2 parameter checks; 70 E2, 400 E2R, and 28 K1 corollary checks | Rational inputs, including values immediately adjacent to floor-function and parameter boundaries |
| Homodyne discrepancy | 4 noise strengths, each evaluated at two quadrature resolutions | Direct convolution of the two oscillator wavefunction densities |

### Loss and the phase criterion

The inputs are supported on Fock levels $`0,\ldots,15`$, with a three-dimensional reference. They include the vacuum, a number state, coherent and reference-entangled vacuum/high-level superpositions, rare tails of weight $`10^{-6}`$, random purifications, and mixed joint states.

The pure-loss channel uses its Fock-basis Kraus operators:

```math
K_\ell|n\rangle
=\sqrt{\binom n\ell(1-\eta)^\ell\eta^{n-\ell}}
\,|n-\ell\rangle.
```

Loss cannot populate a level above the finite input support. The finite Kraus sum therefore gives the full output for these inputs; there is no discarded loss-output tail. A sparse tensor implementation is cross-checked against separate dense multiplication by $`K_\ell\otimes I_R`$. The script also checks Kraus completeness, trace and reference preservation, and the exact energy relation $`E_{\rm out}=\eta E_{\rm in}`$.

The phase laws comprise three zero-first-moment examples, the identity phase, two biased antipodal laws, two balanced laws with angle error, and a law with both errors. The imperfect binary laws also check the explicit first-moment identity in [P3](../science/phase_criterion.md#p3-residual-phase-imbalance-and-control-accuracy).

The measured trace distance to the vacuum/reference replacement state is compared with the preamplifier bound underlying G3 and P3:

```math
T\!\left[(\mathcal L_\eta\Phi_\mu\otimes\mathrm{id})(\rho),
|0\rangle\langle0|\otimes\rho_R\right]
\le\min\!\left\{1,
\eta E+|m_1|\sqrt{\eta E}
+\eta\sqrt{\frac{E(E+1)}{2(1-\eta)}}\right\}.
```

The suite does **not** simulate a truncated amplifier. The transition from this loss estimate to the displacement-channel estimate uses the analytic amplifier factorization and trace-distance contraction in [gaussian_encryption.md](../science/gaussian_encryption.md). Finite examples do not establish a uniform bound over an energy-constrained state space.

### Cutoff cipher C1

For each cutoff, the physical support includes three additional Fock levels. The reference has dimension $`d+1`$. The script explicitly builds every Weyl-plus-sign unitary

```math
U_{a,b,s}=X^aZ^b\oplus sI,\qquad s\in\{-1,+1\},
```

and applies its inverse to every test input. The inputs include a maximally entangled low-block state, coherent and entangled low/high superpositions, random joint states, and a mixed state. Averaging the actual keyed outputs is compared with the formula in [C1](../science/finite_key.md):

```math
(\mathcal C_d\otimes\mathrm{id})(\rho)
=\pi_d\otimes\rho_R^{\rm low}+\rho^{\rm high}.
```

The suite verifies both identities

```math
T\!\left[(\mathcal C_d\otimes\mathrm{id})(\rho),
\pi_d\otimes\rho_R\right]=q,
\qquad q=\operatorname{Tr}(Q_d\rho_A),
```

```math
\operatorname{Tr}[N\mathcal C_d(\rho)]
=\frac{d-1}{2}(1-q)+\operatorname{Tr}(NQ_d\rho Q_d).
```

Additional inputs attain $`\min\{1,E/d\}`$ for the stated fixed replacer, including energy budgets on both sides of $`E=d`$. These are checks of the construction and that fixed-replacer equality. They do not optimize the replacement state or numerically establish the infinite-support energy supremum.

### Rational arithmetic

Python's standard-library `fractions.Fraction` is used throughout this group. No floating-point comparison enters the checks of $`B_d`$, the $`4/27`$ constant in E2, the $`1/16`$ constant in E2R, or the $`1/4`$ constant in K1.

The direct finite sum for $`B_d`$ is compared with its floor-function expression and fractional-part identity. The grid includes offsets of $`10^{-9}/d`$ around its corners. E2 cases straddle the branch change in $`p_d`$ and include $`\epsilon=1/6`$. E2R cases include $`\epsilon+\gamma=1/8`$, pure secrecy or pure correctness error, and mixtures close to those endpoints.

For E2R, the square-root bound is certified without evaluating a square root: the script checks that $`y=1/2-\epsilon/p_d`$ is nonnegative and that $`\gamma/p_d\le y^2`$. This implies the desired $`\epsilon/p_d+\sqrt{\gamma/p_d}\le1/2`$. These finite parameter checks catch errors in constants and boundary handling; the general argument remains the proof in [energy_cost.md](../science/energy_cost.md).

### Independently integrated homodyne witness

The final group compares a measurement witness with the printed Theorem 1, Eq. (21), of [Ouyang et al., *Physical Review Research* **2**, 013332 (2020)](https://doi.org/10.1103/PhysRevResearch.2.013332); this is Theorem 2 in [arXiv:1902.10972v2](https://arxiv.org/abs/1902.10972v2). The source and analytical discrepancy are discussed in [displacement_comparison.md](../science/displacement_comparison.md). The conventions are $`Q=(a+a^\dagger)/\sqrt2`$ and displacement noise $`V=2\sigma^2`$. The input pair is

```math
|\psi_\pm\rangle=\frac{|0\rangle\pm|1\rangle}{\sqrt2}.
```

The program constructs their quadrature densities from the vacuum and first-excited oscillator wavefunctions. It numerically convolves those densities with a Gaussian of variance $`V`$, then integrates the absolute density difference. The convolution uses Gauss-Hermite quadrature; the outer integral uses Gauss-Legendre quadrature on each side of zero. The signed difference is convolved directly to reduce numerical cancellation. The closed-form total variation is used only as an independent comparison after integration:

```math
\mathrm{TV}_{\rm homodyne}
=\frac1{\sqrt{\pi(V+1/2)}}.
```

The output window is $`[-12,12]`$ in units of $`\sqrt{V+1/2}`$. Two quadrature resolutions and the normalization of both convolved densities are checked. This is ordinary numerical integration, not an interval-arithmetic certification of the omitted tails. The analytic expression establishes the exact witness.

At $`\sigma=100`$, the recorded run gives:

| Quantity | Value |
| --- | ---: |
| Independently integrated homodyne total variation | 0.003989372937164246 |
| Printed cutoff-$`n=1`$ bound, Theorem 1 / Eq. (21) | 0.0008750025000000001 |
| Witness / printed bound | 4.55927033027248 |
| Change between quadrature resolutions | $`3.4\times10^{-17}`$ |

The suite expects the witness to exceed the printed formula at this parameter. A passing discrepancy check therefore records a conflict with that formula, not its validation. A homodyne measurement supplies a lower bound on the quantum trace distance; the program does not reconstruct the infinite-dimensional displacement-channel output.

## Recorded run

The recorded report was produced with Python 3.12.14, NumPy 2.3.5, and Linux x86-64. All four groups passed. The largest recorded Kraus/channel identity errors were below $`4\times10^{-15}`$; homodyne normalization errors were below $`5\times10^{-14}`$. The exact rational checks passed with equality or the required inequality. See [results.json](results.json) for the platform string, run time, and per-group details.
