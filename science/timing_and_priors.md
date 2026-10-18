# Timing access and partial calibration

Two assumptions delimit the Kerr query threshold: which durations count as available gate uses, and how much the linear phase is known before sensing. A fixed finite catalog of positive commensurate durations preserves the subthreshold vanishing-confidence theorem. A nuisance prior that narrows with the photon budget can instead restore three-use consistency.

For the original three-use fixed gate, suppose the Kerr phase has any fixed absolutely continuous prior and the independent linear phase is uniform on an interval of known center and width $`w_N`$. Consistency is possible if and only if $`w_N\to0`$. The quantitative bounds proved here are:

| Estimation objective with three fixed uses | Sufficient calibration width | Proved necessary width |
|---|---|---|
| Consistency | $`w_N\to0`$ | $`w_N\to0`$ |
| Wrapped RMS error $`O(N^{-2})`$ | $`w_N=O(N^{-3})`$ | $`w_N=O((\log N)^{-1/2})`$ |
| Fixed high confidence at a suitable constant times $`N^{-2}`$ | $`w_N=O(N^{-1})`$ | $`w_N=O((\log N)^{-1/2})`$ for any confidence bounded away from zero at a fixed constant times $`N^{-2}`$ |

The last two rows do not match. They are sufficient constructions and necessary bounds, not a sharp calibration-rate threshold.

The [model](model.md) remains canonical. Achievable protocols below use a total sensing-plus-reference photon budget at most $`N`$. Quantitative adaptive converses allow the larger class with occupation at most $`N`$ at every query. An initial photon count without this occupation condition, or a mean energy bound by itself, is not the quantitative hypothesis.

## A fixed finite positive commensurate duration catalog

Let $`\mathcal A`$ be a nonempty finite set of positive integers, fixed independently of the photon cap and the requested resolution. In a common physical time unit, the available exposure with label $`a\in\mathcal A`$ is

```math
U_a(\theta,\beta)
=\exp[-ia\theta T(\hat n)-ia\beta\hat n].
\tag{D}
```

This also describes a fixed finite catalog of positive rational durations after choosing a common time unit. Both Hamiltonian coefficients scale with duration. The physical coefficients and their prior must be specified before such a rescaling: an opaque gate whose phases are only given modulo $`2\pi`$ does not, by itself, define its fractional powers.

Count each exposure as one use, including any adaptive selection of its duration. The total query count is at most three. Classical feedback and coherent choices among the allowed duration labels are included. There are no controls during a single uninterrupted exposure in this model.

**Catalog theorem.** For an unknown common linear phase and every fixed joint absolutely continuous prior, success in any shrinking Kerr-phase window tends to zero uniformly over all finite caps and all protocols with at most three uses from the catalog. For a known linear phase, the analogous conclusion holds for at most two uses and every fixed absolutely continuous Kerr-phase prior.

### A weighted three-use identity

Fix an ordered duration schedule $`(a,b,c)`$ and a query history $`(n_1,n_2,n_3)`$. Shorter histories can be padded with vacuum at any allowed positive duration. Set

```math
\begin{aligned}
A_0&=a+b+c,\\
s&=an_1+bn_2+cn_3,\\
g&=aT(n_1)+bT(n_2)+cT(n_3),\\
u&=n_1-n_3,\qquad v=n_2-n_3.
\end{aligned}
```

Expanding the weighted variance gives

```math
\begin{aligned}
2A_0g+A_0s-s^2
&=ab(n_1-n_2)^2+ac(n_1-n_3)^2+bc(n_2-n_3)^2\\
&=a(b+c)u^2-2abuv+b(a+c)v^2\\
&=:Q_{a,b,c}(u,v).
\end{aligned}
\tag{W}
```

This positive definite binary quadratic form has matrix determinant

```math
D_{a,b,c}=abc(a+b+c)>0
```

and discriminant $`-4D_{a,b,c}`$.

Let $`p`$ be an odd prime not dividing $`2D_{a,b,c}`$ such that

```math
\left(\frac{-D_{a,b,c}}p\right)=-1.
\tag{I}
```

Here the parentheses denote a Legendre symbol. Over an odd finite field, a nondegenerate binary quadratic form has a nonzero zero exactly when its discriminant is a square; completing the square proves this criterion. Condition (I) therefore implies

```math
p\mid Q_{a,b,c}(u,v)
\quad\Longrightarrow\quad
p\mid u,\ p\mid v
\quad\Longrightarrow\quad
p^2\mid Q_{a,b,c}(u,v).
```

The coefficient $`2A_0`$ in (W) is invertible modulo $`p^2`$, since $`A_0`$ divides $`D_{a,b,c}`$. For every fixed weighted exposure $`s`$, the schedule's possible Kerr frequencies therefore omit $`p-1`$ residue classes modulo $`p^2`$.

### One prime progression works for every schedule

There are at most $`|\mathcal A|^3`$ ordered three-use schedules. Let $`D_*`$ be a positive common multiple of all their determinants. Every prime

```math
p\equiv-1\pmod{4D_*}
\tag{AP}
```

satisfies (I) for every schedule.

To verify this, $`p\equiv3\pmod4`$, so $`(-1/p)=-1`$. For an odd prime factor $`\ell`$ of any determinant, quadratic reciprocity and $`p\equiv-1\pmod\ell`$ give

```math
\left(\frac{\ell}{p}\right)
=\left(\frac{p}{\ell}\right)
 (-1)^{(\ell-1)/2}
=\left(\frac{-1}{\ell}\right)
 (-1)^{(\ell-1)/2}
=1.
```

If a determinant has a factor two, then $`D_*`$ is even and (AP) gives $`p\equiv7\pmod8`$, so $`(2/p)=1`$ as well. Thus $`(D_{a,b,c}/p)=1`$ for every schedule and $`(-D_{a,b,c}/p)=-1`$. These primes also avoid every determinant.

The progression in (AP) is reduced, so its reciprocal-prime sum diverges. This is an established arithmetic-progression result; see [NIST DLMF](../references/RELATED_WORK.md#dlmf27).

### Taking the union of adaptive schedules

For a finite set $`\mathcal P`$ of primes in (AP), let

```math
M=\prod_{p\in\mathcal P}p^2,
\qquad
\rho_{\mathcal P}
=\prod_{p\in\mathcal P}
\left(1-\frac1p+\frac1{p^2}\right).
```

At each fixed weighted $`s`$, each schedule occupies at most $`M\rho_{\mathcal P}`$ frequency residues modulo $`M`$. Their union occupies at most

```math
\min\!\left\{M,\ |\mathcal A|^3M\rho_{\mathcal P}\right\}
```

residues. The bound does not require the occupied residue sets to be disjoint or to be the same for different schedules.

Purifying a controlled or adaptive schedule choice gives the same type of Fourier expansion as in the [identical-gate proof](query_thresholds.md#adaptive-fourier-reduction), now with frequencies $`g=\sum_j a_jT(n_j)`$ and $`s=\sum_j a_jn_j`$. The coefficient vectors may coherently combine schedules, but their support lies inside the union just counted. Haar averaging the common $`\beta`$ groups equal actual weighted exposures $`s`$, irrespective of which schedule produced them.

The [cyclic residue bound](global_confidence.md#a-cyclic-residue-bound) therefore gives

```math
\Pr_{\rm Haar}\{d<\pi/M\}
\leq\min\!\left\{1,\ |\mathcal A|^3\rho_{\mathcal P}\right\}.
\tag{CU}
```

The catalog size is a fixed constant and $`\rho_{\mathcal P}\to0`$. This proves the uniform shrinking-window converse. The [density-truncation argument](global_confidence.md#every-fixed-absolutely-continuous-joint-prior) transfers it to every fixed joint absolutely continuous prior.

No coprimality condition on $`a,b,c`$ is needed. The chosen primes avoid their finite set of bad divisors.

### The known-linear-phase catalog

For a two-use schedule $`(a,b)`$, the relevant identity is

```math
8g+a+b
=a(2n_1-1)^2+b(2n_2-1)^2.
\tag{KW}
```

The binary form on the right has determinant $`ab`$. Choose a common multiple of these determinants over all schedules and use the same progression construction. At every selected prime, divisibility by $`p`$ forces divisibility by $`p^2`$, and the coefficient eight is invertible. Each schedule omits $`p-1`$ frequency residues modulo $`p^2`$. A union over at most $`|\mathcal A|^2`$ schedules, followed by the cyclic lemma and one-dimensional density truncation, proves the known-phase assertion.

### Limits of the catalog theorem

The catalog, its finite cardinality, and its positive common time unit remain fixed as $`N`$ and the resolution change. A growing catalog, an unbounded set of integer durations, arbitrary incommensurate durations, inverse exposures, or controls during the evolution requires a separate argument. A positive lower bound on duration by itself is not the hypothesis just proved.

This is a converse for the enlarged catalog. The exact numerical Haar floors of the identical-gate model need not remain the same. When the original primitive unit-duration gate is present, the known three-use and unknown four-use constructions remain available, so the extra fixed positive commensurate durations do not lower the corresponding activation thresholds. A catalog without that primitive need not admit the same sufficiency statement; a common divisor of all weights can, for example, leave an exact phase alias.

Time-weighted exposure is also a separate resource from the number of gate calls. The theorem keeps the duration catalog fixed and makes no claim that different schedules have equal interaction time. [Access variants](access_variants.md) gives explicit consequences of changing the timing or inverse-query access.

## Three uses with a shrinking nuisance interval

Return to three identical uses of the primitive fixed gate. Let $`\theta`$ have a fixed absolutely continuous prior on the circle. Independently, let $`\beta`$ be uniform on an interval of width

```math
0\leq w_N\leq2\pi
```

and known center $`\beta_0`$. The interval may cross the angular origin. A known number rotation compensates its center, so use a centered representative $`b=\beta-\beta_0\in[-w_N/2,w_N/2]`$. Width zero means an exactly known phase.

The constructive bounds below are pointwise in $`\theta`$ after averaging over the named interval prior for $`b`$. They therefore hold for every Kerr-phase prior. The explicit finite-cap converse formulas are first stated for uniform $`\theta`$; fixed absolutely continuous Kerr priors inherit the necessary rates through density truncation.

### An effective photon budget

Choose an integer $`K\leq N`$ and define

```math
M=\left\lfloor\frac{K(K-3)}6\right\rfloor.
```

For large enough $`K`$, the [three-triangular construction](query_thresholds.md#three-uses) supplies a representative $`\mathbf n(g)`$ for every $`0\leq g\leq M`$ with total $`s_g\leq K`$. Let

```math
|g\rangle
=|\mathbf n(g)\rangle_{\rm sense}
 |K-s_g\rangle_{\rm bypass},
\qquad
c_g=\sqrt{\frac{2}{M+2}}
     \sin\frac{(g+1)\pi}{M+2}.
```

The sensing and bypass modes contain exactly $`K`$ photons in every component. The available cap is $`N`$; unused photons need not be interrogated. After the three uses, the code state is

```math
|\psi_{\theta,b}\rangle
=\sum_{g=0}^{M}c_g e^{-ig\theta-is_gb}|g\rangle.
\tag{PC}
```

Use the [finite padded Fourier POVM](query_thresholds.md#a-finite-readout-with-constant-pointwise-risk) with any $`J\geq M+2`$ outcomes. It can equivalently be implemented by two offset Fourier grids. This construction uses ideal permitted preparation and readout on the specified representatives; the present argument does not assign a gate count to the three-triangular preparation interface.

### Exact risk under the interval prior

Write $`\Delta s_g=s_{g+1}-s_g`$ and define $`\mathrm{sinc}x=\sin x/x`$, with value one at zero. Fourier orthogonality leaves only adjacent frequencies in the first error harmonic. At a fixed $`b`$, the cosine score is

```math
\sum_{g=0}^{M-1}c_gc_{g+1}\cos(b\Delta s_g),
```

independent of $`\theta`$. Averaging $`b`$ uniformly gives the exact risk

```math
\begin{aligned}
R(K,w)
&=R_0(K)
 +2\sum_{g=0}^{M-1}c_gc_{g+1}
 \left[1-\mathrm{sinc}
 \left(\frac{w\Delta s_g}{2}\right)\right],\\
R_0(K)
&=2\left[1-\cos\frac{\pi}{M+2}\right].
\end{aligned}
\tag{SR}
```

The ideal risk obeys $`R_0(K)=O(K^{-4})`$. Since

```math
1-\mathrm{sinc}x
=\int_0^1[1-\cos(tx)]\,dt
\leq\frac{x^2}{6},
```

and $`|\Delta s_g|\leq K`$, equation (SR) yields

```math
R(K,w)
\leq R_0(K)
 +\frac{w^2}{12}\sum_{g=0}^{M-1}c_gc_{g+1}(\Delta s_g)^2
\leq C K^{-4}+\frac{w^2K^2}{12}.
\tag{RB}
```

The final step uses $`\sum_gc_gc_{g+1}=\cos[\pi/(M+2)]\leq1`$.

As $`N\to\infty`$ and $`w=w_N\to0`$, choose $`K`$ of order

```math
\min\{N,w^{-1/3}\},
```

with $`K=N`$ when $`w=0`$. Integer rounding is immaterial once $`K\to\infty`$. Then

```math
R=O(N^{-4}+w_N^{4/3}),
\qquad
\sqrt{\mathbb E d^2}
=O(N^{-2}+w_N^{2/3}).
\tag{RM}
```

In particular, $`w_N=O(N^{-3})`$ suffices for wrapped RMS error $`O(N^{-2})`$. Any width sequence tending to zero suffices for consistency. The effective budget $`K`$ is a design choice balancing this construction's two errors; it is not a necessary limit on usable photons in every protocol.

### A stronger sufficient rate for fixed confidence

For the code in (PC), let

```math
S=\sum_gs_g|g\rangle\langle g|,
\qquad
\rho_w=\mathbb E_b[e^{-ibS}\rho_0e^{ibS}],
```

where $`\rho_0`$ is the state at $`b=0`$ for a fixed $`\theta`$. The spectral range of $`S`$ is at most $`K`$. Shift it by a scalar so that $`\|S\|_\infty\leq K/2`$; this does not change its conjugation channel. For any density matrix $`\rho`$,

```math
\|[S,[S,\rho]]\|_1
\leq4\|S\|_\infty^2\|\rho\|_1
\leq K^2.
```

Taylor's integral remainder therefore gives

```math
\|e^{-ibS}\rho_0e^{ibS}
  -\rho_0-b\rho'_0\|_1
\leq\frac{b^2K^2}{2}.
```

The centered interval has $`\mathbb E b=0`$ and $`\mathbb E b^2=w^2/12`$. Averaging cancels the linear term, so

```math
\|\rho_w-\rho_0\|_1\leq\frac{w^2K^2}{24}.
\tag{TD}
```

Any measurement event changes in probability by at most half this trace norm. The bound is uniform in $`\theta`$, since its encoding commutes with $`S`$. Combining (TD) with the ideal risk tail bound gives, for $`0<\delta\leq\pi`$,

```math
\begin{aligned}
\Pr_w\{d<\delta\}
&\geq
1-\frac{R_0(K)}{4\sin^2(\delta/2)}
 -\frac{w^2K^2}{48}\\
&\geq
1-\frac{C}{K^4\delta^2}
 -\frac{w^2K^2}{48}.
\end{aligned}
\tag{CB}
```

Fix a failure target $`0<\varepsilon<1`$. Choose

```math
K=\left\lfloor\min\{N,c_\varepsilon/w\}\right\rfloor
```

with $`c_\varepsilon`$ small enough that the last term in (CB) is at most $`\varepsilon/2`$. Then choose $`\delta=C_\varepsilon/K^2`$ with $`C_\varepsilon`$ large enough to make the ideal failure at most $`\varepsilon/2`$. In the asymptotic regime $`w_N\to0`$, this gives

```math
\Pr_w\{d<\delta\}\geq1-\varepsilon,
\qquad
\delta=O_\varepsilon\!\left(\max\{N^{-2},w_N^2\}\right).
\tag{FC}
```

For width $`w_N\leq B/N`$, a constant fraction of the available photons suffices, with that fraction depending on $`B`$ and $`\varepsilon`$. Therefore $`w_N=O(N^{-1})`$ suffices for every fixed high-confidence target at an appropriate constant times $`N^{-2}`$.

It also suffices for confidence tending to one in every shrinking window wider than that scale by a diverging factor. Suppose

```math
w_N\leq B/N,\qquad
\delta_N\to0,\qquad
A_N=N^2\delta_N\to\infty.
```

Choose

```math
K_N=\left\lfloor\frac{N}{A_N^{1/4}}\right\rfloor.
```

Then $`K_N\to\infty`$, $`K_N\leq N`$ eventually, and the two failure terms in (CB) are respectively $`O(A_N^{-1})`$ and $`O(A_N^{-1/2})`$. Both vanish. This confidence statement does not give wrapped RMS error $`O(N^{-2})`$ at width $`O(N^{-1})`$, nor confidence tending to one at a fixed multiple of $`N^{-2}`$.

## The exact qualitative calibration criterion

For the independent uniform-interval nuisance family just specified and a fixed absolutely continuous Kerr-phase prior,

```math
\boxed{
\text{Three-use consistency is possible}
\quad\Longleftrightarrow\quad
w_N\longrightarrow0.
}
\tag{IFF}
```

The forward construction follows from (RM).

For necessity, suppose $`w_N`$ does not tend to zero. There is then a subsequence with $`w_N\geq w_*>0`$. Relative to uniform measure on the nuisance circle, each interval prior has density at most $`2\pi/w_*`$, uniformly over this subsequence and regardless of its center.

Let $`F_3(\delta)`$ be the Haar success supremum from the [strong converse](global_confidence.md#the-uniform-shrinking-window-theorem). For uniform $`\theta`$, interval-prior success is at most $`(2\pi/w_*)F_3(\delta)`$. For another fixed Kerr prior, let $`f`$ be its density relative to uniform circle measure. For every fixed cutoff $`C>0`$,

```math
P_{f,w_N}^{\Pi}(\delta)
\leq
C\frac{2\pi}{w_*}F_3(\delta)
+\int_{\{f>C\}} f\,d\mu_\theta .
```

First send $`\delta\to0`$, then $`C\to\infty`$. Success in any shrinking window tends to zero along the subsequence, uniformly over protocols. Consistency would instead allow a sufficiently slowly shrinking window with success tending to one, a contradiction.

Equivalently, if sine risk tended to zero, Markov's inequality would provide such a shrinking high-confidence window. Because the loss is bounded and vanishes only at zero angular distance, sine-risk convergence and convergence in probability are equivalent here.

The Kerr prior must be fixed and absolutely continuous for this necessity proof. A known exact Kerr phase or an independently shrinking Kerr prior is a different problem. Equation (IFF) concerns uniform nuisance intervals, including their known centers; it is not a statement about every singular or mixed nuisance-prior family.

## A finite-cap necessary calibration bound

A frequency-count argument gives a useful, though nonmatching, constraint at resolution $`N^{-2}`$.

### A general cardinality bound

For a Haar-averaged nuisance decomposition

```math
\rho_\theta=\sum_s|\psi_{\theta,s}\rangle\langle\psi_{\theta,s}|,
\qquad
\psi_{\theta,s}=\sum_{g\in S_s}e^{-ig\theta}v_{g,s},
```

let $`D=\max_s|S_s|`$. For every estimator,

```math
\Pr_{\rm Haar}\{d<\delta\}
\leq\min\{1,D\delta/\pi\},
\qquad 0<\delta\leq\pi.
\tag{N1}
```

For a POVM element $`E(d\phi)`$, Cauchy–Schwarz gives

```math
\left\|\sqrt{E(d\phi)}
\sum_{g\in S_s}e^{-ig\theta}v_{g,s}\right\|^2
\leq
D\sum_{g\in S_s}
\langle v_{g,s}|E(d\phi)|v_{g,s}\rangle .
```

For each reported angle $`\phi`$, its success set of true $`\theta`$ values has uniform measure $`\delta/\pi`$. Integrate over this set and over outcomes, use POVM completeness, and then use $`\sum_{g,s}\|v_{g,s}\|^2=1`$. This proves (N1) without an orthogonality assumption on the adaptive coefficients.

### Counting the three-use Kerr frequencies

Under the hard per-query occupation cap, define

```math
\begin{aligned}
S_{s,N}
&=\left\{
 \sum_{j=1}^3T(n_j):
 n_1+n_2+n_3=s,\quad
 0\leq n_j\leq N
 \right\},\\
D_N&=\max_s|S_{s,N}|.
\end{aligned}
```

Every allowed three-use adaptive support is a subset of these histories. For a fixed $`s`$, the affine map

```math
g\longmapsto
Q=3g+\frac{3s-s^2}{2}
=\frac12\sum_{i<j}(n_i-n_j)^2
```

is injective and gives a value of $`x^2-xy+y^2`$. To bound its range, let the smallest and largest occupations differ by $`r\leq N`$, and write the middle occupation as a distance $`y\in[0,r]`$ above the smallest. Then

```math
Q=\frac{r^2+y^2+(r-y)^2}{2}
=r^2-y(r-y)
\leq N^2.
```

Let $`B_Q(X)`$ count the distinct positive integers at most $`X`$ represented by the primitive positive definite binary quadratic form $`Q(x,y)=x^2-xy+y^2`$, whose discriminant is $`-3`$. Bernays' theorem gives

```math
B_Q(X)=O\!\left(\frac{X}{\sqrt{\log X}}\right)
```

for this fixed form. This is imported number theory, not an estimate on the number of representations of an integer. See [Moree and Osburn](../references/RELATED_WORK.md#moree2006), equation (6) in the MPIM version, or equation (2.3) in the arXiv version, for the stated Bernays asymptotic.

The injective map and the possible value zero imply

```math
D_N\leq1+B_Q(N^2)
=O\!\left(\frac{N^2}{\sqrt{\log N}}\right).
\tag{N2}
```

Additional constraints on $`s`$ or on realizable adaptive histories can only reduce this set.

### Transferring the count to the interval prior

For uniform $`\theta`$ and a uniform nuisance interval of width $`w>0`$, the joint prior density relative to two-phase Haar measure is at most $`2\pi/w`$. Although this prior no longer fully dephases the nuisance, pointwise nonnegativity of success probability permits the density comparison

```math
\begin{aligned}
\Pr_w\{d<\delta\}
&\leq\min\{1,2D_N\delta/w\}\\
&\leq
\min\!\left\{1,\frac{C\delta N^2}{w\sqrt{\log N}}\right\}.
\end{aligned}
\tag{N3}
```

No block decomposition under the interval prior is assumed; (N3) compares the actual experiment to its Haar average.

At a fixed constant resolution $`\delta=cN^{-2}`$, if $`w_N\sqrt{\log N}\to\infty`$, then success tends to zero. If success is required to stay above a fixed positive level for all sufficiently large $`N`$, it is necessary that

```math
w_N=O((\log N)^{-1/2}).
\tag{NW}
```

For a bounded Kerr-prior density, insert its density bound into (N3). For any fixed absolutely continuous density and a claimed success level $`\eta>0`$, truncate at a fixed cutoff whose tail mass is below $`\eta/2`$. The bounded part must then supply at least $`\eta/2`$ success. This gives the same necessary rate (NW), with constants depending on the prior, the confidence level, and the fixed resolution coefficient.

### A corresponding risk lower bound

For uniform $`\theta`$ and interval width $`0<w\leq2\pi`$, put

```math
a=\frac{w}{2D_N}\leq\pi.
```

Equation (N3) implies $`\Pr\{d>x\}\geq1-x/a`$ for $`0\leq x\leq a`$, up to boundary atoms that do not affect the following integral. The layer-cake formula for the sine loss gives

```math
\begin{aligned}
R
&=\int_0^\pi2\sin x\,\Pr\{d>x\}\,dx\\
&\geq2\int_0^a\sin x\left(1-\frac xa\right)\,dx\\
&=2[1-\mathrm{sinc}a].
\end{aligned}
\tag{NR}
```

For small $`a`$ this is $`a^2/3+O(a^4)`$. Using (N2) gives, for sufficiently large $`N`$,

```math
R\geq c\,\frac{w_N^2\log N}{N^4}.
\tag{NR2}
```

The constant can be chosen uniformly over $`0<w_N\leq2\pi`$; the continuous function $`2[1-\mathrm{sinc}a]/a^2`$ has a positive minimum on $`[0,\pi]`$ after its removable singularity is filled.

Thus $`R=O(N^{-4})`$ requires (NW). For another fixed absolutely continuous Kerr prior, the same necessary width follows from the fixed-confidence argument: a risk bound $`O(N^{-4})`$ implies a nonzero fixed confidence in some fixed-constant $`N^{-2}`$ window by Markov's inequality. The exact formula (NR) itself is stated for the uniform Kerr prior.

For a fixed nonzero nuisance width, this finite-cap bound is weaker than the [energy independent strong converse](global_confidence.md). Its purpose is to constrain priors that themselves depend on $`N`$.

## The quantitative gap

The exact qualitative answer is (IFF). For the finer resolution target, the constructive RMS rate uses the crude bound $`|\Delta s_g|\leq K`$ in (RB). A smaller weighted sum

```math
\sum_gc_gc_{g+1}(\Delta s_g)^2
```

for a suitable choice of triangular representations could improve that upper bound. More general probes might use several representatives at the same Kerr frequency or a different estimation strategy. None of these possible improvements is established by the present argument.

Conversely, the Bernays count discards information about the weights and correlations between frequency sectors. Its necessary width $`O((\log N)^{-1/2})`$ is much weaker than the proved sufficient widths $`O(N^{-1})`$ for fixed confidence and $`O(N^{-3})`$ for RMS. There is no proof here that $`N^{-1}`$ is a necessary calibration threshold, nor that the RMS sufficient rate is optimal.

The positive-catalog converse, the qualitative interval theorem, and the finite-cap inequalities have separate hypotheses. Keeping those hypotheses explicit is what allows the original four-use result, partial prior calibration, and changed timing access to coexist without treating them as contradictory claims.
