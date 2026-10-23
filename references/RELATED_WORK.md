# Related work and source map

The model in this repository combines exact keyed recovery on an oscillator, a mean-photon-number constraint on arbitrary reference-entangled messages, and an explicit charge for ciphertext energy. These requirements should be kept together when comparing results. Hilbert–Schmidt approximation, pairwise secrecy on coherent states, authentication error, and energy-constrained diamond secrecy are different guarantees.

Optical displacement encryption, secret phase rotations, finite-dimensional quantum one-time pads, and moment cancellation are established ideas. The results developed here concern their quantitative consequences in the [specified model](../science/model.md): the reversible-cipher energy converse, matching finite-key construction, and reference-aware bounds for independent phase randomization followed by Gaussian displacement. The comparison below identifies the relevant earlier statements without claiming that the underlying controls or analytical tools are new.

Each source heading has an anchor equal to its key in [references.bib](references.bib). Page numbers refer to printed pages unless stated otherwise.

## 1. Quantum encryption, recoverability, and the security metric

<a id="ambainis2000private"></a>
### Ambainis, Mosca, Tapp and de Wolf (2000)

**Private Quantum Channels.** FOCS 2000, pp. 547–553. [DOI](https://doi.org/10.1109/SFCS.2000.892142); [author-hosted paper](https://homepages.cwi.nl/~rdewolf/publ/qc/AMTW00.pdf).

This is foundational finite-dimensional private-channel work. Uniform Weyl randomization on a finite subspace is the standard quantum one-time-pad ingredient in the [finite-key construction](../science/finite_key.md). Extending those unitaries to the oscillator while controlling coherence with the unbounded tail is a separate step. The related [arXiv:quant-ph/0003101v2](https://arxiv.org/abs/quant-ph/0003101v2) preprint lists Mosca, Tapp and de Wolf; that author list should not be substituted for the four-author conference publication.

<a id="desrosiers2010entropic"></a>
### Desrosiers and Dupuis (2010)

**Quantum Entropic Security and Approximate Quantum Encryption.** IEEE Transactions on Information Theory **56**(7), 3455–3464. [DOI](https://doi.org/10.1109/TIT.2010.2048488); [arXiv:0707.0691v2](https://arxiv.org/abs/0707.0691v2), 15 April 2010.

Section VI, Theorem 6, gives approximate quantum Shannon impossibility with a reference system. This supplies the finite-dimensional key-cardinality principle used in the [key converse](../science/finite_key.md). Its norm convention must be translated explicitly. Equation (41) also requires the squared factor documented by Lai and Chung below. The bosonic argument additionally uses an energy-diluted, reference-flagged entangled state; the finite-dimensional theorem alone does not lower-bound ciphertext energy.

<a id="lai2019encryption"></a>
### Lai and Chung (2019; preprint 2018)

**Quantum encryption and generalized Shannon impossibility.** Designs, Codes and Cryptography **87**, 1961–1972. [DOI and published article](https://link.springer.com/article/10.1007/s10623-018-00597-3); [arXiv:1801.03656v2](https://arxiv.org/abs/1801.03656v2), 27 September 2018.

The preprint title is *Quantum Encryption and Generalized Quantum Shannon Impossibility*. Its introductory Eq. (1) and footnote 1, corresponding to Note 1 in the journal article, record the squared-factor correction to Desrosiers–Dupuis Eq. (41). Theorem 11 treats imperfect correctness as well as secrecy. These are finite-dimensional key-alphabet results. The repository states its own distance conventions and includes the overlap proof needed for its infinite-dimensional decoder, rather than transferring constants between definitions implicitly.

<a id="nayak2007invertible"></a>
### Nayak and Sen (2007)

**Invertible quantum operations and perfect encryption of quantum states.** Quantum Information and Computation **7**(1–2), 103–110. [Journal record](https://www.rintonpress.com/journals/doi/QIC7.1-2-6.html); [arXiv:quant-ph/0605041](https://arxiv.org/abs/quant-ph/0605041).

The structure of reversible finite-dimensional channels is established background. The [energy converse](../science/energy_cost.md) proves the orthogonality and spectral statements it needs directly for normal oscillator channels. It does not invoke this finite-dimensional structure theorem as an unqualified infinite-dimensional result.

<a id="shirokov2018energy"></a>
### Shirokov (2018)

**On the Energy-Constrained Diamond Norm and Its Application in Quantum Information Theory.** Problems of Information Transmission **54**(1), 20–33. [DOI](https://doi.org/10.1134/S0032946018010027); [arXiv:1706.00361v2](https://arxiv.org/abs/1706.00361v2), 23 June 2017.

The preprint title is *Energy-constrained diamond norms and their use in quantum information theory*. This provides the infinite-dimensional, reference-stable norm framework behind the secrecy definition. Applying that framework to ciphertext replacement does not itself establish a reversible-encryption resource bound.

<a id="winter2017energy"></a>
### Winter (2017)

**Energy-constrained diamond norm with applications to the uniform continuity of continuous variable channel capacities.** [arXiv:1712.10267v1](https://arxiv.org/abs/1712.10267v1), 29 December 2017.

This is another primary source for energy-constrained channel comparison and the role of an unrestricted reference system. Its channel-capacity continuity questions differ from charging the energy of an exactly decryptable ciphertext.

<a id="fuchs1999cryptographic"></a>
### Fuchs and van de Graaf (1999)

**Cryptographic distinguishability measures for quantum-mechanical states.** IEEE Transactions on Information Theory **45**(4), 1216–1227. [DOI](https://doi.org/10.1109/18.761271); [arXiv:quant-ph/9712042](https://arxiv.org/abs/quant-ph/9712042).

The trace-distance/fidelity inequalities used in the proofs are standard tools from this work. Throughout the repository, trace distance includes the factor $`1/2`$ and fidelity without a square means root fidelity.

<a id="uhlmann1976transition"></a>
### Uhlmann (1976)

**The “transition probability” in the state space of a $`*`$-algebra.** Reports on Mathematical Physics **9**(2), 273–279. [DOI](https://doi.org/10.1016/0034-4877(76)90060-4); [author-hosted paper](https://www.physik.uni-leipzig.de/~uhlmann/PDF/Uh76a.pdf).

Purification and fidelity comparisons in the key converse use the standard Uhlmann principle. The explicit decoder overlap estimate in that proof supplies the additional dimension-dependent ingredient.

## 2. Continuous-variable encryption

<a id="bradler2005private"></a>
### Brádler (2005)

**Continuous-variable private quantum channel.** Physical Review A **72**, 042313. [DOI](https://doi.org/10.1103/PhysRevA.72.042313); [arXiv:quant-ph/0505118v2](https://arxiv.org/html/quant-ph/0505118v2), 18 July 2005.

Section III studies finite displacement ensembles for coherent states in a bounded phase-space region, using Hilbert–Schmidt estimates; Section IV discusses Holevo information. The paragraph after Eq. (17) also describes a fixed displacement followed by a random phase shift. Thus phase operations already occur in early private-channel proposals. The Hilbert–Schmidt target in the displacement argument follows the input displacement, so that comparison should not be read as a fixed replacement-channel guarantee for arbitrary reference-entangled messages.

<a id="kruger2006gaussian"></a>
### Krüger (2006)

**Quantum Information Theory with Gaussian Systems.** Doctoral dissertation, Technische Universität Carolo-Wilhelmina zu Braunschweig. [Primary dissertation PDF](https://d-nb.info/984129804/34), Chapter 5.

Equation (5.7), p. 107, bounds pairwise trace norm for products of bounded-energy coherent states under Gaussian displacement. Proposition 5.1 and Corollary 5.2, p. 113, give a truncated and discretized finite-key construction; the single-mode corollary takes noise parameter $`g\ge400E_{\max}/\epsilon^2`$. This already establishes inverse-square error dependence for displacement encryption on a coherent-state family. Its full trace norm and noise-covariance parameter should not be identified with this repository's half trace distance and $`V`$ without conversion. The input family does not include an arbitrary entangled reference, and no universal reversible-cipher ciphertext-energy converse is supplied.

<a id="jeong2015gaussian"></a>
### Jeong, Kim and Lee (2015)

**Gaussian private quantum channel with squeezed coherent states.** Scientific Reports **5**, 13974. [DOI](https://doi.org/10.1038/srep13974); [arXiv:1412.6870v2](https://arxiv.org/html/1412.6870v2), 14 September 2015.

This extends displacement-based private channels using squeezing, with Hilbert–Schmidt estimates, accessible-information considerations, and a beam-splitter attack example. It provides useful optical-encryption precedent. Those guarantees do not establish the mean-energy-only, arbitrary-reference replacement criterion used here.

<a id="ouyang2020homomorphic"></a>
### Ouyang, Tan, Fitzsimons and Rohde (2020)

**Homomorphic encryption of linear optics quantum computation on almost arbitrary states of light with asymptotically perfect security.** Physical Review Research **2**, 013332. [DOI](https://doi.org/10.1103/PhysRevResearch.2.013332); [published PDF](https://eprints.whiterose.ac.uk/id/eprint/198725/1/PhysRevResearch.2.013332.pdf); [arXiv:1902.10972v2](https://arxiv.org/html/1902.10972v2), 19 March 2020.

This predecessor treats arbitrary finite-cutoff states using pairwise trace distance. The [quantitative comparison](../science/displacement_comparison.md) checks its rate separately from asymptotic secrecy and homomorphic functionality.

<a id="temel2025authentication"></a>
### Temel and Škorić (2025)

**Authentication of continuous-variable quantum messages.** Quantum Information Processing **24**, 369, published 14 November 2025. [Published article](https://link.springer.com/article/10.1007/s11128-025-04991-4).

The trap-based authentication protocol uses a Gaussian quantum one-time pad and a security definition with a reference system. Theorem 4.1 and Lemma 4.2 analyze authentication and a finite-width displacement twirl. Their parameters include squeezing and trap width; the exponential width correction is not a uniform mean-input-energy secrecy law. The discussion also identifies subtleties in the continuum displacement model. No authentication claim follows from the encryption bounds in this repository, and the authentication theorem should not be substituted for a ciphertext-energy converse.

<a id="kuang2023phase"></a>
### Kuang and Chan (2023)

**Quantum encryption in phase space with displacement operators.** EPJ Quantum Technology **10**, 26. [Published article](https://link.springer.com/article/10.1140/epjqt/s40507-023-00183-0).

This uses secret, synchronized displacement choices for coherent-state optical modulation, including QPSK and 16-QAM. Its communication alphabet and key-sequence model differ from information-theoretic encryption of an unknown quantum message with arbitrary side information.

<a id="kuang2025dynamic"></a>
### Kuang (2025)

**Quantum encryption in phase space with dynamic displacement operators and quantum permutation pad.** Academia Quantum **2**, published 6 January 2025. [DOI](https://doi.org/10.20935/AcadQuant7462); [published PDF](https://inspirehep.net/files/738afa7cd22e2d0412324f884e810fb5).

Section 2.3 explicitly composes a phase operation and a displacement, $`D(\alpha)P(\phi)`$. Section 2.5 discusses key-pad search complexity. This is direct precedent for the component sequence; it does not prove a trace-distance theorem on the whole mean-energy ball.

<a id="zhang2026practical"></a>
### Zhang, Kuang, Xu, Wen, Wu, Zhang and Dong (2026)

**Toward practical quantum encryption in phase space: simulated QPSK and 16-QAM with dynamic displacement operators.** EPJ Quantum Technology **13**, 41, published 27 February 2026. [Published article](https://link.springer.com/article/10.1140/epjqt/s40507-026-00480-4).

The simulation combines displacement and phase settings for coherent-state constellations, with bit-error-rate and signal-processing analysis. It reinforces the optical-control precedent. Its discrete modulation experiment does not establish arbitrary-reference secrecy or an optimal ciphertext-energy scaling law.

<a id="ray2026design"></a>
### Ray and Škorić (2026)

**Continuous-variable approximate unitary 2-design, with applications to unclonable encryption.** [arXiv:2603.06393v1](https://arxiv.org/html/2603.06393v1), 6 March 2026.

This constructs an approximate design on a discretized, finite quadrature window and applies it to classical-bit unclonable encryption. Lemma 3.1 controls discretization under its tail assumptions. Finite-window approximation and unclonability are different requirements from exact recovery on the full oscillator and ordinary reference-aware secrecy. The work does not supply the ciphertext-energy converse used here.

## 3. Gaussian channel identities and convergence

<a id="ivan2011operatorsum"></a>
### Ivan, Sabapathy and Simon (2011)

**Operator-sum representation for bosonic Gaussian channels.** Physical Review A **84**, 042311. [DOI](https://doi.org/10.1103/PhysRevA.84.042311); [arXiv:1012.4266](https://arxiv.org/abs/1012.4266).

Sections IV and V give attenuator and amplifier operator-sum representations; Section IX treats compositions representing noisy Gaussian channels. These Fock-basis identities underlie the estimates in the [Gaussian chapter](../science/gaussian_encryption.md) and the [matrix-element comparison](../science/displacement_comparison.md). They are attributed analytical inputs, rather than new encryption results.

<a id="mishra2023teleportation"></a>
### Mishra, Khabbazi Oskouei and Wilde (2023)

**Optimal input states for quantifying the performance of continuous-variable unidirectional and bidirectional teleportation.** Physical Review A **107**, 062603. [DOI](https://doi.org/10.1103/PhysRevA.107.062603); [accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.107.062603).

Section III, p. 3, immediately before Eq. (8), explicitly writes additive noise as a quantum-limited attenuator followed by a quantum-limited amplifier, with $`\eta=1/(1+\xi)`$. In the present notation this is $`\mathcal N_V=\mathcal A_{V+1}\circ\mathcal L_{1/(V+1)}`$. The source applies it to energy-constrained teleportation performance; its use here is to estimate the averaged encryption channel.

<a id="bertini2024trace"></a>
### Bertini, De Sole and Posta (2024)

**Trace distance ergodicity for quantum Markov semigroups.** Journal of Functional Analysis **286**(7), 110340. [DOI](https://doi.org/10.1016/j.jfa.2024.110340); [arXiv:2206.11923v2](https://arxiv.org/html/2206.11923v2), 30 January 2024.

Section 5 describes polynomial eigenoperators of the thermal Bose Ornstein–Uhlenbeck semigroup. Removing low-degree coefficients can therefore remove slow spectral components; that observation is an inference from its formulas, not a parity-encryption theorem stated there. Theorem 5.4 uses the all-order moment class in Eq. (5.9) and a faithful thermal invariant state. It is not a first-moment-only, arbitrary-reference estimate for loss toward vacuum.

<a id="depalma2018conditional"></a>
### De Palma and Huber (2018)

**The conditional entropy power inequality for quantum additive noise channels.** Journal of Mathematical Physics **59**, 122201. [DOI](https://doi.org/10.1063/1.5027495); [arXiv:1803.00470v2](https://arxiv.org/abs/1803.00470v2), 4 December 2018.

Section 9, Theorem 9, proves thermal Ornstein–Uhlenbeck relative-entropy contraction with a reference system. A direct Pinsker conversion gives a square-root trace-distance rate. It does not supply the first-harmonic cancellation estimate used here, and its faithful thermal reference cannot simply be replaced by vacuum in a relative-entropy expression.

<a id="becker2021convergence"></a>
### Becker, Datta, Lami and Rouzé (2021)

**Convergence Rates for the Quantum Central Limit Theorem.** Communications in Mathematical Physics **383**, 223–279. [Published article](https://link.springer.com/article/10.1007/s00220-021-03988-1); [arXiv:1912.06129](https://arxiv.org/abs/1912.06129).

Theorem 6 proves accelerated Hilbert–Schmidt central-limit convergence when the relevant third-order characteristic-function derivative vanishes, under centering and finite fourth-moment assumptions. This explicitly establishes moment-cancellation acceleration in bosonic convergence theory. It concerns combining many copies and approaching the Gaussian state with matching moments, rather than reference-stable erasure of a single arbitrary input using only its mean photon number.

These comparisons delimit the analytical claim. Suppressing a slow moment is a familiar mechanism. The additional issue in encryption is a uniform trace-distance statement that retains an arbitrary reference. Scalar centering of the oscillator marginal is insufficient: a reference can record the sign of a symmetric coherent-state mixture. The [phase criterion](../science/phase_criterion.md) addresses the stronger operator-valued cancellation.

## 4. General references

<a id="weedbrook2012gaussian"></a>
### Weedbrook et al. (2012)

**Gaussian quantum information.** Reviews of Modern Physics **84**, 621–669. [DOI](https://doi.org/10.1103/RevModPhys.84.621); [arXiv:1110.3234](https://arxiv.org/abs/1110.3234).

Sections II and V provide background on states, Gaussian unitaries, measurements, and channels. The review uses a quadrature normalization different from this repository's vacuum variance $`1/2`$; physical parameters must be converted before comparing formulas.

<a id="holevo2019quantum"></a>
### Holevo (2019), second revised and expanded edition

**Quantum Systems, Channels, Information: A Mathematical Introduction.** De Gruyter, Berlin and Boston. [Publisher](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490/html); [contents](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490-toc/html). DOI: 10.1515/9783110642490.

Chapters 6, 11 and 12 cover channels, input constraints, and Gaussian systems. This supplies mathematical background for the distinction between finite-dimensional randomization and constrained infinite-dimensional channel problems.

<a id="watrous2018theory"></a>
### Watrous (2018)

**The Theory of Quantum Information.** Cambridge University Press. [DOI](https://doi.org/10.1017/9781316848142); [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).

Chapters 2–4 provide the finite-dimensional channel, purification, distinguishability, fidelity, and mixed-unitary background used in the proofs. The oscillator-specific energy and normal-channel arguments are supplied separately in the science chapters.
