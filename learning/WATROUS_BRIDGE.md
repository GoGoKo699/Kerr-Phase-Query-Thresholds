# From Watrous to Kerr phase query thresholds

The educational anchor is **John Watrous, _The Theory of Quantum Information_ (2018)**. Use the [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/) and its [complete standard-layout author manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). All section and printed-page pointers below refer to that manuscript, whose preface is dated January 2018. The [bibliographic record](../references/RELATED_WORK.md#watrous2018) distinguishes this version from the published edition.

This bridge connects the source's finite-dimensional quantum-information language to the project's physical question: how many complete forward uses of an unknown Kerr gate suffice for an increasingly accurate **global** estimate? The [30 milestones](MILESTONES.md) organize the route. The authoritative statements and proofs remain in [the scientific model](../science/model.md) and its linked topic files.

Watrous supplies the language of registers, states, channels, measurements and discrimination. The phase-estimation reductions, arithmetic and control constructions require the separate derivations and primary research attributions linked here. Chapter 1 reviews mathematical prerequisites without proving all of them; the explanations below supply the particular connections the project needs. Reading the entire book is not a prerequisite for this route.

## Source map

The page column gives **section start pages**, not nonoverlapping page ranges. Printed page 1 is page 9 of the complete PDF. Chapter files are parts of the same selected source: [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), and the optional [Chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf).

| Needed idea | Watrous pointer; printed start page | Connection supplied here |
|---|---|---|
| Vectors, tensor products, spectra and norms | §§1.1.1–1.1.3; pp. 1, 8, 24; tensor products p. 6 | Occupations become basis labels; the relevant generator spectrum becomes a Fourier support set. |
| Convexity, measures and probability | §§1.2.1–1.2.2; pp. 35, 47 | Priors, nuisance averages and confidence events enter an operational estimation problem. |
| States, reductions and purification | §§2.1.2–2.1.3; pp. 61, 67; Theorem 2.10 p. 71 | Retained ancillas and work registers permit coherent protocol bookkeeping. |
| Channels and their representations | §§2.2.1–2.2.2; pp. 72, 77; Corollary 2.27 p. 89 | Parameter-independent processing preserves the query-generated frequency description. |
| Measurements | §§2.3.1–2.3.2; pp. 100, 105; Theorem 2.42 p. 109 | A finite POVM must normalize on its stated space and produce a complete estimate. |
| State discrimination | §§3.1.1–3.1.2; pp. 125, 132; Theorem 3.4 p. 128 | Fine phase estimation would distinguish a shifted cyclic grid of hypotheses. |
| Measurement stability | Proposition 3.5 p. 130; §3.2 p. 139; Theorem 3.33 p. 161 | Preparation errors must be converted to outcome or risk errors with consistent conventions. |
| Optional optimization language | §1.2.3 p. 53 | The project's explicit path-matrix calculation gives the required spectral certificate directly. |
| Optional invariant-measure background | §7.2.1 p. 408 | The circle average needed here follows from an elementary Fourier integral below. |

The source defines finite-outcome measurements. Its finite-dimensional Naimark theorem does not by itself justify a continuous phase POVM; the project supplies the integral normalization and an exact finite readout. Its unitary Haar measure in Chapter 7 is broader machinery than the uniform circle integral needed here. The physical loading interface and digital complexity estimates also need their own arguments.

## Notation and conventions

| Watrous or standard matrix notation | Repository notation and meaning |
|---|---|
| A column vector $`u`$, adjoint $`u^*`$, outer product $`uu^*`$ | $`\lvert u\rangle`$, $`\langle u\rvert`$, $`\lvert u\rangle\langle u\rvert`$; normalized vectors represent pure states. |
| $`\langle u,v\rangle=u^*v`$ | $`\langle u\mid v\rangle`$; the inner product is linear in its second argument. |
| A unitary $`U`$ and its induced channel | $`\rho\mapsto U\rho U^\dagger`$; a scalar phase of $`U`$ disappears from this channel. |
| Measurement effect $`\mu(y)`$ | $`E_y\ge0`$, with $`\sum_yE_y=I`$ and $`p(y)=\mathrm{Tr}(E_y\rho)`$. An effect alone does not specify a postmeasurement state. |
| Trace norm $`\|\rho-\sigma\|_1`$ | Watrous calls this the trace distance on p. 34. When using $`D=\tfrac12\|\rho-\sigma\|_1`$, an event-probability difference is at most $`D`$. |
| Fidelity, Definition 3.11 p. 139 | $`F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$ is unsquared; for pure states it is the magnitude of the overlap. |
| Identity on a specified register | $`I_{\mathcal C}`$ for the code, or $`I_{35}`$ for the full four-photon sector; these are different operators. |

The photon cap $`N`$, query count $`q`$, cumulative linear exposure $`s`$, nonlinear frequency $`g`$, and consecutive-band length $`L`$ are distinct. A tensor factor need not be a separate query. A large matrix dimension is not a count of calls, and a cumulative exposure in a sequential history is not automatically an initial photon number.

## From a Fock mode to a finite register

A photon-number eigenstate satisfies $`\hat n|n\rangle=n|n\rangle`$. The Kerr generator is the triangular number

```math
T(n)=\frac{n(n-1)}2,
\qquad
T(0),T(1),T(2),T(3),T(4)=0,0,1,3,6.
```

At a fixed queried occupation cap, the relevant mode has basis $`|0\rangle,\ldots,|N\rangle`$. Watrous's finite-register framework applies at each such $`N`$; the dimension can grow along the asymptotic sequence. Tensor products describe several modes and ancillas, while the physical resource condition selects an allowed subspace of that product.

For example, four modes with exactly four photons have $`\binom{4+4-1}{4-1}=35`$ occupation basis states. A code using four of those states is isomorphic to a four-dimensional register, but implementing a logical unitary or measurement requires specifying its action in the physical space. This distinction connects §§1.1 and 2.1 to [the finite protocol](../science/four_photon_protocol.md).

For upper bounds, the total photon cap includes any bypass photons when a bypass is used. For adaptive lower bounds, the permitted class is larger: each queried mode has occupation at most $`N`$, and the controls and ancillas can be arbitrary. A converse proved for that larger class also covers the more restricted construction. The resource statement in [the model](../science/model.md#query-and-photon-resources) makes the comparison precise.

## One call and a global estimate

One call acts diagonally:

```math
U_{\theta,\beta}|n\rangle
=e^{-i\theta T(n)-i\beta n}|n\rangle.
```

The same $`\beta`$ occurs in every call. A single occupation eigenstate acquires only a scalar phase and reveals neither parameter. Superposing occupations creates relative phases: $`(|0\rangle+|2\rangle)/\sqrt2`$ acquires relative factor $`e^{-i(\theta+2\beta)}`$. If $`\beta`$ is unknown, that observation does not isolate $`\theta`$. A superposition of occupations 0 and 1 carries no Kerr phase because both have $`T(n)=0`$.

Even with known $`\beta`$, a large frequency difference need not identify a global phase. A two-frequency probe with difference $`G`$ has the same encoded state when $`\theta`$ changes by $`2\pi/G`$. Increasing $`G`$ produces finer repeated fringes while leaving many globally indistinguishable possibilities. The complete estimation task includes resolving those possibilities under the declared prior.

Watrous's states and channels make this operational: the experiment supplies a parameter-dependent output state, and a measurement maps it to a reported estimate. Every unknown-gate call used for that report, including preliminary sensing and repeated probes, contributes to $`q`$. Interleaved known processing can be represented by channels, or coherently with retained registers using purification and dilation. Those representation theorems do not supply a physical implementation for free, nor do they prove the query-support restriction; that is the separate [adaptive Fourier reduction](../science/query_thresholds.md#adaptive-fourier-reduction).

## Why a common linear phase creates sectors

For a parallel occupation tuple $`\boldsymbol n=(n_1,\ldots,n_q)`$, define

```math
s=\sum_{j=1}^q n_j,
\qquad
g=\sum_{j=1}^q T(n_j).
```

Its phase is $`e^{-i\theta g-i\beta s}`$. Averaging a uniform unknown $`\beta`$ removes cross terms with different $`s`$ because

```math
\int_0^{2\pi}e^{-i\beta(s-s')}\frac{d\beta}{2\pi}
=\begin{cases}1,&s=s',\\0,&s\ne s'.\end{cases}
```

Coherences **within** a fixed-$`s`$ sector survive. On that sector the nuisance contributes one common scalar phase, so the Kerr frequencies can remain observable. This is block dephasing, related to the basis-dephasing examples in Watrous §2.2.3, pp. 94–95, but with a larger surviving block whenever several tuples have the same total.

For adaptive protocols, coherent expansion over query histories gives the same integer labels $`(g,s)`$. The coefficient vectors need not be orthogonal, and the weight of an averaged sector may depend on $`\theta`$. The canonical converse retains those possibilities. It does not replace an adaptive protocol by an unjustified orthogonal parallel code.

The word **common** is essential. Independent uniform phases $`\beta_j`$ at each call enforce equality of each history occupation $`n_j=n'_j`$, hence equality of the corresponding Kerr phase. Their averaged channel carries no $`\theta`$ information. Replacing one static nuisance by fresh dephasing at each use therefore changes the estimation task. See [why sharing the linear phase is essential](../science/interpretation.md#why-sharing-the-linear-phase-is-essential).

## From loss to frequency adjacency

The shortest angular error $`d(\hat\theta,\theta)`$ lies in $`[0,\pi]`$. The chosen sine loss and its relation to wrapped squared error are

```math
\ell(\hat\theta-\theta)=4\sin^2\!\left(\frac{\hat\theta-\theta}{2}\right)
=2-2\cos(\hat\theta-\theta),
\qquad
\frac4{\pi^2}d^2\le\ell\le d^2.
```

Risk is $`R=\mathbb E\ell`$; wrapped RMS is $`\sqrt{\mathbb E d^2}`$; confidence at radius $`\delta`$ is $`\Pr(d<\delta)`$. The inequalities give corresponding risk and RMS exponents. A positive risk floor alone does not imply that confidence vanishes in every shrinking window: a distribution may put substantial mass near zero and the rest at large error. The project's confidence theorem needs its separate discrimination argument.

For an orthonormal representative code with consecutive frequencies, ignore a common frequency offset and write

```math
|\psi_\theta\rangle=\sum_{j=0}^{L-1}a_j e^{-ij\theta}|e_j\rangle,
\qquad a_j\ge0,\qquad\sum_j a_j^2=1.
```

The canonical phase readout gives

```math
R=2-2\sum_{j=0}^{L-2}a_ja_{j+1}.
```

Only adjacent frequencies enter because the loss has just the constant and first Fourier harmonics. Let $`A_L`$ be the path matrix with ones immediately above and below the diagonal. Then $`a^TA_La=2\sum_j a_ja_{j+1}`$. Its largest eigenvalue and normalized maximizing vector are

```math
\lambda_{\max}=2\cos\frac\pi{L+1},
\qquad
a_j=\sqrt{\frac2{L+1}}\sin\frac{(j+1)\pi}{L+1}.
```

Thus $`R_L=2-2\cos(\pi/(L+1))`$. If the frequency set has holes, its adjacency graph splits into paths; the longest consecutive run controls this optimization. A large range or many scattered frequencies cannot substitute for a long run. For $`L=\Theta(N^2)`$, the risk is $`\Theta(N^{-4})`$.

The [longest-run proof](../science/query_thresholds.md#the-longest-consecutive-run-bound) extends the lower bound to arbitrary adaptive coefficient vectors. Its [finite readout](../science/query_thresholds.md#a-finite-readout-with-constant-pointwise-risk) supplies constant pointwise risk for an actual orthogonal code. The covariant optimization and sine-state idea are established ingredients, attributed to [D'Ariano–Macchiavello–Sacchi](../references/RELATED_WORK.md#dariano1998) and [van Dam et al.](../references/RELATED_WORK.md#vandam2007).

## A complete four-photon example

Take one call on each of four modes and use the following orthonormal code inside the 35-state sector:

| Label | Occupations | Total $`s`$ | Kerr frequency $`g`$ |
|---|---|---:|---:|
| $`e_0`$ | $`\lvert1111\rangle`$ | 4 | 0 |
| $`e_1`$ | $`\lvert2110\rangle`$ | 4 | 1 |
| $`e_2`$ | $`\lvert0220\rangle`$ | 4 | 2 |
| $`e_3`$ | $`\lvert3100\rangle`$ | 4 | 3 |

The nuisance factor is $`e^{-4i\beta}`$ throughout, so it cancels at every fixed parameter value without a nuisance average. Prepare amplitudes $`(a,b,b,a)`$, where

```math
a=\sqrt{\frac{5-\sqrt5}{20}},
\qquad
b=\sqrt{\frac{5+\sqrt5}{20}},
\qquad 2a^2+2b^2=1.
```

After encoding and dropping the common nuisance phase,

```math
|\psi_\theta\rangle
=a|e_0\rangle+b e^{-i\theta}|e_1\rangle
+b e^{-2i\theta}|e_2\rangle+a e^{-3i\theta}|e_3\rangle.
```

For $`\ell=0,\ldots,7`$, set

```math
\phi_\ell=\frac{2\pi\ell}{8},
\qquad
|v_\ell\rangle=\sum_{j=0}^{3}e^{-ij\phi_\ell}|e_j\rangle,
\qquad
E_\ell=\frac18|v_\ell\rangle\langle v_\ell|.
```

The finite Fourier identity gives $`\sum_\ell E_\ell=I_{\mathcal C}`$ on the code $`\mathcal C`$. To complete the same eight labels on the full sector, define

```math
E_\ell^{\mathrm{full}}
=E_\ell+\delta_{\ell0}(I_{35}-\Pi_{\mathcal C}).
```

These effects are positive and sum to $`I_{35}`$. Outside-code detection records are assigned to label zero; nothing is postselected away. On the ideal code this addition has zero probability. Report $`\hat\theta=+\phi_\ell`$, with

```math
p(\ell\mid\theta)
=\frac18\left|\sum_{j=0}^3a_j e^{ij(\phi_\ell-\theta)}\right|^2,
\qquad (a_0,a_1,a_2,a_3)=(a,b,b,a).
```

The minus sign in the seed vector is what produces the difference $`\phi_\ell-\theta`$ in the Born amplitude. Fourier orthogonality verifies both normalization and, after multiplying by the sine loss, the constant risk

```math
R_4=2-2(2ab+b^2)=\frac{3-\sqrt5}{2}.
```

This is smaller than the three-use Haar lower bound $`2-\sqrt2`$. It is a finite separation; the asymptotic four-use theorem requires a growing consecutive band, proved independently.

The readout has a concrete implementation. Choose an offset $`\alpha=0`$ or $`\pi/4`$ with equal probability, apply $`Z(\alpha)=\mathrm{diag}(e^{ij\alpha})`$, then the Fourier matrix

```math
(F_+)_{mj}=\frac12e^{2\pi i m j/4},\qquad m,j=0,1,2,3,
```

and measure the code label $`m`$. Report $`\phi=\alpha+2\pi m/4`$. The sign convention is explicit, and the two four-point grids give the eight effects above. The [physical construction](../science/four_photon_protocol.md#logical-phases-and-an-explicit-fourier-compilation) specifies selected pair gates and an echoed logical rotation on the full sector. These nonlinear calibrated controls and their costs are additional assumptions. An abstract four-dimensional Fourier matrix alone is not a physical gate construction.

## From fine estimation to finite discrimination

Watrous §3.1 asks how well a measurement can distinguish an ensemble of known states. For the converse, select $`M`$ equally spaced target phases

```math
\theta_k=\alpha+\frac{2\pi k}{M},\qquad k=0,\ldots,M-1.
```

Give the offset $`\alpha`$ to the estimator. This extra information can only help. If its angular error is less than $`\pi/M`$, rounding to the nearest grid point identifies $`k`$. Fine estimation would therefore solve a finite discrimination problem.

On this grid, frequencies with the same residue modulo $`M`$ have the same dependence on $`k`$. If each nuisance sector occupies at most $`D`$ residues, the [cyclic residue lemma](../science/global_confidence.md#a-cyclic-residue-bound) bounds Haar-averaged success by $`D/M`$. Its Cauchy–Schwarz proof keeps nonorthogonal coefficient vectors and the actual sector weights. Merely counting a physical Hilbert-space dimension would not establish the required adaptive bound.

The modulus is chosen for an arithmetic obstruction, not tied to $`N`$. Products of suitable prime squares make the occupied fraction arbitrarily small, uniformly in the photon cap. Once a modulus is fixed, every sufficiently small error window lies below $`\pi/M`$. This order of choices proves

```math
\lim_{\delta\downarrow0}\ \sup_{N,\,\mathrm{allowed\ protocols}}
\Pr_{\mathrm{Haar}}(d<\delta)=0
```

below the threshold. The full theorem and its attribution to established discrimination machinery are in [global confidence](../science/global_confidence.md).

For a fixed absolutely continuous prior density $`f`$ relative to uniform measure, split $`f`$ at a constant $`C`$. An event probability is at most its Haar probability times $`C`$, plus $`\int_{f>C}f`$. The tail tends to zero as $`C`$ grows; then the Haar converse handles the bounded part. This includes fixed correlated target–nuisance densities. It does not assert a uniform result for singular promises or priors concentrating with $`N`$.

## Arithmetic that the quantum source does not supply

The quantum reduction leaves a concrete integer problem: which sums of triangular numbers occur, and which survive at a fixed total occupation?

With known linear phase, one use has no run longer than two. For two uses, the triangular residues modulo 9 are $`\{0,1,3,6\}`$; their pairwise sums miss residues 5 and 8. This bounds the longest run by five, and a matching finite run exists. With three uses, Gauss's three-triangular-number theorem supplies a consecutive band whose length grows quadratically within the photon cap. The exact Haar floors are therefore $`1`$ and $`2-\sqrt3`$ below the three-use threshold. See [the known-phase proof](../science/query_thresholds.md#a-known-linear-phase).

With an unknown common phase, arithmetic must be evaluated within fixed-$`s`$ sectors. For three occupations, suitable integer differences $`u,v`$ give

```math
3g+\frac{3s-s^2}{2}=u^2-uv+v^2.
```

The right side is an Eisenstein norm. Its missing class modulo 4 bounds the consecutive run and gives the three-use floor $`2-\sqrt2`$. Its stronger prime-square exclusions drive the vanishing-confidence theorem: for primes $`p\equiv2\pmod3`$, a norm cannot have $`p`$-adic valuation exactly one. Excluding those residues modulo $`p^2`$ leaves a fraction at most $`1-1/p+1/p^2`$. The Chinese remainder theorem multiplies these fractions across distinct primes, and their product tends to zero. The known-phase two-use proof uses the corresponding Gaussian norm and primes $`p\equiv3\pmod4`$.

For four uses, choose an odd exposed total $`s\le N`$. The construction transforms the representation problem into three squares for

```math
Q=8g+4s-s^2\equiv3\pmod8,
```

then chooses signs and inverts the transform to obtain nonnegative occupations. This gives a consecutive band of length $`s^2/24+O(s)`$. Legendre's theorem provides the existence input; the project's positivity and photon accounting complete the construction. The [four-use proof](../science/query_thresholds.md#four-uses-with-an-unknown-common-linear-phase) states the precise interval.

The representation theorems, prime-progression result, Chinese remainder theorem and binary-form counting asymptotic are [attributed mathematical ingredients](../references/RELATED_WORK.md#classical-arithmetic-used-in-the-proofs). Watrous supplies none of these gate-specific evaluations. The allocation of 14 background and 16 research milestones reflects the need to understand both the operational quantum model and this arithmetic before assembling the full result.

## Resources, priors and the complete story

The [model](../science/model.md) joins the mechanism to its exact claim: three calls suffice with known $`\beta`$, and four with a common unknown $`\beta`$. Below threshold, every shrinking confidence window has vanishing success for each fixed absolutely continuous prior. At threshold, the constructive risk is pointwise $`O(N^{-4})`$, giving wrapped RMS $`O(N^{-2})`$. Any chosen fixed confidence follows at a suitable constant multiple of $`N^{-2}`$; confidence tending to one is proved when $`\delta_N\to0`$ and $`N^2\delta_N\to\infty`$.

One useful connection to Watrous's reductions and purifications concerns the decoded preparation state. For an error that preserves each frequency label, write

```math
|\Psi_\theta\rangle=\sum_j a_j e^{-ij\theta}|j\rangle|\chi_j\rangle,
\qquad \|\chi_j\|=1.
```

Tracing out the work register multiplies the index coherence between $`j`$ and $`k`$ by $`\langle\chi_k|\chi_j\rangle`$. The same adjacent-frequency calculation gives

```math
R-R_{\mathrm{ideal}}
=\sum_j a_ja_{j+1}\|\chi_{j+1}-\chi_j\|^2.
```

Thus nearby normalized work states give a quadratic task-specific error bound. This conclusion uses the displayed structure; for a generic state perturbation, bounded loss only gives $`|R(\rho)-R(\sigma)|\le4D(\rho,\sigma)`$. The [full preparation error argument](../science/robustness.md#residual-work-states-and-coherent-arithmetic) explains why the constructive algorithm has the required form.

Several supporting results determine how to interpret the full theorem:

| Connection | Consequence and canonical account |
|---|---|
| State preparation versus query complexity | The [four-use coherent preparation construction](../science/coherent_preparation.md) uses $`O(N\mathrm{polylog}N)`$ digital work without QRAM and a separate coherent number-to-Fock interface. Only known preparation operations are inverted. |
| A photon cap versus exactly exposed photons | The four-use upper bound chooses an odd total at most $`N`$. Requiring exactly $`N`$ exposed photons for every parity has a [five-use asymptotic threshold](../science/query_thresholds.md#exactly-even-exposed-photon-totals). |
| A fixed clock versus changed gate access | A [fixed finite positive commensurate duration catalog](../science/timing_and_priors.md#a-fixed-finite-positive-commensurate-duration-catalog) preserves the stated converse. A shrinking duration or an inverse call enables the separate [access constructions](../science/access_variants.md). |
| A fixed prior versus improving calibration | For a fixed absolutely continuous Kerr prior and an independent uniform nuisance interval of known center and width $`w_N`$, three-use consistency holds exactly when $`w_N\to0`$. The [quantitative sufficient and necessary rates](../science/timing_and_priors.md#the-quantitative-gap) leave an unresolved gap. |
| An independent nuisance term versus a changed target generator | An independent cubic phase preserves the converse through a simulation argument. Its [upper-bound tolerance](../science/robustness.md) requires additional control or decay assumptions. A higher term multiplied by $`\theta`$ changes the estimation family. |
| A shared spectral obstruction versus a new physical protocol | The [Ising application](../science/ising_application.md) transfers the obstruction to one uninterrupted fixed-time interrogation with arbitrary input. It does not establish a four-use Ising construction. |

The first phase culminates at M14 with the complete estimation model. The second culminates at M30 with the theorem, its proof mechanism, resources and boundaries understood together. Use the [milestone map](MILESTONES.md) for this progression and [interpretation](../science/interpretation.md) for the connected scientific narrative. The [verification suite](../verification/README.md) checks finite arithmetic and control claims; the universal and asymptotic statements depend on the written proofs and their cited inputs.
