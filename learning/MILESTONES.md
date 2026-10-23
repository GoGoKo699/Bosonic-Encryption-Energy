# Thirty milestones for bosonic encryption energy

This map follows the scientific question from the states carried by one oscillator to the resources required to encrypt them. It has exactly **30 project-defined milestones** in two phases: **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The allocation reflects the need to join reference-aware quantum encryption with Gaussian optical physics before developing the energy, key, and phase-coherence arguments.

The sole educational anchor is **Weedbrook et al., *Gaussian Quantum Information***, [Reviews of Modern Physics 84, 621 (2012)](https://doi.org/10.1103/RevModPhys.84.621), available as [arXiv:1110.3234v1](https://arxiv.org/abs/1110.3234v1). Section labels below follow the PDF's lettered subsections. The experimental arXiv HTML uses numerical subsection labels for the same headings. [WEEDBROOK_BRIDGE.md](WEEDBROOK_BRIDGE.md) supplies the selected reading route, notation translation, and steps from that foundation to this project.

The anchor pointers identify relevant foundations; they do not attribute the project's encryption theorems to the review. In particular, the energy-constrained replacement criterion, flagged-state reductions, and quantum Shannon argument require the locally supplied explanations and proofs. Primary research dependencies remain attributed in the linked science chapters. This map covers the connected argument and its consequential assumptions, rather than every calculation or neighboring subject.

| Phase | Milestones | Local-to-global development | Synthesis endpoint |
| --- | --- | --- | --- |
| Background/preliminaries | M01–M12 | Oscillator states and energy; references and distinguishability; optical controls and measurements | M12 assembles the complete encryption experiment and resource model |
| Narrative/innovation | M13–M30 | Support and tail arguments become resource laws; controlled coherences become a sharp optical rate criterion | M30 joins the resource laws, optical mechanism, evidence, and scope |

Each milestone inherits the phase in which it appears. Dependencies name earlier milestones; the linked scientific headings are the authoritative locations of definitions, statements, and proofs.

## Phase I: Background/preliminaries — M01–M12

### M01. One oscillator and its charged energy

**Central question:** What physical system carries a plaintext or ciphertext, and what counts as its energy?

**Understanding target:** Identify the Fock levels, number operator, and vacuum; distinguish photon number from physical energy at a fixed frequency. Recognize why one nondegenerate oscillator provides only finitely many orthogonal states below any finite energy threshold.

**Dependencies and story role:** No earlier milestone. Establishes the carrier whose spectrum later turns distinguishability into an energy cost.

**Conceptual connection:** The infinite Fock basis and continuous quadratures describe the same oscillator. The fixed spectrum is a resource assumption, not merely notation.

**Source pointers:** Weedbrook §§II.A and II.B.1; [Model, “1. Carrier and message family”](../science/model.md#1-carrier-and-message-family).

### M02. Populations, coherence, and mixtures

**Central question:** What information can a state contain beyond its photon-number probabilities?

**Understanding target:** Distinguish a coherent superposition from a mixture with the same populations. Explain what off-diagonal Fock matrix elements describe and why erasing selected coherences can change distinguishability without changing mean photon number.

**Dependencies and story role:** M01. Introduces the local information that the optical constructions will control.

**Conceptual connection:** Phase-space descriptions complement the Fock description, but a covariance matrix does not specify an arbitrary non-Gaussian state. The message family includes both Gaussian and non-Gaussian states.

**Source pointers:** Weedbrook §§II.A.1, II.B.2, and II.B.4; [Model, “1. Carrier and message family”](../science/model.md#1-carrier-and-message-family); [Phase criterion, “Definitions and conventions”](../science/phase_criterion.md#definitions-and-conventions).

### M03. A mean-energy bound permits rare high levels

**Central question:** Why does a small mean photon number fail to impose a photon cutoff?

**Understanding target:** Explain how weight $`E/n`$ at a sufficiently high level $`n\ge E`$ can obey the same budget as a low-energy state. Relate the bound $`N\ge dQ_d`$ to the tail estimate $`\mathrm{Tr}(Q_d\rho)\le E/d`$, while retaining the possible coherence of a general input.

**Dependencies and story role:** M01–M02. Establishes the rare events used both to force resource costs and to bound construction error.

**Conceptual connection:** A constraint on an average controls tail probability but leaves the dimension of possible message support unbounded.

**Source pointers:** Weedbrook §II.A for the Fock description; [Model, “1. Carrier and message family”](../science/model.md#1-carrier-and-message-family); [Finite key, “Proof of the secrecy formula”](../science/finite_key.md#proof-of-the-secrecy-formula).

### M04. Information retained in a reference system

**Central question:** What changes when another system remembers a branch of the plaintext preparation?

**Understanding target:** Distinguish an oscillator marginal from its joint state with a reference. Explain classical flags, entanglement, and why a claim about the marginal alone need not hide correlations. Recognize that the reference is neither transmitted as free ciphertext nor available to the encoder.

**Dependencies and story role:** M02–M03. Makes the later flagged witnesses and operator-valued coherence estimates meaningful.

**Conceptual connection:** The same reference framework covers a classical record of a rare event and coherent quantum side information; the two play different roles in the resource converses.

**Source pointers:** Weedbrook §§II.B.7 and II.D.1; [Model, “1. Carrier and message family”](../science/model.md#1-carrier-and-message-family); [Interpretation, “4. Why centering the reduced state is insufficient”](../science/interpretation.md#4-why-centering-the-reduced-state-is-insufficient).

### M05. Keyed recovery and the averaged channel

**Central question:** How can encryption be reversible for its recipient while looking noisy without the key?

**Understanding target:** Separate a keyed encoder–decoder pair from the channel averaged over an independent classical key. Explain exact recovery on the full oscillator, including its reference correlations, and allow reversible CPTP encoders beyond unitary examples.

**Dependencies and story role:** M02 and M04. Establishes the correctness condition behind every central converse and construction.

**Conceptual connection:** A mixed description caused by an unknown key can coexist with exact conditional recovery. A mathematical decomposition of the averaged channel need not describe the sender's physical sequence of operations.

**Source pointers:** Weedbrook §§II.A.2 and V.A; [Model, “2. Secret key and exact recovery”](../science/model.md#2-secret-key-and-exact-recovery).

### M06. Secrecy as replacement without disturbing the reference

**Central question:** What does it mean for every allowed ciphertext to reveal essentially no additional information?

**Understanding target:** Interpret half trace distance and its contraction under channels. Explain why secrecy compares the joint output with one input-independent state $`\tau_C\otimes\rho_R`$. Distinguish a proved bound for a specified target from a lower bound against every replacement target.

**Dependencies and story role:** M03–M05. Turns the message family and observer's information into a uniform operational criterion.

**Conceptual connection:** State distinguishability becomes a channel guarantee by including every allowed input and reference. The infinite-dimensional energy constraint belongs to that quantification.

**Source pointers:** Weedbrook §III.A.1; [Model, “3. Secrecy and distance convention”](../science/model.md#3-secrecy-and-distance-convention); [Gaussian encryption, “Conventions and secrecy criterion”](../science/gaussian_encryption.md#conventions-and-secrecy-criterion).

### M07. Displacements and phase rotations

**Central question:** What do the two keyed optical controls change, and how are they reversed?

**Understanding target:** Explain how displacement shifts phase space and a phase rotation changes Fock coherences while preserving number populations. Translate the review's quadrature normalization and rotation convention using the bridge, and preserve the order of operations when taking the inverse.

**Dependencies and story role:** M01–M02 and M05. Supplies the elementary controls for the optical branch of the story.

**Conceptual connection:** A geometric phase-space transformation is also an exact unitary action on all Fock states, including non-Gaussian messages and their reference correlations.

**Source pointers:** Weedbrook §§I.D, II.B.2, and II.B.4; [Weedbrook bridge](WEEDBROOK_BRIDGE.md); [Phase criterion, “Definitions and conventions”](../science/phase_criterion.md#definitions-and-conventions).

### M08. Thermal ciphertext and displacement energy

**Central question:** Why is the encrypted vacuum a useful replacement target for Gaussian displacement?

**Understanding target:** Identify the thermal vacuum output and the displacement parameter $`V`$ as added mean photon number. Distinguish the average energy formula from a bound for every individual key. Explain why Gaussian keyed controls need not produce a Gaussian averaged channel when phase mixing is included.

**Dependencies and story role:** M01, M05, and M07. Connects the optical noise parameter to the resource charged by the project.

**Conceptual connection:** The same parameter can describe phase-space noise and ciphertext excitation only after the conventions are fixed. The random displacement has unbounded support even when its average energy is finite.

**Source pointers:** Weedbrook §§II.B.1–II.B.2 and V.B; [Gaussian encryption, “Conventions and secrecy criterion”](../science/gaussian_encryption.md#conventions-and-secrecy-criterion) and [“G3. A single phase bit suffices for the improved exponent”](../science/gaussian_encryption.md#g3-a-single-phase-bit-suffices-for-the-improved-exponent); [Model, “4. The charged resources”](../science/model.md#4-the-charged-resources).

### M09. Gaussian channels on arbitrary inputs

**Central question:** What do attenuation and amplification mean beyond their action on covariance matrices?

**Understanding target:** Distinguish a channel's Gaussian classification from a restriction to Gaussian inputs. Relate attenuation and amplification to environmental dilations, and explain why characteristic functions or Fock Kraus operators are needed to establish channel identities on arbitrary states.

**Dependencies and story role:** M02, M05, and M07–M08. Prepares the analytical channel representation used to prove optical secrecy.

**Conceptual connection:** Simple optical noise models provide exact tools for a message family that includes rare tails and non-Gaussian coherence.

**Source pointers:** Weedbrook §§II.A.1, II.B.6–II.B.7, and V.A–V.B; [Gaussian encryption, “G1. Standard factorization and the displacement-only benchmark”](../science/gaussian_encryption.md#g1-standard-factorization-and-the-displacement-only-benchmark).

### M10. Measurements as lower-bound witnesses

**Central question:** How can a particular optical measurement disprove a proposed secrecy guarantee?

**Understanding target:** Distinguish homodyne from heterodyne outcomes and interpret their classical total variation distance. Explain measurement contraction and the extra factor of one half when a pairwise output distance is converted into a lower bound against an arbitrary replacer.

**Dependencies and story role:** M06–M08. Establishes the operational witnesses that will determine the optical exponents and check earlier claims.

**Conceptual connection:** A convenient measurement need not be optimal to supply a valid impossibility witness. A measurement lower bound and an arbitrary-reference upper bound are different forms of evidence.

**Source pointers:** Weedbrook §§II.E.1–II.E.2 and III.A.1; [Displacement comparison, “1. Conventions”](../science/displacement_comparison.md#1-conventions); [Gaussian encryption, “Conventions and secrecy criterion”](../science/gaussian_encryption.md#conventions-and-secrecy-criterion).

### M11. Purification and fidelity as recovery tools

**Central question:** How can near-perfect recovery constrain information retained by an environment?

**Understanding target:** Interpret purification as a representation of a mixed state and distinguish root fidelity from its square. Understand how a nearly recovered entangled state can be compared with a product purification, and why tracing auxiliary systems preserves a valid distance bound.

**Dependencies and story role:** M04–M06. Supplies the conceptual proof tools for the correctness extension and the finite-key converse without introducing an extra transmitted resource.

**Conceptual connection:** Closeness of recovered quantum states controls both concentration of encoded states and the number of classical key branches needed to hide entanglement.

**Source pointers:** Weedbrook §§III.A.3 and V.A; [Energy cost, “5. Robust variant of E2: approximate keyed recovery”](../science/energy_cost.md#5-robust-variant-of-e2-approximate-keyed-recovery); [Finite key, “2. The known finite-dimensional key lemma”](../science/finite_key.md#2-the-known-finite-dimensional-key-lemma).

### M12. Background synthesis: the complete encryption experiment

**Central question:** Which objects, promises, and resources must be specified before comparing encryption schemes?

**Understanding target:** Assemble the fixed oscillator, mean-energy message family, arbitrary reference, independent key, exact keyed recovery, and replacement criterion into one model. Separate ciphertext excitation, key-alphabet size, discrete phase entropy, and continuous control randomness; identify which physical costs the model charges.

**Dependencies and story role:** M01–M11. Integrates the background into the common framework used by both scientific branches.

**Conceptual connection:** The Gaussian review supplies operations and measurements, while the project's full model determines the cryptographic quantifiers. Encryption using a pre-existing secret key and distributing a new key are distinct operational tasks.

**Source pointers:** Weedbrook §§V.A–V.B, with §VI.A only for the task distinction; [Model, “2. Secret key and exact recovery”](../science/model.md#2-secret-key-and-exact-recovery), [“3. Secrecy and distance convention”](../science/model.md#3-secrecy-and-distance-convention), and [“4. The charged resources”](../science/model.md#4-the-charged-resources); [Weedbrook bridge](WEEDBROOK_BRIDGE.md).

## Phase II: Narrative/innovation — M13–M30

### M13. Reversibility forces a diffuse encoded state

**Central question:** Why can an exactly reversible encoder not concentrate a uniform collection of orthogonal inputs into one ciphertext direction?

**Understanding target:** Follow the E1 argument from perfectly recoverable Fock labels to orthogonal encoded supports, then to $`\mathcal E(\pi_d)\le I/d`$. Explain why averaging over keys preserves that inequality even for reversible CPTP encoders with private randomness.

**Dependencies and story role:** M01, M05–M06, and M12. Starts the resource converse with a local statement about recoverability and spectral concentration.

**Conceptual connection:** The authorized decoder's ability to distinguish inputs constrains the observer's average state before any energy calculation is made.

**Source pointers:** Weedbrook §§III.A.1 and V.A for foundations; [Energy cost, “2. E1: exact recovery preserves diffuseness”](../science/energy_cost.md#2-e1-exact-recovery-preserves-diffuseness).

### M14. Diffuseness becomes a photon-number cost

**Central question:** How does a bound on concentration force occupation of higher Fock levels?

**Understanding target:** Relate the rank of each low-energy projector to its maximum probability in a diffuse state. Interpret the energy tail sum and $`B_d(\delta)`$ as the excitation forced by proximity to such a state, including its finite-parameter floor-function structure.

**Dependencies and story role:** M01, M03, M06, and M13. Converts E1's abstract support constraint into the physical quantity being charged.

**Conceptual connection:** State-space dimension becomes energy through the fixed nondegenerate spectrum. A changed spectrum or an uncharged side register would change this step.

**Source pointers:** Weedbrook §§II.A and II.B.1 for the oscillator foundation; [Energy cost, “3. From diffuseness to photon number”](../science/energy_cost.md#3-from-diffuseness-to-photon-number).

### M15. A rare flagged branch forces energetic vacuum encryption

**Central question:** Why must even the ciphertext of vacuum pay for large message subspaces that are used only rarely?

**Understanding target:** Follow the reference-flagged dilution of $`\pi_d`$ and the role of $`p_d\le1/2`$ in comparing its ciphertext with the encrypted vacuum. Combine that comparison with M14 to understand E2, its inverse-linear resource law, and the impossibility of perfect secrecy at fixed $`E>0`$.

**Dependencies and story role:** M03–M06 and M13–M14. Joins the local support and tail arguments into the universal energy obstruction.

**Conceptual connection:** Mean-energy admissibility and reference-aware secrecy jointly keep a large, rare branch relevant. Infinite ciphertext energy does not remove the normalization contradiction at zero error.

**Source pointers:** Weedbrook §§III.A.1 and V.A for the distance and channel background; [Energy cost, “4. E2: a universal ciphertext-energy converse”](../science/energy_cost.md#4-e2-a-universal-ciphertext-energy-converse); [Interpretation, “1. Why even the vacuum must become energetic”](../science/interpretation.md#1-why-even-the-vacuum-must-become-energetic).

### M16. The energy obstruction survives small correctness error

**Central question:** Which part of the converse persists when decoding is close to, rather than exactly, the identity?

**Understanding target:** Distinguish averaged reference-aware correctness error $`\gamma`$ from secrecy error $`\epsilon`$. Explain how a flagged entangled input and purification replace exact diffuseness by an approximate concentration bound, giving E2R with $`\epsilon/p_d+\sqrt{\gamma/p_d}`$.

**Dependencies and story role:** M11 and M13–M15. Extends the converse while keeping the altered correctness assumption explicit.

**Conceptual connection:** Approximate recovery bounds how much encoded probability can concentrate in a low-dimensional subspace. The resulting robust lower bound is not a complete optimal tradeoff for independently varied correctness and secrecy errors.

**Source pointers:** Weedbrook §§III.A.3 and V.A; [Energy cost, “5. Robust variant of E2: approximate keyed recovery”](../science/energy_cost.md#5-robust-variant-of-e2-approximate-keyed-recovery).

### M17. A finite-block cipher with full-oscillator inverses

**Central question:** How can a finite key randomize a low-energy block while preserving every possible tail state for the recipient?

**Understanding target:** Explain the separate actions of the finite Weyl twirl and the random relative sign between the low block and its complement. Recognize the direct-sum unitary's exact inverse and why the tail is preserved rather than physically discarded.

**Dependencies and story role:** M02–M05 and M12. Introduces the construction that will attain the energy law.

**Conceptual connection:** Finite-dimensional randomization can be embedded in the full oscillator. The block sign removes cross-block coherence; it is a different operation from optical photon parity.

**Source pointers:** Weedbrook §§II.A and V.A for the state and channel framework; [Finite key, “1. C1: a finite Fock-block construction”](../science/finite_key.md#1-c1-a-finite-fock-block-construction); [Interpretation, “4. Why centering the reduced state is insufficient”](../science/interpretation.md#4-why-centering-the-reduced-state-is-insufficient).

### M18. Exact tail leakage and the attained energy order

**Central question:** Why does the finite-block construction have secrecy error exactly equal to the tail probability?

**Understanding target:** Use the orthogonal supports of the two difference terms to explain $`T=q`$ for arbitrary references and $`\delta_E(\mathcal C_d;\pi_d)=\min\{1,E/d\}`$. Connect the cutoff choice to $`C_{\rm vac}=(d-1)/2`$ and the supremum $`C_{\max}(E)=E+(d-1)/2`$.

**Dependencies and story role:** M03–M06, M15, and M17. Shows how a complete construction meets the converse's energy order.

**Conceptual connection:** Rare tails supply the exact error mechanism and also explain why the maximal average ciphertext energy may be approached without being attained. The equality is for the specified replacer.

**Source pointers:** Weedbrook §§II.A and III.A.1 for foundations; [Finite key, “Proof of the secrecy formula”](../science/finite_key.md#proof-of-the-secrecy-formula), [“Proof of the energy formulas”](../science/finite_key.md#proof-of-the-energy-formulas), and [“Choosing the cutoff”](../science/finite_key.md#choosing-the-cutoff).

### M19. The quantum Shannon ingredient counts key branches

**Central question:** Why does hiding a $`d`$-dimensional entangled input require a key alphabet of order $`d^2`$?

**Understanding target:** Understand the known bound $`M\ge d^2(1-\delta)^2`$ through fidelity, a classical key extension, and controlled decoding. Distinguish counting key branches from bounding ciphertext rank, and retain the projection inequality needed when decoder outputs are infinite-dimensional.

**Dependencies and story role:** M04–M06 and M11. Supplies the attributed finite-dimensional ingredient for the second resource converse.

**Conceptual connection:** Hiding quantum correlations is stronger than randomizing unassisted input states. The argument permits nonuniform key probabilities and private encoder randomness but concludes a cardinality bound.

**Source pointers:** Weedbrook §§III.A.3 and V.A for foundations; [Finite key, “2. The known finite-dimensional key lemma”](../science/finite_key.md#2-the-known-finite-dimensional-key-lemma), including its primary-source attribution and complete proof.

### M20. Energy dilution gives the matching finite-key law

**Central question:** How does the finite-dimensional key bound constrain encryption under only a mean-energy promise?

**Understanding target:** Follow K1's flagged maximally entangled branch and distinguish its probability $`r_d\le1`$ from E2's $`p_d\le1/2`$. Combine K1 with C1 to obtain alphabet order $`(E/\epsilon)^2`$ and fixed-length cost $`2\log_2(E/\epsilon)+O(1)`$ in the stated regime.

**Dependencies and story role:** M03–M04, M15, and M17–M19. Completes the resource branch by connecting lower bounds with one common construction.

**Conceptual connection:** The two converses share dilution but exploit different reference information. Matching energy and key orders do not determine every energy–key tradeoff or the optimum Shannon entropy of a nonuniform key.

**Source pointers:** Weedbrook §§III.A.3 and V.A for the foundational tools; [Finite key, “3. K1: the energy-constrained key-cardinality converse”](../science/finite_key.md#3-k1-the-energy-constrained-key-cardinality-converse) and [“4. The joint resource statement”](../science/finite_key.md#4-the-joint-resource-statement).

### M21. Factorization reveals the optical leakage mechanism

**Central question:** Why is displacement encryption usefully analyzed as strong loss followed by amplification?

**Understanding target:** Interpret $`\mathcal N_V=\mathcal A_{V+1}\circ\mathcal L_{1/(V+1)}`$ as an exact identity of averaged channels. Explain why characteristic functions establish it beyond Gaussian inputs, and why the amplifier permits a preamplifier trace-distance upper bound.

**Dependencies and story role:** M05–M09 and M12. Opens the optical mechanism using the background channel tools.

**Conceptual connection:** Fictitious attenuation separates the probability of a surviving excitation from the coherence attached to it. The keyed sender still applies a reversible displacement, not physical loss.

**Source pointers:** Weedbrook §§II.A.1 and V.A–V.B; [Gaussian encryption, “G1. Standard factorization and the displacement-only benchmark”](../science/gaussian_encryption.md#g1-standard-factorization-and-the-displacement-only-benchmark).

### M22. Displacement alone leaves an inverse-square-root signal

**Central question:** Why does broad Gaussian displacement require noise of order $`\epsilon^{-2}`$ at fixed positive input energy?

**Understanding target:** Connect the arbitrary-reference loss upper bound with a coherent-state measurement lower bound. Explain how a nonvacuum probability of order $`\eta E`$ can coexist with a coherent contribution of square-root order, giving the G1 exponent.

**Dependencies and story role:** M06, M08–M11, and M21. Establishes the benchmark that additional phase randomization changes.

**Conceptual connection:** Small excitation probability alone does not imply an equally small trace distance when vacuum coherence remains. The matching exponent follows from an upper guarantee and an independent operational witness.

**Source pointers:** Weedbrook §§II.B.2, II.E.1–II.E.2, and III.A.1; [Gaussian encryption, “G1 bound”](../science/gaussian_encryption.md#g1-bound); [Displacement comparison, “2. Coherent-state lower bound for any replacement target”](../science/displacement_comparison.md#2-coherent-state-lower-bound-for-any-replacement-target).

### M23. Full phase averaging makes leakage a population effect

**Central question:** What changes when all off-diagonal number coherences are removed before displacement?

**Understanding target:** Explain the reference-valued number blocks produced by uniform phase averaging. Follow G2 from binomial loss to exact preamplifier distance equal to nonvacuum weight, and hence to the uniform bound $`E/(V+1)`$.

**Dependencies and story role:** M02, M04, M07, and M21–M22. Provides a simple mechanism for the improved energy dependence before reducing the phase randomness.

**Conceptual connection:** Complete phase averaging removes the coherent obstruction while retaining reference correlations within number blocks. The keyed phase and displacement are still individually invertible, and both ideal keys are continuous.

**Source pointers:** Weedbrook §§II.B.4 and V.B; [Gaussian encryption, “G2. Full phase averaging attains a linear energy bound”](../science/gaussian_encryption.md#g2-full-phase-averaging-attains-a-linear-energy-bound).

### M24. One parity bit cancels the slow coherence

**Central question:** Why is complete phase averaging unnecessary for an inverse-linear secrecy exponent?

**Understanding target:** Explain which coherences parity averaging removes and which survive. Follow the separation of vacuum population and cross-block coherence in G3, including why weighted Kraus-branch estimates need only the first photon-number moment. Distinguish Gaussian keyed unitaries from an average that need not be a Gaussian channel.

**Dependencies and story role:** M02–M04, M07, and M21–M23. Identifies the smaller optical control that changes the exponent for arbitrary references.

**Conceptual connection:** Canceling the vacuum–one-photon contribution removes the square-root loss scale. The proof must control reference-valued coherences; merely centering the oscillator's scalar first moment is insufficient.

**Source pointers:** Weedbrook §§II.B.4 and V.B; [Gaussian encryption, “G3. A single phase bit suffices for the improved exponent”](../science/gaussian_encryption.md#g3-a-single-phase-bit-suffices-for-the-improved-exponent) and [“Proof with an arbitrary reference”](../science/gaussian_encryption.md#proof-with-an-arbitrary-reference); [Interpretation, “4. Why centering the reduced state is insufficient”](../science/interpretation.md#4-why-centering-the-reduced-state-is-insufficient).

### M25. The first Fourier moment classifies the exponent

**Central question:** Which independent phase distributions reproduce the parity scheme's improved rate?

**Understanding target:** Relate each Fock coherence to the corresponding phase Fourier moment. Explain why $`m_1=0`$ is sufficient for the $`V^{-1}`$ upper bound, why a vacuum–one-photon witness makes it necessary, and why a diagonal witness rules out a faster exponent within this family.

**Dependencies and story role:** M07, M10, and M21–M24. Turns one successful construction into the necessary-and-sufficient P1 classification.

**Conceptual connection:** Coherent and population witnesses constrain different possible improvements. The classification fixes both positive $`E`$ and the phase law as $`V`$ grows, and applies to optimized and thermal replacement targets.

**Source pointers:** Weedbrook §§II.B.4, II.E.2, and III.A.1 for foundations; [Phase criterion, “P1. The first-harmonic criterion”](../science/phase_criterion.md#p1-the-first-harmonic-criterion), including its three proof subsections.

### M26. One additional phase bit is minimal

**Central question:** What amount of discrete phase randomness is necessary to cancel the first moment exactly?

**Understanding target:** Interpret $`m_1=0`$ as a weighted cancellation of unit-circle vectors. Explain why no atom can have probability above one half and why equality in the entropy bound requires two equiprobable antipodal phases.

**Dependencies and story role:** M07, M12, M24–M25. Converts the cancellation criterion into the restricted phase-key optimality statement P2.

**Conceptual connection:** The minimum is one bit of additional discrete phase entropy within independent phase preprocessing. It neither counts the continuous displacement key nor replaces K1's alphabet bound for general finite-key ciphers.

**Source pointers:** Weedbrook §§I.D and II.B.4 for probability/phase conventions; [Phase criterion, “P2. One bit is the minimum discrete phase entropy”](../science/phase_criterion.md#p2-one-bit-is-the-minimum-discrete-phase-entropy); [Model, “4. The charged resources”](../science/model.md#4-the-charged-resources).

### M27. Imperfect phase cancellation sets a control-accuracy scale

**Central question:** How do probability bias and phase-angle error reintroduce the slower signal?

**Understanding target:** Interpret the additional P3 term $`|m_1|\sqrt{E/(V+1)}`$ and the binary-law formula for $`|m_1|`$. Relate shrinking imbalance to the error target, distinguishing a deliberately improved phase law from a fixed nonzero imbalance that eventually restores the slower exponent.

**Dependencies and story role:** M07 and M24–M26. Connects the ideal criterion to quantified deviations in its specified controls.

**Conceptual connection:** Both angle and probability errors matter through the same first harmonic. This sensitivity statement is narrower than a full optical-device or transmission-noise model.

**Source pointers:** Weedbrook §II.B.4 for the rotation foundation; [Phase criterion, “P3. Residual phase imbalance and control accuracy”](../science/phase_criterion.md#p3-residual-phase-imbalance-and-control-accuracy) and [“A noisy binary phase implementation”](../science/phase_criterion.md#a-noisy-binary-phase-implementation).

### M28. Fixed-energy exponents do not imply uniform low-energy bounds

**Central question:** Why does parity's inverse-linear noise exponent still leave a small-energy limitation?

**Understanding target:** Use the surviving vacuum–two-photon coherence to understand the $`\sqrt E/(V+1)`$ lower witness. Distinguish fixed-$`E`$ asymptotics from a bound uniform as $`E\downarrow0`$, and compare parity with full phase averaging and the finite-block construction.

**Dependencies and story role:** M02–M03, M10, M18, and M23–M25. Delimits the optical improvement before the final cross-model comparison.

**Conceptual connection:** Canceling one angular harmonic does not cancel all of them. The remaining coherence changes the dependence on the input-energy budget without changing the fixed-energy exponent in $`V`$.

**Source pointers:** Weedbrook §§II.B.4 and II.E.2 for foundations; [Gaussian encryption, “The low-energy limitation of a binary phase”](../science/gaussian_encryption.md#the-low-energy-limitation-of-a-binary-phase); [Interpretation, “5. Finite parameters, low energy, and phase precision”](../science/interpretation.md#5-finite-parameters-low-energy-and-phase-precision).

### M29. A finite-support witness checks the claimed displacement rate

**Central question:** How can an exactly supported two-level input separate a valid asymptotic claim from an incorrect quantitative bound?

**Understanding target:** Follow the homodyne witness for $`(|0\rangle\pm|1\rangle)/\sqrt2`$, including convolution, half-distance normalization, and the conversion $`V=2\sigma^2`$. Explain the conflict with the printed finite-cutoff rate, the separate supporting-inequality check, and the limited role of numerical verification.

**Dependencies and story role:** M02, M06–M10, and M21–M22. Integrates the measurement, channel, and convention tools into a precise comparison with earlier work.

**Conceptual connection:** A finite-support counterexample can test a universal cutoff claim without truncating the channel output. The discrepancy concerns specified statements; displacement-only asymptotic secrecy remains established by G1.

**Source pointers:** Weedbrook §§I.D, II.E.1, III.A.1, and V.B; [Displacement comparison, “3. Exact homodyne witness at photon cutoff one”](../science/displacement_comparison.md#3-exact-homodyne-witness-at-photon-cutoff-one), [“4. Comparison with the published finite-cutoff statement”](../science/displacement_comparison.md#4-comparison-with-the-published-finite-cutoff-statement), and [“5. A direct check of the supporting matrix-element inequality”](../science/displacement_comparison.md#5-a-direct-check-of-the-supporting-matrix-element-inequality); [Verification, “Independently integrated homodyne witness”](../verification/README.md#independently-integrated-homodyne-witness).

### M30. Narrative synthesis: resource laws, optical mechanism, and scope

**Central question:** What single scientific account connects unavoidable ciphertext energy, finite keys, and the benefit of one optical phase bit?

**Understanding target:** Join E2–C1–K1's matching resource orders with G1–G3 and P1–P3's coherence mechanism. Compare the ideal finite-key construction with the simple Gaussian keyed controls without combining their advantages through an unproved discretization. Carry the fixed spectrum, arbitrary-reference secrecy, correctness assumptions, single-use model, and low-energy qualifications into every interpretation.

**Dependencies and story role:** M12–M29. Synthesizes the entire narrative, including the robust extension, source comparison, and the distinction between analytic proof and finite verification.

**Conceptual connection:** Reversibility and the number of low-energy states impose a universal cost; the chosen random controls determine whether an optical implementation attains the favorable error exponent. Ciphertext excitation, total device work, and key-generation costs remain different quantities.

**Source pointers:** Weedbrook §§III.A and V.A–V.B as the unifying foundations; [Interpretation, “6. The physical accounting and its boundaries”](../science/interpretation.md#6-the-physical-accounting-and-its-boundaries); [Finite key, “4. The joint resource statement”](../science/finite_key.md#4-the-joint-resource-statement); [Model, “6. Boundaries that travel with the claims”](../science/model.md#6-boundaries-that-travel-with-the-claims); [Weedbrook bridge](WEEDBROOK_BRIDGE.md).
