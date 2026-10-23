# From Gaussian quantum information to energy-constrained encryption

The task is to encrypt an unknown state of one oscillator while preserving its exact recovery by a receiver who knows the key. The plaintext may be entangled with another system and may have an arbitrarily long photon-number tail. Its only size constraint is a bound on its mean photon number. The project connects this task to two resource questions: how much energy the ciphertext must carry, and how phase randomization changes the noise needed by an optical construction.

The single educational anchor is **Christian Weedbrook et al., _Gaussian Quantum Information_, Reviews of Modern Physics 84, 621–669 (2012)**: [published article](https://doi.org/10.1103/RevModPhys.84.621), [selected arXiv:1110.3234v1 PDF](https://arxiv.org/pdf/1110.3234v1), and [HTML of that version](https://arxiv.org/html/1110.3234v1). The selected preprint is dated October 14, 2011. Section, equation, and page pointers below refer to that PDF, whose printed page numbers coincide with its PDF page numbers. They are not the journal's page numbers.

The [30-milestone map](MILESTONES.md) organizes the project's understanding targets. This bridge translates the anchor into the project's notation and supplies the conceptual connections to the canonical proofs in [science/](../science/model.md). The research papers cited for particular theorem ingredients remain attribution and proof dependencies; they are not additional educational anchors.

## Selective reading route

The useful route is selective. Read the indicated source passage alongside the corresponding project account.

| Step | Anchor passage in the selected PDF | Connection to this project |
|---|---|---|
| 1. Identify the carrier | I.D and II.A–II.A.1, pp. 4–6; Eqs. (3)–(7), (14)–(20) | Fock levels, quadratures, and moments give the objects in [the model, §1](../science/model.md#1-carrier-and-message-family). Keep the difference between a mean-energy constraint and a finite-dimensional Hilbert space visible. |
| 2. Identify the keyed controls | II.A.2 and II.B.1, II.B.2, II.B.4, pp. 6–7; Eqs. (22)–(28), (34) | Translate displacements, phase rotations, and thermal states into [G1–G3](../science/gaussian_encryption.md). A key chooses an invertible operation even when the key-averaged channel loses information. |
| 3. Interpret distinguishability | III.A.1 and III.A.3, pp. 13–14; Eqs. (67)–(69), (79) | Connect state discrimination to [the secrecy metric](../science/model.md#3-secrecy-and-distance-convention). Check the trace-distance and fidelity conventions below before reading G1 or K1. |
| 4. Understand the lower-bound experiments | II.E.1–II.E.2, p. 12; Eq. (63) and the heterodyne POVM | Homodyne and heterodyne outcomes provide witnesses in [G1](../science/gaussian_encryption.md#g1-standard-factorization-and-the-displacement-only-benchmark), [P1](../science/phase_criterion.md#p1-the-first-harmonic-criterion), and [the displacement comparison](../science/displacement_comparison.md). A measurement gives a lower bound on quantum distinguishability. |
| 5. Understand the channel identity | V.A–V.B, pp. 20–22; Eqs. (107)–(110), Table I / Eq. (113), and Eqs. (116)–(117) | Loss, amplification, and additive noise lead to the analytical factorization in G1. The characteristic-function check below explains why it applies to arbitrary plaintexts. |
| 6. Add an optical picture if useful | II.B.6–II.B.7, p. 8 | The beam splitter and two-mode squeezing give pictures for the auxiliary loss and amplifier channels. Those auxiliary channels are used in the proof, not as the keyed encoder. |
| 7. Locate the cryptographic task boundary | Opening of VI and VI.A.1, pp. 27–28 | The review's QKD discussion concerns generating a shared secret key. This project assumes an independent shared key and studies encryption of a quantum plaintext. |

The HTML uses numbered subsections where the PDF uses letters: PDF I.D is HTML I.4; II.A.1 is II.1.1; II.B.4 is II.2.4; II.E.2 is II.5.2; III.A.3 is III.1.3; V.B is V.2; and VI.A.1 is VI.1.1. Search by the section title when changing formats.

The Gaussian capacity, cluster-computing, and detailed QKD-security sections are not prerequisites for the project proofs. The bridge below supplies the missing route to the oscillator energy and key converses.

## Notation dictionary

### Quadrature units, photon number, and covariance

Use the subscript $`W`$ for the review's quadratures. To avoid a collision with the project's noise parameter $`V`$, call the review's covariance matrix $`\Gamma_W`$ here; it is printed as $`V`$ in the review.

| Object | Review convention | Project convention and translation |
|---|---|---|
| Annihilation operator | $`a=(q_W+ip_W)/2`$ | The same $`a=(q+ip)/\sqrt2`$ |
| Quadratures | $`q_W=a+a^\dagger`$, $`p_W=i(a^\dagger-a)`$ | $`q=q_W/\sqrt2`$, $`p=p_W/\sqrt2`$ |
| Commutator | $`[q_W,p_W]=2i`$ | $`[q,p]=i`$ |
| Covariance matrix | $`(\Gamma_W)_{ij}=\langle\{\Delta x_{W,i},\Delta x_{W,j}\}\rangle/2`$ | $`\Gamma=\Gamma_W/2`$ |
| Vacuum covariance | $`I_2`$ | $`I_2/2`$ |
| Number operator | $`\hat n=a^\dagger a`$; the review also uses $`N`$ for the number of modes | $`N=a^\dagger a`$; this project has one ciphertext mode |
| Thermal state | $`\rho_{\rm th}(\bar n)`$ with covariance $`(2\bar n+1)I_2`$ | Mean photon number remains $`\bar n`$; covariance becomes $`(\bar n+1/2)I_2`$ |
| Coherent amplitude | $`\alpha=(\bar q_W+i\bar p_W)/2`$ | The same physical amplitude $`\alpha=(\bar q+i\bar p)/\sqrt2`$; no rescaling of $`\alpha`$ |

These translations follow from I.D, Eqs. (6)–(7), covariance definition (15), thermal state (27), and displacement definition (28). The same displacement operator is used in both conventions:

```math
D(\alpha)=e^{\alpha a^\dagger-\bar\alpha a},
\qquad
D(\alpha)^\dagger aD(\alpha)=a+\alpha.
```

Consequently, its shift of the project quadratures is $`\sqrt2(\mathrm{Re}\,\alpha,\mathrm{Im}\,\alpha)`$, while its shift of the review's quadratures is twice the real and imaginary parts. The dimensionless physical excitation, $`\langle N\rangle`$, does not change when quadrature coordinates change. In particular,

```math
\langle N\rangle
=\frac{\mathrm{Tr}\,\Gamma+\|\bar x\|^2-1}{2}
=\frac{\mathrm{Tr}\,\Gamma_W+\|\bar x_W\|^2-2}{4}.
```

This identity also shows why finite mean photon number supplies finite quadrature second moments, while it does not require finite photon-number variance $`\langle N^2\rangle-\langle N\rangle^2`$. These are different moment conditions.

### Phase sign

The project uses

```math
R(\theta)=e^{i\theta N},
\qquad
R(\theta)|n\rangle=e^{in\theta}|n\rangle.
```

The review's operator definition beside Eq. (34) is $`R_W(\theta)=e^{-i\theta N}`$. Hence $`R(\theta)=R_W(-\theta)`$. Direct conjugation gives

```math
\begin{aligned}
R_W(\theta)^\dagger aR_W(\theta)&=e^{-i\theta}a,\\
R(\theta)^\dagger aR(\theta)&=e^{i\theta}a,\\
R(\theta)^\dagger
\begin{pmatrix}q\\p\end{pmatrix}
R(\theta)
&=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}
\begin{pmatrix}q\\p\end{pmatrix}.
\end{aligned}
```

**Source-version note.** In arXiv v1, the sentence adjacent to Eq. (34) prints $`a\mapsto e^{i\theta}a`$ for the review's rotation. That sign disagrees with its displayed unitary and rotation matrix under the Heisenberg convention of Eq. (22). The translation above follows the unitary and matrix. At $`\theta=\pi`$ both sign choices give photon parity $`(-1)^N`$.

### Additive-noise parameters

The project's scalar $`V>0`$ is defined by the distribution of the complex displacement key:

```math
p_V(\alpha)=\frac{e^{-|\alpha|^2/V}}{\pi V},
\qquad
\mathbb E|\alpha|^2=V,
\qquad
\mathrm{Var}(\mathrm{Re}\,\alpha)
=\mathrm{Var}(\mathrm{Im}\,\alpha)=V/2.
```

It follows that the displacement adds quadrature covariance $`VI_2`$ in project units and $`2VI_2`$ in review units:

```math
\Gamma\longmapsto\Gamma+VI_2,
\qquad
\Gamma_W\longmapsto\Gamma_W+2VI_2.
```

In review Eq. (108), the channel matrices are therefore $`T=I_2`$ and $`N_{\rm noise}=2VI_2`$. In the additive-noise class $`B_2`$ of Table I, the printed parameter $`\bar n`$ satisfies **$`\bar n_{B_2}=2V`$**. Its use as a channel-noise parameter should not be confused with the mean photon number of a thermal state. The encrypted vacuum here is $`\tau_V=\rho_{\rm th}(V)`$, with mean photon number $`V`$ and review covariance $`(2V+1)I_2`$.

The project uses $`\eta`$ for loss transmissivity and $`G`$ for amplifier power gain. These correspond to the review's $`\tau`$ in the loss and amplifier classes, respectively. For the quantum-limited channels the environmental thermal photon number is zero. In review units their parameters are

```math
\begin{array}{c|cc}
\text{channel}&T&N_{\rm noise}\\ \hline
\mathcal L_\eta&\sqrt\eta\,I_2&(1-\eta)I_2\\
\mathcal A_G&\sqrt G\,I_2&(G-1)I_2.
\end{array}
```

These symbols are also distinct from the project's replacement state $`\tau`$ and number operator $`N`$.

### Trace distance and fidelity

The review's $`D(\rho,\sigma)`$ in Eq. (68) equals the project's $`T(\rho,\sigma)=\|\rho-\sigma\|_1/2`$. Equal-prior state discrimination succeeds with probability $`(1+T)/2`$. A distance bound $`T\le\varepsilon`$ limits the difference between probabilities of any event to $`\varepsilon`$; the advantage of a binary guessing experiment above $`1/2`$ is at most $`\varepsilon/2`$.

The review's fidelity in Eq. (79) is squared. The proofs in this project use root fidelity:

```math
F_{\rm project}(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1,
\qquad
F_{\rm review}(\rho,\sigma)=F_{\rm project}(\rho,\sigma)^2.
```

Keeping this square explicit matters in the key bound $`M\ge d^2(1-\delta)^2`$.

## From Gaussian channels to security for arbitrary states

The anchor provides a compact language for Gaussian states and Gaussian channels. The security question quantifies over every allowed joint state $`\rho_{AR}`$, including non-Gaussian states and entangled references. A calculation of first and second moments does not determine such an arbitrary state.

This distinction does not prevent the use of Gaussian-channel identities. In [G1](../science/gaussian_encryption.md#g1-standard-factorization-and-the-displacement-only-benchmark), the equality

```math
\mathcal N_V
=\mathcal A_{V+1}\circ\mathcal L_{1/(V+1)}
```

is an equality of channels on all oscillator states. For example, let $`\chi_\rho(z)=\mathrm{Tr}[\rho D(z)]`$. The loss and amplifier characteristic-function rules give

```math
\chi_{(\mathcal A_G\circ\mathcal L_\eta)(\rho)}(z)
=\chi_\rho(\sqrt{G\eta}\,z)
\exp\!\left[-\frac{G(1-\eta)+G-1}{2}|z|^2\right].
```

With $`G=V+1`$ and $`\eta=1/G`$, this becomes $`\chi_\rho(z)e^{-V|z|^2}`$, the characteristic function of Gaussian displacement noise. Characteristic functions determine arbitrary trace-class states. The identity therefore remains valid when the channel is tensored with the identity on a reference. The detailed standard attribution is in G1, to [Ivan–Sabapathy–Simon](../references/RELATED_WORK.md#ivan2011operatorsum) and [Mishra–Khabbazi Oskouei–Wilde](../references/RELATED_WORK.md#mishra2023teleportation).

For the proof, this converts large displacement noise into small transmissivity. If the attenuated joint state is close to $`|0\rangle\langle0|\otimes\rho_R`$, applying the amplifier preserves an upper bound on that distance and sends vacuum to $`\tau_V`$. The sender's actual encoder remains the keyed unitary $`D(\alpha)R(\theta)`$. Its inverse is $`R(\theta)^\dagger D(-\alpha)`$; the mathematical attenuation is not a physical step that the receiver must undo.

There is a second distinction between a keyed operation and its average. Every selected displacement and phase rotation is Gaussian and acts on arbitrary input states. Their random average need not be a Gaussian channel. For instance, parity averaging sends a nonzero coherent state to the mixture of its two opposite amplitudes. Its quadrature distribution is a two-component Gaussian mixture, which is not a single Gaussian. The project neither restricts the plaintext to Gaussian states nor applies a Gaussian-extremality assumption to its security supremum.

## The steps supplied by this project

### 1. A reference-aware secrecy target and a mean-energy tail

The [model](../science/model.md) asks for one input-independent ciphertext state $`\tau`$ such that

```math
\delta_E(\mathcal C;\tau)
=\sup_{\rho_{AR}:\,\mathrm{Tr}(N\rho_A)\le E}
\frac12\left\|
(\mathcal C\otimes\mathrm{id}_R)(\rho_{AR})
-\tau\otimes\rho_R
\right\|_1
\le\varepsilon.
```

The ciphertext must be nearly independent of both the plaintext and its correlation with $`R`$. This is half the energy-constrained diamond distance from a replacement channel. The general norm framework is an imported mathematical ingredient, attributed to [Shirokov](../references/RELATED_WORK.md#shirokov2018energy) and [Winter](../references/RELATED_WORK.md#winter2017energy); the encryption reductions are supplied in the project.

A mean-energy constraint permits a probability $`E/n`$ of photon number $`n`$ for arbitrarily large $`n`$. The reference may record that branch. Discarding the branch as atypical would change the security problem. The elementary bound $`\mathrm{Tr}(Q_d\rho_A)\le E/d`$, where $`Q_d`$ projects onto levels at least $`d`$, instead controls its contribution without assuming finite support.

When deriving a lower bound with two plaintexts, keep two uses of trace distance separate. A measured total variation distance $`t`$ proves that their output trace distance is at least $`t`$. For an arbitrary common replacement target, the triangle inequality then gives error at least $`t/2`$. This extra factor is already accounted for in G1 and P1.

### 2. Exact recovery forces a diffuse ciphertext

The recovery condition is $`\mathcal D_k\mathcal E_k=\mathrm{id}`$ for every key in use. The energy converse allows arbitrary reversible CPTP encoders, including private ancillary randomness. It is broader than the optical construction.

For a uniform state $`\pi_d=P_d/d`$ on the first $`d`$ Fock levels, exact recovery preserves the perfect distinguishability of those levels. Their encoded states therefore have orthogonal supports. [E1](../science/energy_cost.md#2-e1-exact-recovery-preserves-diffuseness) turns this into

```math
\overline{\mathcal E}(\pi_d)\le I/d,
\qquad
\mathrm{Tr}\!\left[P_m\overline{\mathcal E}(\pi_d)\right]\le m/d.
```

The second inequality limits how much ciphertext probability can fit inside any $`m`$-dimensional subspace. In one oscillator, the lowest $`m`$ energy levels span exactly such a subspace.

The mean energy of $`\pi_d`$ is $`(d-1)/2`$, so a large $`d`$ cannot be tested directly at fixed $`E`$. [E2](../science/energy_cost.md#4-e2-a-universal-ciphertext-energy-converse) inserts this state with a small, reference-flagged probability. Secrecy then forces its diffuse ciphertext to be close to the encrypted vacuum. Summing the probabilities above each energy threshold gives a lower bound on the vacuum ciphertext's mean photon number. Choosing the block dimension at order $`E/\varepsilon`$ yields the universal energy scaling.

This argument is a spectral and recoverability argument, not a covariance argument. It charges the ciphertext's excitation at a fixed oscillator frequency. It does not compute control work, heat dissipation, or the energy needed to generate the key.

### 3. A finite key can attain the same energy order

In [C1](../science/finite_key.md#1-c1-a-finite-fock-block-construction), a finite-dimensional Weyl randomization acts on the first $`d`$ levels. A separate random relative sign cancels coherence between that block and its complement. Every key is a unitary on the entire oscillator:

```math
U_{abs}=W_{ab}\oplus sI_{Q_d\mathcal H},
\qquad s\in\{-1,+1\}.
```

Thus the high-energy tail remains exactly recoverable. Its probability, rather than a discarded-tail approximation, determines the secrecy error:

```math
\delta_E(\mathcal C_d;\pi_d)=\min\{1,E/d\},
\qquad
M=2d^2,
\qquad
C_{\rm vac}=(d-1)/2.
```

This block-relative sign is different from the optical parity $`(-1)^N`$. The construction uses ideal Fock-block unitaries and supplies a finite total key. It does not establish that those unitaries have the same implementation cost as a displacement and phase plate.

### 4. The key converse needs entanglement as well as orthogonality

E1 only uses distinguishable Fock labels. The $`d^2`$ key-cardinality dependence requires recovery of their quantum coherence. [K1](../science/finite_key.md#3-k1-the-energy-constrained-key-cardinality-converse) therefore uses a maximally entangled state on a $`d`$-dimensional subspace, diluted by a reference flag to obey the mean-energy bound.

The imported finite-dimensional ingredient is the approximate quantum Shannon lemma of [Desrosiers–Dupuis](../references/RELATED_WORK.md#desrosiers2010entropic), with the squared fidelity factor explicitly recorded by [Lai–Chung](../references/RELATED_WORK.md#lai2019encryption). Its form here is

```math
T\!\left[
(\mathrm{id}\otimes\overline{\mathcal E})(\Phi_d),
\pi_R\otimes\tau
\right]\le\delta<1
\quad\Longrightarrow\quad
M\ge d^2(1-\delta)^2.
```

The science chapter gives the complete extension and controlled-decoder proof, including the use of Uhlmann's theorem and fidelity contraction. The proof permits infinite-dimensional ciphertexts and arbitrary key probabilities. It counts key labels; it does not assume that ciphertext rank is bounded by the number of keys.

After energy dilution, the result is a cardinality law $`M=\Theta((E/\varepsilon)^2)`$. The matching construction can use $`2\log_2(E/\varepsilon)+O(1)`$ uniform fixed-length bits. A cardinality bound for arbitrary priors is not a matching Shannon-entropy bound for arbitrary nonuniform keys.

### 5. One Fourier coefficient controls the optical exponent

Let the independent phase law be $`\mu`$ and set

```math
m_k=\int e^{ik\theta}\,d\mu(\theta),
\qquad
\Phi_\mu(|n\rangle\langle n+k|)
=m_{-k}|n\rangle\langle n+k|.
```

The harmonic $`m_1`$ is a property of the phase distribution. It is distinct from the mean photon number and from the mean quadrature amplitude. If $`m_1=0`$, every adjacent Fock coherence vanishes, including its operator coefficient on the reference. Requiring only $`\langle a\rangle=0`$ for a reduced state does not enforce that cancellation.

After the auxiliary loss channel, the probability of any nonvacuum output is at most $`\eta E`$. Without phase cancellation, a vacuum–one-photon coherence can remain at order $`\sqrt\eta`$. Cancellation removes that leading contribution. The remaining vacuum-to-excited cross block begins with two transmitted photons.

That observation alone is not a uniform proof under only a mean-energy constraint. [G3](../science/gaussian_encryption.md#g3-a-single-phase-bit-suffices-for-the-improved-exponent) supplies a weighted Cauchy–Schwarz argument over loss branches. The useful cancellation in its binomial sum, for integers $`0\le k\le n`$, is

```math
\frac{\binom nk}{n-k+1}
=\frac{\binom{n+1}k}{n+1}.
```

The factor $`1/(n+1)`$ turns the binomial second factorial-moment estimate into a bound involving only $`\sum_n np_n`$. Thus the proof does not silently assume a finite photon-number second moment. It yields

```math
\delta_E(\mathcal N_V\circ\Phi_\mu;\tau_V)
\le
\min\!\left\{1,\frac{E}{V+1}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}
\quad\text{when }m_1=0.
```

Uniform full phase averaging removes all number coherences and gives the stronger uniform bound $`E/(V+1)`$ in G2. A fair binary phase choice at zero and $`\pi`$ is enough for the displayed G3 bound.

[P1](../science/phase_criterion.md#p1-the-first-harmonic-criterion) completes the exponent statement with measurement witnesses. A nonzero $`m_1`$ leaves a vacuum–one-photon witness of order $`V^{-1/2}`$. A diagonal vacuum/one-photon witness prevents any phase law from improving beyond order $`V^{-1}`$ at fixed positive $`E`$. Thus the error has order $`V^{-1}`$ exactly when $`m_1=0`$, and otherwise has order $`V^{-1/2}`$, for a fixed independent phase law.

[P2](../science/phase_criterion.md#p2-one-bit-is-the-minimum-discrete-phase-entropy) shows that exact first-harmonic cancellation needs at least one bit of discrete phase entropy, attained by two equiprobable antipodal phases. This is **one additional phase bit**. The displacement key remains continuous. The phase statement does not provide a finite total key for the optical cipher.

Two qualifications matter when using the exponent. At very low $`E`$, the binary scheme has an intrinsic $`\sqrt E/(V+1)`$ contribution from vacuum–two-photon coherence. Also, a phase law whose imbalance changes with $`V`$ is governed by the finite-parameter bound [P3](../science/phase_criterion.md#p3-residual-phase-imbalance-and-control-accuracy), rather than by the fixed-law asymptotic dichotomy.

### 6. The QKD chapter addresses a different use of the key

The review's VI.A.1 describes a key-generation task: quantum communication produces correlated classical data, followed by classical processing to obtain a secret key. This project begins with an independent secret key and requires recovery of a quantum state, including its coherence with a reference. Its secrecy error, charged ciphertext energy, and exact-decoding condition are defined in [the model](../science/model.md).

Consequently, a QKD key-rate formula or a Gaussian-attack reduction is not an ingredient of the present proofs. The shared optical vocabulary does not transfer those security theorems to this encryption task. The established results here are single-use secrecy statements; they do not establish authentication, key reuse, or recovery after transmission loss.

## A finite-parameter example

Take an input mean-photon budget $`E=1`$ and target secrecy error $`\varepsilon=1/128`$. Two constructions illustrate different resources:

| Construction | Concrete parameters | Guaranteed error | Key and ciphertext energy |
|---|---|---|---|
| Finite Fock block, C1 | $`d=128`$ | Exactly $`1/128`$ relative to $`\pi_{128}`$ | $`M=2(128)^2=32768`$, hence 15 uniform bits; $`C_{\rm vac}=63.5`$ and $`C_{\max}(1)=64.5`$ photons |
| Gaussian displacement plus fair parity, G3 | $`V=256`$ | At most $`1/257+1/\sqrt{256\cdot257}<1/128`$ relative to $`\tau_{256}`$ | One phase bit in addition to the continuous displacement key; $`C_{\rm vac}=256`$ and $`C_{\max}(1)=257`$ photons |

For C1, the mean-energy promise allows probability $`1/128`$ in level 128, so the error bound is attained by a vacuum/level-128 mixture. The formula for $`C_{\max}`$ is a supremum over a different family of increasingly rare, increasingly energetic inputs; the same plaintext need not attain both resource extrema.

For the optical construction, the encrypted vacuum has project covariance $`256.5I_2`$ and review covariance $`513I_2`$. The review's additive-noise channel parameter is $`\bar n_{B_2}=512`$, while the thermal output's photon number is 256. This example checks the distinction between noise units, physical photons, and key resources. It does not compare the device work needed to implement the two encoders.

## Where each kind of claim is proved

| Kind of claim | Authoritative location |
|---|---|
| Gaussian-state language, optical controls, measurements, and channel conventions | The selected Weedbrook anchor, using the route above |
| Exact model, arbitrary-reference secrecy, and charged resources | [Model](../science/model.md) |
| Reversible-encoding diffuseness and the ciphertext-energy converse, including the separately stated approximate-correctness extension | [Energy cost](../science/energy_cost.md) |
| Full-oscillator finite-key construction and key-cardinality converse | [Finite key](../science/finite_key.md) |
| All-state channel factorization, displacement benchmark, full phase average, and parity bound | [Gaussian encryption](../science/gaussian_encryption.md) |
| First-harmonic criterion, minimum discrete phase entropy, and control imbalance | [Phase criterion](../science/phase_criterion.md) |
| Physical interpretation and limitations | [Interpretation](../science/interpretation.md) |
| Attribution of imported theorem ingredients and comparison with earlier encryption work | [Related work](../references/RELATED_WORK.md) |
| Meaning and scope of reproducible finite checks | [Verification guide](../verification/README.md) |
| The complete project understanding map | [Milestones M01–M30](MILESTONES.md) |

The canonical statements and complete proofs remain in the scientific chapters. This bridge identifies how the chosen source supports them and where the project supplies additional arguments.
