# Why the number of uses changes global calibration

The query threshold comes from the frequencies that an experiment can combine coherently. Quadratic growth supplies large frequencies, while global calibration also requires enough frequencies with the right spacings. A common unknown linear phase restricts which of those combinations survive nuisance averaging. Three and four uses fall on opposite sides of a specific arithmetic obstruction.

## Local sensitivity and a complete estimate

With a known linear phase, the state proportional to $`|0\rangle+|N\rangle`$ acquires relative phase $`\theta T(N)`$. Its interference varies on a scale proportional to $`N^{-2}`$. There are also many fringes over a full phase period. A local sensitivity calculation presumes sufficient information to resolve the relevant fringe; a complete global estimator must obtain that information within its counted resources.

This local/global distinction in nonlinear quantum metrology is established background, including [Hall and Wiseman](../references/RELATED_WORK.md#hall2012). The present result gives a fixed-query classification for the particular integer Kerr spectrum. It permits optimized probes and measurements, rather than drawing a converse from the behavior of one chosen state.

A constant risk lower bound alone would still allow occasional precise answers. The stronger [confidence theorem](global_confidence.md) bounds discrimination among many evenly spaced phase hypotheses. Missing residues modulo prime squares, combined through the Chinese remainder theorem, make the accessible fraction of these hypotheses arbitrarily small, regardless of the photon cap. This is why below threshold even the probability of an increasingly accurate answer must vanish.

The obstruction does not require exact aliasing between two phases. For example, accessible frequency differences can include one, so a suitable state has no smaller exact phase period. Exact identifiability of distinct parameters and a uniformly useful single-estimate confidence guarantee are different properties.

## The common nuisance and the arithmetic geometry

For $`q`$ parallel sensing occupations, the phase labels are

```math
s=\sum_{j=1}^{q}n_j,\qquad
g=\frac12\left(\sum_{j=1}^{q}n_j^2-s\right).
```

When the linear phase is known, all totals can interfere. Three triangular numbers fill every nonnegative integer, and a photon-bounded part of that representation gives a consecutive band of quadratic length.

When the common linear phase is uniformly unknown, its average removes cross terms with different $`s`$. Within each surviving sector, three occupations yield values of the binary form $`u^2-uv+v^2`$. At primes inert for this form, divisibility by $`p`$ forces divisibility by $`p^2`$. These recurring omissions give the strong converse.

Four occupations leave a ternary form. On a suitable odd-$`s`$ sector, the required integer is congruent to three modulo eight, and the three-square theorem fills a quadratic-length interval. Thus a state with fixed total occupation cancels the common nuisance while retaining enough consecutive nonlinear frequencies. The change from three to four is a property of this form and its allowed sectors; it is not a general rule assigning one extra query to every nuisance parameter.

The exact-photon parity refinement in [query thresholds](query_thresholds.md) also matters conceptually. Four-use achievability under a cap chooses a suitable odd exposed total. Requiring exactly $`N`$ photons to be exposed for every parity is a stronger resource promise with a different uniform query threshold.

## A resource comparison

| Access and prior | Established conclusion | Resource condition that matters |
|---|---|---|
| Identical forward uses; known linear phase | Two or fewer uses have vanishing shrinking-window confidence; three achieve $`O(N^{-4})`$ sine risk. | The supplied linear calibration is not acquired through uncounted queries. |
| Identical forward uses; unknown common linear phase | Three or fewer uses have vanishing shrinking-window confidence; four achieve $`O(N^{-4})`$ pointwise sine risk. | The nuisance is common, and an odd exposed total may be chosen below the cap. |
| Fixed finite positive commensurate duration catalog | The same subthreshold confidence obstruction persists. | The catalog and clock unit are independent of $`N`$. |
| Three identical uses; fixed absolutely continuous target prior and independent uniform linear-phase interval of known center and width $`w_N`$ | Consistency is possible exactly when $`w_N\to0`$. | The concentrating nuisance prior supplies improving external information. |
| One selected duration proportional to $`N^{-1}`$ | The displayed construction achieves $`O(N^{-1})`$ risk and consistency. | Both Hamiltonian coefficients scale with the duration, and real coefficient representatives are supplied. |
| One forward and one inverse use | The displayed construction achieves $`\Theta(N^{-2})`$ risk. | The inverse changes the sign of both unknown terms. |

The sufficient and necessary quantitative bounds on $`w_N`$ do not coincide. The qualitative criterion is sharp; the complete interpolation of optimal confidence and RMS rates is not established. A fixed high confidence at a constant multiple of $`N^{-2}`$ is also distinct from confidence tending to one. The precise quantifiers are retained in [the model](model.md) and [timing and priors](timing_and_priors.md).

## Why sharing the linear phase is essential

The four-mode fixed-total construction turns $`\beta\sum_jn_j`$ into a global phase. If each call instead has an independent uniformly distributed linear phase, the single-call averaged channel is

```math
\int_0^{2\pi}\frac{d\beta}{2\pi}
U_{\theta,\beta}\rho U_{\theta,\beta}^{\dagger}
=\sum_n |n\rangle\langle n|\rho|n\rangle\langle n|,
```

with identity operators on any ancillas understood. This channel is independent of $`\theta`$. Composing it with parameter-independent controls supplies no target information. This fully independent Haar-nuisance model is different from the shared unknown phase used in the threshold theorem; intermediate correlation models require their own analysis.

Heralding does not turn the subthreshold model into a constant-yield accurate sensor. If the conditional success probability of a heralded output remains bounded away from zero in a shrinking window, the acceptance probability must vanish. Retrying those sensing attempts increases the total query count. In contrast, the bounded retries used to prepare sine amplitudes occur before any target call and have a separately counted control cost.

## What the explicit upper bound requires

[Coherent preparation](coherent_preparation.md) replaces a large stored representative table with reversible arithmetic and fixed-point quantum search. The resulting digital cost is $`O(N\mathrm{polylog}N)`$, with logarithmic-size integer registers. The construction retains its work register and reverses only known controls after sensing. It does not require the inverse unknown gate.

That digital construction has a separate interface to photonic Fock occupations. The specified loader makes its conditional-control assumptions and photon creation during preparation explicit. The four-photon example avoids the asymptotic search and gives concrete number-preserving selected pair gates, an echoed logical rotation, and finite Fourier readout. These are ideal control constructions. They do not supply measured fidelities or establish the performance of a complete laboratory implementation.

The [robustness analysis](robustness.md) reflects the same distinction. Independent parameter-free processing and fixed or independently sampled higher phases preserve the lower bounds through a simulation argument. The four-use upper bound needs adequate control of the relative phase errors; it is not automatically robust to a fixed uncorrected cubic coefficient as $`N`$ grows. A higher term proportional to the target parameter changes the spectral generator and must be analyzed anew.

## Relationship to general theory

The consecutive-band optimum is standard covariant phase-estimation machinery. The cyclic confidence argument specializes established finite-group and region-estimation methods, including [Copeland and Pommersheim](../references/RELATED_WORK.md#copeland2021), [Zhandry](../references/RELATED_WORK.md#zhandry2015), and [Walter and Renes](../references/RELATED_WORK.md#walter2014). Fixed-point search uses [Yoder, Low and Chuang](../references/RELATED_WORK.md#yoder2014). The number-theoretic representation and counting theorems are imported and explicitly attributed.

The added account evaluates the gate's integer spectra, handles a common nuisance under the actual query and photon conditions, and takes the residue obstructions to continuous shrinking-window conclusions. Closely related activation examples and Hamiltonian-learning models are compared in [related work](../references/RELATED_WORK.md) without identifying their resource definitions with this one.

The [Ising application](ising_application.md) illustrates the same obstruction in another fixed-time quadratic spectrum. Its all-input conclusion follows from that spectrum, while its fixed particle number, coupling normalization and interrogation time remain part of the theorem.

## Evidence and the boundary of the account

The universal and asymptotic claims follow from the written arguments and the cited mathematical theorems. The [verification suite](../verification/README.md) independently checks finite spectra, constructive identities, local residue omissions, finite readout probabilities and the full four-photon control sector. Those checks can reveal errors in finite ingredients; they do not replace the proofs or constitute external peer review.

The bounded contribution consists of the fixed-query thresholds and the stated supporting results. Optimal prior-rate interpolation, general growing or incommensurate timing catalogs, and complete noisy hardware performance remain outside its established scope.
