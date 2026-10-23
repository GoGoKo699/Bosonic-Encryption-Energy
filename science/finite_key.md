# Finite-key encryption and the key-cardinality law

The ciphertext-energy converse can be attained in order of growth with a finite classical key. The construction randomizes a finite block of Fock levels and preserves the high-energy tail reversibly. A separate random sign removes coherence between the two blocks. Since the tail has probability at most its mean-energy budget divided by the cutoff, the resulting secrecy error is explicit even when the plaintext is entangled with a reference.

This chapter proves the construction C1 and the matching key-cardinality lower bound K1. The finite-dimensional ingredient of K1 is the known approximate quantum Shannon bound of Desrosiers–Dupuis, with the squared fidelity factor noted by Lai–Chung. The new resource reduction here is to apply that bound to a rare, flagged entangled state that satisfies the oscillator's mean-energy constraint.

Throughout, the plaintext and ciphertext are each the single oscillator of [model.md](model.md). The key is classical and independent of the plaintext and its reference. Exact keyed recovery holds on the entire oscillator. We use $`T=\frac12\|\cdot\|_1`$, the fixed-replacer error $`\delta_E(\mathcal C;\tau)`$, and the optimized error $`\delta_E^*(\mathcal C)`$ defined there.

## 1. C1: a finite Fock-block construction

Choose an integer $`d\ge1`$ and define

```math
P_d=\sum_{j=0}^{d-1}|j\rangle\langle j|,
\qquad
Q_d=I-P_d,
\qquad
\pi_d=P_d/d.
```

On the $`d`$-dimensional subspace $`P_d\mathcal H`$, introduce the Weyl operators

```math
X_d|j\rangle=|(j+1)\bmod d\rangle,
\qquad
Z_d|j\rangle=e^{2\pi i j/d}|j\rangle,
\qquad
W_{ab}=X_d^aZ_d^b,
```

where $`0\le a,b<d`$. Their uniform average implements the usual finite-dimensional quantum one-time pad. This randomization mechanism is standard; see [Mosca–Tapp–de Wolf](https://arxiv.org/abs/quant-ph/0003101v2).

The secret key is a uniform triple $`(a,b,s)`$, where $`s\in\{+1,-1\}`$. Its encoder is the full-oscillator unitary

```math
U_{abs}=W_{ab}\oplus sI_{Q_d\mathcal H}.
```

The direct sum specifies the action on both subspaces. Decryption applies $`U_{abs}^\dagger`$, so recovery is exact on every oscillator state, with or without a reference. The scheme uses $`M=2d^2`$ keys.

### Theorem C1 — Exact security and energy formulas

Let $`\mathcal C_d`$ be the average of the unitary channels $`U_{abs}`$. For every joint state $`\rho_{AR}`$,

```math
(\mathcal C_d\otimes\mathrm{id}_R)(\rho_{AR})
=\pi_d\otimes\rho_R^{\rm low}+\rho_{AR}^{\rm high},
```

where

```math
\rho_R^{\rm low}
=\mathrm{Tr}_A[(P_d\otimes I_R)\rho_{AR}(P_d\otimes I_R)],
\qquad
\rho_{AR}^{\rm high}
=(Q_d\otimes I_R)\rho_{AR}(Q_d\otimes I_R).
```

These operators are subnormalized. Writing $`q=\mathrm{Tr}(Q_d\rho_A)`$, the secrecy error relative to $`\pi_d`$ is exactly

```math
T\!\left[(\mathcal C_d\otimes\mathrm{id}_R)(\rho_{AR}),
         \pi_d\otimes\rho_R\right]=q.
```

Consequently, for every $`E\ge0`$,

```math
\boxed{\delta_E(\mathcal C_d;\pi_d)=\min\{1,E/d\}.}
```

The average ciphertext of the vacuum is $`\pi_d`$, so

```math
\boxed{C_{\rm vac}=\frac{d-1}{2}.}
```

For an arbitrary input of finite mean photon number,

```math
\mathrm{Tr}[N\mathcal C_d(\rho_A)]
=\frac{d-1}{2}\mathrm{Tr}(P_d\rho_A)
 +\mathrm{Tr}(NQ_d\rho_AQ_d).
```

In particular, the supremum of the average-key output energy over allowed inputs is

```math
\boxed{C_{\max}(E)=E+\frac{d-1}{2}.}
```

For every individual key and every allowed input, the output energy is at most $`E+d-1`$.

### Proof of the averaged-channel formula

First average over $`s`$. The low/high off-diagonal blocks acquire opposite signs and cancel. The high/high block is unchanged. For a low-block matrix unit,

```math
\frac1{d^2}\sum_{a,b=0}^{d-1}
W_{ab}|i\rangle\langle j|W_{ab}^\dagger
=\delta_{ij}\pi_d.
```

Indeed, the $`b`$-sum is zero for $`i\ne j`$ and leaves $`|i\rangle\langle i|`$ when $`i=j`$; the subsequent $`a`$-sum distributes that basis vector uniformly over the block. Expanding the low block as

```math
\sum_{i,j=0}^{d-1}|i\rangle\langle j|\otimes R_{ij}
```

therefore gives $`\pi_d\otimes\sum_iR_{ii}=\pi_d\otimes\rho_R^{\rm low}`$. This is an operator identity on the reference, so the proof does not assume an uncorrelated or classical input.

The sign bit has a specific role: it makes the low/high cancellation exact. Extending a finite-dimensional twirl by the identity does not, by itself, specify a vanishing average on off-diagonal blocks.

### Proof of the secrecy formula

Partial tracing over the oscillator removes low/high cross terms, hence

```math
\rho_R=\rho_R^{\rm low}+\rho_R^{\rm high},
\qquad
\rho_R^{\rm high}=\mathrm{Tr}_A\rho_{AR}^{\rm high}.
```

Subtracting the replacer output gives

```math
\Delta_{AR}
=\rho_{AR}^{\rm high}-\pi_d\otimes\rho_R^{\rm high}.
```

The two terms are positive, each has trace $`q`$, and their oscillator supports are orthogonal: the first lies in $`Q_d\mathcal H`$, the second in $`P_d\mathcal H`$. Therefore

```math
\|\Delta_{AR}\|_1=2q,
\qquad
T=q.
```

Since $`N\ge dQ_d`$, the energy bound gives $`q\le E/d`$, and always $`q\le1`$. For $`E\le d`$, equality is attained by

```math
\rho_A=(1-E/d)|0\rangle\langle0|+(E/d)|d\rangle\langle d|.
```

For $`E\ge d`$, the input $`|d\rangle\langle d|`$ attains error one. This proves the exact supremum. It is an exact formula for the stated replacer $`\pi_d`$; no claim that this replacer minimizes $`\delta_E(\mathcal C_d;\tau)`$ over all $`\tau`$ is needed.

### Proof of the energy formulas

The averaged-channel formula gives

```math
\mathrm{Tr}[N\mathcal C_d(\rho_A)]
=e_d(1-q)+h,
\qquad
e_d=(d-1)/2,
\qquad
h=\mathrm{Tr}(NQ_d\rho_AQ_d).
```

The vacuum has $`q=h=0`$. For any allowed input, $`h\le E`$, so the output energy is at most $`e_d+E`$. To show this is the supremum when $`E>0`$, take integers $`n\ge\max\{d,E\}`$ and inputs

```math
\rho_A^{(n)}=(1-E/n)|0\rangle\langle0|+(E/n)|n\rangle\langle n|.
```

Their energy is $`E`$ and their average ciphertext energy is

```math
E+e_d(1-E/n)\longrightarrow E+e_d.
```

The supremum need not be attained when $`d\ge2`$ and $`E>0`$. For $`E=0`$ the only allowed input is the vacuum, which gives the same formula. Finally, for each individual key the low-block output is supported on photon numbers at most $`d-1`$, while the tail energy is unchanged. This yields the per-key bound $`E+d-1`$. $`\square`$

### Choosing the cutoff

For $`E>0`$ and $`\epsilon>0`$, choose

```math
d=\max\left\{1,\left\lceil E/\epsilon\right\rceil\right\}.
```

The construction then has exact recovery, secrecy at most $`\epsilon`$, and

```math
M=2d^2,
\qquad
C_{\rm vac}=\frac{d-1}{2}<\frac{E}{2\epsilon},
\qquad
C_{\max}(E)<E+\frac{E}{2\epsilon}.
```

When $`E=0`$, no encryption is needed because the oscillator must be in the vacuum and cannot be entangled with a reference. The nontrivial asymptotic regime is $`E>0`$ and small $`\epsilon`$.

C1 is an information-theoretic construction using ideal Fock-block unitaries. It gives a finite key and exact full-oscillator recovery; it does not establish an efficient optical implementation of those unitaries. The phase/displacement construction in [gaussian_encryption.md](gaussian_encryption.md) addresses a different implementation model, with a continuous displacement key.

## 2. The known finite-dimensional key lemma

The lower bound uses a standard quantum Shannon argument. It is included in full to specify the trace-distance convention and to avoid an unnecessary assumption that the ciphertext or decoder output is finite-dimensional.

The exact-correctness inequality is due to [Desrosiers–Dupuis, DD2010](https://arxiv.org/abs/0707.0691v2). [Lai–Chung, LC2019](https://arxiv.org/abs/1801.03656v2), equation (1) and the note concerning DD2010 equation (41), explicitly record the corrected squared factor. Their broader result also treats imperfect correctness. We use only the exact-correctness lemma below; its finite-dimensional content is prior work.

### Lemma — Approximate quantum Shannon bound

Let $`R`$ be $`d`$-dimensional and let $`\Phi_d`$ be maximally entangled between $`R`$ and a $`d`$-dimensional subspace of the plaintext. Suppose a scheme uses a finite classical key alphabet of size $`M`$, with arbitrary probabilities, and has exact keyed recovery on this subspace. If

```math
\omega_{RC}
=(\mathrm{id}_R\otimes\overline{\mathcal E})(\Phi_d),
\qquad
T(\omega_{RC},\pi_R\otimes\tau_C)\le\delta<1,
\qquad
\pi_R=I_R/d,
```

then

```math
\boxed{M\ge d^2(1-\delta)^2.}
```

The conclusion permits a separable infinite-dimensional ciphertext and decoder output, and allows a mixed private ancilla in the encoder. It is a cardinality bound, not a bound of the same form on the Shannon entropy of an arbitrary nonuniform key.

### Proof

Use the unsquared fidelity convention

```math
F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1.
```

The Fuchs–van de Graaf inequality gives $`F(\omega_{RC},\pi_R\otimes\tau_C)\ge1-\delta`$. Retain the key in the state

```math
\omega_{RCK}
=\sum_{k=1}^{M}p_k\omega^k_{RC}\otimes|k\rangle\langle k|,
\qquad
\omega^k_{RC}
=(\mathrm{id}_R\otimes\mathcal E_k)(\Phi_d).
```

By the extension form of Uhlmann's theorem, $`\pi_R\otimes\tau_C`$ has an extension $`\zeta_{RCK}`$ with

```math
F(\omega_{RCK},\zeta_{RCK})\ge1-\delta.
```

Dephase the extension in the key basis. This does not change its $`RC`$ marginal, and fidelity cannot decrease because $`\omega_{RCK}`$ was already classical on $`K`$. We may therefore write

```math
\zeta_{RCK}=\sum_{k=1}^{M}\zeta^k_{RC}\otimes|k\rangle\langle k|,
\qquad
\sum_{k=1}^{M}\zeta^k_{RC}=\pi_R\otimes\tau_C,
\qquad
0\le\zeta^k_{RC}\le\pi_R\otimes\tau_C.
```

Apply the decoder controlled by $`K`$ and then discard $`K`$. Exact correctness maps $`\omega_{RCK}`$ to $`\Phi_d`$. The same channel maps $`\zeta_{RCK}`$ to

```math
\zeta'_{RA'}
=\sum_{k=1}^{M}
 (\mathrm{id}_R\otimes\mathcal D_k)(\zeta^k_{RC}).
```

Fidelity contraction and the purity of $`\Phi_d`$ imply

```math
\mathrm{Tr}(\Phi_d\zeta'_{RA'})
=F(\Phi_d,\zeta'_{RA'})^2
\ge(1-\delta)^2.
```

On the other hand, positivity of every decoder and the block inequality give

```math
\begin{aligned}
\mathrm{Tr}(\Phi_d\zeta'_{RA'})
&\le
\sum_{k=1}^{M}
\mathrm{Tr}\!\left[
 \Phi_d(\pi_R\otimes\mathcal D_k(\tau_C))
\right]\\
&=
\frac1{d^2}\sum_{k=1}^{M}
\mathrm{Tr}[P_d\mathcal D_k(\tau_C)]\\
&\le\frac{M}{d^2}.
\end{aligned}
```

Here $`P_d`$ projects onto the target $`d`$-dimensional output subspace. The last line is an inequality: an infinite-dimensional decoder may place part of $`\mathcal D_k(\tau_C)`$ outside that subspace. Positivity and trace preservation are sufficient. Combining the lower and upper bounds on the overlap proves the lemma. $`\square`$

Uhlmann's theorem is used only to extend a state, not to give the adversary or decoder access to an additional system. One may purify on a sufficiently large separable space before taking the extension, so the argument does not depend on a finite ciphertext dimension.

## 3. K1: the energy-constrained key-cardinality converse

### Theorem K1 — Finite-key lower bound

Let $`E>0`$ and let a single-oscillator encryption scheme have exact keyed recovery on the full oscillator, a finite key alphabet of size $`M`$, and $`\delta_E^*(\overline{\mathcal E})\le\epsilon`$. For each integer $`d\ge2`$, define

```math
r_d=\min\left\{1,\frac{2E}{d-1}\right\}.
```

Then, whenever $`\epsilon<r_d`$,

```math
\boxed{
M\ge d^2\left(1-\frac{\epsilon}{r_d}\right)^2.
}
```

Equivalently, the right side may be written with a positive part for all parameters. The dilution probability $`r_d`$ can reach one here, unlike the $`p_d\le1/2`$ used in the vacuum-energy comparison E2.

### Proof

Let $`R`$ be $`d`$-dimensional, let $`F`$ be a two-dimensional flag, and take

```math
\Omega_{ARF}
=(1-r_d)|0\rangle\langle0|_A\otimes\pi_R\otimes|0\rangle\langle0|_F
 +r_d\Phi_{d,AR}\otimes|1\rangle\langle1|_F.
```

The reference is $`RF`$. Its marginal is

```math
\Omega_{RF}
=\pi_R\otimes\big[(1-r_d)|0\rangle\langle0|_F
                         +r_d|1\rangle\langle1|_F\big],
```

and the input energy is $`r_d(d-1)/2\le E`$.

For a secrecy witness $`\tau_C`$, trace distance splits across the two flag blocks. In particular, its nonnegative high-block contribution satisfies

```math
r_d\,
T\!\left[
 (\overline{\mathcal E}\otimes\mathrm{id}_R)(\Phi_d),
 \tau_C\otimes\pi_R
\right]
\le\epsilon.
```

There is no factor of two from a triangle inequality: the reference flag directly isolates this block. The finite-dimensional key lemma, applied with $`\delta=\epsilon/r_d`$, proves the result. For an infimum over replacers, use an approximating witness and pass to the limit. $`\square`$

The proof differs from a rank argument for a random-unitary channel. A reversible CPTP encoder may append mixed randomness and produce ciphertexts of unbounded rank. K1 remains valid because the controlled-decoder argument counts classical key branches rather than ciphertext rank.

### Explicit cardinality and fixed-length bounds

For $`E>0`$ and $`0<\epsilon\le1/2`$,

```math
\boxed{M\ge\max\left\{1,\frac{E^2}{4\epsilon^2}\right\}.}
```

For $`E/\epsilon\ge1`$, choose $`d=\lfloor E/\epsilon\rfloor+1`$. Then

```math
\frac{\epsilon}{r_d}
=\max\left\{\epsilon,\frac{\epsilon(d-1)}{2E}\right\}
\le\frac12,
```

so K1 gives $`M\ge d^2/4\ge E^2/(4\epsilon^2)`$. For $`E/\epsilon<1`$, the assertion follows from $`M\ge1`$.

If the key cost is measured by the logarithm of its alphabet size, this implies

```math
\log_2 M\ge2\log_2(E/\epsilon)-2.
```

C1, with $`d=\lceil E/\epsilon\rceil`$ in the regime $`E/\epsilon\ge1`$, gives

```math
M=2\lceil E/\epsilon\rceil^2,
\qquad
\log_2 M
=2\log_2(E/\epsilon)+O(1).
```

Thus the optimal finite key-alphabet size has order $`(E/\epsilon)^2`$. If an exactly uniform binary key of fixed integer length is desired, choose a power-of-two cutoff

```math
d=2^{\lceil\log_2\max\{1,E/\epsilon\}\rceil}.
```

Then the construction uses precisely $`1+2\log_2d`$ uniform bits and changes the energy and cardinality bounds by only constant factors. The lower bound applies to any key probabilities; it does not identify the optimum variable-length or Shannon-entropy key cost for nonuniform schemes.

## 4. The joint resource statement

In the regime of small secrecy error and $`E/\epsilon\to\infty`$, the two resource laws are attained by the same exactly reversible finite-key scheme:

```math
C_{\rm vac}=\Theta(E/\epsilon),
\qquad
M=\Theta((E/\epsilon)^2),
\qquad
\log_2M=2\log_2(E/\epsilon)+O(1).
```

For the energy lower bound, use E2 in [energy_cost.md](energy_cost.md); for the key lower bound, use K1. The upper bounds come from C1. These are separate lower bounds with a common construction achieving both orders, not a claim that every scheme lies on a fully determined energy-versus-key tradeoff curve.

The classical flag has different roles in the two converses. E2 compares a diffuse ciphertext to the ciphertext of the vacuum and uses $`p_d\le1/2`$ to control their distance. K1 isolates an entangled branch and can use $`r_d\le1`$. The entangled reference is what transfers the finite-dimensional quantum Shannon bound with its $`d^2`$ dependence; an unassisted state-randomization criterion would be a different task.

The finite key and full-oscillator reversibility also distinguish C1 from physically truncating and discarding the tail. Every key acts unitarily on the entire Hilbert space. The tail's information remains recoverable by the authorized recipient, while its probability bounds its contribution to the adversary's distinguishing advantage.

## Sources used in this chapter

- **MTW2000:** Michele Mosca, Alain Tapp, and Ronald de Wolf, *Private Quantum Channels and the Cost of Randomizing Quantum Information*, [arXiv:quant-ph/0003101v2](https://arxiv.org/abs/quant-ph/0003101v2). Standard quantum one-time-pad background. The related FOCS 2000 publication includes Andris Ambainis and has bibliography key `ambainis2000private`.
- **DD2010:** Simon Pierre Desrosiers and Frédéric Dupuis, *Quantum entropic security and approximate quantum encryption*, IEEE Transactions on Information Theory 56, 3455–3464 (2010); [arXiv:0707.0691v2](https://arxiv.org/abs/0707.0691v2), [DOI](https://doi.org/10.1109/TIT.2010.2048488). Known approximate quantum Shannon lemma; bibliography key `desrosiers2010entropic`.
- **LC2019:** Ching-Yi Lai and Kai-Min Chung, *Quantum encryption and generalized Shannon impossibility*, Designs, Codes and Cryptography 87, 1961–1972 (2019); [DOI](https://doi.org/10.1007/s10623-018-00597-3). The [arXiv:1801.03656v2 preprint](https://arxiv.org/abs/1801.03656v2) is titled *Quantum Encryption and Generalized Quantum Shannon Impossibility*. Equation (1), the squared-factor correction, and imperfect-correctness extensions; bibliography key `lai2019encryption`.
- **FvdG1999:** Christopher A. Fuchs and Jeroen van de Graaf, *Cryptographic Distinguishability Measures for Quantum Mechanical States*, IEEE Transactions on Information Theory 45, 1216–1227 (1999); [arXiv:quant-ph/9712042v2](https://arxiv.org/abs/quant-ph/9712042v2). Fidelity/trace-distance inequalities; bibliography key `fuchs1999cryptographic`.
- **Uhlmann1976:** Armin Uhlmann, *The “transition probability” in the state space of a $`*`$-algebra*, Reports on Mathematical Physics 9, 273–279 (1976); [DOI](https://doi.org/10.1016/0034-4877(76)90060-4). Purification and state-extension fidelity; bibliography key `uhlmann1976transition`.

The broader comparison with continuous-variable encryption is in [RELATED_WORK.md](../references/RELATED_WORK.md). The standard finite-dimensional key lemma and Weyl twirl are explicitly separated above from the oscillator energy constraint and its flagged-state reduction.
