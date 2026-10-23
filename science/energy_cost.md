# Ciphertext energy required by reversible encryption

Encryption must make different plaintexts look alike to a reader without the key, while preserving their distinguishability for the authorized decoder. For one oscillator, preserving many distinguishable states has a physical cost: a state spread over many orthogonal directions cannot place all its probability in the lowest Fock levels. This chapter turns that observation into a finite-parameter lower bound on the energy of an encrypted vacuum.

The mean-energy assumption is central. It permits a plaintext to occupy a large Fock subspace with small probability, even when its average photon number is modest. A reference flag records when that event occurs. Secrecy must cover the flagged state as well as the vacuum, which forces the vacuum ciphertext to resemble an encoded, highly diffuse state.

The main result applies to arbitrary exactly reversible quantum channels, including encoders that use a mixed private ancilla. It does not require unitary encryption, Gaussian operations, a finite key alphabet, or a photon-number cutoff on the plaintext. The matching finite-key construction is given in [finite_key.md](finite_key.md).

## 1. Setting and notation

We use the single-oscillator model of [model.md](model.md). Both plaintext and ciphertext have Fock basis $`\{|n\rangle:n\ge0\}`$ and number operator

```math
N=\sum_{n=0}^{\infty}n|n\rangle\langle n|.
```

The secret classical key is independent of the plaintext and its reference. For each key $`k`$, normal CPTP maps $`\mathcal E_k`$ and $`\mathcal D_k`$ obey exact keyed recovery,

```math
\mathcal D_k\circ\mathcal E_k=\mathrm{id}.
```

The averaged encoder is $`\overline{\mathcal E}=\mathbb E_k\mathcal E_k`$. Define

```math
\tau_0=\overline{\mathcal E}(|0\rangle\langle0|),
\qquad
C_{\rm vac}=\mathrm{Tr}(N\tau_0).
```

An infinite value of $`C_{\rm vac}`$ is allowed. All energy bounds below are then automatically satisfied.

Trace distance is $`T(\rho,\sigma)=\frac12\|\rho-\sigma\|_1`$. Secrecy with a fixed replacer state $`\tau`$ means

```math
\delta_E(\overline{\mathcal E};\tau)
=
\sup_{\substack{\rho_{AR}\ge0,\ \mathrm{Tr}\rho_{AR}=1\\
                 \mathrm{Tr}(N\rho_A)\le E}}
T\!\left(
 (\overline{\mathcal E}\otimes\mathrm{id}_R)(\rho_{AR}),
 \tau\otimes\rho_R
\right)
\le\epsilon.
```

The reference is arbitrary and is not available to the encoder. We also use $`\delta_E^*(\overline{\mathcal E})=\inf_\tau\delta_E(\overline{\mathcal E};\tau)`$. The theorems hold when this infimum is at most $`\epsilon`$: if the infimum is not attained, apply the proof with $`\epsilon+\xi`$ and let $`\xi\downarrow0`$.

For an integer $`d\ge1`$, let

```math
P_d=\sum_{n=0}^{d-1}|n\rangle\langle n|,
\qquad
\pi_d=\frac{P_d}{d},
\qquad
e_d=\mathrm{Tr}(N\pi_d)=\frac{d-1}{2}.
```

Although $`\pi_d`$ need not itself satisfy the input-energy bound, an appropriately diluted and flagged version does.

## 2. E1: exact recovery preserves diffuseness

### Theorem E1 — Diffuse-output bound

Suppose $`\mathcal E`$ has a CPTP left inverse on the full input oscillator. Then, for every $`d\ge1`$,

```math
\mathcal E(\pi_d)\le\frac{I}{d}.
```

Consequently, for an average of exactly reversible encoders,

```math
\sigma_d:=\overline{\mathcal E}(\pi_d)\le\frac{I}{d}.
```

In particular, every rank-$`m`$ ciphertext projector $`P`$ satisfies

```math
\mathrm{Tr}(P\sigma_d)\le\frac{m}{d}.
```

### Proof

Write $`\rho_j=\mathcal E(|j\rangle\langle j|)`$ for $`0\le j<d`$. Applying the decoder and measuring the Fock basis distinguishes the states $`\rho_j`$ perfectly. Equivalently, trace-distance contraction gives, for $`i\ne j`$,

```math
1=T(|i\rangle\langle i|,|j\rangle\langle j|)
\le T(\rho_i,\rho_j)\le1.
```

Two density operators have trace distance one exactly when their supports are orthogonal. If $`S_j`$ is the support projection of $`\rho_j`$, then the $`S_j`$ are pairwise orthogonal. A density operator has all eigenvalues at most one, so $`\rho_j\le S_j`$. Therefore

```math
\mathcal E(\pi_d)
=\frac1d\sum_{j=0}^{d-1}\rho_j
\le\frac1d\sum_{j=0}^{d-1}S_j
\le\frac{I}{d}.
```

Averaging this operator inequality over the independent key proves the assertion for $`\sigma_d`$. Taking its expectation in a rank-$`m`$ projector proves the last statement. The argument uses finite sums and remains valid on the infinite-dimensional ciphertext space. $`\square`$

Only perfect recovery of the Fock labels is needed for E1. Recovery of their coherences becomes necessary for the stronger key-cardinality result K1 in [finite_key.md](finite_key.md). The general structure of invertible quantum operations is established in [Nayak–Sen](https://arxiv.org/abs/quant-ph/0605041v4); the support argument above proves precisely what is needed here without invoking a finite-dimensional structure theorem.

## 3. From diffuseness to photon number

We will use the following elementary estimate. For $`0\le\delta\le1`$, define

```math
B_d(\delta)
=\sum_{m=1}^{\infty}
  \left(1-\delta-\frac{m}{d}\right)_+,
\qquad (x)_+=\max\{x,0\}.
```

The sum has finitely many nonzero terms. Setting $`L=\lfloor d(1-\delta)\rfloor`$ gives the exact expression

```math
B_d(\delta)
=L(1-\delta)-\frac{L(L+1)}{2d}.
```

For convenience, set $`B_d(\delta)=0`$ when $`\delta\ge1`$.

### Tail-sum lemma

If a state $`\omega`$ obeys

```math
\mathrm{Tr}(P_m\omega)\le\frac{m}{d}+\delta
\quad\text{for every integer }m\ge1,
```

then

```math
\mathrm{Tr}(N\omega)\ge B_d(\delta).
```

For $`0\le\delta\le1`$, this implies the simpler bound

```math
\mathrm{Tr}(N\omega)
\ge
\max\left\{
0,\ \frac{d(1-\delta)^2}{2}-\frac{1-\delta}{2}
\right\}.
```

### Proof

The oscillator has one level at each nonnegative integer, so monotone convergence gives the exact tail-sum identity

```math
\mathrm{Tr}(N\omega)
=\sum_{m=1}^{\infty}\mathrm{Tr}[(I-P_m)\omega].
```

Each summand is at least $`(1-\delta-m/d)_+`$. This proves the first assertion, including when the energy diverges. To obtain the second, put $`a=1-\delta`$ and $`f=da-\lfloor da\rfloor`$. Direct summation gives

```math
B_d(\delta)
=\frac{da^2-a}{2}+\frac{f(1-f)}{2d}
\ge\frac{da^2-a}{2}.
```

The energy is also nonnegative. $`\square`$

One way to establish the lemma's premise is to find a state $`\sigma\le I/d`$ with $`T(\omega,\sigma)\le\delta`$. The operational characterization of trace distance then gives

```math
\mathrm{Tr}(P_m\omega)
\le\mathrm{Tr}(P_m\sigma)+\delta
\le\frac{m}{d}+\delta.
```

Thus being close to a diffuse state forces a substantial probability of occupying higher Fock levels.

## 4. E2: a universal ciphertext-energy converse

### Theorem E2 — Energy required by exact reversible encryption

Let $`E>0`$ and let the scheme have exact keyed recovery and $`\delta_E^*(\overline{\mathcal E})\le\epsilon`$. For every integer $`d\ge2`$, set

```math
p_d=\min\left\{\frac12,\frac{2E}{d-1}\right\},
\qquad
\delta_d=\frac{\epsilon}{p_d}
=\max\left\{2\epsilon,\frac{\epsilon(d-1)}{2E}\right\}.
```

Then

```math
C_{\rm vac}\ge B_d(\delta_d).
```

In particular, when $`\delta_d<1`$,

```math
C_{\rm vac}
\ge
\max\left\{
0,\ \frac{d(1-\delta_d)^2}{2}-\frac{1-\delta_d}{2}
\right\}.
```

Any worst-case average-key output-energy budget $`C_{\max}(E)`$ is at least this large, since the vacuum is an allowed input.

### Proof

First take a replacer $`\tau`$ with secrecy error at most $`\epsilon`$. Let $`F`$ be a two-dimensional reference flag and consider

```math
\Omega_{AF}
=(1-p_d)|0\rangle\langle0|_A\otimes|0\rangle\langle0|_F
 +p_d\pi_d\otimes|1\rangle\langle1|_F.
```

Its input energy is $`p_d(d-1)/2\le E`$. Because the two flag blocks are orthogonal, the secrecy condition is exactly

```math
(1-p_d)T(\tau_0,\tau)
+p_dT(\sigma_d,\tau)
\le\epsilon.
```

The choice $`p_d\le1/2`$ ensures that the first coefficient is at least the second. Triangle inequality therefore yields

```math
p_d T(\sigma_d,\tau_0)
\le
p_dT(\sigma_d,\tau)+p_dT(\tau,\tau_0)
\le\epsilon.
```

Hence $`T(\sigma_d,\tau_0)\le\delta_d`$. Theorem E1 gives $`\sigma_d\le I/d`$, so the tail-sum lemma applied to $`\tau_0`$ proves the result. If only the infimum over replacers is bounded, replace $`\epsilon`$ by $`\epsilon+\xi`$ and take $`\xi\downarrow0`$; $`B_d`$ is continuous. $`\square`$

The reference in this proof is entirely classical. It prevents averaging a rare, revealing event into an unrecorded mixture. Neither a coherent reference nor an assumption about high photon-number moments is needed for E2.

### An explicit bound without a dimension optimization

For every $`E>0`$ and $`0<\epsilon\le1/6`$,

```math
\boxed{
C_{\rm vac}
\ge
\max\left\{0,\frac{4E}{27\epsilon}-\frac13\right\}.
}
```

To see this when $`E/\epsilon\ge3/2`$, choose

```math
d=\left\lfloor\frac{2E}{3\epsilon}\right\rfloor+1.
```

Then $`d\ge2`$, $`\delta_d\le1/3`$, and $`d\ge2E/(3\epsilon)`$. The function $`da^2/2-a/2`$ is increasing for $`a\ge2/3`$ and $`d\ge2`$, so E2 gives

```math
C_{\rm vac}
\ge\frac{2d}{9}-\frac13
\ge\frac{4E}{27\epsilon}-\frac13.
```

When $`E/\epsilon<3/2`$, the displayed lower bound is zero and follows from nonnegativity. For sharper numerical constants at specific parameters, maximize $`B_d(\delta_d)`$ over the integers $`d`$; the finite-parameter theorem is the primary statement.

### Perfect secrecy is impossible in this model

For $`E>0`$, exact keyed recovery and zero secrecy error cannot both hold for a normal ciphertext state, even if infinite energy and an infinite key alphabet are permitted.

Indeed, the flag argument at $`\epsilon=0`$ gives $`\sigma_d=\tau_0`$ for every $`d`$. E1 then implies $`\tau_0\le I/d`$ for every $`d`$. For each fixed $`m`$,

```math
\mathrm{Tr}(P_m\tau_0)\le\frac{m}{d}\longrightarrow0.
```

Letting $`m\to\infty`$ contradicts $`\mathrm{Tr}\tau_0=1`$. If $`\delta_E^*=0`$ is given as an infimum, an approximating sequence of replacers first establishes the same equality by taking its error to zero.

### Matching order of growth

Construction C1 in [finite_key.md](finite_key.md) uses

```math
d=\max\left\{1,\left\lceil\frac{E}{\epsilon}\right\rceil\right\}
```

and has exact keyed recovery, secrecy error at most $`\epsilon`$, and

```math
C_{\rm vac}=\frac{d-1}{2}<\frac{E}{2\epsilon},
\qquad
C_{\max}(E)=E+\frac{d-1}{2}.
```

Together with E2, these inequalities establish the optimal order $`E/\epsilon`$ as $`\epsilon\to0`$ with $`E/\epsilon\to\infty`$. The constants shown are sufficient for this scaling statement; they are not asserted to be the optimal constants.

## 5. Robust variant of E2: approximate keyed recovery

The exact converse also has a quantitative stability statement. This section changes the correctness assumption explicitly; E1, E2, C1, and K1 retain exact keyed recovery.

Let

```math
\mathcal R=\mathbb E_k(\mathcal D_k\circ\mathcal E_k)
```

be the decoded channel averaged over the independent key. Suppose its reference-aware correctness error obeys

```math
\sup_{\mathrm{Tr}(N\rho_A)\le E}
T\!\left[(\mathcal R\otimes\mathrm{id}_R)(\rho_{AR}),
         \rho_{AR}\right]
\le\gamma.
```

A separate correctness guarantee of $`\gamma`$ for every key implies this averaged guarantee, but the averaged guarantee is sufficient for what follows.

### Theorem E2R — A bound with secrecy and correctness errors

Assume $`\delta_E^*(\overline{\mathcal E})\le\epsilon`$ and the above correctness bound. For $`d\ge2`$ use the same $`p_d`$ as in E2 and define

```math
\widehat\delta_d
=\frac{\epsilon}{p_d}+\sqrt{\frac{\gamma}{p_d}}.
```

Then

```math
C_{\rm vac}\ge B_d(\widehat\delta_d),
```

with a nontrivial conclusion whenever $`\widehat\delta_d<1`$.

### Proof

The flagged secrecy proof of E2 did not use correctness, so it still gives

```math
T(\sigma_d,\tau_0)\le\frac{\epsilon}{p_d}.
```

It remains to replace E1 by an approximate concentration estimate. Let $`R`$ be $`d`$-dimensional and write

```math
|\Phi_d\rangle_{RA}
=\frac1{\sqrt d}\sum_{j=0}^{d-1}|j\rangle_R|j\rangle_A,
\qquad
\Phi_d=|\Phi_d\rangle\langle\Phi_d|.
```

For each key define its entanglement infidelity on this input by

```math
\eta_k
=1-\mathrm{Tr}\!\left[
\Phi_d\,
(\mathrm{id}_R\otimes\mathcal D_k\mathcal E_k)(\Phi_d)
\right].
```

A state which uses $`\Phi_d`$ with probability $`p_d`$, a vacuum input otherwise, and a classical flag distinguishing the two cases has input energy at most $`E`$. Correctness on this flagged state implies

```math
\mathbb E_k\eta_k\le\frac{\gamma}{p_d}.
```

Here the probability of the $`\Phi_d`$ projector is a permissible distinguishing measurement, so its shortfall is no larger than trace distance.

We next show that every rank-$`m`$ ciphertext projector $`P`$ satisfies

```math
\mathrm{Tr}[P\mathcal E_k(\pi_d)]
\le\frac{m}{d}+\sqrt{\eta_k}.
```

Choose Stinespring isometries for the encoder and decoder. Applied successively to $`\Phi_d`$, they produce a pure state $`|\Psi_k\rangle_{RA'BG}`$, where $`A'`$ is the recovered oscillator, $`B`$ the decoder environment, and $`G`$ the encoder environment. If $`\eta_k<1`$, projecting $`RA'`$ onto $`|\Phi_d\rangle`$ and normalizing produces

```math
|\Phi_d\rangle_{RA'}\otimes|\xi_k\rangle_{BG}
```

with squared overlap $`1-\eta_k`$ with $`|\Psi_k\rangle`$. The trace distance between these pure states is $`\sqrt{\eta_k}`$. After tracing out $`R`$ and $`G`$, contraction gives

```math
T\!\left(
V_k\mathcal E_k(\pi_d)V_k^\dagger,
\pi_d\otimes\xi_{k,B}
\right)
\le\sqrt{\eta_k},
```

where $`V_k:C\to A'B`$ is the decoder isometry. The state on the right is bounded above by $`I/d`$, and $`V_kPV_k^\dagger`$ is a rank-$`m`$ projector. Taking its expectation proves the concentration estimate. When $`\eta_k=1`$, the estimate follows directly from the trivial bound $`\mathrm{Tr}[P\mathcal E_k(\pi_d)]\le1`$.

Averaging and using concavity of the square root now yields

```math
\mathrm{Tr}(P\sigma_d)
\le\frac{m}{d}+\mathbb E_k\sqrt{\eta_k}
\le\frac{m}{d}+\sqrt{\frac{\gamma}{p_d}}.
```

Combining this with the secrecy comparison, and taking $`P=P_m`$, gives

```math
\mathrm{Tr}(P_m\tau_0)
\le\frac{m}{d}+\widehat\delta_d.
```

The tail-sum lemma completes the proof. The infimum-over-replacers case follows by the same limiting argument as E2. $`\square`$

The pure-state trace-distance identity and contraction used here are standard; see [Fuchs–van de Graaf](https://arxiv.org/abs/quant-ph/9712042v2). The proof specifies both environments so that no finite ciphertext-dimension assumption is hidden in the concentration step.

### A simple robust corollary

If $`s=\epsilon+\gamma`$ satisfies $`0<s\le1/8`$, then

```math
\boxed{
C_{\rm vac}
\ge\max\left\{0,\frac{E}{16(\epsilon+\gamma)}-\frac14\right\}.
}
```

For $`E/s\ge2`$, take $`d=\lfloor E/(2s)\rfloor+1`$. Then $`p_d\ge4s`$, and, putting $`x=\epsilon/s`$,

```math
\widehat\delta_d
\le\frac{x}{4}+\frac12\sqrt{1-x}
\le\frac12.
```

The last inequality is $`\sqrt{1-x}\le1-x/2`$. The tail-sum bound gives $`C_{\rm vac}\ge d/8-1/4\ge E/(16s)-1/4`$. If $`E/s<2`$, the claimed lower bound is zero. This establishes that correctness errors of order $`\epsilon`$ preserve an energy lower bound of order $`E/\epsilon`$.

No optimal dependence on $`\gamma`$ alone is claimed. Erasing a high-energy tail can create a coherence error proportional to the square root of the tail probability, so a matching achievability theorem for independently varied secrecy and correctness errors requires additional analysis.

## 6. Scope of the result

The photon-number spectrum is part of the theorem. An uncharged output register with arbitrarily many orthogonal states would destroy the relation between rank and photon number. A multimode output, a degenerate Hamiltonian, or additional transmitted systems must therefore be included in a new resource model before the converse is applied.

The bound concerns the average ciphertext of the vacuum and consequently lower-bounds a worst-case average-key output-energy budget. It does not say that every key increases the energy by the same amount. It also does not measure work dissipated, control-pulse energy, or the energy needed to establish the key.

Exact recovery is imposed on the full oscillator for the central theorem, while secrecy is imposed only on the mean-energy ball. This asymmetry is deliberate: it permits perfectly reversible encryption of rare high-energy components and is satisfied by the unitary constructions. The independently stated E2R quantifies one relaxation of correctness without changing the meaning of E2.

## Sources used in this chapter

- **NS2007:** Ashwin Nayak and Pranab Sen, *Invertible Quantum Operations and Perfect Encryption of Quantum States*, Quantum Information & Computation 7, 103–110 (2007); [arXiv:quant-ph/0605041v4](https://arxiv.org/abs/quant-ph/0605041v4). Background on invertible CPTP encoders; E1 has a direct proof above. Bibliography key `nayak2007invertible`.
- **FvdG1999:** Christopher A. Fuchs and Jeroen van de Graaf, *Cryptographic Distinguishability Measures for Quantum Mechanical States*, IEEE Transactions on Information Theory 45, 1216–1227 (1999); [arXiv:quant-ph/9712042v2](https://arxiv.org/abs/quant-ph/9712042v2). Trace-distance and fidelity tools; bibliography key `fuchs1999cryptographic`.

For the relation to earlier bosonic encryption work, see [the literature discussion](../references/RELATED_WORK.md). The finite-dimensional quantum Shannon lower bound is attributed and proved in the companion [finite-key chapter](finite_key.md).
