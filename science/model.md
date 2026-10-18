# Global calibration of a Kerr phase

An optical or microwave mode can accumulate a phase proportional to the number of photon pairs. The generator grows quadratically with occupation, so nearby parameter values can produce rapidly changing states. Global calibration asks whether one complete experiment can identify the phase throughout its allowed range. The spacing and arithmetic of the available frequencies then matter alongside their size.

This project determines how many identical forward uses of an ideal Kerr gate are needed for increasingly fine global calibration. A known linear phase gives an exact threshold of three uses. A common unknown linear phase raises that threshold to four. Below each threshold, the probability of landing in **any shrinking error window** tends to zero, uniformly over probes, ancillary systems, feedback and final measurements. At the threshold, explicit states achieve sine risk proportional to the inverse fourth power of the photon cap.

The general phase-estimation and finite-group discrimination tools used in the proofs are established results. The contribution developed here is their arithmetic evaluation for this gate, the resulting continuous-parameter confidence thresholds, and the explicitly scoped timing, prior and preparation consequences. See [the attribution account](../references/RELATED_WORK.md).

## The gate and the estimation task

For nonnegative integer occupation $`n`$, define the triangular number

```math
T(n)=\frac{n(n-1)}2.
```

One use of the unknown gate is

```math
U_{\theta,\beta}
=\exp[-i\theta T(\hat n)-i\beta\hat n].
```

Both $`\theta`$ and $`\beta`$ are phases modulo $`2\pi`$. The same pair acts in every use. The task is to report $`\hat\theta`$; there is no accuracy requirement on $`\beta`$. Learning this one coefficient does not by itself learn the full gate on arbitrary superpositions of photon numbers.

In the **known-linear-phase model**, $`\beta`$ is supplied and its phase can be compensated by a known control. In the **unknown-common-phase model**, $`\beta`$ is not supplied. Exact Bayesian risk statements use independent uniform phases. The confidence converse will allow every fixed joint absolutely continuous prior, including correlated densities and narrow fixed intervals.

The original resource is an opaque fixed-duration gate. Calling a shorter evolution, the inverse gate, or a controlled power of the gate is an additional access assumption. A fractional power also requires a choice of real Hamiltonian coefficients beyond their values modulo $`2\pi`$. Those distinctions are quantified in [timing and priors](timing_and_priors.md) and [access variants](access_variants.md).

## Query and photon resources

The query count $`q`$ is the total number of unknown-gate uses in **one complete estimate**. It includes separate probe preparations that are measured and combined, preliminary calibration calls, and calls in failed sensing attempts. Parameter-independent preparation can be retried before any unknown gate is used; such retries consume control resources but no target queries.

The lower bounds allow arbitrary parameter-independent initial states, ancillary systems, interleaved controls, intermediate measurements and feedback, and a final joint POVM. Intermediate measurements can be purified into ancillary registers. Known controls may depend on previous outcomes, the cap, the prior and the requested accuracy; they cannot depend on an unknown parameter except through the recorded query outcomes.

Two photon conditions are kept separate:

| Condition | Meaning | Role here |
|---|---|---|
| Peak occupation cap | The mode entering each unknown-gate call has occupation at most $`N`$. Other parameter-independent controls and ancillas are unrestricted. | A deliberately liberal class for adaptive converses. |
| Total photon cap in the construction | The parallel sensing modes and any explicitly included bypass reference contain at most $`N`$ photons in total. | A stricter condition satisfied by all principal achievable protocols. |

The lower bounds therefore apply to any more restrictive photon budget that still contains the displayed parallel construction. Sequential reuse can accumulate up to $`qN`$ photon exposures while keeping a peak occupation of $`N`$. It is not legitimate to identify that cumulative exposure with the initial number of photons.

The total photon cap counts the bypass mode when a fixed-total superposition needs one. Digital workspace, calibrated nonlinear controls, state preparation, readout and the number-to-Fock interface are separately identified in [coherent preparation](coherent_preparation.md). Four calls is a target-query result, not a claim of four elementary operations or an all-inclusive energy advantage. No QRAM is assumed.

Each adaptive history has integers

```math
g=\sum_{j=1}^{q}T(n_j),\qquad
s=\sum_{j=1}^{q}n_j,
```

and hence $`0\le g\le qT(N)`$ under the peak occupation cap. In a parallel state of fixed total sensing occupation, $`s`$ is that total; in an adaptive history it is cumulative linear exposure. These are the same algebraic label with different resource interpretations.

## Error, confidence and consistency

Let $`d(\hat\theta,\theta)\in[0,\pi]`$ be the shortest angular distance. The periodic loss is

```math
\ell(\hat\theta,\theta)
=4\sin^2\!\left(\frac{\hat\theta-\theta}{2}\right),
\qquad
R=\mathbb E[\ell(\hat\theta,\theta)].
```

For every outcome,

```math
\frac{4}{\pi^2}d^2\le\ell\le d^2.
```

Thus a matching $`\Theta(N^{-4})`$ optimal sine-risk law is equivalent to a matching $`\Theta(N^{-2})`$ wrapped root-mean-square error law. Risk is averaged over measurement outcomes and, when stated as Bayesian risk, the named prior. A pointwise bound holds for every fixed value of both phases.

For a prior $`w`$, define the success probability at half-width $`\delta`$ by

```math
P_w^\Pi(\delta)
=\Pr_w^\Pi\{d(\hat\theta,\theta)<\delta\}.
```

Consistency means that a sequence of protocols has error converging to zero in probability. In particular, consistency permits some sequence $`\delta_N\to0`$ for which the success probability tends to one. The converse below is stronger: below the query threshold every shrinking-window success probability tends to zero.

## Principal results and their proof homes

### R1. Exact fixed-query threshold and Haar risk

For all sufficiently large caps, the optimal uniform-prior risks have the following values. Every constant floor is attained by a parallel state obeying the total photon cap; the lower bounds hold in the larger adaptive peak-cap class.

| Linear phase | One use | Two uses | Three uses | Four uses |
|---|---:|---:|---:|---:|
| Known | $`1`$ | $`2-\sqrt3`$ | $`\Theta(N^{-4})`$ | The three-use protocol can be padded with a vacuum call. |
| Common and unknown | $`2`$ | $`1`$ | $`2-\sqrt2`$ | $`\Theta(N^{-4})`$ |

The finite lower-cap qualifications and exact spectral formulas are in [query thresholds](query_thresholds.md). Four uses with unknown $`\beta`$ employ a fixed odd total sensing occupation $`s\le N`$, so the nuisance contributes only a global phase. A consecutive Kerr-frequency band of length $`s^2/24+O(s)`$ supports the optimum sine amplitudes.

### R2. Vanishing confidence below threshold

Let $`w`$ be any fixed probability density with respect to uniform measure on the two-phase torus. For unknown common $`\beta`$,

```math
\lim_{\delta\downarrow0}
\sup_{N\ge1}\sup_{\Pi:\,q\le3}
P_w^\Pi(\delta)=0.
```

For known $`\beta`$, the analogous statement holds for every fixed absolutely continuous prior on $`\theta`$ and $`q\le2`$. Consequently, no photon-dependent sequence of allowed probes, adaptive controls and measurements can retain nonzero success probability in any shrinking window below the respective threshold.

This statement includes arbitrarily narrow **fixed** priors. It does not cover a point prior, a discrete prior, a density supported on a lower-dimensional curve, or a sequence of priors concentrating with $`N`$. It also does not say that two finite parameter values are necessarily exactly aliased. The mechanism is a uniform limitation on discrimination among increasingly large cyclic families. The proof is in [global confidence](global_confidence.md).

### R3. Attained global resolution

The three-use known-phase and four-use unknown-phase constructions satisfy a **pointwise** $`R\le C N^{-4}`$ bound. For every fixed failure target $`\varepsilon>0`$, an appropriate constant $`C_\varepsilon`$ gives confidence at least $`1-\varepsilon`$ in a window of half-width $`C_\varepsilon N^{-2}`$. Moreover,

```math
\delta_N\to0,\qquad N^2\delta_N\to\infty
\quad\Longrightarrow\quad
P^\Pi(\delta_N)\to1.
```

A fixed multiple of $`N^{-2}`$ provides a fixed confidence guarantee; the stated risk bound does not imply confidence tending to one at that fixed multiple. The matching risk lower bound in R1 is a uniform-prior statement. R3's upper bound holds for every prior because it is pointwise.

### S1. Timing and prior calibration

The subthreshold confidence obstruction persists for any fixed finite catalog of positive commensurate durations, including coherent or adaptive choices among them. The catalog and its time unit remain independent of $`N`$. The exact four-use sufficiency claim refers to the original primitive identical gate.

If $`\theta`$ has a fixed absolutely continuous prior and $`\beta`$ is independently uniform on an interval of known center and width $`w_N`$, three uses are consistent **if and only if** $`w_N\to0`$. Quantitative sufficient and necessary bounds are also proved, but they do not match. The precise statements and open rate gap are in [timing and priors](timing_and_priors.md).

### S2. Explicit preparation and a finite witness

An unconditional coherent arithmetic search prepares the four-use frequency band with $`O(N\operatorname{polylog}N)`$ digital operations, assuming the separately specified coherent Fock-loading interface. This replaces a quadratic lookup table. A four-photon code has exact sine risk

```math
R_4=\frac{3-\sqrt5}{2}
\lt 2-\sqrt2,
```

and therefore already beats the unrestricted three-use Haar floor. Its selected pair rotations and finite Fourier measurement are explicit. See [coherent preparation](coherent_preparation.md), [the four-photon protocol](four_photon_protocol.md), and [robustness](robustness.md).

### S3. Access changes and a spin-system corollary

A shrinking duration can restore consistency with one use when both Hamiltonian coefficients scale with duration. A forward/inverse pair also restores consistency. The exact resource changes are proved in [access variants](access_variants.md).

The same cyclic-residue method gives an all-input strong converse for learning an unnormalized all-to-all Ising coupling from one uninterrupted evolution at fixed duration. Its distinct Hamiltonian and particle-number assumptions are stated in [the Ising application](ising_application.md).

## Connected reading route

Read [query thresholds](query_thresholds.md) for the spectral mechanism, then [global confidence](global_confidence.md) for the stronger statistical consequence. [Timing and priors](timing_and_priors.md) isolates which timing and calibration changes matter. The construction, finite witness and perturbation pages explain what the upper bound requires operationally. [Interpretation](interpretation.md) joins the conclusions, and [verification](../verification/README.md) identifies the finite checks that support the analytical account.

Parameter-independent channels between or after uses can be incorporated in the converse. Loss during the unknown evolution, independently fluctuating linear phases on different calls, and a higher nonlinearity proportional to $`\theta`$ change the model. The corresponding scope is developed where it affects a result, rather than being absorbed into an unqualified experimental claim.
