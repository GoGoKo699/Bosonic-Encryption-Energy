# Gaussian controls for energy-constrained quantum encryption

An unknown oscillator state can be encrypted by a secret displacement and recovered by applying the inverse displacement. A broad displacement distribution hides the input, but the amount of noise required depends on whether the encryption also removes phase coherence. This chapter proves that a single additional secret phase bit changes the required displacement energy from order $`\varepsilon^{-2}`$ to order $`\varepsilon^{-1}`$ at fixed positive input energy. The guarantees hold when the plaintext is entangled with an arbitrary reference system.

The displacement parameter remains a continuous secret random variable in these constructions. The phrase **one additional bit** refers only to the binary phase rotation. It does not assert that the complete cipher uses a finite classical key.

## Conventions and secrecy criterion

The input and ciphertext are each one oscillator, with number operator $`N=a^\dagger a`$ and vacuum energy zero. The quadratures obey $`[q,p]=i`$, so the vacuum covariance matrix is $`I_2/2`$. Write

```math
T(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\qquad
D(\alpha)=\exp(\alpha a^\dagger-\bar\alpha a).
```

For a channel $`\mathcal C`$ and a fixed ciphertext state $`\tau`$, the reference-aware secrecy error is

```math
\delta_E(\mathcal C;\tau)
=\sup_{\rho_{AR}:\,\mathrm{Tr}N\rho_A\le E}
T\!\left((\mathcal C\otimes\mathrm{id}_R)(\rho_{AR}),
          \tau\otimes\rho_R\right).
```

The supremum includes arbitrary reference systems. The best fixed target gives

```math
\delta_E^*(\mathcal C)=\inf_\tau\delta_E(\mathcal C;\tau).
```

These definitions agree with [the model](model.md). Every achievability bound below uses a specified thermal target. Every lower bound explicitly identified as an **arbitrary-replacer bound** applies to $`\delta_E^*`$, and therefore also to the error relative to that thermal target. A pairwise distinguishability witness gives half its trace distance as an arbitrary-replacer lower bound: if two allowed inputs produce $`\omega_+`$ and $`\omega_-`$, then

```math
\max\{T(\omega_+,\tau),T(\omega_-,\tau)\}
\ge\frac12T(\omega_+,\omega_-)
```

for every $`\tau`$. The factor of $`1/2`$ in this inequality is additional to the factor already included in the definition of trace distance.

Let $`\mathcal N_V`$ be the Gaussian displacement channel

```math
\mathcal N_V(\rho)
=\int_{\mathbb C}\frac{d^2\alpha}{\pi V}
  e^{-|\alpha|^2/V}D(\alpha)\rho D(\alpha)^\dagger,
\qquad V>0.
```

The parameter is normalized so that $`\mathbb E|\alpha|^2=V`$. In particular, the vacuum output is the thermal state

```math
\tau_V=\mathcal N_V(|0\rangle\langle0|)
=\sum_{n=0}^\infty\frac{V^n}{(V+1)^{n+1}}
  |n\rangle\langle n|,
\qquad \mathrm{Tr}N\tau_V=V.
```

If $`\rho`$ has finite mean photon number, averaging over the centered displacement distribution gives

```math
\mathrm{Tr}N\mathcal N_V(\rho)
=\mathrm{Tr}N\rho+V.
```

Secret phase rotations preserve the input photon number, so this same energy formula applies to every construction in this chapter. It describes the averaged ciphertext energy. The displacement distribution has unbounded support, and there is no finite upper bound on the displacement energy for every individual key value.

## G1. Standard factorization and the displacement-only benchmark

### The loss–amplifier factorization

Let $`\mathcal L_\eta`$ denote the quantum-limited attenuator of power transmissivity $`0\le\eta\le1`$, and let $`\mathcal A_G`$ denote the quantum-limited amplifier of power gain $`G\ge1`$. The standard factorization is

```math
\boxed{\quad
\mathcal N_V=\mathcal A_{V+1}\circ\mathcal L_{1/(V+1)}.
\quad}
```

This identity and the Fock-basis Kraus representation used below are established Gaussian-channel facts; see [Ivan, Sabapathy and Simon (2011)](../references/RELATED_WORK.md#ivan2011operatorsum). The factorization with precisely $`\eta=1/(1+V)`$ is also stated in [Mishra, Khabbazi Oskouei and Wilde (2023)](../references/RELATED_WORK.md#mishra2023teleportation).

For completeness, it can be checked on the Weyl characteristic function $`\chi_\rho(z)=\mathrm{Tr}\rho D(z)`$:

```math
\begin{aligned}
\chi_{\mathcal L_\eta(\rho)}(z)
 &=\chi_\rho(\sqrt\eta z)
   e^{-(1-\eta)|z|^2/2},\\
\chi_{\mathcal A_G(\rho)}(z)
 &=\chi_\rho(\sqrt G z)
   e^{-(G-1)|z|^2/2},\\
\chi_{\mathcal N_V(\rho)}(z)
 &=\chi_\rho(z)e^{-V|z|^2}.
\end{aligned}
```

Taking $`G=V+1`$ and $`\eta=1/G`$ gives the third expression. Characteristic functions determine arbitrary trace-class states, so this establishes channel equality for non-Gaussian inputs as well. A covariance-matrix calculation alone would only check the parameters on Gaussian states.

The factorization is a mathematical tool for analyzing the averaged encryption channel. The sender implements the keyed displacement unitary, whose inverse is available to the recipient. The sender does not physically apply an irreversible loss channel followed by an amplifier.

### G1 bound

For every $`E\ge0`$ and $`V>0`$,

```math
\boxed{
\frac12\mathrm{erf}\!\sqrt{\frac{E}{V+1}}
\;\le\;\delta_E^*(\mathcal N_V)
\;\le\;\delta_E(\mathcal N_V;\tau_V)
\;\le\;\min\!\left\{1,\sqrt{\frac{2E}{V+1}}\right\}.
}
```

Consequently, at any fixed $`E>0`$, displacement-only encryption has secrecy error $`\Theta(V^{-1/2})`$ as $`V\to\infty`$. Inverting this relation, it requires $`V=\Theta(E/\varepsilon^2)`$ as $`\varepsilon\downarrow0`$. The lower bound holds for any fixed replacement state, not just $`\tau_V`$.

### Proof of the lower bound

Use the two coherent plaintexts $`|\sqrt E\rangle`$ and $`|-\sqrt E\rangle`$. Both have mean photon number $`E`$. Heterodyne measurement of their encrypted outputs gives the classical densities

```math
q_\pm(z)=\frac1{\pi s}
\exp\!\left(-\frac{|z\mp\sqrt E|^2}{s}\right),
\qquad s=V+1.
```

Their likelihood-ratio decision boundary is $`\mathrm{Re}z=0`$. Since each real marginal has variance $`s/2`$, their total variation distance is exactly

```math
\mathrm{TV}(q_+,q_-)
=2\Phi\!\left(\sqrt{\frac{2E}{s}}\right)-1
=\mathrm{erf}\!\sqrt{\frac Es},
```

where $`\Phi`$ is the standard normal distribution function. Measurement cannot increase trace distance, so the quantum outputs have trace distance at least this value. Applying the pairwise triangle inequality stated above gives the factor $`1/2`$ in G1.

More explicitly, if some fixed replacement state achieves error at most $`0<\varepsilon<1/2`$, then

```math
V+1\ge
\frac{E}{[\mathrm{erf}^{-1}(2\varepsilon)]^2}
=\frac{E}{\pi\varepsilon^2}(1+o(1))
\quad (\varepsilon\downarrow0).
```

This is a lower bound on the best possible replacement target for the displacement-only channel. It is not an assertion that heterodyne measurement attains the quantum trace distance.

### Proof of the arbitrary-reference upper bound

Put $`\eta=1/(V+1)`$ and let

```math
\omega_{BR}=(\mathcal L_\eta\otimes\mathrm{id}_R)(\rho_{AR}).
```

If $`p_n=\langle n|\rho_A|n\rangle`$, its nonvacuum probability is

```math
t=1-\sum_{n=0}^\infty(1-\eta)^n p_n
\le\eta\sum_{n=0}^\infty np_n
\le\eta E.
```

Let $`\omega_R^0=\langle0|\omega_{BR}|0\rangle`$ be the unnormalized vacuum block. Trace preservation implies $`0\le\omega_R^0\le\rho_R`$, with $`\mathrm{Tr}\omega_R^0=1-t`$. Use root fidelity $`F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$. Because the second state has vacuum support on $`B`$,

```math
F(\omega_{BR},|0\rangle\langle0|\otimes\rho_R)
=F(\omega_R^0,\rho_R)
\ge\mathrm{Tr}\omega_R^0=1-t.
```

The inequality follows from $`\rho_R\ge\omega_R^0`$ and operator monotonicity of the square root:
$`\sqrt{\omega_R^0}\rho_R\sqrt{\omega_R^0}\ge(\omega_R^0)^2`$.
Fuchs–van de Graaf therefore gives

```math
T(\omega_{BR},|0\rangle\langle0|\otimes\rho_R)
\le\sqrt{1-(1-t)^2}
\le\sqrt{2\eta E}.
```

Finally apply $`\mathcal A_{V+1}\otimes\mathrm{id}_R`$. Trace distance contracts, and the amplifier maps the vacuum to $`\tau_V`$. Including the trivial upper bound of one proves G1. This argument retains the original reference marginal throughout; replacing the conditional vacuum reference state by $`\rho_R`$ without a bound would not justify the result.

Gaussian displacement private channels and finite displacement approximations have an established history; see [Brádler (2005)](../references/RELATED_WORK.md#bradler2005private) and [Krüger (2006)](../references/RELATED_WORK.md#kruger2006gaussian). Their assumptions and metrics, and the quantitative issue in the later finite-cutoff displacement bound of [Ouyang et al. (2020)](../references/RELATED_WORK.md#ouyang2020homomorphic), are compared in the related-work chapter. G1 uses the explicit convention and arbitrary-reference criterion defined here.

## G2. Full phase averaging attains a linear energy bound

Define the phase-averaging channel

```math
\Phi_{\mathrm{ph}}(\rho)
=\int_0^{2\pi}\frac{d\theta}{2\pi}
e^{i\theta N}\rho e^{-i\theta N}.
```

The key selects $`\alpha`$ from the Gaussian distribution and an independent uniform phase $`\theta`$. Encryption uses $`U_{\alpha,\theta}=D(\alpha)e^{i\theta N}`$, and decryption uses $`U_{\alpha,\theta}^\dagger`$. Correctness is exact for every input state. Both key variables are continuous in this ideal construction.

For every $`E\ge0`$ and $`V>0`$,

```math
\boxed{
\delta_E(\mathcal N_V\circ\Phi_{\mathrm{ph}};\tau_V)
\le\min\!\left\{1,\frac{E}{V+1}\right\}.
}
```

To prove this, phase average an arbitrary joint state:

```math
(\Phi_{\mathrm{ph}}\otimes\mathrm{id}_R)(\rho_{AR})
=\sum_{n=0}^\infty |n\rangle\langle n|\otimes\rho_R^n,
```

where every $`\rho_R^n`$ is positive, $`\sum_n\rho_R^n=\rho_R`$, and $`\sum_n n\mathrm{Tr}\rho_R^n\le E`$. These reference blocks need not have orthogonal supports.

Loss maps each number state to a binomial distribution,

```math
\mathcal L_\eta(|n\rangle\langle n|)
=\sum_{k=0}^n\binom nk\eta^k(1-\eta)^{n-k}|k\rangle\langle k|.
```

The resulting joint state is block diagonal in the transmitted photon number. Its nonvacuum weight is

```math
t=\sum_n\bigl[1-(1-\eta)^n\bigr]\mathrm{Tr}\rho_R^n
\le\eta E.
```

Its difference from $`|0\rangle\langle0|\otimes\rho_R`$ has a negative vacuum block of trace $`-t`$ and positive nonvacuum blocks of total trace $`t`$. Their oscillator supports are orthogonal. The trace distance is therefore exactly $`t`$ before amplification. Applying the amplifier and setting $`\eta=1/(V+1)`$ proves G2.

Taking $`V+1\ge E/\varepsilon`$ makes the secrecy error at most $`\varepsilon`$. The mean energy of the vacuum ciphertext is $`V`$, and the average ciphertext energy of an allowed plaintext is at most $`E+V`$. The result is uniform in $`E`$, including energies much smaller than one photon.

## G3. A single phase bit suffices for the improved exponent

Full phase averaging removes every off-diagonal Fock matrix element. Removing all such coherences is not necessary to obtain the inverse-linear error exponent. Define photon parity and its binary average by

```math
P=e^{i\pi N}=(-1)^N,
\qquad
\Phi_2(\rho)=\frac12(\rho+P\rho P).
```

Choose an independent uniform bit $`b\in\{0,1\}`$ and apply

```math
U_{\alpha,b}=D(\alpha)P^b,
\qquad
U_{\alpha,b}^\dagger=P^bD(-\alpha).
```

Both displacement and a $`\pi`$ phase rotation are Gaussian unitaries; see the conventions in [Weedbrook et al. (2012)](../references/RELATED_WORK.md#weedbrook2012gaussian). Their keyed inverse recovers the plaintext exactly. The averaged channel $`\mathcal N_V\circ\Phi_2`$ need not map Gaussian states to Gaussian states; the statement about Gaussian controls concerns the operations selected by the key.

For every $`E\ge0`$ and $`V>0`$,

```math
\boxed{
\delta_E(\mathcal N_V\circ\Phi_2;\tau_V)
\le\min\!\left\{1,
\frac{E}{V+1}
+\sqrt{\frac{E(E+1)}{2V(V+1)}}\right\}.
}
```

In particular, for $`V\ge1`$,

```math
\delta_E(\mathcal N_V\circ\Phi_2;\tau_V)
\le\min\!\left\{1,
\frac{E+\sqrt{E(E+1)}}{V+1}\right\}.
```

For $`E\ge1`$, the numerator is at most $`(1+\sqrt2)E`$. Thus a sufficient choice is $`V\ge1`$ with $`V+1\ge(1+\sqrt2)E/\varepsilon`$. At every fixed $`E>0`$, one phase bit changes the displacement-energy dependence from $`\varepsilon^{-2}`$ to $`\varepsilon^{-1}`$.

### Proof with an arbitrary reference

It suffices to prove the bound for a pure joint input after enlarging the reference: any mixed state has such a purification, and tracing the additional reference system contracts the distance to the corresponding replacement state. Expand

```math
|\psi\rangle_{AR}=\sum_{n=0}^\infty|n\rangle_A|r_n\rangle_R,
\qquad
p_n=\langle r_n|r_n\rangle,
\qquad
\sum_n p_n=1,\quad\sum_n np_n\le E.
```

No orthogonality condition is imposed on the reference vectors $`|r_n\rangle`$. Parity averaging splits this vector into its unnormalized even and odd sectors and removes their mutual coherence.

The loss Kraus operator indexed by the number $`l`$ of lost photons acts as

```math
K_l|n\rangle=
\begin{cases}
\displaystyle\sqrt{\binom nl}(1-\eta)^{l/2}\eta^{(n-l)/2}|n-l\rangle,
&n\ge l,\\
0,&n<l.
\end{cases}
```

Let $`\omega=(\mathcal L_\eta\circ\Phi_2\otimes\mathrm{id}_R)(|\psi\rangle\langle\psi|)`$, and put $`P_0=|0\rangle\langle0|\otimes I_R`$ and $`Q_0=I-P_0`$. Its nonvacuum probability obeys the same estimate as before,

```math
t=\mathrm{Tr}Q_0\omega
=1-\sum_n(1-\eta)^np_n\le\eta E.
```

The new step controls the off-diagonal block $`C=P_0\omega Q_0`$. In loss branch $`l`$, only the input parity sector containing $`n=l`$ has a vacuum component. Its coherent nonvacuum components have transmitted number $`k=n-l`$ even and at least two. The squared norm of that branch's vacuum vector is

```math
a_l=(1-\eta)^l p_l,
```

and the squared norm of its coherent nonvacuum vector is

```math
b_l=\sum_{\substack{k\ge2\\k\ \text{even}}}
\binom{l+k}{k}(1-\eta)^l\eta^k p_{l+k}.
```

Each branch cross block is rank one, with trace norm $`\sqrt{a_lb_l}`$. The triangle inequality followed by weighted Cauchy–Schwarz gives

```math
\|C\|_1
\le\sum_l\sqrt{a_lb_l},
\qquad
\left(\sum_l\sqrt{a_lb_l}\right)^2
\le\left[\sum_l(l+1)a_l\right]
   \left[\sum_l\frac{b_l}{l+1}\right].
```

The first factor is bounded by $`E+1`$. To bound the second, discard the even-$`k`$ restriction, set $`n=l+k`$, and use

```math
\frac{\binom nk}{n-k+1}=\frac{\binom{n+1}k}{n+1}.
```

For $`0<\eta<1`$, nonnegativity permits exchanging the sums, which gives

```math
\begin{aligned}
\sum_l\frac{b_l}{l+1}
&\le\sum_n\frac{p_n}{(n+1)(1-\eta)}
    \Pr\{\mathrm{Bin}(n+1,\eta)\ge2\}\\
&\le\sum_n\frac{p_n}{(n+1)(1-\eta)}
    \frac{n(n+1)\eta^2}{2}\\
&\le\frac{\eta^2E}{2(1-\eta)}.
\end{aligned}
```

The second line uses $`\Pr(K\ge2)\le\mathbb E[K(K-1)]/2`$. Consequently,

```math
\|C\|_1\le
\eta\sqrt{\frac{E(E+1)}{2(1-\eta)}}.
```

To convert this to the required distance, write $`\omega_+=Q_0\omega Q_0`$ and $`\rho_R^+=\mathrm{Tr}_B\omega_+`$. The reference marginal remains $`\rho_R`$. The block-diagonal part of $`\omega-|0\rangle\langle0|\otimes\rho_R`$ is therefore

```math
\omega_+-|0\rangle\langle0|\otimes\rho_R^+.
```

Its trace norm is $`2t`$ by orthogonality of the oscillator supports. The off-diagonal part $`C+C^\dagger`$ has trace norm $`2\|C\|_1`$. Thus

```math
T(\omega,|0\rangle\langle0|\otimes\rho_R)
\le t+\|C\|_1
\le\eta E+
\eta\sqrt{\frac{E(E+1)}{2(1-\eta)}}.
```

Apply the amplifier, use trace-distance contraction, and substitute $`\eta=1/(V+1)`$. This proves G3. The argument requires only the first photon-number moment. It does not assume a hard Fock cutoff or a finite photon-number variance.

### The low-energy limitation of a binary phase

The factor $`\sqrt{E(E+1)}`$ cannot in general be replaced by a constant times $`E`$, uniformly as $`E\downarrow0`$, for this binary-phase cipher. Consider, for $`0<E<2`$,

```math
|\psi_\pm\rangle=
\sqrt{1-E/2}\,|0\rangle
\pm\sqrt{E/2}\,|2\rangle.
```

These plaintexts have energy $`E`$ and are invariant under parity. Put $`s=V+1`$ and $`g_s(z)=e^{-|z|^2/s}/(\pi s)`$. Gaussian convolution of their Husimi densities gives

```math
q_+(z)-q_-(z)
=\frac{2\sqrt{E(1-E/2)}}{s^2}
  \mathrm{Re}(z^2)g_s(z).
```

For $`Z`$ distributed according to $`g_s`$, the radial and angular variables are independent, with $`\mathbb E|Z|^2=s`$ and $`\mathbb E|\cos(2\arg Z)|=2/\pi`$. Hence

```math
\mathrm{TV}(q_+,q_-)
=\frac{2\sqrt{E(1-E/2)}}{\pi(V+1)}.
```

The arbitrary-replacer lower bound is half this value:

```math
\boxed{
\delta_E^*(\mathcal N_V\circ\Phi_2)
\ge\frac{\sqrt{E(1-E/2)}}{\pi(V+1)},
\qquad 0<E<2.
}
```

In particular, at small $`E`$ the binary-phase cipher has unavoidable leakage of order $`\sqrt E/V`$. G2's full phase averaging removes the vacuum–two-photon coherence as well and obtains $`E/(V+1)`$ uniformly. The distinction matters when varying the input-energy budget; it does not change G3's inverse-linear dependence on $`V`$ for fixed $`E>0`$.

## Relation to the phase criterion and key resources

The binary construction works because its phase distribution has zero first Fourier coefficient. [The phase-criterion chapter](phase_criterion.md) proves that this condition characterizes the improved exponent within independent phase-preprocessing schemes. It also proves that one bit is the minimum discrete phase-key entropy for exact cancellation, and quantifies imperfect cancellation.

Composition of optical phase rotations and displacements is prior art; see the comparisons with [Kuang and Chan (2023)](../references/RELATED_WORK.md#kuang2023phase), [Kuang (2025)](../references/RELATED_WORK.md#kuang2025dynamic), and [Zhang et al. (2026)](../references/RELATED_WORK.md#zhang2026practical). The mathematical claims here concern the stated reference-aware error and energy budget. They do not identify the number of bits needed to approximate a continuous displacement key, and they do not confer authentication, key reuse, or security after disclosure of that key.
