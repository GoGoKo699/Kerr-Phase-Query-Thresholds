# Residual spectral phases and robustness

A higher-order phase has different consequences depending on whether its coefficient is independent of the target parameter. A fixed unknown cubic phase preserves the subthreshold converse, because revealing its value turns it into a known control. Its effect on a particular four-use measurement still has to be bounded. A cubic term proportional to the target parameter changes the generator itself and is a different estimation family.

The statements below use the [canonical query model](model.md), with a common phase on every call. They concern coherent spectral phases, not photon loss or uncontrolled changes of the gate between calls.

## A parameter-independent cubic coefficient preserves the converse

Consider the perturbed gate

```math
\widetilde U_{\theta,\beta,\kappa}
=K_\kappa U_{\theta,\beta},
\qquad
K_\kappa=\exp\!\left[-i\kappa\binom{\hat n}{3}\right].
```

First let $`\kappa`$ be fixed independently of $`\theta,\beta`$. Give its exact value to the estimator. Relative to the remaining unknown parameters, $`K_\kappa`$ is now a parameter-independent control. Every adaptive $`q`$-call protocol using $`\widetilde U`$ can be simulated with $`q`$ ideal calls to $`U`$, inserting the known $`K_\kappa`$ at each call. Conversely, the cubic factor can be undone by its known inverse. Both operations preserve occupation and hence the peak photon cap.

Thus the experiment class with $`\kappa`$ revealed is equivalent to the ideal query class. Withholding $`\kappa`$ cannot improve estimation. The [uniform-prior risk floors](query_thresholds.md#one-to-three-uses-with-an-unknown-common-linear-phase) and the [fixed-absolutely-continuous-prior confidence converse](global_confidence.md#unknown-common-linear-phase) therefore persist for $`q\le3`$. In particular, the three-call sine risk is at least $`2-\sqrt2`$ under independent uniform $`\theta,\beta`$.

An independently sampled $`\kappa`$ is handled by conditioning and averaging. The conditional $`\theta,\beta`$ prior remains the same fixed density, and the ideal converse is uniform over the protocol chosen for each revealed value of $`\kappa`$.

This converse does not give a four-use robustness theorem. The particular four-use state and readout may fail if an uncorrected cubic phase becomes large across their support. The following bounds address that separate question.

## The exact error functional for a representative code

Suppose consecutive frequencies $`j=0,\ldots,K-1`$ have real nonnegative amplitudes $`a_j`$, and a residual diagonal unitary adds phase $`h_j`$ to the selected representative of frequency $`j`$. The state is

```math
\sum_j a_j e^{-ij\theta-ih_j}|j\rangle.
```

The [two-grid Fourier measurement](four_photon_protocol.md#two-offset-fourier-grids) gives the exact pointwise risk

```math
R(\theta)
=2-2\sum_{j=0}^{K-2}a_ja_{j+1}
       \cos(h_{j+1}-h_j).
```

For sine amplitudes, write $`R_K=2-2\cos[\pi/(K+1)]`$. Then

```math
\begin{aligned}
R-R_K
&=2\sum_j a_ja_{j+1}
       \bigl[1-\cos(h_{j+1}-h_j)\bigr]\\
&\le\sum_j a_ja_{j+1}(h_{j+1}-h_j)^2.
\end{aligned}
```

Only adjacent phase increments enter this error functional. A common phase has no effect. An increment bound $`\max_j|h_{j+1}-h_j|=O(N^{-2})`$ is sufficient to retain $`O(N^{-4})`$ risk; increments tending to zero suffice for consistency of this readout. Since the cosine is periodic, one may also use principal phase increments modulo $`2\pi`$ in the bound.

A phase linear in the index illustrates the relevant systematic error. For $`h_j=cj+h_0`$,

```math
R=2-2\cos\frac\pi{K+1}\cos c.
```

For a fixed nonzero $`c\pmod{2\pi}`$, this tends to $`2-2\cos c`$. The residual changes the estimated phase by $`c`$ even though the measurement retains a narrow distribution around that shifted value.

## Residual work states and coherent arithmetic

The coherent preparation algorithm does not select a unique number-theory representation. Different representatives may acquire different cubic phases, leaving residual work-register information after decoding. The relevant exact identity is therefore the more general one from [coherent preparation](coherent_preparation.md#a-finite-readout-with-exact-pointwise-risk).

For the decoded state

```math
\sum_j a_j e^{-ij\theta}|j\rangle|\chi_j(\theta,\kappa)\rangle,
\qquad
\|\chi_j\|=1,
```

the finite Fourier readout gives

```math
R(\theta,\kappa)
=R_K+\sum_j a_ja_{j+1}
             \|\chi_{j+1}-\chi_j\|^2.
```

This includes both relative phases and the distinguishability of work states. No canonical representative assumption is needed.

On the exactly-$`s`$-photon sector, the combined cubic generator is

```math
H_3=\sum_{i=1}^4\binom{n_i}{3},
\qquad
0\le H_3\le\binom{s}{3}.
```

The upper bound counts triples within individual modes as a subset of all triples of the $`s`$ photons; it is attained when all photons occupy one mode. Thus

```math
\|e^{-i\kappa H_3}-I\|
\le |\kappa|\binom{s}{3}.
```

If the coherent representation search has unmarked amplitude at most $`\delta`$ in every frequency block, the ideal quadratic gate gives $`\|\chi_j(\theta,0)-|0\rangle\|\le2\delta`$. Unitary invariance and the triangle inequality imply

```math
\|\chi_j(\theta,\kappa)-|0\rangle\|
\le 2\delta+|\kappa|\binom{s}{3}.
```

All candidates, including the unmarked fallback, have total $`s`$, so the same bound applies to the entire loaded state. It follows that

```math
\boxed{
R(\theta,\kappa)
\le R_K+
\left[4\delta+2|\kappa|\binom{s}{3}\right]^2.
}
```

This is uniform in $`\theta,\beta`$. With $`s=\Theta(N)`$, $`K=\Theta(N^2)`$, and $`\delta=O(N^{-2})`$, the condition $`|\kappa|=O(N^{-5})`$ is sufficient for $`O(N^{-4})`$ risk. The weaker conditions $`\delta\to0`$ and $`\kappa N^3\to0`$ suffice for consistency.

These are conservative sufficient conditions. They do not establish an optimal tolerance or show that every fixed nonzero uncorrected cubic coefficient prevents four-use consistency. A general common diagonal perturbation can be treated in the same way by replacing $`|\kappa|\binom{s}{3}`$ with a norm bound on its residual phase after removing a scalar part.

### Compensation using retained labels

If $`\kappa`$ is known, the label-preserving construction can cancel the phase without a physical inverse cubic interaction. Compute

```math
h(\boldsymbol n)=\sum_i\binom{n_i}{3}
```

reversibly from the retained occupation registers and apply $`e^{i\kappa h(\boldsymbol n)}`$ to those registers before unloading. The physical Fock state on that branch has precisely the same occupations, so this digital phase cancels $`e^{-i\kappa H_3}`$ on every branch, including a fallback. Reversing the arithmetic clears the helper register.

The integer $`h`$ has $`O(\log N)`$ bits. Known bitwise phase rotations and reversible polynomial arithmetic therefore add only $`\mathrm{polylog}N`$ digital operations to the already assumed coherent interface. If compensation uses an estimate $`\kappa_0`$, the previous bounds apply to the residual $`\kappa-\kappa_0`$. The accuracy required of that estimate remains a separate calibration resource.

## Cubic structure at fixed total photon number

Fixed total photon number removes the linear nuisance but does not generally make a cubic phase a scalar. Define

```math
\begin{aligned}
x&=n_1+n_2-n_3-n_4,\\
y&=n_1-n_2+n_3-n_4,\\
z&=n_1-n_2-n_3+n_4,
\end{aligned}
\qquad
Q=x^2+y^2+z^2=8g+4s-s^2.
```

The inverse Hadamard map gives

```math
\sum_i n_i^2=\frac{s^2+Q}{4},
\qquad
\sum_i n_i^3=\frac{s^3}{16}
                +\frac{3sQ}{16}
                +\frac{3xyz}{8}.
```

Substituting $`\binom n3=(n^3-3n^2+2n)/6`$ yields

```math
\sum_i\binom{n_i}{3}
=\frac{s^3}{96}
 +\frac{(s-4)Q}{32}
 -\frac{s^2}{8}
 +\frac{s}{3}
 +\frac{xyz}{16}.
```

At fixed $`s`$, this is an affine function of $`g`$ with slope $`(s-4)/4`$, plus the representation-dependent term $`xyz/16`$. That product can have magnitude $`O(N^3)`$. Thus the arithmetic frequency representatives can have different cubic phases even when their linear and quadratic labels agree.

## Exact tolerance of the four-photon protocol

For the code $`1111,2110,0220,3100`$, the cubic generator has eigenvalues $`0,0,0,1`$. Only the last code word acquires the residual phase. The exact risk is

```math
\begin{aligned}
R_4(\theta,\kappa)
&=\frac{3-\sqrt5}{2}
  +2ab(1-\cos\kappa)\\
&=\frac{3-\sqrt5}{2}
  +\frac{1-\cos\kappa}{\sqrt5}.
\end{aligned}
```

It remains below the unrestricted three-use Haar floor precisely when

```math
\cos\kappa>
\frac{2\sqrt{10}-\sqrt5-3}{2}
\simeq0.5442436714.
```

In the central phase interval this is

```math
|\kappa|<0.9953090186\text{ radians}.
```

The comparison remains meaningful for an unknown independent cubic coefficient: the converse above still applies, while the displayed four-use bound is pointwise in that coefficient. For an independent distribution of $`\kappa`$, its average risk is obtained by replacing $`\cos\kappa`$ with $`\mathbb E\cos\kappa`$. The finite tolerance interval does not imply the same tolerance for a growing-photon construction.

## Changes of estimation family

The unitary

```math
\exp\!\left[
-i\theta\left(T(\hat n)+\epsilon\binom{\hat n}{3}\right)
-i\beta\hat n
\right]
```

has a modified target generator. Even when $`\epsilon`$ is known, the extra factor depends on unknown $`\theta`$ and cannot be inserted as a parameter-independent control in the preceding simulation. Its frequency arithmetic and parameter period can change. The quadratic-model converse is therefore not transferred to this family. On a bounded real interval of $`\theta`$, the upper-bound sensitivity calculation may still be used with $`|\kappa|\le|\epsilon|\sup|\theta|`$, but it does not provide a matching converse.

For a coefficient correlated with the target parameters, conditioning on its revealed value also changes their prior. The transfer argument requires the resulting conditional prior to satisfy the confidence theorem's hypotheses. In particular, it gives no conclusion when that conditional prior is singular. Correlation alone is not an automatic counterexample; the conditional experiment has to be specified.

[Photon-number phase control](../references/RELATED_WORK.md#heeres2015) and [JC-based oscillator control](../references/RELATED_WORK.md#huang2026jc) explicitly resolve or model physical phase corrections. They motivate specifying a residual spectral model but do not establish the photon-dependent calibration accuracy used in the sufficient asymptotic bound. Decoherence, loss during the unknown evolution, or independently varying per-call coefficients require separate channel models.

