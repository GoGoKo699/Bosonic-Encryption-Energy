# Which phase randomizations change the secrecy exponent?

Gaussian displacement suppresses optical coherences at different rates. The vacuum–one-photon coherence produces distinguishability of order $`V^{-1/2}`$ when the displacement adds $`V`$ photons on average. Removing that first angular harmonic changes the secrecy error to order $`V^{-1}`$, even for an arbitrary reference entangled with the plaintext. This chapter gives an exact criterion, identifies the minimum discrete phase randomness that satisfies it, and quantifies residual phase imbalance.

The statements concern a specified family: an independent secret phase rotation is followed by isotropic Gaussian displacement. The phase distribution is fixed while $`V`$ tends to infinity in the asymptotic classification. Correlated phase/displacement keys, additional Gaussian unitaries, and distributions deliberately changed with $`V`$ require separate statements.

## Definitions and conventions

Use the oscillator, displacement parameter, thermal state, and trace-distance conventions of [the Gaussian-encryption chapter](gaussian_encryption.md). In particular, $`V=\mathbb E|\alpha|^2`$ is the mean photon number added by the displacement, $`\tau_V`$ is the encrypted vacuum, and $`T=\|\cdot\|_1/2`$. The secrecy quantities are

```math
\delta_E(\mathcal C;\tau)
=\sup_{\rho_{AR}:\,\operatorname{Tr}N\rho_A\le E}
T\!\left((\mathcal C\otimes\operatorname{id}_R)(\rho_{AR}),
          \tau\otimes\rho_R\right),
\qquad
\delta_E^*(\mathcal C)=\inf_\tau\delta_E(\mathcal C;\tau).
```

Let $`\mu`$ be a probability measure on phase angles modulo $`2\pi`$. Its phase channel and Fourier coefficients are

```math
\Phi_\mu(\rho)
=\int e^{i\theta N}\rho e^{-i\theta N}\,d\mu(\theta),
\qquad
m_k=\int e^{ik\theta}\,d\mu(\theta),
\qquad k\in\mathbb Z.
```

Thus $`m_0=1`$, $`m_{-k}=\bar m_k`$, $`|m_k|\le1`$, and

```math
\Phi_\mu(|n\rangle\langle n+k|)
=m_{-k}|n\rangle\langle n+k|.
```

The averaged encryption channel is $`\mathcal C_{V,\mu}=\mathcal N_V\circ\Phi_\mu`$. The phase and displacement are sampled independently. Every key selects the unitary $`D(\alpha)e^{i\theta N}`$, so inverse decoding is exact. Phase averaging leaves the vacuum unchanged, making $`\tau_V`$ the same natural replacement target for every $`\mu`$.

## P1. The first-harmonic criterion

Fix $`E>0`$ and a phase law $`\mu`$ that does not depend on $`V`$. Then

```math
\boxed{
\begin{array}{ll}
m_1=0:
&\delta_E^*(\mathcal C_{V,\mu})=\Theta(V^{-1}),
\quad\delta_E(\mathcal C_{V,\mu};\tau_V)=\Theta(V^{-1}),\\[2mm]
m_1\ne0:
&\delta_E^*(\mathcal C_{V,\mu})=\Theta(V^{-1/2}),
\quad\delta_E(\mathcal C_{V,\mu};\tau_V)=\Theta(V^{-1/2}).
\end{array}
}
```

The constants in these asymptotic statements may depend on the fixed $`E`$ and $`\mu`$. They are not uniform as $`E\downarrow0`$ or $`m_1\to0`$. The classification includes arbitrary-reference secrecy; the lower witnesses happen to need no reference.

### Sufficiency: zero first harmonic

If $`m_1=0`$, the G3 proof extends to give

```math
\delta_E(\mathcal C_{V,\mu};\tau_V)
\le\min\!\left\{1,
\frac E{V+1}+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}.
```

Here is the change needed in that proof. Purify the input and write $`|\psi\rangle=\sum_n|n\rangle|r_n\rangle`$, with $`p_n=\|r_n\|^2`$. In a loss branch indexed by $`l`$, the vacuum component comes from $`n=l`$. The phase-averaged cross block from this vacuum component to transmitted photon number $`k`$ is multiplied by $`m_{-k}`$.

For a fixed $`l`$, the left vector of every such cross term is the same vacuum-reference vector. The entire branch cross block is therefore rank one, even though the phase-averaged branch state itself need not be pure. Its norm is bounded by $`\sqrt{a_lb_l}`$, where

```math
a_l=(1-\eta)^lp_l,
\qquad
b_l=\sum_{k\ge2}\binom{l+k}{k}(1-\eta)^l\eta^k p_{l+k}.
```

The $`k=1`$ term vanishes because $`m_1=0`$, and $`|m_k|\le1`$ bounds every remaining coefficient. The weighted Cauchy–Schwarz and binomial estimates from G3 apply unchanged. With $`\eta=1/(V+1)`$ and the standard amplifier factorization, they prove the displayed bound.

### Necessity: a nonzero first harmonic leaves a coherent witness

Put $`e=\min(E,1/2)`$ and consider

```math
|\psi_\pm\rangle=
\sqrt{1-e}\,|0\rangle\pm\sqrt e\,|1\rangle.
```

Both inputs obey the energy bound. Let $`s=V+1`$ and $`g_s(z)=e^{-|z|^2/s}/(\pi s)`$. Heterodyne measurement of $`\mathcal C_{V,\mu}(|\psi_\pm\rangle\langle\psi_\pm|)`$ gives two densities whose difference is exactly

```math
q_+(z)-q_-(z)
=\frac{4\sqrt{e(1-e)}}s
\operatorname{Re}(m_1\bar z)\,g_s(z).
```

To see the normalization, the unencrypted Husimi densities are

```math
Q_\pm(z)=\frac{e^{-|z|^2}}\pi
\left[1-e+e|z|^2
\pm2\sqrt{e(1-e)}\operatorname{Re}z\right].
```

Phase averaging multiplies the first harmonic by $`m_1`$. Convolution with the complex Gaussian displacement law replaces the first harmonic by $`\operatorname{Re}(m_1\bar z)/s`$ times $`g_s(z)`$. Equivalently, for independent circular Gaussians of variances one and $`V`$, the conditional mean of the first variable given their sum $`z`$ is $`z/s`$.

A rotation of the classical heterodyne outcome absorbs $`\arg m_1`$. Since $`\mathbb E_{g_s}|\operatorname{Re}Z|=\sqrt{s/\pi}`$, the exact classical distance is

```math
\operatorname{TV}(q_+,q_-)
=\frac{2|m_1|\sqrt{e(1-e)}}{\sqrt{\pi(V+1)}}.
```

The quantum trace distance is at least this value. Taking half the pairwise distance therefore gives the arbitrary-replacer bound

```math
\boxed{
\delta_E^*(\mathcal C_{V,\mu})
\ge\frac{|m_1|\sqrt{e(1-e)}}{\sqrt{\pi(V+1)}},
\qquad e=\min(E,1/2).
}
```

This is a lower bound for every replacement target, including $`\tau_V`$. The exact formula is for the heterodyne total variation distance; no equality with the optimized quantum trace distance is assumed.

If $`m_1\ne0`$ is fixed, this lower bound is of order $`V^{-1/2}`$. For the matching upper bound, phase preprocessing preserves the mean photon number and the reference marginal. Applying G1 to the phase-averaged input gives

```math
\delta_E(\mathcal C_{V,\mu};\tau_V)
\le\min\!\left\{1,\sqrt{\frac{2E}{V+1}}\right\}.
```

### A diagonal witness excludes faster decay

To complete the $`\Theta(V^{-1})`$ statement when $`m_1=0`$, it remains to show that no phase law can make the error decay faster than $`V^{-1}`$ at fixed $`E>0`$. This can be proved directly, without invoking a general energy converse.

Take $`e_d=\min(E,1)`$ and the two allowed diagonal inputs

```math
\rho_0=|0\rangle\langle0|,
\qquad
\rho_d=(1-e_d)|0\rangle\langle0|+e_d|1\rangle\langle1|.
```

Every phase channel leaves them unchanged. For the vacuum and one-photon inputs, Gaussian convolution gives the post-displacement heterodyne densities

```math
q_0(z)=g_s(z),
\qquad
q_1(z)=g_s(z)\left[\frac{s-1}s+\frac{|z|^2}{s^2}\right].
```

Under $`g_s`$, the random variable $`U=|Z|^2/s`$ has an exponential distribution of mean one, and $`\mathbb E|U-1|=2/\exp(1)`$. Consequently,

```math
\operatorname{TV}(q_1,q_0)=\frac1{\exp(1)(V+1)},
\qquad
\operatorname{TV}(q_d,q_0)=\frac{e_d}{\exp(1)(V+1)}.
```

The two resulting lower bounds must be distinguished. The arbitrary-replacer bound is

```math
\boxed{
\delta_E^*(\mathcal C_{V,\mu})
\ge\frac{\min(E,1)}{2\exp(1)(V+1)}.
}
```

For the thermal target specifically, the vacuum output equals that target, so no pairwise triangle factor is needed:

```math
\delta_E(\mathcal C_{V,\mu};\tau_V)
\ge\frac{\min(E,1)}{\exp(1)(V+1)}.
```

Together with the zero-harmonic upper bound, these inequalities complete P1 for every fixed $`E>0`$.

## P2. One bit is the minimum discrete phase entropy

Suppose the independent phase key is discrete, with probabilities $`p_j`$ and angles $`\theta_j`$, and satisfies

```math
\sum_j p_j e^{i\theta_j}=0.
```

Then its Shannon entropy in bits obeys

```math
\boxed{H(K)=-\sum_jp_j\log_2p_j\ge1.}
```

Equality holds precisely for two equiprobable antipodal phases, up to relabeling and a common phase rotation.

For the proof, isolate any atom:

```math
p_j=|p_je^{i\theta_j}|
=\left|\sum_{k\ne j}p_ke^{i\theta_k}\right|
\le\sum_{k\ne j}p_k=1-p_j.
```

Thus $`p_j\le1/2`$ for every $`j`$. Every positive-probability term has $`-\log_2p_j\ge1`$, so $`H(K)\ge1`$. Equality forces every positive probability to equal $`1/2`$, leaving exactly two atoms. Their vectors can sum to zero only if their phases differ by $`\pi`$. Conversely, that distribution has zero first harmonic and entropy one.

The result remains valid for countably many phase values, allowing infinite entropy. It is a statement about discrete Shannon entropy, not differential entropy of a continuous phase variable. It also does not count the independent displacement key. Gaussian displacements are sampled from a continuous distribution in this model, and their exact sampling has not been assigned a finite bit cost.

P2 is a minimum within the family specified here. It does not exclude alternative encryption ensembles with correlated keys or different unitaries. Nor does it imply that a fresh phase bit may be reused: independence from the plaintext and the rest of the key, as specified by the cipher, is part of the analysis.

## P3. Residual phase imbalance and control accuracy

Perfect cancellation is not required to obtain a finite-error guarantee. For an arbitrary phase law, including one with nonzero $`m_1`$,

```math
\boxed{
\delta_E(\mathcal C_{V,\mu};\tau_V)
\le\min\!\left\{1,
\frac E{V+1}
+|m_1|\sqrt{\frac E{V+1}}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}.
}
```

This bound can be combined with G1 by taking the smaller upper bound. The extra term quantifies the remaining first harmonic; it vanishes exactly under the P1 criterion.

### Proof

Use the pure-state Fock expansion and loss-branch notation from G3. Split the vacuum/nonvacuum cross block into its transmitted-$`k=1`$ component $`C_1`$ and its components with $`k\ge2`$. The latter satisfy the previously proved bound. For the former, the trace norm of loss branch $`l`$ is

```math
|m_1|\sqrt\eta\sqrt{l+1}(1-\eta)^l
\sqrt{p_lp_{l+1}}.
```

Therefore

```math
\begin{aligned}
\|C_1\|_1
&\le |m_1|\sqrt\eta
\sum_{l\ge0}\sqrt{l+1}(1-\eta)^l\sqrt{p_lp_{l+1}}\\
&\le |m_1|\sqrt\eta
\sqrt{\left[\sum_l(1-\eta)^lp_l\right]
       \left[\sum_l(l+1)(1-\eta)^lp_{l+1}\right]}\\
&\le |m_1|\sqrt{\eta E}.
\end{aligned}
```

The nonvacuum diagonal contribution is at most $`\eta E`$. Adding the $`k\ge2`$ cross-block estimate and applying the amplifier gives P3. The proof has the same arbitrary-reference scope as G3.

### A noisy binary phase implementation

Suppose the phase is zero with probability $`p`$, and $`\pi+\Delta`$ with probability $`1-p`$. Then

```math
m_1=p-(1-p)e^{i\Delta},
\qquad
|m_1|^2=(2p-1)^2+4p(1-p)\sin^2(\Delta/2).
```

With balanced probabilities, $`|m_1|=|\sin(\Delta/2)|`$. With an exact $`\pi`$ phase separation, $`|m_1|=|2p-1|`$. The bound therefore treats angle error and probability imbalance in the same measurable parameter.

For example, if $`E\ge1`$ and $`0<\varepsilon\le1`$, a sufficient explicit choice is

```math
V+1\ge\frac{2(1+\sqrt2)E}{\varepsilon},
\qquad
|m_1|\le\frac\varepsilon2\sqrt{\frac{V+1}{E}}.
```

The first condition makes the zero-harmonic part of P3 at most $`\varepsilon/2`$ and also ensures $`V\ge1`$. The second makes the remaining term at most $`\varepsilon/2`$. If $`V+1`$ is proportional to $`E/\varepsilon`$, the allowed first harmonic is of order $`\sqrt\varepsilon`$.

The necessity witness in P1 gives the complementary condition: if any fixed replacement state achieves error at most $`\varepsilon`$, then

```math
|m_1|\le
\varepsilon\sqrt{\frac{\pi(V+1)}{e(1-e)}},
\qquad e=\min(E,1/2).
```

Thus at fixed $`E>0`$ and $`V=\Theta(E/\varepsilon)`$, first-harmonic imbalance must also be $`O(\sqrt\varepsilon)`$. The constants in this necessary condition depend on the fixed energy through $`e`$; it is not a uniform large-$`E`$ precision lower bound.

For a fixed nonzero imbalance, the $`V^{-1/2}`$ regime eventually dominates, as P1 states. If the phase law is deliberately improved as $`V`$ grows, P3 gives the relevant finite-parameter guarantee; that situation is outside P1's fixed-law asymptotic classification.

## Interpretation and boundaries

The phase bit cancels the lowest-order angular coherence that survives Gaussian smoothing. It does not dephase the entire oscillator. Higher even coherences remain, explaining both the reference-aware $`V^{-1}`$ upper bound and the intrinsic small-$`E`$ limitation established in G3.

The control operations are established optical primitives, and phase/displacement encryption compositions already occur in the related literature; see [the source comparison](../references/RELATED_WORK.md). The results here identify the phase moment that determines the secrecy exponent under a mean-energy bound. They do not supply a finite discretization of the displacement key, authenticate the ciphertext, allow key reuse, or describe security after key disclosure.
