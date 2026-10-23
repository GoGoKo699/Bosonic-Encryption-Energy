# Displacement-only encryption: quantitative comparison

Gaussian displacement alone suppresses the distinguishability of bounded-energy messages at order $`V^{-1/2}`$, where $`V`$ is the added mean photon number. A homodyne measurement already witnesses this rate. This chapter gives the calculation, then checks a published finite-cutoff bound using states supported exactly on the vacuum and one-photon levels.

The result is a quantitative comparison. The [Gaussian chapter](gaussian_encryption.md) proves asymptotic secrecy with an arbitrary reference and shows how secret phase randomization changes the rate. The [related-work chapter](../references/RELATED_WORK.md) separates these guarantees from earlier coherent-state, finite-cutoff, and homomorphic-encryption results.

## 1. Conventions

Use $`[q,p]=i`$, $`q=(a+a^\dagger)/\sqrt2`$, and $`N=a^\dagger a`$. Vacuum has quadrature variance $`1/2`$. The displacement and its averaged channel are

```math
D(\alpha)=e^{\alpha a^\dagger-\bar\alpha a},
\qquad
\mathcal N_V(\rho)=
\int_{\mathbb C}\frac{d^2\alpha}{\pi V}
e^{-|\alpha|^2/V}D(\alpha)\rho D(\alpha)^\dagger.
```

Thus $`\mathbb E|\alpha|^2=V`$, and the mean ciphertext photon number is the input mean plus $`V`$. The real displacement of $`q`$ is $`\sqrt2\operatorname{Re}\alpha`$, a centered Gaussian of variance $`V`$. If the input homodyne density is $`p`$, the output density is $`p*g_V`$, where

```math
g_t(q)=\frac{1}{\sqrt{2\pi t}}e^{-q^2/(2t)}.
```

We use half trace distance $`T(\rho,\sigma)=\|\rho-\sigma\|_1/2`$ and total variation $`\operatorname{TV}(p,p')=\int|p-p'|/2`$. Measurement contracts trace distance:

```math
T(\rho,\sigma)\ge\operatorname{TV}(p_\rho,p_\sigma).
```

The optimized replacement error $`\delta_E^*(\mathcal C)`$ is defined in [the model](model.md). A pairwise witness lower-bounds this error with an additional factor of $`1/2`$:

```math
\delta_E^*(\mathcal C)\ge
\frac12 T\!\left(\mathcal C(\rho_+),\mathcal C(\rho_-)\right)
```

whenever both plaintexts have mean photon number at most $`E`$. This follows from the triangle inequality for every fixed replacement state, before taking the infimum over replacements.

## 2. Coherent-state lower bound for any replacement target

Take coherent plaintexts $`|\sqrt E\rangle`$ and $`|-\sqrt E\rangle`$. Their encrypted homodyne densities are normal distributions with means $`\pm\sqrt{2E}`$ and common variance $`s=V+1/2`$. The likelihood-ratio boundary is $`q=0`$, giving

```math
\begin{aligned}
\operatorname{TV}(p_{+,V},p_{-,V})
&=2\Phi\!\left(\sqrt{\frac{2E}{s}}\right)-1\\
&=\operatorname{erf}\!\sqrt{\frac{E}{V+1/2}}.
\end{aligned}
```

Here $`\Phi`$ is the standard normal cumulative distribution and $`\operatorname{erf}`$ is the error function. Consequently,

```math
\boxed{
\delta_E^*(\mathcal N_V)
\ge\frac12\operatorname{erf}
\!\sqrt{\frac{E}{V+1/2}}.
}
```

This homodyne witness is slightly stronger than the heterodyne witness in G1 of the [Gaussian chapter](gaussian_encryption.md), which has denominator $`V+1`$. Both have the same asymptotic exponent. Combining the present lower bound with G1's arbitrary-reference upper bound yields

```math
\frac12\operatorname{erf}\!\sqrt{\frac{E}{V+1/2}}
\le\delta_E^*(\mathcal N_V)
\le\delta_E(\mathcal N_V;\tau_V)
\le\min\!\left\{1,\sqrt{\frac{2E}{V+1}}\right\}.
```

For every fixed $`E>0`$, the error is therefore $`\Theta(V^{-1/2})`$ as $`V\to\infty`$. In particular, secrecy error at most $`0<\varepsilon<1/2`$ requires

```math
V+\frac12\ge
\frac{E}{[\operatorname{erf}^{-1}(2\varepsilon)]^2}
=\frac{E}{\pi\varepsilon^2}(1+o(1))
\quad(\varepsilon\downarrow0).
```

The matching upper bound has the same inverse-square error dependence. Earlier coherent-state displacement encryption already exhibited this scaling; see [Krüger (2006), Chapter 5](../references/RELATED_WORK.md#kruger2006gaussian).

Coherent states do not have a hard photon cutoff. To test a bound stated for cutoff states, a separate witness with finite support is needed.

## 3. Exact homodyne witness at photon cutoff one

Consider the orthogonal plaintexts

```math
|\psi_\pm\rangle=\frac{|0\rangle\pm|1\rangle}{\sqrt2}.
```

Each has mean photon number $`1/2`$ and support entirely in the first two Fock levels. The real quadrature wavefunctions of those levels are

```math
\varphi_0(q)=\pi^{-1/4}e^{-q^2/2},
\qquad
\varphi_1(q)=\sqrt2q\,\varphi_0(q).
```

The two input densities differ by

```math
p_+(q)-p_-(q)
=2\varphi_0(q)\varphi_1(q)
=2\sqrt2q\,g_{1/2}(q).
```

Because $`qg_{1/2}(q)=-g'_{1/2}(q)/2`$ and Gaussian convolution adds variances, their encrypted density difference is exactly

```math
\begin{aligned}
p_{+,V}(q)-p_{-,V}(q)
&=-\sqrt2\,(g_{1/2}*g_V)'(q)\\
&=-\sqrt2\,g'_{V+1/2}(q)\\
&=\frac{\sqrt2}{V+1/2}\,qg_{V+1/2}(q).
\end{aligned}
```

For a centered normal variable of variance $`s`$, $`\mathbb E|Q|=\sqrt{2s/\pi}`$. Integrating the absolute density difference therefore gives

```math
\begin{aligned}
\operatorname{TV}(p_{+,V},p_{-,V})
&=\frac{\sqrt2}{2s}\sqrt{\frac{2s}{\pi}}
=\frac{1}{\sqrt{\pi s}},\\
T\!\left(
\mathcal N_V(|\psi_+\rangle\langle\psi_+|),
\mathcal N_V(|\psi_-\rangle\langle\psi_-|)
\right)
&\ge\boxed{\frac{1}{\sqrt{\pi(V+1/2)}}}.
\end{aligned}
```

The displayed classical distance is exact. It is used as a lower bound on the quantum distance, with no claim that homodyne is the optimal measurement. The calculation has no truncation error and does not require numerical diagonalization.

## 4. Comparison with the published finite-cutoff statement

The source is [Ouyang, Tan, Fitzsimons and Rohde (2020)](../references/RELATED_WORK.md#ouyang2020homomorphic). Its noise law is $`e^{-|\alpha|^2/(2\sigma^2)}/(2\pi\sigma^2)`$, hence

```math
V=2\sigma^2.
```

For unambiguous version and page references:

| Location | Statement |
|---|---|
| [Published PDF](https://eprints.whiterose.ac.uk/id/eprint/198725/1/PhysRevResearch.2.013332.pdf), Theorem 1, p. 013332-4; Eq. (21), p. 013332-5 | Pairwise trace-distance bound for arbitrary states with photon cutoff $`n`$ |
| [arXiv:1902.10972v2](https://arxiv.org/html/1902.10972v2), Theorem 2 | Corresponding preprint statement |
| Published Appendix D, Lemma 10 and Eq. (D22), p. 013332-12 | Pointwise off-diagonal comparison used in the proof |

The asserted bound is

```math
B_n(\sigma)=\frac1{\sigma^2}
\left[
\frac n4+
\frac12\left(1+\frac{1}{2\sigma^2}\right)^n+
4(n+1)
\right].
```

The source uses half trace distance. Substituting the cutoff-one inputs from Section 3, its bound and the homodyne lower bound would have to satisfy

```math
\frac1{\sqrt{\pi(2\sigma^2+1/2)}}
\le B_1(\sigma)
=\frac{35}{4\sigma^2}+\frac1{4\sigma^4}.
```

They do not. For example, at $`\sigma=100`$,

```math
\frac1{\sqrt{\pi(20000+1/2)}}\simeq0.00398937,
\qquad
B_1(100)=0.0008750025.
```

More generally, the left side is of order $`\sigma^{-1}`$ and the asserted upper bound is of order $`\sigma^{-2}`$. A constant change of trace-distance or variance convention cannot reconcile those exponents.

## 5. A direct check of the supporting matrix-element inequality

There is also a local check within the supporting estimate. It uses the standard factorization

```math
\mathcal N_V=\mathcal A_{V+1}\circ\mathcal L_{1/(V+1)}
```

and Fock formulas from Gaussian-channel theory; see [Ivan, Sabapathy and Simon (2011)](../references/RELATED_WORK.md#ivan2011operatorsum) and [Mishra, Khabbazi Oskouei and Wilde (2023)](../references/RELATED_WORK.md#mishra2023teleportation). For the quantum-limited amplifier,

```math
\mathcal A_G(|m\rangle\langle n|)
=\sum_{\ell=0}^{\infty}
\sqrt{\binom{m+\ell}{\ell}\binom{n+\ell}{\ell}}\,
\frac{(G-1)^\ell}{G^{\ell+(m+n)/2+1}}\,
|m+\ell\rangle\langle n+\ell|.
```

Loss acts on the two needed operators as

```math
\mathcal L_\eta(|0\rangle\langle1|)
=\sqrt\eta\,|0\rangle\langle1|,
\qquad
\mathcal L_\eta(|1\rangle\langle1|)
=(1-\eta)|0\rangle\langle0|+\eta|1\rangle\langle1|.
```

Putting $`G=V+1`$ and $`\eta=1/G`$, for every integer $`j\ge0`$ this yields

```math
\begin{aligned}
c_j
&=\langle j|\mathcal N_V(|0\rangle\langle1|)|j+1\rangle
=\frac{\sqrt{j+1}\,V^j}{(V+1)^{j+2}},\\
d_j
&=\langle j+1|\mathcal N_V(|1\rangle\langle1|)|j+1\rangle
=\frac{(j+1+V^2)V^j}{(V+1)^{j+3}}.
\end{aligned}
```

Specializing the source's Eq. (D22) to its indices $`i=0`$ and $`k=1`$ requires $`c_j\le(y/x)d_j`$, where $`y=1/V`$ and $`x=V/(V+1)`$. Substitution reduces that inequality to

```math
\sqrt{j+1}\,V^2\le j+1+V^2.
```

At $`j=3`$ and $`V=10`$, this would read $`200\le104`$. The parameters have $`\sigma^2=V/2=5>0`$, within the stated domain of Lemma 10. This is an explicit failure of that pointwise estimate, independently of the homodyne argument.

## 6. Scope of the comparison

The calculation identifies a discrepancy in the asserted universal finite-cutoff rate and in a supporting inequality. Displacement-only encryption still has asymptotically vanishing secrecy error: Section 2 and G1 prove matching $`V^{-1/2}`$ scaling under the stronger arbitrary-reference criterion. The calculations here do not analyze the other functional claims of the homomorphic protocol.

The improved $`V^{-1}`$ behavior in [G2 and G3](gaussian_encryption.md) arises after a specified independent secret phase operation. It is a different averaged channel. Both the phase controls and the general idea of canceling slow moments have prior literature, as recorded in [Related work](../references/RELATED_WORK.md). The relevant distinction is the proved secrecy guarantee, its reference-system scope, and its energy dependence.
