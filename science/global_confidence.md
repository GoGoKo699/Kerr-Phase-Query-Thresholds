# Global confidence below the query threshold

Below the Kerr query threshold, the problem is stronger than a nonzero average error floor. With at most three identical forward uses and an unknown common linear phase, the probability of estimating the Kerr phase inside any shrinking angular window tends to zero, uniformly over all finite photon caps and all allowed adaptive protocols. With a known linear phase, the same statement holds for at most two uses.

The result initially follows for uniform phases and then extends to every fixed absolutely continuous prior. Thus a narrow but fixed calibration range does not remove the subthreshold obstruction. A prior that becomes narrower as the photon budget grows is a separate statistical model, analyzed in [timing and priors](timing_and_priors.md).

The [canonical model](model.md) specifies the gate, query count, photon caps, and loss. This page uses the [adaptive Fourier expansion](query_thresholds.md#adaptive-fourier-reduction)

```math
|\Psi_{\theta,\beta}\rangle
=\sum_{g,s}e^{-ig\theta-is\beta}|v_{g,s}\rangle,
\qquad
g=\sum_jT(n_j),\quad s=\sum_jn_j,
```

with arbitrary, possibly nonorthogonal, coefficient vectors. A finite occupation cap makes every frequency set finite. Every bound below is uniform in that cap.

The cyclic discrimination argument is a specialization of established finite-group query and confidence-region bounds, including [Copeland and Pommersheim](../references/RELATED_WORK.md#copeland2021), [Walter and Renes](../references/RELATED_WORK.md#walter2014), and [Meyer](../references/RELATED_WORK.md#meyer2025). The direct proof is included because it makes the adaptive and nuisance-phase assumptions explicit. The Kerr residue obstructions and their uniform continuous-confidence consequence are the application developed here.

## A cyclic residue bound

Suppose a normalized state family admits a positive decomposition

```math
\rho_\theta
=\sum_s|\psi_{\theta,s}\rangle\langle\psi_{\theta,s}|,
\qquad
|\psi_{\theta,s}\rangle
=\sum_{g\in S_s}e^{-ig\theta}|v_{g,s}\rangle,
\qquad
\sum_s\|\psi_{\theta,s}\|^2=1.
\qquad\text{(C1)}
```

The Fourier vectors and different $`s`$ terms need not be orthogonal. Suppose that each $`S_s`$ occupies at most $`D`$ residue classes modulo a positive integer $`M`$. Then every measurement and estimator obeys

```math
\Pr_{\theta\ {\rm uniform}}
\left\{d(\hat\theta,\theta)<\frac{\pi}{M}\right\}
\leq\frac{D}{M}.
\qquad\text{(C2)}
```

Here $`d`$ is shortest angular distance. The strict window excludes the harmless nearest-neighbor tie at the boundary.

### Proof

Give the estimator additional classical information

```math
\alpha=\theta\bmod(2\pi/M).
```

For each fixed $`\alpha\in[0,2\pi/M)`$, the remaining hypotheses are the $`M`$ equally likely points

```math
\theta_k=\alpha+\frac{2\pi k}{M},
\qquad 0\leq k\lt M.
```

Let $`A_s`$ be the occupied residue set in block $`s`$ and group

```math
|w_{r,s}\rangle
=\sum_{\substack{g\in S_s\\g\equiv r\ ({\rm mod}\ M)}}
e^{-ig\alpha}|v_{g,s}\rangle .
```

Then

```math
|\psi_{\theta_k,s}\rangle
=\sum_{r\in A_s}e^{-2\pi i rk/M}|w_{r,s}\rangle,
\qquad |A_s|\leq D.
```

For any hypothesis POVM $`E_0,\ldots,E_{M-1}`$, which may depend on $`\alpha`$, Cauchy–Schwarz gives

```math
\begin{aligned}
P_{\rm guess}
&=\frac1M\sum_{k,s}
\left\|
\sqrt{E_k}
\sum_{r\in A_s}e^{-2\pi i rk/M}w_{r,s}
\right\|^2\\
&\leq\frac{D}{M}
\sum_{k,s,r}\|\sqrt{E_k}w_{r,s}\|^2\\
&=\frac{D}{M}\sum_{s,r}\|w_{r,s}\|^2.
\end{aligned}
```

Averaging the state normalization in (C1) over $`k`$ and using discrete Fourier orthogonality shows

```math
\sum_{s,r}\|w_{r,s}\|^2
=\frac1M\sum_{k,s}\|\psi_{\theta_k,s}\|^2
=1.
```

Thus $`P_{\rm guess}\leq D/M`$ at each $`\alpha`$. An angle estimate with error less than $`\pi/M`$ identifies the nearest promised hypothesis. Integrating over $`\alpha`$ proves (C2). Providing $`\alpha`$ can only improve the estimator, so the original experiment satisfies the same bound.

This proof does not replace the mixed state by a rank estimate, does not require a measurement that reveals $`s`$, and does not assume that each block has a constant norm as $`\theta`$ changes. The positive decomposition and normalization of their sum are sufficient.

## Unknown common linear phase

For uniform $`\beta`$, the Fourier expansion gives (C1) after nuisance averaging. With at most three uses, pad any shorter history with vacuum and write

```math
g=T(n_1)+T(n_2)+T(n_3),
\qquad s=n_1+n_2+n_3.
```

As in the [risk-floor proof](query_thresholds.md#one-to-three-uses-with-an-unknown-common-linear-phase), let $`u=n_1-n_3`$, $`v=n_2-n_3`$. The identity

```math
3g+\frac{3s-s^2}{2}
=Q(u,v),
\qquad
Q(u,v)=u^2-uv+v^2
\qquad\text{(E)}
```

links each fixed-$`s`$ support to norms in the Eisenstein integers.

### Prime-power obstructions

Let $`p\equiv2\pmod3`$ be prime. The equation $`Q(u,v)=0`$ over $`\mathbb F_p`$ has only the zero solution. For odd $`p`$, a nonzero $`v`$ would make $`u/v`$ a root of $`X^2-X+1`$; this would give a nontrivial cube root of unity after changing its sign, incompatible with $`3\nmid p-1`$. If $`v=0`$, the equation forces $`u=0`$. For $`p=2`$, direct evaluation gives the same conclusion.

It follows that

```math
p\mid Q(u,v)
\quad\Longrightarrow\quad
p\mid u,\ p\mid v
\quad\Longrightarrow\quad
p^2\mid Q(u,v).
\qquad\text{(V)}
```

Therefore $`Q`$ cannot occupy any of the $`p-1`$ nonzero multiples of $`p`$ modulo $`p^2`$. Since $`p\ne3`$, the affine map from $`g`$ to the left hand side of (E) is invertible modulo $`p^2`$ for each fixed integer $`s`$. Each such frequency support occupies at most

```math
p^2-p+1
```

residue classes modulo $`p^2`$.

Choose any finite set $`\mathcal P`$ of these primes and define

```math
M_{\mathcal P}=\prod_{p\in\mathcal P}p^2,
\qquad
D_{\mathcal P}=\prod_{p\in\mathcal P}(p^2-p+1),
\qquad
\rho_{\mathcal P}
=\frac{D_{\mathcal P}}{M_{\mathcal P}}
=\prod_{p\in\mathcal P}
\left(1-\frac1p+\frac1{p^2}\right).
\qquad\text{(CRT)}
```

The Chinese remainder theorem bounds the number of permitted simultaneous residue classes by $`D_{\mathcal P}`$, uniformly in $`s`$. Applying (C2) gives, for every cap and every allowed protocol,

```math
\Pr_{\rm Haar}
\left\{d<\frac{\pi}{M_{\mathcal P}}\right\}
\leq\rho_{\mathcal P}.
\qquad\text{(U)}
```

The reciprocal sum of primes in the reduced progression $`2\bmod3`$ diverges. Hence $`\rho_{\mathcal P}\to0`$ as the finite set increases through those primes. These number-theoretic ingredients are standard; the [NIST references](../references/RELATED_WORK.md#dlmf27) provide the Chinese remainder theorem and reciprocal-prime progression asymptotics.

### The uniform shrinking-window theorem

Define

```math
F_3(\delta)
=\sup_{N\geq1}
 \sup_{\Pi:\,q\leq3}
\Pr_{\rm Haar}^{\Pi}\{d<\delta\},
```

where the second supremum ranges over the adaptive class in [the model](model.md). Given any $`\varepsilon>0`$, first choose a finite $`\mathcal P`$ with $`\rho_{\mathcal P}<\varepsilon`$. Equation (U) then gives $`F_3(\delta)<\varepsilon`$ whenever $`0<\delta\leq\pi/M_{\mathcal P}`$. Therefore

```math
\boxed{\lim_{\delta\downarrow0}F_3(\delta)=0.}
\qquad\text{(SC)}
```

The modulus is chosen from the desired error tolerance, independently of the photon cap and independently of the protocol. This order of quantifiers is what rules out a sequence of increasingly energetic adaptive probes.

In particular, if $`N\to\infty`$, $`\delta_N\to0`$, and $`\Pi_N`$ is any sequence with at most three uses, then its success probability at $`\delta_N`$ tends to zero. No consistency is possible in that class. The theorem does not assert that every pair of parameter values is exactly aliased or that every individual parameter point is equally difficult.

### A finite-resolution consequence

At modulus four, every one-, two-, and three-use fixed-$`s`$ support occupies at most one, two, and three residues, respectively. The two-use claim follows from a translated square spectrum for even $`s`$ and a fixed parity for odd $`s`$; the three-use claim follows from (E). Thus

```math
\Pr_{\rm Haar}\{d<\pi/4\}
\leq
\begin{cases}
1/4,&q=1,\\
1/2,&q=2,\\
3/4,&q=3.
\end{cases}
```

These are useful simple bounds. Equality for the continuous-window estimation problem is not claimed for every row.

## Every fixed absolutely continuous joint prior

Let $`\mu`$ be normalized Haar measure on the two-phase torus and let a fixed joint prior have density $`w=d\pi/d\mu`$. The prior may correlate the two phases and need not have a bounded density. For any protocol, define its conditional success probability $`p_\delta(\theta,\beta)\in[0,1]`$. For every cutoff $`C>0`$,

```math
\begin{aligned}
P_\pi^\Pi(\delta)
&=\int w\,p_\delta\,d\mu\\
&\leq C\int p_\delta\,d\mu
  +\int_{\{w>C\}}w\,d\mu\\
&\leq C F_3(\delta)
  +\int_{\{w>C\}}w\,d\mu.
\end{aligned}
\qquad\text{(AC)}
```

For fixed $`C`$, the first term tends to zero by (SC). The second can be made arbitrarily small by increasing $`C`$, since $`w`$ is integrable. Consequently

```math
\boxed{
\lim_{\delta\downarrow0}
\sup_{N\geq1}
\sup_{\Pi:\,q\leq3}
P_\pi^\Pi(\delta)=0
}
\qquad\text{(J)}
```

for every fixed absolutely continuous joint prior.

The protocol can depend on the prior. It can also depend on $`N`$ and on the requested resolution. The uniform Haar bound in (AC) already includes all those choices. The prior itself must remain fixed in this statement; there is no uniform limit over all possible prior densities.

In particular, any rectangle of positive fixed widths gives an absolutely continuous prior, however narrow those widths are. A fixed density on a bounded region of real Hamiltonian coefficients can also be folded to the phase torus; its pushforward is absolutely continuous. An unwrapped estimate accurate on that region would imply an accurate wrapped estimate, so it cannot avoid the wrapped converse.

A known exact nuisance phase, a point or discrete prior, a distribution supported on a lower-dimensional curve, or a prior concentrating with $`N`$ is outside (J). The [interval calibration theorem](timing_and_priors.md#three-uses-with-a-shrinking-nuisance-interval) treats one important family of concentrating priors explicitly.

## Known linear phase

With $`\beta`$ known, omit the nuisance blocks. At most two uses have frequencies

```math
g=T(n_1)+T(n_2).
```

They satisfy the Gaussian norm identity

```math
4g+1
=(n_1+n_2-1)^2+(n_1-n_2)^2.
\qquad\text{(G)}
```

For every prime $`p\equiv3\pmod4`$, a sum of two squares divisible by $`p`$ has both coordinates divisible by $`p`$ and is therefore divisible by $`p^2`$. Indeed, a nonzero coordinate modulo $`p`$ would produce a square root of $`-1`$. The coefficient four in (G) is invertible modulo $`p^2`$, so each such prime again removes $`p-1`$ frequency residues.

Using products over primes $`3\bmod4`$ gives exactly the bound (CRT)–(U) for the known-phase problem. Their reciprocal sum also diverges. Thus for every fixed absolutely continuous prior $`\pi_\theta`$,

```math
\lim_{\delta\downarrow0}
\sup_{N\geq1}
\sup_{\Pi:\,q\leq2}
P_{\pi_\theta}^\Pi(\delta)=0.
\qquad\text{(K)}
```

The density-truncation proof is now one-dimensional. The [three-use triangular-band probe](query_thresholds.md#three-uses) gives the matching consistency activation at three uses, so the known-phase and unknown-common-phase thresholds are respectively three and four.

## Confidence attained at the threshold

The three-use known-phase and four-use unknown-phase sine probes have finite measurements with pointwise risk $`R\leq C N^{-4}`$. For any $`0<\delta\leq\pi`$, monotonicity of the sine loss gives

```math
\Pr\{d\geq\delta\}
\leq\frac{R}{4\sin^2(\delta/2)}
\leq\frac{C N^{-4}}{4\sin^2(\delta/2)}.
\qquad\text{(A)}
```

This is pointwise in the unknown phases and therefore holds under any prior. For each fixed failure tolerance $`\varepsilon>0`$, a sufficiently large constant $`C_\varepsilon`$ gives confidence at least $`1-\varepsilon`$ in a window of half-width $`C_\varepsilon N^{-2}`$ for large $`N`$. If

```math
\delta_N\to0,
\qquad N^2\delta_N\to\infty,
```

then (A) gives success tending to one.

A fixed multiple of $`N^{-2}`$ produces a fixed confidence guarantee from this argument. It does not establish confidence tending to one at a fixed multiple. The matching $`\Theta(N^{-4})`$ optimal-risk lower bound in [query thresholds](query_thresholds.md) is a Haar-prior statement; the upper bound just used is pointwise.

## Heralding and retries

Suppose a subthreshold protocol sometimes accepts an estimate and otherwise aborts. Complete its abort branch with any parameter independent estimate. Under the named prior,

```math
\Pr\{\mathrm{accept}\}\,
\Pr\{d<\delta\mid\mathrm{accept}\}
=\Pr\{\mathrm{accept}\ \text{and}\ d<\delta\}
\leq\Pr\{\text{completed estimate has }d<\delta\}.
```

The completed protocol has the same target-query count. Equations (SC), (J), or (K) therefore bound the product on the left. In a shrinking window, a conditional success probability bounded away from zero requires the acceptance probability to tend to zero.

This consequence uses the joint success event, so it remains valid when acceptance changes the posterior distribution. It does not forbid parameter independent preparation retries performed before any unknown-gate call. If an experiment retries after sensing, every call in those attempts contributes to the total query count of the complete estimate.

## What the proof establishes

The obstruction is a limit on globally discriminating increasingly large cyclic families from a fixed number of allowed exposures. The arithmetic support can extend to arbitrarily large frequencies while occupying too few residue classes at selected moduli. This is compatible with a large local generator variance or a high local Fisher information.

The theorem is uniform over every finite hard cap, and it already includes ancillary systems, interleaved parameter independent channels, and adaptive measurements. Extending it to a different access model requires checking the frequency support again. [Timing and priors](timing_and_priors.md) carries this out for fixed finite positive commensurate duration catalogs and gives the precise scope of partial nuisance calibration.
