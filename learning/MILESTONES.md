# Thirty milestones for the Kerr query threshold

This map defines thirty project-level understanding targets. Phase I contains fourteen background and preliminary milestones, moving from individual quantum systems to a complete global-estimation experiment. Phase II contains sixteen narrative and innovation milestones, moving from the first spectral obstructions to the full account of confidence, construction, calibration, and access.

Each milestone has one central question, an understanding target, earlier prerequisites and its role in the story, a conceptual connection, and canonical source pointers. The dependency links refer only to earlier milestones and identify mathematical dependencies.

The educational anchor is John Watrous's *The Theory of Quantum Information*, using the [2018 author draft](../references/RELATED_WORK.md#watrous2018). The [Watrous bridge source map](WATROUS_BRIDGE.md#source-map) fixes the relevant sections and conventions. Watrous supplies the finite-dimensional state, channel, measurement, and norm framework. The project bridges explicitly supply the passage to photon-limited Fock systems, adaptive Fourier histories, circle averaging, and Kerr estimation. The number-theoretic representation results and other established research ingredients retain their existing primary-source attribution.

## Phase I: Background and preliminaries

### M01. Quantum states and relative phase

**Question.** Which features of a quantum state can carry information about an unknown phase?

**Target.** A state is represented operationally by a positive, unit-trace density operator. A pure vector and any scalar phase multiple define the same density operator, whereas relative phases between distinguishable basis components can change measurement probabilities. Mixed states, coherent superpositions, and classical uncertainty over a preparation are different descriptions with different off-diagonal structure. This distinction identifies which parameter-dependent phases can survive into an observable estimate.

**Prerequisites and story role.** No earlier milestone. This establishes the state language from which the generator, nuisance, and measurement arguments are built.

**Connection.** The four-use construction will make the linear nuisance a global phase while preserving relative Kerr phases. That separation is already meaningful at the level of a two-component state.

**Canonical sources.** [Watrous source map](WATROUS_BRIDGE.md#source-map), especially §2.1.2; [notation and conventions](WATROUS_BRIDGE.md#notation-and-conventions); [the gate and estimation task](../science/model.md#the-gate-and-the-estimation-task).

### M02. Fock occupations and nonlinear generators

**Question.** How does photon occupation turn the Kerr gate into integer phase frequencies?

**Target.** The number states $`|n\rangle`$ diagonalize both $`\hat n`$ and $`T(\hat n)=\hat n(\hat n-1)/2`$. One fixed call contributes $`e^{-i\theta T(n)-i\beta n}`$ to occupation $`n`$. Thus the linear and quadratic terms label the same component by different integers, including the degeneracy $`T(0)=T(1)=0`$. A hard cap on the queried occupation supplies a finite subspace even though the full Fock space is infinite.

**Prerequisites and story role.** [M01](#m01-quantum-states-and-relative-phase). This identifies the concrete representation whose arithmetic will determine the threshold.

**Connection.** A generator that grows quadratically supplies large phase frequencies, but its growth does not specify how densely those frequencies fill the integers.

**Canonical sources.** [From a Fock mode to a finite register](WATROUS_BRIDGE.md#from-a-fock-mode-to-a-finite-register); [the gate and estimation task](../science/model.md#the-gate-and-the-estimation-task); [a known linear phase](../science/query_thresholds.md#a-known-linear-phase).

### M03. Composite systems and photon accounting

**Question.** Which tensor factors and photons belong to the same experiment?

**Target.** Sensing modes, a bypass reference, digital labels, and ancillary systems are distinct tensor factors. The superposition $`\sum_{n=0}^N c_n|n\rangle_{\rm sense}|N-n\rangle_{\rm bypass}`$ keeps the counted photon total fixed and retains relative coherence between joint sensing-and-reference components. Its reduced sensing state alone is number diagonal. The peak occupation entering each query, the total photons in a parallel preparation, and the cumulative photons exposed over several calls are different resource quantities. An unrestricted ancilla does not itself introduce another unknown-gate frequency.

**Prerequisites and story role.** [M01](#m01-quantum-states-and-relative-phase), [M02](#m02-fock-occupations-and-nonlinear-generators). This makes the resource promise precise before controls or adaptive reuse are introduced.

**Connection.** The known-phase three-use probe needs a counted bypass reference, while the unknown-phase four-use probe uses a fixed exposed total. Both can obey the same total photon cap through different tensor structures.

**Canonical sources.** [Watrous source map](WATROUS_BRIDGE.md#source-map), including the tensor-product discussion in §1.1.1; [the Fock-to-register bridge](WATROUS_BRIDGE.md#from-a-fock-mode-to-a-finite-register); [query and photon resources](../science/model.md#query-and-photon-resources).

### M04. Channels, ancillas, and adaptive controls

**Question.** How can measurements and feedback be included in one parameter-independent quantum circuit?

**Target.** A channel describes admissible state evolution, including discarded environments. Purifications and isometric dilations retain those environments in a larger system. An intermediate measurement with an outcome-dependent continuation requires an instrument and a classical record; its POVM effects alone specify only outcome probabilities. Retaining the records permits a coherent description of feedback. Known controls can depend on the prior, budget, and earlier outcomes while remaining independent of the unknown parameters apart from information acquired through counted queries.

**Prerequisites and story role.** [M01](#m01-quantum-states-and-relative-phase), [M03](#m03-composite-systems-and-photon-accounting). This defines the broad protocol class needed for adaptive lower bounds.

**Connection.** The later Fourier coefficients can be nonorthogonal because controls combine histories. Purification preserves all such protocols without assuming that every history is physically readable.

**Canonical sources.** [Watrous source map](WATROUS_BRIDGE.md#source-map), §2.1.3 and §§2.2.1–2.2.2; [query and photon resources](../science/model.md#query-and-photon-resources); [adaptive Fourier reduction](../science/query_thresholds.md#adaptive-fourier-reduction).

### M05. Measurements and finite POVMs

**Question.** How does a quantum output become an angular estimate?

**Target.** Positive measurement effects that sum to the identity determine outcome probabilities through the Born rule. An estimator attaches an angle to each outcome, possibly after classical randomization or postprocessing. A finite POVM can be realized by an enlarged projective measurement, and a classical mixture of projective measurements is also a POVM. These descriptions must specify both the effects and the reported values before a risk or confidence statement is meaningful.

**Prerequisites and story role.** [M01](#m01-quantum-states-and-relative-phase), [M04](#m04-channels-ancillas-and-adaptive-controls). This provides the measurement language for exact risk and discrimination arguments.

**Connection.** The project eventually uses two offset Fourier grids to obtain constant pointwise sine risk with finitely many outcomes. A continuous covariant outcome space is not required for that attainment.

**Canonical sources.** [Watrous source map](WATROUS_BRIDGE.md#source-map), §§2.3.1–2.3.2; [from loss to frequency adjacency](WATROUS_BRIDGE.md#from-loss-to-frequency-adjacency); [finite readout with constant pointwise risk](../science/query_thresholds.md#a-finite-readout-with-constant-pointwise-risk).

### M06. Periodic parameters and global identifiability

**Question.** Why does large phase sensitivity not by itself resolve a global parameter?

**Target.** Integer spectral gaps make the encoded parameter periodic. A superposition with a large gap can have many narrow fringes over the parameter circle, so a local change scale does not identify the correct fringe in a complete estimate. The presence of a unit gap can remove a smaller exact period without guaranteeing useful shrinking-window confidence from a fixed number of calls. A real Hamiltonian coefficient and its phase modulo $`2\pi`$ must also be distinguished when durations change.

**Prerequisites and story role.** [M02](#m02-fock-occupations-and-nonlinear-generators), [M05](#m05-measurements-and-finite-povms). This separates the global task from local sensitivity before asymptotic precision is discussed.

**Connection.** The fixed-query obstruction concerns the usable distribution of frequencies across an entire parameter domain. Exact pairwise identifiability and global estimation accuracy therefore require different arguments.

**Canonical sources.** [One call and a global estimate](WATROUS_BRIDGE.md#one-call-and-a-global-estimate); [local sensitivity and a complete estimate](../science/interpretation.md#local-sensitivity-and-a-complete-estimate); [the gate and estimation task](../science/model.md#the-gate-and-the-estimation-task).

### M07. Common nuisance phases and block averaging

**Question.** What coherence remains after averaging a common unknown linear phase?

**Target.** Uniform circle averaging uses $`\int e^{-i(s-t)\beta}\,d\beta/(2\pi)=\delta_{s,t}`$. It preserves coherence between components with the same cumulative linear exposure and removes cross terms between different exposures. For parallel modes, that exposure is their summed occupation; a fixed total makes the common linear phase a scalar. Independently averaged linear phases on each call produce a different channel and remove the target information in each call of this model.

**Prerequisites and story role.** [M02](#m02-fock-occupations-and-nonlinear-generators), [M03](#m03-composite-systems-and-photon-accounting), [M04](#m04-channels-ancillas-and-adaptive-controls), [M06](#m06-periodic-parameters-and-global-identifiability). This explains the nuisance-sector restriction that raises the query threshold.

**Connection.** Shared uncertainty leaves degenerate sectors in which useful interference survives. The arithmetic problem is therefore to find many Kerr frequencies inside one surviving sector.

**Canonical sources.** [Why a common linear phase creates sectors](WATROUS_BRIDGE.md#why-a-common-linear-phase-creates-sectors); [adaptive Fourier reduction](../science/query_thresholds.md#adaptive-fourier-reduction); [why sharing the linear phase is essential](../science/interpretation.md#why-sharing-the-linear-phase-is-essential).

### M08. Sine loss, wrapped RMS, and confidence

**Question.** Which error statements follow from a sine-risk bound?

**Target.** For shortest angular distance $`d\in[0,\pi]`$, the loss $`\ell(d)=4\sin^2(d/2)`$ satisfies $`4d^2/\pi^2\leq\ell(d)\leq d^2`$. Thus a matching $`N^{-4}`$ sine-risk law corresponds to a matching $`N^{-2}`$ wrapped RMS law. The bound $`\Pr\{d\geq\delta\}\leq R/[4\sin^2(\delta/2)]`$ translates risk into confidence. Fixed high confidence at a constant times $`N^{-2}`$ and confidence tending to one are distinct conclusions.

**Prerequisites and story role.** [M05](#m05-measurements-and-finite-povms), [M06](#m06-periodic-parameters-and-global-identifiability). This fixes the statistical meaning of every precision scale used later.

**Connection.** The loss has only a constant and first Fourier harmonic. That simple harmonic structure is why adjacent spectral frequencies, rather than every pair of frequencies, determine its optimum.

**Canonical sources.** [From loss to frequency adjacency](WATROUS_BRIDGE.md#from-loss-to-frequency-adjacency); [error, confidence, and consistency](../science/model.md#error-confidence-and-consistency); [confidence attained at the threshold](../science/global_confidence.md#confidence-attained-at-the-threshold).

### M09. Distinguishability and prior comparison

**Question.** How do quantum distinguishability and classical prior weights bound success?

**Target.** Quantum hypothesis testing relates a measurement's success to the distinguishability of its input states. Trace distance bounds the change in any event probability and cannot increase under parameter-independent channels. Separately, a prior changes the classical weighting of the same conditional probabilities. A bounded density gives a direct comparison with a reference prior; an integrable density can be split into a bounded part and a small tail. These tools serve different roles in robust constructions and prior-independent converses.

**Prerequisites and story role.** [M04](#m04-channels-ancillas-and-adaptive-controls), [M05](#m05-measurements-and-finite-povms), [M08](#m08-sine-loss-wrapped-rms-and-confidence). This supplies the operational probability bounds needed beyond average sine loss.

**Connection.** Partial calibration uses a trace-distance comparison of two output states, while the fixed-prior strong converse uses density truncation. Both transfer a bound to a new statistical situation, but their assumptions are different.

**Canonical sources.** [Watrous source map](WATROUS_BRIDGE.md#source-map), §§3.1.1–3.1.2; [from fine estimation to finite discrimination](WATROUS_BRIDGE.md#from-fine-estimation-to-finite-discrimination); [every fixed absolutely continuous joint prior](../science/global_confidence.md#every-fixed-absolutely-continuous-joint-prior).

### M10. Query histories and Fourier support

**Question.** Why do all allowed fixed-use protocols have an integer Fourier description?

**Target.** Inserting number projectors at each of $`q`$ queries assigns a history the two frequencies $`g=\sum_jT(n_j)`$ and $`s=\sum_jn_j`$. Purification and collection of equal labels give $`|\Psi_{\theta,\beta}\rangle=\sum_{g,s}e^{-ig\theta-is\beta}|v_{g,s}\rangle`$. The vectors need not be orthogonal. Parameter-independent controls change these coefficients but keep their support within the allowed history set. A hard occupation cap gives finite ranges, and averaged normalization gives the Parseval identity used by the bounds.

**Prerequisites and story role.** [M02](#m02-fock-occupations-and-nonlinear-generators), [M04](#m04-channels-ancillas-and-adaptive-controls), [M07](#m07-common-nuisance-phases-and-block-averaging). This converts a general quantum protocol into a constrained spectral object.

**Connection.** The lower bounds can relax the physical circuit to a larger set of possible history frequencies. That relaxation strengthens their scope while making no assumption that every relaxed frequency basis is freely preparable.

**Canonical sources.** [Adaptive Fourier reduction](../science/query_thresholds.md#adaptive-fourier-reduction); [the finite-dimensional source map and project bridges](WATROUS_BRIDGE.md#source-map); [query and photon resources](../science/model.md#query-and-photon-resources).

### M11. Consecutive spectra and path optimization

**Question.** Why does the longest adjacent frequency run determine sine risk?

**Target.** The first harmonic of the loss couples only neighboring integer frequencies. A POVM first-moment operator is a contraction, so arbitrary adaptive coefficients give a score bounded by adjacent norm products. Missing frequencies split this quadratic form into path graphs. A path with $`L`$ vertices has optimal score $`\cos[\pi/(L+1)]`$ and sine amplitudes, giving risk $`2[1-\cos(\pi/(L+1))]`$. Equality requires allowed orthogonal representatives and a suitable readout; a finite padded or two-grid Fourier POVM supplies that readout.

**Prerequisites and story role.** [M05](#m05-measurements-and-finite-povms), [M08](#m08-sine-loss-wrapped-rms-and-confidence), [M10](#m10-query-histories-and-fourier-support). This is the spectral optimization tool behind every exact floor and dense-band upper bound.

**Connection.** A local adjacency operator turns an arithmetic statement about missing integers into an operational risk bound. The same sine state will recur in both the asymptotic constructions and the four-photon example.

**Canonical sources.** [The longest consecutive run bound](../science/query_thresholds.md#the-longest-consecutive-run-bound); [the loss-to-adjacency bridge](WATROUS_BRIDGE.md#from-loss-to-frequency-adjacency); [established phase-estimation ingredients](../references/RELATED_WORK.md#dariano1998).

### M12. Congruences and the Chinese remainder theorem

**Question.** How do local residue omissions become global support restrictions?

**Target.** A polynomial frequency set can omit residue classes modulo a small integer even while its maximum frequency grows. Omitted classes bound consecutive runs. For coprime moduli, the Chinese remainder theorem combines permitted residue sets by multiplying their cardinalities. Repeated restrictions modulo prime squares can therefore make the permitted fraction small. A divergence statement for reciprocal primes in a reduced progression is the separate analytic ingredient that makes the relevant infinite product vanish.

**Prerequisites and story role.** [M10](#m10-query-histories-and-fourier-support), [M11](#m11-consecutive-spectra-and-path-optimization). This introduces the local-to-global arithmetic operation needed for both fixed floors and the strong converse.

**Connection.** A missing class modulo four gives a fixed-resolution restriction; a controlled sequence of prime-power omissions will give a statement about every shrinking resolution.

**Canonical sources.** [Arithmetic beyond the quantum source](WATROUS_BRIDGE.md#arithmetic-that-the-quantum-source-does-not-supply); [prime-power obstructions](../science/global_confidence.md#prime-power-obstructions); [the existing CRT and prime-progression references](../references/RELATED_WORK.md#dlmf27).

### M13. Quadratic forms and representation theorems

**Question.** When do quadratic representation theorems fill frequencies, and when do norms leave holes?

**Target.** Binary quadratic norms such as $`x^2+y^2`$ and $`x^2-xy+y^2`$ have primes at which divisibility by $`p`$ forces divisibility by $`p^2`$. In contrast, the three-square criterion and three-triangular-number theorem provide representation existence for suitable integer families. A third kind of statement, Bernays' theorem, counts distinct integers represented by a fixed binary form. Representation existence, residue exclusion, and counting represented values are different number-theoretic inputs.

**Prerequisites and story role.** [M02](#m02-fock-occupations-and-nonlinear-generators), [M12](#m12-congruences-and-the-chinese-remainder-theorem). This supplies the precise arithmetic ingredients before they are applied to query histories.

**Connection.** The change in the number of available occupation variables changes the quadratic form after the common linear constraint is imposed. That change will distinguish the obstructed three-use spectrum from the four-use filled band.

**Canonical sources.** [Arithmetic beyond the quantum source](WATROUS_BRIDGE.md#arithmetic-that-the-quantum-source-does-not-supply); [Sun](../references/RELATED_WORK.md#sun2007); [Mortenson](../references/RELATED_WORK.md#mortenson2017); [Moree and Osburn's account of Bernays' theorem](../references/RELATED_WORK.md#moree2006).

### M14. The complete operational estimation model

**Question.** What must be fixed before a query-threshold assertion has a definite meaning?

**Target.** A complete estimation problem specifies the parameter family and prior, the allowed input and control systems, the meaning of one unknown-gate use, the photon promise, the final estimator, and the loss or success event. In this project, $`q`$ counts every target use contributing to one complete estimate. The headline access is an identical fixed forward gate, the nuisance is common, and the task is to learn the Kerr coefficient rather than the full gate action. Peak-cap converses and stricter parallel total-cap constructions are stated separately.

**Prerequisites and story role.** [M09](#m09-distinguishability-and-prior-comparison), [M11](#m11-consecutive-spectra-and-path-optimization), [M13](#m13-quadratic-forms-and-representation-theorems). This closes the preliminary phase by joining the quantum, statistical, and arithmetic descriptions into one experiment.

**Connection.** The same formal expression can represent a different task when prior concentration, inverse access, timing control, or cumulative exposure changes. The model supplies the reference against which every subsequent variation is compared.

**Canonical sources.** [Query and photon resources](../science/model.md#query-and-photon-resources); [error, confidence, and consistency](../science/model.md#error-confidence-and-consistency); [resources, priors, and the complete story](WATROUS_BRIDGE.md#resources-priors-and-the-complete-story).

## Phase II: Narrative and innovation

### M15. Known-phase risk floors

**Question.** Why do one and two uses retain a nonzero global risk when the linear phase is known?

**Target.** One triangular spectrum has a longest consecutive run of two, yielding exact sine risk one. Sums of two triangular spectra miss residues five and eight modulo nine, so their longest run has at most five frequencies. The explicit band $`0,\ldots,4`$ attains risk $`2-\sqrt3`$ within total photon cap five. These witnesses and the adaptive spectral bound establish exact sufficiently-large-cap floors, even though a unit frequency gap already permits exact identifiability.

**Prerequisites and story role.** [M11](#m11-consecutive-spectra-and-path-optimization), [M12](#m12-congruences-and-the-chinese-remainder-theorem), [M14](#m14-the-complete-operational-estimation-model). This is the first complete application of the spectral method and establishes the known-phase obstruction.

**Connection.** The size of the largest generator eigenvalue keeps increasing, while the longest usable adjacent run remains bounded. This gives a concrete instance of the local-versus-global distinction.

**Canonical sources.** [One and two known-phase uses](../science/query_thresholds.md#one-and-two-uses); [the longest consecutive run bound](../science/query_thresholds.md#the-longest-consecutive-run-bound); [one call and a global estimate](WATROUS_BRIDGE.md#one-call-and-a-global-estimate).

### M16. Three-use known-phase activation

**Question.** How does the third known-phase use create a band of quadratic length within the photon cap?

**Target.** Three-triangular-number completeness gives every nonnegative Kerr frequency. For a representing triple with total $`s`$, the inequality $`s^2\leq6g+3s`$ places every $`g\leq\lfloor N(N-3)/6\rfloor`$ within total cap $`N`$. A counted bypass reference completes each component to the same photon total. Sine amplitudes over this band and finite Fourier readout give pointwise $`O(N^{-4})`$ risk, with the matching Haar lower exponent supplied by the available frequency range.

**Prerequisites and story role.** [M13](#m13-quadratic-forms-and-representation-theorems), [M15](#m15-known-phase-risk-floors). This completes the known-phase threshold through an explicit attainable construction.

**Connection.** A classical existence theorem becomes an estimation upper bound only after the representation's photon cost, the coherent state, and the readout are all specified.

**Canonical sources.** [Three known-phase uses](../science/query_thresholds.md#three-uses); [the Fock-to-register bridge](WATROUS_BRIDGE.md#from-a-fock-mode-to-a-finite-register); [three-square and triangular representation ingredients](../references/RELATED_WORK.md#mortenson2017).

### M17. Unknown-common-phase risk floors

**Question.** Why does a common unknown linear phase obstruct one, two, and three uses?

**Target.** The nuisance average restricts the support to each fixed cumulative exposure $`s`$. One use leaves a singleton frequency. Two uses give translated squares when $`s`$ is even and a fixed parity when $`s`$ is odd. Three uses obey $`3g+(3s-s^2)/2=u^2-uv+v^2`$, which excludes one frequency class modulo four. The resulting exact risks are $`2`$, $`1`$, and $`2-\sqrt2`$, with explicit fixed-total witnesses attaining the latter two.

**Prerequisites and story role.** [M07](#m07-common-nuisance-phases-and-block-averaging), [M13](#m13-quadratic-forms-and-representation-theorems), [M14](#m14-the-complete-operational-estimation-model). This identifies the arithmetic obstruction introduced by the nuisance-sector constraint.

**Connection.** The common nuisance does not merely add noise to a previously optimal probe. It changes which frequency pairs may interfere after averaging, thereby changing the arithmetic support relevant to the optimum.

**Canonical sources.** [One to three uses with an unknown common linear phase](../science/query_thresholds.md#one-to-three-uses-with-an-unknown-common-linear-phase); [the common-phase sector bridge](WATROUS_BRIDGE.md#why-a-common-linear-phase-creates-sectors); [the common nuisance and arithmetic geometry](../science/interpretation.md#the-common-nuisance-and-the-arithmetic-geometry).

### M18. Four-use activation in an odd fixed-total sector

**Question.** How do four modes retain the common-nuisance cancellation while filling enough Kerr frequencies?

**Target.** For an odd exposed total $`s`$, the interval from $`(s^2-4s+3)/8`$ to $`\lfloor s(s-3)/6\rfloor`$ has a representation at every integer frequency. The transformed value $`8g+4s-s^2`$ is three modulo eight and is at most $`s^2/3`$. The three-square theorem and inverse Hadamard map give integral, nonnegative occupations of total $`s`$. The resulting $`\Theta(N^2)`$ consecutive band yields pointwise $`O(N^{-4})`$ risk with common $`\beta`$ only a scalar phase.

**Prerequisites and story role.** [M13](#m13-quadratic-forms-and-representation-theorems), [M16](#m16-three-use-known-phase-activation), [M17](#m17-unknown-common-phase-risk-floors). This completes the unknown-common-phase threshold at the level of an ideal coherent construction.

**Connection.** A fixed linear constraint leaves a binary quadratic form for three occupations and a ternary form for four. The representation theorem acts on the latter, while odd total occupation supplies a suitable congruence class.

**Canonical sources.** [Four uses with an unknown common linear phase](../science/query_thresholds.md#four-uses-with-an-unknown-common-linear-phase); [the arithmetic bridge](WATROUS_BRIDGE.md#arithmetic-that-the-quantum-source-does-not-supply); [the three-square criterion](../references/RELATED_WORK.md#sun2007).

### M19. The four-photon threshold witness

**Question.** What finite experiment already separates four uses from every allowed three-use protocol?

**Target.** The code words $`1111,2110,0220,3100`$ all expose four photons and have consecutive Kerr frequencies zero through three. Sine amplitudes on this code give the exact pointwise risk $`(3-\sqrt5)/2`$, below the unrestricted three-use Haar floor $`2-\sqrt2`$. The comparison keeps the common nuisance, total query count, and photon convention aligned. This finite witness demonstrates a strict advantage without relying on a large-$`N`$ limit.

**Prerequisites and story role.** [M11](#m11-consecutive-spectra-and-path-optimization), [M17](#m17-unknown-common-phase-risk-floors), [M18](#m18-four-use-activation-in-an-odd-fixed-total-sector). This grounds the asymptotic threshold in one complete finite code before its controls are developed.

**Connection.** The same path eigenvector that optimized the abstract spectral problem determines four concrete Fock amplitudes. An even exposed total can support this finite improvement even though the asymptotic four-use construction selects odd totals.

**Canonical sources.** [Code and risk](../science/four_photon_protocol.md#code-and-risk); [a complete four-photon example](WATROUS_BRIDGE.md#a-complete-four-photon-example); [the three-use comparison floor](../science/query_thresholds.md#one-to-three-uses-with-an-unknown-common-linear-phase).

### M20. Cyclic discrimination from occupied residues

**Question.** How does fine angular estimation imply discrimination among a finite cyclic family?

**Target.** Revealing $`\alpha=\theta\bmod(2\pi/M)`$ leaves $`M`$ equally likely phase hypotheses. Grouping each nuisance block's Fourier coefficients by residues modulo $`M`$ gives at most $`D`$ contributing residue vectors when its support occupies at most $`D`$ classes. Cauchy–Schwarz, POVM completeness, and averaged state normalization then give success at most $`D/M`$ for error below $`\pi/M`$. The proof requires neither orthogonal coefficients nor constant norms of the individual nuisance blocks.

**Prerequisites and story role.** [M09](#m09-distinguishability-and-prior-comparison), [M10](#m10-query-histories-and-fourier-support), [M12](#m12-congruences-and-the-chinese-remainder-theorem), [M14](#m14-the-complete-operational-estimation-model). This supplies the statistical mechanism for a converse stronger than the sine-risk floor.

**Connection.** Providing side information turns a continuous accuracy requirement into a discrete decision problem that can only be easier. Spectral residue occupancy becomes an operational probability bound through that reduction.

**Canonical sources.** [A cyclic residue bound and its proof](../science/global_confidence.md#a-cyclic-residue-bound); [fine estimation and finite discrimination](WATROUS_BRIDGE.md#from-fine-estimation-to-finite-discrimination); [established finite-group query theory](../references/RELATED_WORK.md#copeland2021).

### M21. Prime products and vanishing global confidence

**Question.** Why must subthreshold success vanish in every shrinking error window, regardless of photon cap?

**Target.** The unknown-phase three-use Eisenstein norm excludes valuations equal to one at primes $`p\equiv2\pmod3`$. The known-phase two-use identity $`4g+1=x^2+y^2`$ gives the same exclusion at primes $`p\equiv3\pmod4`$. Modulo each $`p^2`$, at most $`p^2-p+1`$ classes remain. CRT products and divergent reciprocal-prime sums drive the permitted fraction to zero. The finite modulus is chosen from the desired resolution before taking a supremum over all finite caps and protocols.

**Prerequisites and story role.** [M15](#m15-known-phase-risk-floors), [M17](#m17-unknown-common-phase-risk-floors), [M20](#m20-cyclic-discrimination-from-occupied-residues). This upgrades the arithmetic floors into the central uniform strong converse.

**Connection.** The order of quantifiers is decisive: increasing photon number cannot overcome a residue restriction already valid at every cap. The obstruction concerns globally useful estimates, not merely a poorly chosen probe.

**Canonical sources.** [The uniform shrinking-window theorem](../science/global_confidence.md#the-uniform-shrinking-window-theorem); [the known-linear-phase strong converse](../science/global_confidence.md#known-linear-phase); [the arithmetic source bridge](WATROUS_BRIDGE.md#arithmetic-that-the-quantum-source-does-not-supply).

### M22. Fixed priors, heralding, and confidence at the threshold

**Question.** How does the confidence theorem apply to realistic fixed priors, accepted outputs, and the attainable protocols?

**Target.** Truncating any fixed joint absolutely continuous density transfers the Haar strong converse even when the phases are correlated or their fixed intervals are narrow. For heralded estimates, acceptance probability times conditional fine-estimation success is bounded by the completed experiment's success; retries after sensing count as further queries. At the threshold, pointwise $`O(N^{-4})`$ risk gives fixed high confidence at a suitable constant times $`N^{-2}`$, and confidence tending to one when $`N^2\delta_N\to\infty`$.

**Prerequisites and story role.** [M09](#m09-distinguishability-and-prior-comparison), [M16](#m16-three-use-known-phase-activation), [M18](#m18-four-use-activation-in-an-odd-fixed-total-sector), [M21](#m21-prime-products-and-vanishing-global-confidence). This completes the statistical meaning of the threshold under the specified prior and reporting conventions.

**Connection.** The converse is uniform over protocols but not over all concentrating prior families. Query-free state-preparation heralding and postselection after target sensing also have different resource implications.

**Canonical sources.** [Every fixed absolutely continuous joint prior](../science/global_confidence.md#every-fixed-absolutely-continuous-joint-prior); [heralding and retries](../science/global_confidence.md#heralding-and-retries); [confidence attained at the threshold](../science/global_confidence.md#confidence-attained-at-the-threshold); [resources and priors](WATROUS_BRIDGE.md#resources-priors-and-the-complete-story).

### M23. Coherent preparation without QRAM

**Question.** How can the four-use band be prepared coherently without storing a representative for every frequency?

**Target.** Reversible arithmetic marks valid three-square representations in a search space of size $`O(N^2)`$. A uniform lower bound on the marked fraction permits one fixed-point amplification schedule to act coherently in every frequency block. The algorithm retains representation labels, assigns a fixed-total fallback to unmarked candidates, and reverses known preparation after four target calls. Sine amplitudes use query-free preparation. With a separately assumed Fock-loading interface, choosing search amplitude tolerance $`\delta=N^{-2}`$ retains $`O(N^{-4})`$ risk at $`O(N\mathrm{polylog}N)`$ digital cost without QRAM.

**Prerequisites and story role.** [M04](#m04-channels-ancillas-and-adaptive-controls), [M18](#m18-four-use-activation-in-an-odd-fixed-total-sector), [M22](#m22-fixed-priors-heralding-and-confidence-at-the-threshold). This turns the existence-based band into a specified algorithm with a distinct control-resource account.

**Connection.** A canonical arithmetic representative is unnecessary because all valid representatives of one Kerr frequency receive the same ideal unknown phase. Retaining labels makes known preparation reversible despite representation multiplicity.

**Canonical sources.** [Construction and resource statement](../science/coherent_preparation.md#construction-and-resource-statement); [a reversible representation predicate](../science/coherent_preparation.md#a-reversible-representation-predicate); [coherent fixed-point amplification](../science/coherent_preparation.md#coherent-fixed-point-amplification); [encoding, four queries, and decoding](../science/coherent_preparation.md#encoding-four-queries-and-decoding); [Yoder, Low, and Chuang](../references/RELATED_WORK.md#yoder2014).

### M24. Finite physical controls and readout

**Question.** What physical control assumptions connect a logical frequency code to a complete bosonic experiment?

**Target.** The four-photon code admits number-preserving selected pair rotations defined on the full participating-mode space, with identity on spectators. Parking and a parity echo cancel unwanted code transitions; logical phases and adjacent rotations compile the finite Fourier transform, followed by two offset grids and Fock detection. The asymptotic construction instead specifies a conditional number-to-Fock loader with retained digital labels and dark-state shelving. Digital operation counts, conditional transfer stages, and demonstrated hardware fidelity remain separate claims.

**Prerequisites and story role.** [M05](#m05-measurements-and-finite-povms), [M19](#m19-the-four-photon-threshold-witness), [M23](#m23-coherent-preparation-without-qram). This makes the physical interfaces and finite readout concrete after the abstract construction is understood.

**Connection.** A correct unitary on a desired code subspace is insufficient unless its action on spectator sectors and possible leakage is also specified. The full control model is part of an attainable upper bound.

**Canonical sources.** [The selected pair primitive](../science/four_photon_protocol.md#the-selected-pair-primitive); [a parity echo for the middle edge](../science/four_photon_protocol.md#a-parity-echo-for-the-middle-edge); [logical phases and Fourier compilation](../science/four_photon_protocol.md#logical-phases-and-an-explicit-fourier-compilation); [two offset Fourier grids](../science/four_photon_protocol.md#two-offset-fourier-grids); [the conditional physical loading lemma](../science/coherent_preparation.md#a-conditional-physical-loading-lemma).

### M25. Exact-exposure parity and the five-use consequence

**Question.** Why does requiring exactly an even exposed total change the four-use asymptotic conclusion?

**Target.** For $`s=2a`$, the four-use spectrum satisfies $`2g+2a-a^2=u^2+v^2+w^2`$. If $`s\equiv2\pmod4`$, a missing class modulo four limits consecutive runs to three; if $`s\equiv0\pmod4`$, a missing class modulo sixteen limits them to fifteen. Explicit witnesses attain these lengths in the stated large-total ranges. These are Haar risk floors and give a full-circle minimax obstruction. A fifth call carrying one photon when needed leaves an odd total in the other four, restoring vanishing Haar risk and a full-circle minimax guarantee for both exact-exposure parities. A band with frequency spacing four explains why a sufficiently narrow target prior can still permit four-use consistency at even exact totals.

**Prerequisites and story role.** [M17](#m17-unknown-common-phase-risk-floors), [M18](#m18-four-use-activation-in-an-odd-fixed-total-sector), [M19](#m19-the-four-photon-threshold-witness). This sharpens the resource promise without altering the headline theorem under an at-most photon cap.

**Connection.** The four-photon finite witness, the odd-total asymptotic band, and the even-total risk floors are compatible. Their conclusions refer to different finite or asymptotic uses of the same exact-exposure condition.

**Canonical sources.** [Exactly even exposed photon totals](../science/query_thresholds.md#exactly-even-exposed-photon-totals); [the common nuisance and arithmetic geometry](../science/interpretation.md#the-common-nuisance-and-the-arithmetic-geometry); [query and photon resources](../science/model.md#query-and-photon-resources).

### M26. Duration catalogs and changed query access

**Question.** Which timing changes preserve the obstruction, and which alter the available experiment?

**Target.** A fixed finite catalog of positive commensurate durations produces weighted binary forms. A common inert-prime progression and a finite union over adaptive schedules preserve the subthreshold strong converse. A duration that shrinks with $`N`$ changes this premise: the displayed one-call construction achieves $`O(N^{-1})`$ risk when both Hamiltonian coefficients scale with duration. A forward/full-inverse pair instead creates consecutive differences and achieves $`\Theta(N^{-2})`$ risk. These are constructive rates in enlarged access models, not their optimality theorems.

**Prerequisites and story role.** [M16](#m16-three-use-known-phase-activation), [M18](#m18-four-use-activation-in-an-odd-fixed-total-sector), [M21](#m21-prime-products-and-vanishing-global-confidence). This identifies fixed positive query access as a substantive part of the threshold.

**Connection.** A fixed clock catalog, a refining clock, a minimum duration, and an inverse gate impose different constraints on the frequency set. Real coefficient representatives and time-weighted exposure must be specified when comparing them.

**Canonical sources.** [A fixed finite positive commensurate duration catalog](../science/timing_and_priors.md#a-fixed-finite-positive-commensurate-duration-catalog); [one shortened call restores consistency](../science/access_variants.md#one-shortened-call-restores-consistency); [a forward/inverse pair](../science/access_variants.md#a-forwardinverse-pair); [fixed clocks, minimum durations, and total time](../science/access_variants.md#fixed-clocks-minimum-durations-and-total-time).

### M27. Partial calibration and the unresolved rate gap

**Question.** How much improving prior information about the linear phase allows three fixed uses to become consistent?

**Target.** For a fixed absolutely continuous Kerr prior and an independent uniform nuisance interval of known center, three-use consistency is possible exactly when its width $`w_N`$ tends to zero. An effective photon budget gives risk $`O(K^{-4}+w_N^2K^2)`$. The proved sufficient widths are $`O(N^{-3})`$ for $`O(N^{-2})`$ RMS and $`O(N^{-1})`$ for fixed high confidence at that resolution. Bernays frequency counting gives the weaker necessary width $`O((\log N)^{-1/2})`$. The qualitative criterion is sharp; these quantitative rates do not match.

**Prerequisites and story role.** [M16](#m16-three-use-known-phase-activation), [M22](#m22-fixed-priors-heralding-and-confidence-at-the-threshold). This treats improving calibration as an explicit change of the statistical resource.

**Connection.** Partial averaging weights neighboring exposure differences by a sinc factor. More photons increase the available Kerr band while making a chosen cross-sector construction more sensitive to residual linear-phase uncertainty.

**Canonical sources.** [Exact risk under the interval prior](../science/timing_and_priors.md#exact-risk-under-the-interval-prior); [the exact qualitative calibration criterion](../science/timing_and_priors.md#the-exact-qualitative-calibration-criterion); [the finite-cap necessary calibration bound](../science/timing_and_priors.md#a-finite-cap-necessary-calibration-bound); [the quantitative gap](../science/timing_and_priors.md#the-quantitative-gap).

### M28. Residual cubic phases and robustness

**Question.** When does an additional spectral phase preserve the converse, and what does it cost an attaining protocol?

**Target.** A fixed or independently sampled cubic coefficient can be revealed and simulated as a parameter-independent control, so it preserves the subthreshold converse. Its effect on a four-use readout is governed by adjacent phase increments or, for retained work registers, adjacent work-state differences. The exact finite-code tolerance and conservative asymptotic bounds follow from that functional; $`|\kappa|=O(N^{-5})`$ is one sufficient condition for retaining the growing construction's $`O(N^{-4})`$ risk. A cubic term proportional to the unknown target changes the generator and needs a different converse.

**Prerequisites and story role.** [M04](#m04-channels-ancillas-and-adaptive-controls), [M19](#m19-the-four-photon-threshold-witness), [M23](#m23-coherent-preparation-without-qram), [M24](#m24-finite-physical-controls-and-readout). This separates stability of a lower bound from accuracy of a specific implementation.

**Connection.** Fixed total occupation cancels a common linear phase but generally leaves representation-dependent cubic phases. Known retained occupation labels can compensate a known cubic coefficient, making calibration accuracy a separately visible resource.

**Canonical sources.** [A parameter-independent cubic coefficient preserves the converse](../science/robustness.md#a-parameter-independent-cubic-coefficient-preserves-the-converse); [residual work states and coherent arithmetic](../science/robustness.md#residual-work-states-and-coherent-arithmetic); [exact tolerance of the four-photon protocol](../science/robustness.md#exact-tolerance-of-the-four-photon-protocol); [changes of estimation family](../science/robustness.md#changes-of-estimation-family).

### M29. The fixed-time Ising application

**Question.** How does the residue method transfer to a quadratic collective-spin spectrum without importing the Kerr query threshold?

**Target.** For a fixed absolutely continuous prior on the real coupling $`J`$, consider one uninterrupted evolution under $`H_N(J)=J\sum_{i\lt j}Z_iZ_j`$. Fixed known $`N`$ permits removal of the scalar term in $`2JS_z^2-JN/2`$. Even and odd particle-number subsequences give square and triangular spectra in phase coordinates $`2Jt`$ and $`4Jt`$. Each occupies only $`(p+1)/2`$ residues modulo an odd prime. CRT products and prior pushforward imply shrinking-window success tends to zero for every input and final POVM at fixed time and coupling convention.

**Prerequisites and story role.** [M20](#m20-cyclic-discrimination-from-occupied-residues), [M22](#m22-fixed-priors-heralding-and-confidence-at-the-threshold), [M26](#m26-duration-catalogs-and-changed-query-access). This tests the method on a second physical representation while retaining its own operational hypotheses.

**Connection.** Spectral degeneracy and ancillary systems can change coefficient vectors without adding frequency residues. The transfer concerns one fixed-time interrogation; it does not establish three- or four-use thresholds for spin controls or for an $`N`$-normalized coupling.

**Canonical sources.** [Spectrum and the two parity subsequences](../science/ising_application.md#spectrum-and-the-two-parity-subsequences); [the uniform confidence bound](../science/ising_application.md#uniform-confidence-bound); [transfer to a real coupling prior](../science/ising_application.md#transfer-to-a-real-coupling-prior); [the Belliardo–Gardner–Jiang–Clerk comparison](../references/RELATED_WORK.md#belliardo2026).

### M30. The complete arithmetic and operational synthesis

**Question.** Which conclusions survive each specified change of prior, access, photon promise, and physical control model?

**Target.** The complete account joins the known-phase threshold of three and unknown-common-phase threshold of four with their adaptive Haar floors, fixed-prior strong converses, and pointwise attaining constructions. Its supporting results distinguish exact exposure from a cap, fixed clocks from altered access, fixed priors from improving calibration, and ideal target-query counts from preparation and hardware resources. Standard quantum-information tools and imported number theory support the project-specific arithmetic classification. Analytical proofs establish universal claims; finite verification checks their concrete ingredients.

**Prerequisites and story role.** [M22](#m22-fixed-priors-heralding-and-confidence-at-the-threshold), [M25](#m25-exact-exposure-parity-and-the-five-use-consequence), [M26](#m26-duration-catalogs-and-changed-query-access), [M27](#m27-partial-calibration-and-the-unresolved-rate-gap), [M28](#m28-residual-cubic-phases-and-robustness), [M29](#m29-the-fixed-time-ising-application). This closes the narrative by connecting all result branches to the same complete-experiment model.

**Connection.** Generator growth determines a local variation scale, arithmetic determines which global frequency combinations exist, shared nuisance structure determines which coherence survives, and the resource and prior specification determines which theorem applies.

**Canonical sources.** [Principal results and their proof homes](../science/model.md#principal-results-and-their-proof-homes); [the resource comparison](../science/interpretation.md#a-resource-comparison); [relationship to general theory](../science/interpretation.md#relationship-to-general-theory); [evidence and the boundary of the account](../science/interpretation.md#evidence-and-the-boundary-of-the-account); [resources, priors, and the complete story](WATROUS_BRIDGE.md#resources-priors-and-the-complete-story).

