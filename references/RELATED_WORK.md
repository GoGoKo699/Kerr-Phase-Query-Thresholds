# Related work and proof ingredients

This source map distinguishes the established methods used in the proofs from their evaluation for the Kerr gate in [the model](../science/model.md). The exact query threshold is for a fixed number of identical forward calls, with every repetition included in that number. The extension to a fixed finite catalog of positive commensurate durations is a converse. Fractional Hamiltonian evolution, inverse access, and a growing catalog require the separate resource accounting in [access variants](../science/access_variants.md).

The general coset-identification theorem, covariant phase optimization, cyclic character-counting bound, three-square theorem, triangular-number theorem, and binary-form counting asymptotics are attributed below. The project does not claim those ingredients as new. Its mathematical claims concern their arithmetic specialization, continuous-parameter confidence consequences, and the stated timing, prior, and preparation results. A bounded literature comparison cannot establish absence of all prior work.

The finite abelian machinery includes composite groups. The additional arithmetic in [the confidence proof](../science/global_confidence.md) uses exclusions modulo prime squares, followed by products of fixed coprime moduli. Finite-field polynomial examples do not evaluate these residue sets. Likewise, granting a power as one free query changes the model: implementing a positive integer power by repeated primitive calls consumes that many calls.

Each heading is also a stable citation anchor and a key in [references.bib](references.bib). PDF page numbers below count the first PDF page as page 1, unless a printed journal page is specified. Numbered pointers refer to the explicitly identified version. Full linked preprints or official texts were inspected for the mathematical statements used here; exceptions and limits are identified individually. A verified publisher record does not imply that its final typeset text was available.

## Quantum queries, covariance and confidence

### copeland2021

**Daniel Copeland and Jamie Pommersheim, “Quantum query complexity of symmetric oracle problems.”** Quantum **5**, 403 (2021). [Publisher and DOI](https://quantum-journal.org/papers/q-2021-03-07-403/); [arXiv:1812.09428v3](https://arxiv.org/pdf/1812.09428v3).

**Pointers:** Theorem 2.1; Theorem 5.1 and Corollary 5.8; Theorem 7.1; Section 7.1. Adaptive finite-group coset identification parallelizes, and the abelian optimum is a character-class count. For a finite phase grid and a nuisance subgroup this supplies the generic maximum-over-nuisance-sector residue-count formula used here. It does not by itself evaluate the Kerr arithmetic. Section 7.1 uses polynomial value oracles over finite fields; a field of prime-power size is not the composite ring of integers modulo that prime power. An unrestricted parallelization result must also be applied carefully when cumulative photon exposure is constrained.

### zhandry2015

**Mark Zhandry, “Quantum Oracle Classification—The Case of Group Structure.”** arXiv:1510.08352v1 (2015). [Full preprint](https://arxiv.org/pdf/1510.08352v1).

**Pointers:** Theorem 4.1; Sections 5.3–5.5. This is the abelian classification result credited by Copeland and Pommersheim, including earlier constant-query threshold phenomena. Polynomial examples use a value oracle whose response register supplies freely selectable Fourier weights. This differs from fixed positive Kerr phase exposures. For example, access to values of f(n) = θ T(n) + β n determines β from f(1) and θ from f(2) − 2f(1) in two classical queries. That observation does not transfer to the opaque phase gate. No journal version is asserted here.

### childsetal2016

**Andrew M. Childs, Wim van Dam, Shih-Han Hung and Igor E. Shparlinski, “Optimal Quantum Algorithm for Polynomial Interpolation.”** ICALP 2016, LIPIcs **55**, 16:1–16:13. [Publisher](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2016.16); [arXiv:1509.09271v2](https://arxiv.org/pdf/1509.09271v2).

**Pointers:** Theorems 1–3. Optimal interpolation success is the fraction of a finite-field coefficient space reached by an explicit moment map; the work also gives sharp query thresholds and algorithms. The map includes freely chosen response-character weights. The finite-field image count and the present fixed-phase, composite-modulus obstruction are different arithmetic problems.

### chen2018

**Jianxin Chen, Andrew M. Childs and Shih-Han Hung, “Quantum algorithm for multivariate polynomial interpolation.”** Proceedings of the Royal Society A **474**, 20170480 (2018). [DOI](https://doi.org/10.1098/rspa.2017.0480); [arXiv:1701.03990v2](https://arxiv.org/pdf/1701.03990v2).

**Pointer:** Section 3.1, especially Eq. (19) in the linked preprint. The continuous real/complex oracle setting gives a success expression from the volume of the image of a moment map. Freely variable oracle inputs and response weights are additional access resources. A continuous polynomial-oracle result should therefore not be cited as a fixed Kerr-gate query classification.

### walter2014

**Michael Walter and Joseph M. Renes, “Lower Bounds for Quantum Parameter Estimation.”** IEEE Transactions on Information Theory **60**(12), 8007–8023 (2014). [DOI](https://doi.org/10.1109/TIT.2014.2365174); [arXiv:1310.2155v3](https://arxiv.org/pdf/1310.2155v3).

**Pointer:** Theorem 12, Eq. (29). Representation data bound confidence-region size and success probability. For a cyclic group with M equally likely hypotheses and r available characters, this gives the success bound r/M. That inequality is an established ingredient. The Kerr proof supplies the residue exclusions and the limiting argument for every shrinking confidence radius.

### meyer2025

**Johannes Jakob Meyer, Sumeet Khatri, Daniel Stilck França, Jens Eisert and Philippe Faist, “Quantum metrology in the finite-sample regime.”** PRX Quantum **6**, 030336 (2025). [DOI](https://doi.org/10.1103/qbn1-p6bq); [arXiv:2307.06370v1](https://arxiv.org/html/2307.06370v1).

**Pointer:** Theorem 10, Eqs. (43)–(44), in the 2023 arXiv version. The paper develops operational accuracy-success guarantees through multiple-hypothesis testing, including phase estimation and general estimation strategies. Confidence-based quantum metrology and shifted-hypothesis bounds are established here; the present application is the arithmetic obstruction in the specified gate model. The preprint's theorem numbering is not assumed identical to the final journal version.

### dariano1998

**G. M. D’Ariano, C. Macchiavello and M. F. Sacchi, “On the general problem of quantum phase estimation.”** Physics Letters A **248**, 103 (1998). [DOI](https://doi.org/10.1016/S0375-9601(98)00702-6); [arXiv:quant-ph/9812034v1](https://arxiv.org/html/quant-ph/9812034v1).

The general solution treats a possibly degenerate phase generator, the optimal covariant measurement, and optimization of the input through the Fourier coefficients of the cost. The first-harmonic cost leads to the familiar tridiagonal eigenvalue problem and sine amplitudes. The project uses this phase-estimation structure after identifying the available frequencies; it does not introduce the sine-state optimization.

### vandam2007

**W. van Dam, G. M. D’Ariano, A. Ekert, C. Macchiavello and M. Mosca, “Optimal quantum circuits for general phase estimation.”** Physical Review Letters **98**, 090501 (2007). [DOI](https://doi.org/10.1103/PhysRevLett.98.090501); [arXiv:quant-ph/0609160v1](https://arxiv.org/html/quant-ph/0609160v1).

The polynomial method treats arbitrary arrangements of a specified number of phase gates, intervening operations and final measurements. For translation-invariant costs it reduces optimization to a simple circuit form and its input amplitudes. This is a direct precedent for handling adaptive phase queries; changing the gate spectrum and accounting for a shared nuisance parameter require the additional analysis in this project.

### hayashi2025

**Masahito Hayashi, “Indefinite causal order strategy does not improve the estimation of group action.”** Quantum **9**, 1891 (2025). [Publisher](https://quantum-journal.org/papers/q-2025-10-22-1891/); [arXiv:2501.09312v2](https://arxiv.org/html/2501.09312v2).

The work establishes parallel optimality for estimation of compact-group actions in its covariant setting, even against indefinite causal order. It is a useful broader model comparator. It does not automatically preserve the cumulative photon constraint imposed on a physical implementation here.

## Classical arithmetic used in the proofs

### sun2007

**Zhi-Wei Sun, “Mixed sums of squares and triangular numbers.”** Acta Arithmetica **127**(2), 103–113 (2007). [Publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/127/2/83897/mixed-sums-of-squares-and-triangular-numbers); [publisher full PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83897); [DOI](https://doi.org/10.4064/aa127-2-1).

**Pointer:** Printed p. 103, the unnumbered Gauss–Legendre Theorem. A nonnegative integer is a sum of three integer squares exactly when it is not of the form 4ᵃ(8b + 7). The same page explains the equivalence between three triangular numbers summing to n and three odd squares summing to 8n + 3. These are classical results, restated here in an accessible primary research source; Sun is not credited as their original discoverer. Its convention x(x + 1)/2 gives the same nonnegative triangular values as T(n) = n(n − 1)/2.

### mortenson2017

**Eric T. Mortenson, “A Kronecker-type identity and the representations of a number as a sum of three squares.”** Bulletin of the London Mathematical Society **49**(5), 770–783 (2017). [DOI](https://doi.org/10.1112/blms.12068); [arXiv:1702.01627v2](https://arxiv.org/pdf/1702.01627v2).

**Pointers:** Theorem 1.3 and the following paragraph, PDF p. 3; Theorem 1.6, Eq. (1.12), p. 4; its proof in Section 4, p. 7. The paper gives classical three-square formulas and a generating identity implying Gauss’s three-triangular-number theorem. The paragraph after Theorem 1.3 explicitly states the three-square exclusion criterion. This supplies a verified proof source for the classical completeness ingredients. It also identifies Gauss’s Disquisitiones Arithmeticae, Articles 291–292, for the primitive three-square count.

### moree2006

**Pieter Moree and Robert Osburn, “Two-dimensional lattices with few distances.”** L’Enseignement Mathématique **52**, 361–380 (2006). [arXiv:math/0604163v2](https://arxiv.org/pdf/math/0604163v2); [MPIM preprint 2006-46](https://archive.mpim-bonn.mpg.de/id/eprint/915/2/preprint_2006_46.pdf).

**Version-specific pointers:** arXiv v2 Eq. (2.3), PDF p. 5; MPIM preprint Eq. (6), PDF p. 4. Both state Bernays’s asymptotic count of integers represented by a fixed primitive positive definite integral binary quadratic form: a positive constant times X/√log X, with a smaller error. The project only needs its upper-bound consequence for the Eisenstein norm form x² − xy + y². The count is of represented integers, not the number of representations. No uniformity in a growing discriminant is inferred.

### brink2011

**David Brink, Pieter Moree and Robert Osburn, “Principal forms X² + nY² representing many integers.”** Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **81**, 129–139 (2011). [DOI](https://doi.org/10.1007/s12188-011-0059-y); [arXiv:1003.1094v2](https://arxiv.org/pdf/1003.1094v2).

**Pointer:** Eq. (2), PDF p. 1, and Section 2. This is another primary research restatement of Bernays’s asymptotic, with discussion of its constant. It identifies the relevant locations in the original thesis as pp. 59 and 115–116. The quantitative argument in this repository can rely on the verified Moree–Osburn statement without requiring retrieval of the original thesis.

### bernays1912

**Paul Bernays, “Über die Darstellung von positiven, ganzen Zahlen durch die primitiven, binären quadratischen Formen einer nicht-quadratischen Diskriminante.”** Doctoral dissertation, Göttingen (1912).

**Historical attribution and access limit:** The identity and theorem attribution are verified through [Moree–Osburn](#moree2006) and [Brink–Moree–Osburn](#brink2011). Their cited digital-library entry point is [the Bielefeld DML](https://www.math.uni-bielefeld.de/~rehmann/DML/). The original thesis full text was not retrieved, so no claim here rests on an independent reading of its pp. 59 or 115–116. The modern primary restatements above provide the checked mathematical input.

### dlmf27

**T. M. Apostol, “Functions of Number Theory,” Chapter 27 of the NIST Digital Library of Mathematical Functions.** Version **1.2.8**, released 2026-09-15. [Chapter](https://dlmf.nist.gov/27).

**Pointers:** [Eq. (27.11.9)](https://dlmf.nist.gov/27.11.E9) gives the asymptotic reciprocal-prime sum in any fixed coprime residue class, with leading term log log X divided by Euler’s totient of the modulus. [Section 27.15](https://dlmf.nist.gov/27.15) states the Chinese remainder theorem for pairwise coprime moduli. These official statements support the divergent inert-prime sum and multiplication of residue fractions. Chapter 27.13 is not used as a source for the three-square criterion.

## Nonlinear estimation, copy thresholds and the Ising comparison

### hall2012

**Michael J. W. Hall and Howard M. Wiseman, “Does nonlinear metrology offer improved resolution? Answers from quantum information theory.”** Physical Review X **2**, 041006 (2012). [DOI](https://doi.org/10.1103/PhysRevX.2.041006); [arXiv:1205.2405v3](https://arxiv.org/pdf/1205.2405v3).

The paper distinguishes local sensitivity from globally averaged resolution using information-theoretic bounds. Section V constructs multiscale nonlinear estimation protocols. Their number of copies or resolution stages grows with the resources; it is not the fixed total-query model here. The local/global distinction and the need to resolve ambiguity are established precedents.

### bagan2008

**Emilio Bagan, Alex Monras and Ramon Muñoz-Tapia, “Phase variance of squeezed vacuum states.”** Physical Review A **78**, 043829 (2008). [DOI](https://doi.org/10.1103/PhysRevA.78.043829); [arXiv:0807.4108v2](https://arxiv.org/pdf/0807.4108v2).

For a specified squeezed-vacuum family, Bayesian phase variance has copy-number-dependent asymptotics: the quadratic photon-number rate requires more than four copies, with a logarithmic borderline at four. This is an important earlier fixed-copy rate threshold. A single copy is already consistent, so the result is different from an all-input impossibility of success at every shrinking confidence radius.

### chiribella2014

**Giulio Chiribella, Rui Chao and Yuxiang Yang, “Superactivation of quantum gyroscopes.”** arXiv:1411.3439v1 (2014). [Full preprint](https://arxiv.org/pdf/1411.3439v1).

The work demonstrates fixed-copy activation in reference-frame alignment using a prescribed entangled-spin resource family, and probabilistic improvements with nonzero acceptance. It is a substantive precedent for the activation theme. Its probe and operational restrictions differ from the all-input Kerr converse. No journal publication is asserted here, and neither activation nor the possibility of heralded metrology is claimed as new in this repository.

### cheng2014

**Jing Cheng, “Quantum metrology for simultaneously estimating the linear and nonlinear phase shifts.”** Physical Review A **90**, 063838 (2014). [Publisher abstract and DOI](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.90.063838).

**Access limit:** Only the official abstract was available; the publisher’s full text required authorization. The abstract studies simultaneous linear and Kerr phases, reports a limitation of NOON states, and compares entangled coherent and cat-state precision bounds. This establishes a direct two-parameter nonlinear-metrology precedent. No inference about the paper’s complete global-prior analysis, proofs or theorem scope is made from the abstract.

### luis2016

**Alfredo Luis, Irene Morales and Ángel Rivas, “Nonlinear fiber gyroscope for quantum metrology.”** Physical Review A **94**, 013830 (2016). [DOI](https://doi.org/10.1103/PhysRevA.94.013830); [arXiv:1607.00755v1](https://arxiv.org/pdf/1607.00755v1).

**Pointer:** Appendix B. The paper analyzes a nonlinear optical gyroscope and includes local multiparameter Fisher-information analysis of linear and nonlinear contributions. It is a nearby physical and nuisance-parameter comparison. Local multiparameter precision does not establish global learnability with a fixed total number of gate calls.

### riberi2025

**Francisco Riberi and Lorenza Viola, “Optimal asymptotic precision bounds for nonlinear quantum metrology under collective dephasing.”** APL Quantum **2**, 026111 (2025). [DOI](https://doi.org/10.1063/5.0255629); [arXiv:2501.00189v1](https://arxiv.org/pdf/2501.00189v1).

**Pointers:** Eq. (1), Section II.B and Sections III–IV. Quadratic signal encoding coexists with collective linear dephasing. The stated estimation regime uses many shots and a local operating point, with temporal noise correlations and interrogation-time optimization. It is not estimation under one common static, unknown linear phase with a fixed total query budget. The full author preprint is available even when the publisher endpoint fails to load.

### belliardo2026

**Federico Belliardo, James W. Gardner, Liang Jiang and Aashish A. Clerk, “Global Precision Bounds and Success-Probability Guarantees in Quantum Parameter Learning.”** arXiv:2608.15528v2 (2026). [Full HTML](https://arxiv.org/html/2608.15528v2); [PDF](https://arxiv.org/pdf/2608.15528v2).

**Pointers:** Section IV.1 and Appendix H, Eqs. (185)–(190). The fixed-time all-to-all Ising example uses the prescribed plus-state input and a square spectrum. This is the direct model comparison for [the Ising application](../science/ising_application.md). The repository’s corollary permits arbitrary inputs and ancillas for one uninterrupted fixed-duration call and any fixed absolutely continuous prior. It does not cover controls during the interaction, multiple calls, varying durations, particle-number superpositions or a size-dependent Hamiltonian normalization. A lower guarantee on performance is not identified with the unknown optimum.

## Timing and preparation resources

### shin2026

**Myeongjin Shin, Junseo Lee and Changhun Oh, “Heisenberg-Limited Hamiltonian Learning Without Short-Time Control.”** PRX Quantum **7**, 043011 (2026), published 2026-10-16. [Publisher](https://journals.aps.org/prxquantum/abstract/10.1103/kjvf-jgqj); [arXiv:2604.27838v1](https://arxiv.org/pdf/2604.27838v1).

**Pointers:** Problem 1 and Theorems 1–2; Section VII, PDF p. 16, in the arXiv version. The model permits all real evolution times above a minimum, with query count growing with the target accuracy and a bounded Hamiltonian norm. Section VII explicitly distinguishes a minimum duration from a discrete time resolution. The fixed finite positive-clock catalog in this repository is a narrower access restriction; the result does not settle that paper’s general clock-resolution question. Publisher metadata was verified; the stated pointers refer to the preprint, not an independently inspected final PDF.

### yoder2014

**Theodore J. Yoder, Guang Hao Low and Isaac L. Chuang, “Fixed-point quantum search with an optimal number of queries.”** Physical Review Letters **113**, 210501 (2014). [DOI](https://doi.org/10.1103/PhysRevLett.113.210501); [arXiv:1409.3305v2](https://arxiv.org/pdf/1409.3305v2).

**Pointers:** Eqs. (1)–(3), PDF pp. 1–2. Given a lower bound on marked weight, fixed-point amplitude amplification guarantees a chosen failure probability with the quadratic search scaling. The project applies this established subroutine to a reversible three-square predicate. The preparation queries are to that known arithmetic predicate, not extra calls to the unknown Kerr gate. The resulting arithmetic gate cost is polynomial in the photon cap N, not in log N.

### huang2026sideband

**Jordan Huang, Thomas J. DiNapoli, Gavin Rockwood, Ming Yuan, Prathyankara Narasimhan, Eesh Gupta, Mustafa Bal, Francesco Crisa, Sabrina Garattoni, Yao Lu, Liang Jiang and Srivatsan Chakram, “Fast Sideband Control of a Multimode Cavity Memory with Weak Dispersive Coupling to a Transmon.”** Physical Review X **16**, 011058 (2026). [Publisher](https://journals.aps.org/prx/abstract/10.1103/t4cv-y398).

**Inspected full version:** [arXiv:2503.10623v1](https://arxiv.org/html/2503.10623v1), titled “Fast Sideband Control of a Weakly Coupled Multimode Bosonic Memory.” The work supplies mode-selectable Jaynes–Cummings swaps, photon-number-dependent rates, dark-state shelving and selected multimode encodings. These are relevant physical ingredients. It does not demonstrate the complete arithmetic-register-controlled four-mode loading interface in this project. Published metadata and the full preprint were checked; the APS PDF was not retrieved.

### huang2026jc

**Jordan Huang, Ethan Kasaba, Thomas J. DiNapoli, Tanay Roy and Srivatsan Chakram, “Universal Jaynes–Cummings Control of an Oscillator.”** arXiv:2605.18658v1 (2026), submitted 2026-05-18. [Full HTML](https://arxiv.org/html/2605.18658v1).

The work establishes single-mode oscillator control and treats driven phase corrections. It supports the availability of a useful control family, while leaving the complete coherent multimode arithmetic interface as an additional assumption. No journal publication is asserted here; quoted process fidelities would require retaining the paper’s postselection and phase-correction qualifications.

### krastanov2015

**Stefan Krastanov, Victor V. Albert, Chao Shen, Chang-Ling Zou, Reinier W. Heeres, Brian Vlastakis, Robert J. Schoelkopf and Liang Jiang, “Universal Control of an Oscillator with Dispersive Coupling to a Qubit.”** Physical Review A **92**, 040303(R) (2015). [DOI](https://doi.org/10.1103/PhysRevA.92.040303); [arXiv:1502.08015v2](https://arxiv.org/pdf/1502.08015v2).

Conditional number-selective operations together with displacements give universal oscillator control and explicit state-preparation constructions. This is a theoretical control ingredient. Universality alone supplies neither the asymptotic runtime nor the experimentally achieved fidelity of the project’s coherent multimode interface.

### heeres2015

**Reinier W. Heeres, Brian Vlastakis, Eric Holland, Stefan Krastanov, Victor V. Albert, Luigi Frunzio, Liang Jiang and Robert J. Schoelkopf, “Cavity State Manipulation Using Photon-Number Selective Phase Gates.”** Physical Review Letters **115**, 137002 (2015). [DOI](https://doi.org/10.1103/PhysRevLett.115.137002); [arXiv:1503.01496v1](https://arxiv.org/pdf/1503.01496v1).

**Pointers:** Figure 2 and PDF pp. 2–3 for parameter calibration; Figure 3 for Kerr correction. The experiment introduces selective number-dependent arbitrary phase gates, corrects Kerr phase evolution and combines these controls with oscillator displacements. It is a relevant calibration and control precedent. Its repeated calibration measurements and variable waiting times must be counted when comparing them with a fixed-query learning task.

