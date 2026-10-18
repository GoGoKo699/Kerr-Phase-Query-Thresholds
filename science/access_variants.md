# What changes when gate access changes

The threshold in [the model](model.md) concerns a fixed number of identical forward uses. This page gives explicit protocols showing why inverse access and improving time resolution cannot be treated as free controls. Both constructions account for a bypass reference in the total photon number. Neither is an optimality theorem for its enlarged access model.

## One shortened call restores consistency

### Access and prior domain

Assume access to a selected Hamiltonian evolution

```math
U(a)=\exp[-ia\{\theta T(\hat n)+\beta\hat n\}],
```

where **both** coefficients scale with the chosen duration multiplier $`a`$. Here $`\theta`$ and $`\beta`$ are real coefficients in specified fixed bounded intervals. Their real representatives are part of the Hamiltonian specification; an opaque gate known only through phases modulo $`2\pi`$ does not determine all its fractional powers.

We still evaluate the wrapped error in $`\theta`$. Write $`|\theta|\le\Theta`$ and $`|\beta|\le B_\beta`$, with these bounds independent of $`N`$.

### A band near the middle of the photon range

Let $`B`$ be the largest odd integer at most $`N`$, with $`B\ge9`$, and set

```math
n_0=\frac{B+1}{2},\qquad
L=\lfloor\sqrt B\rfloor,\qquad
K=2L+1,\qquad a_B=\frac2B.
```

For $`-L\le k\le L`$, use the orthogonal code words

```math
|k\rangle_{\mathrm{code}}
=|n_0+k\rangle_{\mathrm{sense}}
 |N-n_0-k\rangle_{\mathrm{bypass}}.
```

All occupations are nonnegative, the sensing occupation is at most $`B`$, and the total photon number is exactly $`N`$. Prepare the normalized sine state

```math
|\psi\rangle
=\sum_{k=-L}^{L}c_k|k\rangle_{\mathrm{code}},
\qquad
c_k=\sqrt{\frac2{K+1}}
\sin\!\left(\frac{(k+L+1)\pi}{K+1}\right).
```

The elementary identity

```math
a_BT(n_0+k)=a_BT(n_0)+k+\frac{k^2}{B}
```

turns the nonlinear phase into a desired linear frequency plus a slowly varying correction. After removing a global phase, one call produces

```math
\sum_{k=-L}^{L}c_k e^{-ik\theta}e^{-ih_k}|k\rangle_{\mathrm{code}},
\qquad
h_k=\frac{\theta k^2+2\beta k}{B}.
```

The absolute correction $`h_k`$ need not be uniformly small. The measurement risk depends on its difference between neighboring code words.

### Finite readout and its exact risk

Use the $`2K`$-outcome Fourier POVM on the logical index $`j=k+L`$, reporting

```math
\hat\theta_m=\frac{\pi m}{K},\qquad
E_m=\frac1{2K}|f_m\rangle\langle f_m|,
\qquad
|f_m\rangle=\sum_{j=0}^{K-1}e^{-ij\hat\theta_m}|j\rangle.
```

It can be realized as a fair classical choice between two $`K`$-point Fourier projective measurements whose grids differ by $`\pi/K`$. The construction of that finite measurement and its endpoint-alias cancellation are explained in [the four-photon protocol](four_photon_protocol.md).

The exact pointwise sine risk is

```math
R(\theta,\beta)=
2\left[1-\cos\frac{\pi}{K+1}\right]
+2\sum_{k=-L}^{L-1}c_kc_{k+1}
\left[1-\cos\frac{\theta(2k+1)+2\beta}{B}\right].
```

Indeed, the Fourier first moment couples only adjacent indices; their phase difference is

```math
h_{k+1}-h_k=\frac{\theta(2k+1)+2\beta}{B}.
```

Using $`2(1-\cos x)\le x^2`$ and $`\sum c_kc_{k+1}\le1`$ gives

```math
R(\theta,\beta)
\le\frac{\pi^2}{4(L+1)^2}
+\frac{[\Theta(2L-1)+2B_\beta]^2}{B^2}
=O(N^{-1}).
```

The bound is uniform on the specified coefficient intervals. One call of duration proportional to $`N^{-1}`$ therefore achieves wrapped RMS error $`O(N^{-1/2})`$ and consistency. It does not achieve the four-fixed-call $`N^{-2}`$ RMS law.

The state and logical readout are specified directly and require no arithmetic lookup table or QRAM. Their control cost remains an additional resource. If $`\beta`$ is a per-call phase that does **not** scale with duration, the displayed identity does not suppress its effect and this one-call argument does not apply.

## A forward/inverse pair

Now assume that one call to $`U_{\theta,\beta}`$ and one call to its full inverse are available, with both the quadratic and linear terms inverted. Let

```math
K=\left\lfloor\frac{N-1}{2}\right\rfloor+1,
\qquad 0\le k\le K-1,
```

and use the code

```math
|k\rangle_{\mathrm{code}}
=|k+1\rangle_{+}|k\rangle_{-}
 |N-(2k+1)\rangle_{\mathrm{bypass}}.
```

The queried pair has

```math
T(k+1)-T(k)=k,\qquad (k+1)-k=1.
```

A sine superposition therefore becomes, up to the global nuisance phase,

```math
e^{-i\beta}\sum_{k=0}^{K-1}c_k e^{-ik\theta}|k\rangle_{\mathrm{code}}.
```

The finite Fourier readout yields

```math
R=2\left[1-\cos\frac{\pi}{K+1}\right]
=\Theta(N^{-2}),
```

so the wrapped RMS error is $`\Theta(N^{-1})`$. The two-call protocol is consistent even with a completely unknown common linear phase. The positivity of the original forward durations is thus a substantive assumption. No inverse-access optimum is asserted.

## Fixed clocks, minimum durations and total time

[Timing and priors](timing_and_priors.md) proves that a **fixed finite** set of positive integer multiples of a fixed clock step cannot remove the subthreshold obstruction. A fixed clock step together with a fixed upper bound on the total forward evolution time yields such a finite catalog. Allowing increasingly long individual durations can require a catalog that changes with $`N`$. Increasing the number of calls instead leaves the fixed-query regime even when every call repeats one fixed duration.

The distinction between a minimum allowed evolution time and a programmable clock step is also explicit in [Shin, Lee and Oh](../references/RELATED_WORK.md#shin2026). Their Hamiltonian-learning setting allows resource regimes beyond fixed query number and a fixed catalog. The result here addresses this bounded Kerr-query setting; it does not settle their general time-resolution question.

The two escapes above identify concrete additional resources: a refining clock in the first case and a negative exposure in the second. General incommensurate durations, catalogs whose size grows with $`N`$, and optimal tradeoffs between query count and total evolution time are outside the classified contribution.

## Reproducibility

[The access verification](../verification/README.md) checks the shortened-call identity and exact finite-POVM risk at representative photon caps and parameter values. It also checks the weighted quadratic identity used for fixed catalogs. The algebraic arguments above establish the asymptotic guarantees; the finite computations do not establish optimality in the enlarged models.
