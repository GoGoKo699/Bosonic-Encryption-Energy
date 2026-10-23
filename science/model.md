# Quantum encryption with an energy budget

An optical message can have small mean energy while retaining a very small probability of occupying an arbitrarily high photon-number level. Encryption must hide both its classical populations and its quantum coherence with other systems. Those two requirements make a mean-energy promise different from a hard photon cutoff.

This project asks how much excitation an exactly decryptable ciphertext must carry when secrecy is required uniformly over this message family. A second question concerns implementation: when does a secret phase rotation improve Gaussian-displacement encryption, and how much additional phase randomness is needed?

The [energy converse](energy_cost.md), [finite-key construction](finite_key.md), [optical construction](gaussian_encryption.md), and [phase criterion](phase_criterion.md) answer these questions in the model below. The [interpretation](interpretation.md) joins their conclusions and resource boundaries.

## 1. Carrier and message family

The plaintext system $`A`$ and ciphertext system $`C`$ are each a single oscillator. They have the same fixed number spectrum,

```math
\mathcal H_A\simeq\mathcal H_C\simeq\ell^2(\mathbb N_0),
\qquad
N=\sum_{n=0}^{\infty}n\lvert n\rangle\langle n\rvert.
```

Energy is measured in photons above the ground state. Multiplication by $`\hbar\omega`$ converts it to physical excitation energy at the fixed frequency $`\omega`$. Changing the carrier frequency, adding modes, or introducing a degenerate zero-energy register changes this model.

For a prescribed $`E>0`$, admissible messages are all density operators $`\rho_{AR}`$ satisfying

```math
\mathrm{Tr}(N\rho_A)\le E.
```

The reference $`R`$ is arbitrary and may be held by an adversary. It can contain classical flags, quantum entanglement, or both. The only constraint is on the marginal energy of $`A`$. There is no assumption of Gaussian messages, a finite photon cutoff, or a bounded photon-number variance. Normal states and normal channels on separable Hilbert spaces are understood throughout.

The distinction between mean energy and a cutoff is operational. For every integer $`n\ge E`$, the mixture of vacuum and $`\lvert n\rangle`$ with excited-state probability $`E/n`$ is admissible. If the reference records which branch occurred, that rare branch remains part of the secrecy test.

## 2. Secret key and exact recovery

A classical key $`k`$, independent of the joint message $`\rho_{AR}`$, selects a completely positive trace-preserving encoder $`\mathcal E_k:A\to C`$ and decoder $`\mathcal D_k:C\to A`$. The central model requires

```math
\mathcal D_k\circ\mathcal E_k=\mathrm{id}_A
```

for every key of nonzero probability, or almost every key for a continuous distribution. This is exact recovery on the oscillator, including coherence with an arbitrary reference. Unitary encryption is a special case. The converse also allows reversible encoders with private ancillary randomness.

An observer without the key sees the average channel

```math
\overline{\mathcal E}(\rho)
=\int\mathcal E_k(\rho)\,d\mu(k).
```

The integral is assumed to define a normal CPTP map. The finite-key construction uses a finite uniform distribution. The optical construction uses a continuous Gaussian displacement together with an independent phase key.

Only the ciphertext oscillator is transmitted. A private environment may be used inside an encoder, but recovery must be possible from the ciphertext and classical key alone. An extra transmitted classical or quantum register would have to be included in the ciphertext Hamiltonian; it cannot be hidden outside the energy accounting.

## 3. Secrecy and distance convention

We use half trace distance,

```math
T(\rho,\sigma)=\frac12\lVert\rho-\sigma\rVert_1.
```

For a channel $`\mathcal C`$ and a fixed ciphertext state $`\tau`$, define

```math
\delta_E(\mathcal C;\tau)
=\sup_{\rho_{AR}:\mathrm{Tr}(N\rho_A)\le E}
T\!\left[(\mathcal C\otimes\mathrm{id}_R)(\rho_{AR}),
\tau_C\otimes\rho_R\right].
```

The supremum includes arbitrary reference systems. Equivalently, this is one half of the energy-constrained diamond distance from the replacement channel $`\mathcal R_\tau(\rho)=\tau\mathrm{Tr}\rho`$. Its meaning is that the ciphertext reveals at most $`\varepsilon`$ distinguishing advantage, in this distance convention, beyond what the reference already contains.

An encoder is $`\varepsilon`$-secret if there exists one $`\tau`$, independent of the input, for which

```math
\delta_E(\overline{\mathcal E};\tau)\le\varepsilon.
```

For comparisons that allow the best possible target, write

```math
\delta_E^*(\mathcal C)=\inf_\tau\delta_E(\mathcal C;\tau).
```

Constructive upper bounds specify their target state explicitly. Lower bounds against any replacement channel apply to every $`\tau`$ before taking this infimum. The [phase chapter](phase_criterion.md) distinguishes these two uses when converting a pairwise distinguishing experiment into a secrecy lower bound.

This reference-aware replacement criterion is stronger than comparing a selected family of coherent messages or bounding the outcome of a prescribed optical measurement. A homodyne or heterodyne measurement is nevertheless a valid lower-bound witness, because measurement cannot increase trace distance.

The infinite-dimensional norm framework is established background; see the discussion and primary sources in [Related work](../references/RELATED_WORK.md). The results here concern its application to exactly reversible encryption and the explicitly charged ciphertext.

## 4. The charged resources

Two output-energy quantities are useful:

```math
\tau_0=\overline{\mathcal E}(\lvert0\rangle\langle0\rvert),
\qquad
C_{\mathrm{vac}}=\mathrm{Tr}(N\tau_0),
```

and

```math
C_{\max}(E)
=\sup_{\rho_A:\mathrm{Tr}(N\rho_A)\le E}
\mathrm{Tr}\!\left[N\overline{\mathcal E}(\rho_A)\right].
```

Both average over the secret key. The first is the cost of encrypting vacuum; the second is the largest average ciphertext energy over the message family. Their values may be infinite. A lower bound on $`C_{\mathrm{vac}}`$ automatically lower-bounds $`C_{\max}(E)`$.

The cost does not include a device model for control work, laser energy, gate time, or key generation. A reversible receiver may recover excitation. These theorems therefore concern energy carried by encrypted states, rather than dissipated heat or total implementation energy.

For a finite key alphabet, $`M`$ denotes its cardinality. The converse permits a nonuniform distribution and bounds $`\log_2 M`$. A uniform power-of-two construction turns this into a fixed number of secret bits per encryption. This is different from a general Shannon-entropy bound for arbitrary nonuniform keys, and from the differential entropy of a continuous Gaussian variable.

## 5. Results and proof route

| Result | Statement and assumptions | Authoritative account |
|---|---|---|
| E1–E2 | Exact recoverability makes encrypted finite-dimensional uniform states spectrally diffuse. Flagged dilution and the oscillator tail sum force an inverse-linear ciphertext-energy cost. | [Energy cost](energy_cost.md) |
| C1 | A Weyl twirl on the first $`d`$ levels plus a relative sign on the tail has error exactly $`\min\{1,E/d\}`$ and uses $`2d^2`$ keys. | [Finite-key construction](finite_key.md) |
| K1 | An energy-diluted entangled input converts approximate quantum Shannon impossibility into a matching key-cardinality lower bound. | [Finite-key converse](finite_key.md) |
| G1–G3 | Gaussian displacement alone has inverse-square noise requirements; full phase averaging or one parity bit improves the secrecy exponent. | [Gaussian encryption](gaussian_encryption.md) |
| P1–P3 | The first Fourier moment of an independent phase law determines the improved exponent; a binary antipodal law minimizes additional phase entropy; residual imbalance has a quantified effect. | [Phase criterion](phase_criterion.md) |

For the universal energy bound, one convenient finite-parameter consequence is

```math
C_{\mathrm{vac}}
\ge\max\!\left\{0,\frac{4E}{27\varepsilon}-\frac13\right\},
\qquad 0<\varepsilon\le\frac16.
```

The explicit construction has

```math
\delta_E(\overline{\mathcal E};\pi_d)
=\min\{1,E/d\},
\qquad
C_{\mathrm{vac}}=\frac{d-1}{2},
\qquad
C_{\max}(E)=E+\frac{d-1}{2}.
```

Thus the infimum attainable ciphertext energy has scaling $`\Theta(E/\varepsilon)`$ in the small-error, large-$`E/\varepsilon`$ regime. This is a matching scaling law, with no assertion of an optimal leading constant. The finite-key law is $`2\log_2(E/\varepsilon)+O(1)`$ fixed-length bits in the same regime.

For the optical scheme, let $`V`$ denote the Gaussian displacement's added mean photon number. A fair secret parity bit gives the explicit bound

```math
\delta_E(\mathcal N_V\circ\Phi_2;\tau_V)
\le\min\!\left\{1,
\frac{E}{V+1}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\},
\qquad V>0.
```

Here $`\tau_V`$ is the thermal ciphertext of vacuum. The error is $`O(1/V)`$ at every fixed $`E>0`$, and is $`O(E/V)`$ uniformly for $`E\ge1`$ and large enough $`V`$. At $`E\ll1`$, the $`\sqrt E/V`$ contribution is intrinsic to binary phase randomization. Full phase averaging and the finite-key block construction have their own stronger uniform dependence on $`E`$.

## 6. Boundaries that travel with the claims

- Exact keyed recovery is the central correctness assumption. The [energy chapter](energy_cost.md) separately states the quantitative extension to small averaged correctness error, with its own conditions.
- The output is one oscillator with a fixed nondegenerate spectrum. The proof charges the number of orthogonal low-energy output states; a changed spectrum or an extra register requires new accounting.
- The optical phase law is independent of the Gaussian displacement. The first-harmonic classification fixes that law while $`V`$ increases.
- The finite-key construction and the simple optical construction are distinct achievements. Their resource advantages cannot be combined without an additional discretization theorem.
- This is a single-use secrecy model with a secret classical key. Exact inverse operations do not establish robustness to transmission loss or implementation error; the phase-imbalance estimate addresses only its stated control error.

The [interpretation](interpretation.md) explains why these boundaries are consequential. Primary ingredients and the closest earlier encryption claims are compared in [Related work](../references/RELATED_WORK.md), with a detailed [displacement-rate calculation](displacement_comparison.md).
