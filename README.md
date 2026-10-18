# Kerr Phase Query Thresholds

**How many forward uses of a Kerr gate are needed for an increasingly accurate global phase estimate?** For an ideal fixed-duration gate, the exact threshold is **three uses when the linear phase is known** and **four uses when it is common and unknown**.

The gate on a photon-number mode is

```math
U_{\theta,\beta}
=\exp\!\left[-i\theta\frac{\hat n(\hat n-1)}2-i\beta\hat n\right].
```

The target is the nonlinear phase $`\theta`$. The same nuisance phase $`\beta`$ acts in every call. A query is one complete forward gate use, and the count includes all calls used to produce an estimate, including repetitions and preliminary sensing.

| Linear phase | Below the threshold | At the threshold |
|---|---|---|
| Known | With at most two uses, the success probability in every shrinking error window tends to zero. | Three uses attain $`O(N^{-4})`$ sine risk and $`O(N^{-2})`$ wrapped RMS error. |
| Common and unknown | With at most three uses, the success probability in every shrinking error window tends to zero. | Four uses attain the same risk and RMS scaling. |

The impossibility results hold for **every fixed absolutely continuous prior**, arbitrary probes, ancillas, interleaved controls, feedback and final POVMs. The upper bounds are pointwise in the phases and use at most $`N`$ photons in total, including any bypass reference. Matching optimal risk exponents are proved for uniform priors. The adaptive converses permit the larger resource class with occupation at most $`N`$ at each queried mode.

Quadratically large frequencies alone do not give a globally useful estimate. The proof identifies missing arithmetic frequency classes below threshold and constructs a consecutive band of quadratic length at threshold. The general phase-estimation and finite-group discrimination machinery is [established prior work](references/RELATED_WORK.md); the gate-specific arithmetic classification and its stated consequences are developed here.

## Read the science

Start with [the physical model, resource conditions and exact claims](science/model.md). Continue to [query thresholds](science/query_thresholds.md) and [global confidence](science/global_confidence.md). [Interpretation](science/interpretation.md) connects the proof mechanism to the calibration task.

| To inspect | Read |
|---|---|
| Exact one-, two- and three-use risk floors; attained threshold; exposed-photon parity | [Query thresholds](science/query_thresholds.md) |
| Cyclic discrimination, prime residue omissions and all shrinking error windows | [Global confidence](science/global_confidence.md) |
| Fixed positive clock catalogs and improving linear-phase priors | [Timing and priors](science/timing_and_priors.md) |
| QRAM-free arithmetic preparation and its separate Fock-loading interface | [Coherent preparation](science/coherent_preparation.md) |
| Explicit four-photon state, selected pair controls and finite Fourier readout | [Four-photon protocol](science/four_photon_protocol.md) |
| Independent cubic phases and the bounds that survive them | [Robustness](science/robustness.md) |
| One shortened call and a forward/inverse pair | [Access variants](science/access_variants.md) |
| All-input obstruction for one fixed-time all-to-all Ising interrogation | [Ising application](science/ising_application.md) |
| Physical meaning and scope | [Interpretation](science/interpretation.md) |
| Imported ingredients and nearby models | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

[The LLM reading guide](llms.txt) maps questions to these authoritative files.

## Learn the project

The shared learning route uses **John Watrous, _The Theory of Quantum Information_ (2018)** as its single educational anchor. Start with [the source bridge](learning/WATROUS_BRIDGE.md), which maps selected sections of the author manuscript to the project's notation, phase-estimation model and worked four-photon example. Follow the [30-milestone map](learning/MILESTONES.md) for the complete sequence.

The map has **14 background milestones and 16 narrative and innovation milestones**. The first phase builds from states and measurements to the complete operational model, including the Fourier and arithmetic prerequisites. The second builds from the individual risk floors and constructive bands to the full threshold, confidence, resource and access story. Each phase moves from local ingredients to a global synthesis. The allocation reflects the project's two connected foundations: quantum estimation and arithmetic structure.

Every milestone states a central question, an understanding target, earlier prerequisites, its role in the story, a conceptual connection and canonical reading pointers. The [primary research references](references/RELATED_WORK.md) remain the sources for the imported phase-estimation, number-theory and control results. The book supplies the common educational foundation; the scientific files supply the project's full arguments.

## A finite separation

Four photons already give a strict separation from every three-use strategy under uniform phases. The code words

```math
|1111\rangle,\quad |2110\rangle,\quad |0220\rangle,\quad |3100\rangle
```

have the same total occupation and consecutive nonlinear frequencies. A sine-weighted superposition and an eight-outcome Fourier readout achieve

```math
R_4=\frac{3-\sqrt5}{2}\simeq0.381966,
\qquad
R_{q\le3}\ge2-\sqrt2\simeq0.585786,
```

for loss $`4\sin^2((\hat\theta-\theta)/2)`$. The [finite protocol](science/four_photon_protocol.md) specifies its number-preserving selected pair gates and echoed logical rotation. These are nonlinear control assumptions, not ordinary beamsplitter operations.

## Timing, calibration and control costs

Adding a fixed finite set of positive commensurate durations does not remove the subthreshold confidence obstruction. Allowing a duration that shrinks with $`N`$, or supplying inverse-gate access, does change it. These statements keep query count, total exposure and clock precision separate.

For three identical calls, a fixed absolutely continuous target-phase prior, and an independent linear phase uniform on a known-center interval of width $`w_N`$, consistency is possible exactly when $`w_N\to0`$. The proved quantitative sufficient and necessary bounds leave a rate gap. The sharp claim is the qualitative criterion for this prior family; no optimal interpolation is asserted.

The four-use construction needs $`O(N\mathrm{polylog}N)`$ digital operations without QRAM, together with the stated coherent number-to-Fock interface. Preparation, readout and calibrated controls are additional resources. The [robustness bounds](science/robustness.md) distinguish persistence of the converse from tolerance of the four-use construction.

## Reproduce the finite checks

With the [documented dependencies](verification/README.md), run from the repository root:

```bash
python3 verification/run_all.py
```

The suite compares exact arithmetic and numerical results with committed expected outputs. It checks finite spectra, representative occupations, residue omissions, Fourier probabilities and the full 35-state four-photon control sector. General adaptive converses and asymptotic statements are established by the written proofs and imported theorems, not by finite enumeration.

## Consequential scope

The main threshold counts identical fixed-duration forward uses of an ideal gate. The nuisance is common across calls. Fixed priors, concentrating priors, and singular prior promises are distinct. The construction gives any prescribed fixed confidence at an appropriate constant multiple of $`N^{-2}`$; confidence tending to one is proved for shrinking windows wider by a diverging factor. A fixed uncorrected cubic phase, loss during the unknown evolution, and a target-dependent higher nonlinearity are not silently included in the upper bound.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
