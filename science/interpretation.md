# What encryption energy measures

The same unknown oscillator state can be hidden in two different ways. One can randomize a sufficiently large block of number states, or use simple optical controls to wash out the information in phase space. The first construction identifies the resource law. The second explains why the choice of random controls changes the rate at which secrecy improves.

The main conclusion is a joint scaling statement: in the single-oscillator model, exactly recoverable encryption of all mean-energy-bounded states requires ciphertext energy of order $`E/\varepsilon`$ and a finite classical key alphabet of order $`(E/\varepsilon)^2`$. A single construction attains both orders. Gaussian displacement alone uses more energy, but an independent phase law with zero first Fourier moment repairs its small-error exponent. These conclusions concern the explicit [reference-aware secrecy model](model.md), not just the appearance of a few encrypted optical signals.

## 1. Why even the vacuum must become energetic

A reversible encoder must preserve the distinguishability of orthogonal plaintexts. Encrypting the uniform mixture of the first $`d`$ number states therefore produces a state whose largest eigenvalue is at most $`1/d`$, even if the encoder is not unitary and uses private randomness. Averaging over keys preserves this upper bound.

A state with eigenvalues at most $`1/d`$ cannot place nearly all its mass in a small low-energy subspace. There are only $`m`$ orthogonal oscillator levels below photon number $`m`$, so at most $`m/d`$ of its probability lies there. Summing the missing probability over successive cutoffs gives a lower bound on its energy.

The mean-energy constraint does not remove large values of $`d`$. It permits a rare, reference-flagged branch containing that uniform mixture. The flag makes the branch visible to the secrecy criterion, even when its probability is small. Secrecy then forces the ciphertext of the vacuum to resemble the diffuse ciphertext closely enough that it inherits a substantial high-energy tail. This is the mechanism of [E1–E2](energy_cost.md).

The resulting finite-parameter bound is

```math
C_{\rm vac}\ge
\max\!\left\{0,\frac{4E}{27\varepsilon}-\frac13\right\},
\qquad 0<\varepsilon\le\frac16.
```

No leading constant is claimed to be optimal. The point is that the energy cost is already unavoidable for the vacuum input, after averaging over the secret key. Perfect secrecy at any fixed $`E>0`$ is impossible in this model: it would require the same normalized vacuum ciphertext to be bounded above by $`I/d`$ for every finite $`d`$. Allowing that ciphertext to have infinite mean energy does not resolve this normalization contradiction.

The energy argument uses perfect recovery of classical Fock labels and a classical reference flag. It does not need coherent superpositions in its witness. The stronger quantum requirement appears in the key law, where the flagged branch is maximally entangled with a reference and the familiar finite-dimensional quantum Shannon bound supplies the factor $`d^2`$. The two lower bounds share the energy-dilution method while using different witnesses.

## 2. How a finite key attains the resource law

The [finite construction C1](finite_key.md) applies a uniform Weyl operator to the first $`d`$ levels and an independent random relative sign between that block and its complement. Every keyed operation is unitary on the entire oscillator. The high-energy tail remains recoverable; it is not projected away.

The averaged channel removes coherence between the blocks and replaces the low block by its uniform mixture. For every joint plaintext and reference, the trace distance from the specified replacement state is exactly the high-block probability,

```math
T=q=\operatorname{Tr}(Q_d\rho_A)\le\frac{E}{d}.
```

For $`E\le d`$, the inequality is saturated by a suitable mixture of vacuum and the level $`d`$. When $`E\ge d`$, the level $`d`$ attains the maximum possible error of one. This gives a complete error formula, rather than an estimate based on a typical message. The charged resources are

```math
M=2d^2,\qquad
C_{\rm vac}=\frac{d-1}{2},\qquad
C_{\max}(E)=E+\frac{d-1}{2}.
```

The last quantity is a supremum over allowed messages. It can be approached by increasingly rare, increasingly energetic number states. It need not be attained by one finite-energy distribution.

For example, take $`E=1`$ and $`d=128`$. The scheme guarantees error at most $`1/128`$, uses exactly $`2\cdot128^2=2^{15}`$ equally likely keys, encrypts vacuum to a state of mean photon number $`63.5`$, and has maximum average ciphertext energy $`64.5`$ as a supremum. The idealized Fock-block unitaries have not been shown to admit an efficient implementation with elementary Gaussian optics.

The finite-key converse applies even to arbitrary nonuniform key probabilities and reversible CPTP encoders. It bounds key-alphabet cardinality. It does not establish the same formula for the Shannon entropy of an arbitrary nonuniform key, the expected length of a variable-length key, or the precision needed to implement a continuous optical control.

## 3. Why an optical phase bit changes the exponent

For Gaussian displacement noise with added mean photon number $`V`$, the loss–amplifier factorization is

```math
\mathcal N_V=\mathcal A_{V+1}\circ\mathcal L_{1/(V+1)}.
```

This is an identity for the averaged channel; each keyed encryption remains a reversible displacement. The analysis can therefore follow a fictitious strong attenuation with transmissivity $`\eta=1/(V+1)`$ before the final amplifier.

Population outside vacuum is of order $`\eta E`$ after attenuation. Vacuum-to-one-photon coherence can be larger, of order $`\sqrt{\eta E}`$. Gaussian displacement alone leaves this first-order coherent signal available to an observer. A pair of coherent inputs already gives an operational heterodyne witness of the inverse-square-root secrecy rate. The full arbitrary-reference upper bound has the same exponent.

Now average an independent phase rotation with distribution $`\mu`$. The vacuum-to-one-photon term is multiplied by its first Fourier moment,

```math
m_1=\int e^{i\theta}\,d\mu(\theta).
```

If $`m_1=0`$, this term disappears. The remaining vacuum-to-higher-photon coherences can be bounded using only the first moment of the input photon number. The resulting trace-distance error is of order $`1/V`$ at each fixed positive $`E`$. No second-moment assumption or hidden photon cutoff enters this proof.

For a fixed phase law, the [classification P1](phase_criterion.md) is exact at the level of the exponent:

| Phase distribution | Secrecy error as $`V\to\infty`$, at fixed $`E>0`$ |
|---|---|
| $`m_1\ne0`$ | $`\Theta(V^{-1/2})`$ |
| $`m_1=0`$ | $`\Theta(V^{-1})`$ |

Both statements apply to the best fixed replacement state, and also to the specified thermal replacement state. The lower bound in the second row uses a population witness, which phase rotations cannot erase.

Among discrete phase distributions, $`m_1=0`$ requires at least one bit of Shannon entropy. Equality occurs for two equally probable antipodal phases. Thus a fair choice between the identity and parity $`(-1)^N`$ is the least additional discrete phase randomness that obtains the improved exponent within this independent-phase construction.

This statement has a precise scope. The Gaussian displacement key remains continuous. The one-bit minimum concerns the additional phase distribution, not the total key of an arbitrary oscillator encryption scheme. It also does not assert that phase rotations were first introduced here: earlier private-channel and optical-encryption proposals already combine displacement and secret rotations. The [related-work comparison](../references/RELATED_WORK.md) separates those existing ingredients from the reference-aware rate criterion proved here.

## 4. Why centering the reduced state is insufficient

The scalar condition $`\operatorname{Tr}(a\rho_A)=0`$ does not remove a signal stored in correlations with a reference. Consider equally likely coherent states $`|\alpha\rangle`$ and $`|-\alpha\rangle`$ whose signs are recorded in orthogonal reference flags. Their averaged oscillator state has zero first moment. Conditional on the reference, their opposite displacements remain distinguishable.

The phase randomization used here cancels the vacuum-to-one-photon contribution as an operator on the joint ciphertext and reference. This is why the proof applies to arbitrary purifications and flags, rather than only centered reduced states. Keeping that operator structure is essential when converting a phase-space observation into a cryptographic secrecy guarantee.

There are also two different binary controls in the project. C1 uses a relative sign between a chosen finite Fock block and its tail. The optical construction uses parity, which alternates the sign on successive Fock levels. They are different unitaries with different cancellation properties. The exact tail-error formula of C1 does not follow merely by substituting optical parity.

## 5. Finite parameters, low energy, and phase precision

For the fair parity scheme, the proved thermal-target bound is

```math
\delta_E\le
\min\!\left\{1,
\frac{E}{V+1}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}.
```

For $`E\ge1`$, this is at most $`2E/V`$. Consequently, $`V=2E/\varepsilon`$ is a simple sufficient choice. With $`E=1`$ and the error target $`1/128`$, choosing $`V=256`$ gives the explicit upper bound

```math
\frac1{257}+\frac1{\sqrt{256\cdot257}}
\approx0.0077897<\frac1{128}.
```

The mean output photon number is the input energy plus $`V`$. These constants are convenient sufficient values, not an optimization of the optical scheme.

At very low input energy, the dependence on $`E`$ needs care. Parity preserves coherence between vacuum and the two-photon level. The witness in [G3](gaussian_encryption.md) proves an error contribution proportional to $`\sqrt E/(V+1)`$ for small $`E`$. The inverse-linear exponent in $`V`$ remains correct at every fixed $`E>0`$, but a uniform $`O(E/V)`$ claim down to $`E=0`$ would be false. Continuous uniform phase averaging removes all number coherences and gives the stronger bound $`E/(V+1)`$. The finite Fock-block construction also retains its own uniform dependence on $`E`$.

An imperfect phase law leaves residual first moment $`m_1`$. The [imbalance estimate P3](phase_criterion.md) gives

```math
\delta_E\le
\min\!\left\{1,
\frac{E}{V+1}
+|m_1|\sqrt{\frac{E}{V+1}}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}.
```

For a nominal binary choice with probability $`p`$ at phase zero and probability $`1-p`$ at phase $`\pi+\Delta`$,

```math
|m_1|^2=(2p-1)^2+4p(1-p)\sin^2(\Delta/2).
```

At fixed positive $`E`$, maintaining error of order $`\varepsilon`$ with $`V`$ of order $`E/\varepsilon`$ requires residual imbalance of order $`\sqrt\varepsilon`$ or smaller, up to constants. The upper bound makes that precision sufficient and a first-harmonic witness makes its order necessary. A fixed nonzero imbalance eventually restores the slower exponent. These bounds quantify probability bias and angle error; they do not constitute a complete optical-device error model.

## 6. The physical accounting and its boundaries

The universal converse depends on the nondegenerate single-oscillator spectrum. Its key counting step is that the subspace below photon number $`m`$ has dimension $`m`$. Adding modes or a free side register changes that relationship. Lowering the carrier frequency changes the conversion from photon number to joules. The fixed spectrum and the charging of every transmitted degree of freedom must therefore accompany any physical interpretation of the energy law.

The energy carried by a ciphertext is also distinct from work consumed by a device. A decoder may recover excitation; the proof does not model dissipated heat, laser efficiency, control electronics, preparation time, or a thermodynamic cycle. The precise claim is a lower bound on average encrypted-state excitation under the stated secrecy and recovery requirements.

Exact recovery is central to the matching energy and key laws. [E2R](energy_cost.md) shows that the energy obstruction persists when the averaged decoded channel has a small reference-aware correctness error $`\gamma`$. One explicit bound is

```math
C_{\rm vac}\ge
\max\!\left\{0,\frac{E}{16(\varepsilon+\gamma)}-\frac14\right\},
\qquad 0<\varepsilon+\gamma\le\frac18.
```

This robustness statement has its own proof and assumptions. It does not identify an optimal energy–key–correctness tradeoff. Similarly, secrecy for one use does not by itself give authentication, security under key reuse, or tolerance to transmission loss.

The mathematical contributions are complete within those boundaries: a universal energy obstruction, a finite-key construction attaining the joint resource orders, and a sharp first-harmonic classification for independent phase randomization followed by Gaussian displacement. The [verification suite](../verification/README.md) checks the finite formulas and selected joint-state calculations. The infinite-dimensional conclusions rest on the analytic proofs in the scientific chapters.
