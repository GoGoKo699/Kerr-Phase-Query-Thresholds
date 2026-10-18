# Query thresholds for a Kerr phase

The number of fixed forward uses changes whether global estimation can become accurate at all. With a known linear phase, one and two uses have nonzero global risk floors, while three uses achieve a wrapped root mean square error of order $`N^{-2}`$. With an unknown common linear phase, the corresponding threshold is four uses. These statements concern the complete estimate, including every interrogation used to obtain it.

The [access and resource model](model.md) is canonical. This page uses the primitive

```math
U_{\theta,\beta}
=\exp[-i\theta T(\hat n)-i\beta\hat n],
\qquad
T(n)=\frac{n(n-1)}2 .
```

The exact risk values below use independent uniform phase priors on $`[0,2\pi)`$, with the $`\beta`$ prior omitted when that phase is known. Ancillas, parameter independent controls between uses, adaptive feedback, and a final joint measurement are permitted. Each use is a complete fixed duration forward exposure. State preparation and readout do not receive additional information about the unknown parameters.

The explicit probes have total photon number at most $`N`$, including any bypass reference. The adaptive lower bounds hold under the more permissive condition that the occupation entering every queried mode is at most $`N`$. This distinction permits photon reuse and does not equate cumulative exposure with the initial photon number. A mean energy bound alone is not the condition used in the proofs.

## Results and loss

Let $`d\in[0,\pi]`$ be the shortest angular distance between $`\hat\theta`$ and $`\theta`$. We use

```math
\ell(d)=4\sin^2(d/2)=2-2\cos d,
\qquad
R=\mathbb E\,\ell(d).
```

The comparison

```math
\frac{4}{\pi^2}d^2
\leq \ell(d)
\leq d^2
```

means that $`R=\Theta(N^{-4})`$ is equivalent to wrapped root mean square error $`\Theta(N^{-2})`$. The exact floors are:

| Linear phase | Forward uses | Optimal uniform-prior sine risk | A sufficient total photon cap for equality |
|---|---:|---:|---:|
| Known | 1 | $`1`$ | $`N\geq2`$ |
| Known | 2 | $`2-\sqrt3`$ | $`N\geq5`$ |
| Known | 3 | $`\Theta(N^{-4})`$ | Asymptotic in $`N`$ |
| Unknown and common | 1 | $`2`$ | Any cap |
| Unknown and common | 2 | $`1`$ | $`N\geq2`$ |
| Unknown and common | 3 | $`2-\sqrt2`$ | $`N\geq4`$ |
| Unknown and common | 4 | $`\Theta(N^{-4})`$ | Asymptotic in $`N`$ |

The lower bounds allow arbitrary adaptive circuits in the stated class. Parallel probes attain the exact floors and the displayed rates. The photon thresholds in the last column are sufficient witnesses; the table does not claim that all are minimal under every alternative resource convention.

The spectral optimization used below is established phase estimation machinery; see [D'Ariano, Macchiavello, and Sacchi](../references/RELATED_WORK.md#dariano1998), [van Dam et al.](../references/RELATED_WORK.md#vandam2007), and the general query framework of [Copeland and Pommersheim](../references/RELATED_WORK.md#copeland2021). The arithmetic classification of the Kerr histories and the matching fixed-use constructions are the results developed here.

## Adaptive Fourier reduction

Purify the input, every intermediate measurement, and all discarded systems. A protocol with at most $`q`$ uses can be padded to $`q`$ uses by interrogating vacuum. Insert number projectors at each occurrence of the primitive gate. Every query history $`(n_1,\ldots,n_q)`$ then contributes the parameter dependent phase

```math
\exp\left[-i\theta\sum_{j=1}^qT(n_j)
          -i\beta\sum_{j=1}^qn_j\right].
```

Collect histories with the same two integer frequencies. The final purified state has the expansion

```math
|\Psi_{\theta,\beta}\rangle
=\sum_{g,s}e^{-ig\theta-is\beta}|v_{g,s}\rangle,
\qquad
g=\sum_{j=1}^qT(n_j),\quad s=\sum_{j=1}^qn_j.
\qquad\text{(F)}
```

All feedback and control choices are contained in the coefficient vectors $`v_{g,s}`$. These vectors need not be orthogonal. A hard occupation cap makes the expansion finite; the energy independent conclusions are uniform over all finite caps. For a known $`\beta`$, combine the coefficients into vectors $`v_g`$ after inserting its known value.

When $`\beta`$ is uniform, averaging it gives

```math
\rho_\theta
=\sum_s|\psi_{\theta,s}\rangle\langle\psi_{\theta,s}|,
\qquad
|\psi_{\theta,s}\rangle
=\sum_g e^{-ig\theta}|v_{g,s}\rangle.
\qquad\text{(B)}
```

Equation (B) is a positive sum, not an assertion that the vectors belonging to different $`s`$ are physically orthogonal. Its trace is one for every $`\theta`$. Averaging the normalization over both phases also gives the Parseval identity

```math
\sum_{g,s}\|v_{g,s}\|^2=1.
\qquad\text{(P)}
```

The same argument with just $`\theta`$ gives $`\sum_g\|v_g\|^2=1`$ in the known-linear-phase problem. The argument includes classical adaptive protocols through purification and arbitrary joint measurements through their final POVM. It assumes the controls themselves do not encode extra parameter information.

## The longest consecutive run bound

For an integer frequency set $`S`$, let $`L(S)`$ be the largest number of integers in a consecutive run contained in $`S`$. Missing frequencies split the adjacency graph into disjoint finite paths. If every nuisance block in (B) has longest run at most $`L`$, then every protocol with those supports obeys

```math
R\geq 2\left[1-\cos\frac{\pi}{L+1}\right].
\qquad\text{(L)}
```

To prove this without assuming orthogonal Fourier vectors, let $`E(d\phi)`$ be the final estimate POVM and set

```math
A=\int e^{i\phi}E(d\phi).
```

The operator $`A`$ is a contraction. Indeed, Cauchy–Schwarz for the positive operator measure bounds $`|\langle x|A|y\rangle|`$ by $`\|x\|\|y\|`$. Integrating the first error harmonic over the uniform priors gives

```math
\mathbb E\cos(\hat\theta-\theta)
=\mathrm{Re}\sum_{g,s}
  \langle v_{g+1,s}|A|v_{g,s}\rangle
\leq\sum_{g,s}\|v_{g+1,s}\|\,\|v_{g,s}\|.
```

For a single consecutive run of length $`r`$, the right hand quadratic form is half the adjacency matrix of a path. Its largest eigenvalue is $`\cos[\pi/(r+1)]`$, with positive eigenvector proportional to $`\sin[(j+1)\pi/(r+1)]`$. Apply this bound to every run and use (P). This proves (L).

For an arbitrary adaptive circuit, (L) is a lower bound derived from its support. Equality requires an allowed preparation and measurement that realize the optimal amplitudes. When one can prepare orthogonal representatives $`|j\rangle`$ of a run $`g_0,\ldots,g_0+L-1`$, choose

```math
|\psi\rangle
=\sqrt{\frac{2}{L+1}}
  \sum_{j=0}^{L-1}
  \sin\frac{(j+1)\pi}{L+1}\,|j\rangle .
\qquad\text{(S)}
```

The finite readout below attains equality. All claimed exact floors use explicit representatives, so they establish attainability as well as a converse. This qualification prevents an arbitrary collection of adaptive history frequencies from being mistaken for a freely preparable spectral basis.

### A finite readout with constant pointwise risk

No continuous outcome measurement is required. For a run of length $`L`$, choose any integer $`J\geq L+1`$, let $`\phi_m=2\pi m/J`$, and use

```math
|e_m\rangle
=\sum_{j=0}^{L-1}e^{-ij\phi_m}|j\rangle,
\qquad
E_m=\frac1J|e_m\rangle\langle e_m|,
\qquad 0\leq m<J.
\qquad\text{(M)}
```

Fourier orthogonality gives $`\sum_mE_m=I`$. For a state with real amplitudes $`c_j`$ and phase $`e^{-ij\theta}`$, the cosine score is

```math
\mathbb E_\theta\cos(\hat\theta-\theta)
=\sum_{j=0}^{L-2}c_jc_{j+1}
```

at every fixed $`\theta`$. Multiplication by the first error harmonic only introduces index differences of magnitude at most $`L`$, strictly smaller than $`J`$, so there is no additional Fourier alias. With (S), the pointwise risk is exactly the right hand side of (L).

One finite implementation pads the logical state with zero amplitudes and measures a $`J`$-point Fourier basis. An equivalent choice with $`J=2L`$ is a fair mixture of two $`L`$-point Fourier measurements, whose estimate grids differ by $`\pi/L`$. A single $`L`$-point grid has an endpoint alias and only its uniform-prior average equals (L); the padded or two-grid version has the constant pointwise risk stated here. Preparation of the physical representatives and their coherent readout remain resource assumptions, addressed separately in [coherent preparation](coherent_preparation.md).

## A known linear phase

A known $`\beta`$ can be compensated by a known number rotation or absorbed into the preparation and readout. For parallel sensing modes with total occupation at most $`N`$, the accessible frequencies are

```math
S_{q,N}
=\left\{
  \sum_{j=1}^qT(n_j):
  n_j\in\mathbb Z_{\geq0},\quad
  \sum_{j=1}^qn_j\leq N
  \right\}.
```

The same arithmetic, without the total-sum restriction, contains every adaptive support with $`q`$ uses.

### One and two uses

For one use, the distinct triangular frequencies are $`0,1,3,6,10,\ldots`$. The longest consecutive run is $`0,1`$, of length two, giving $`R\geq1`$. Occupations zero and two realize this run at a photon cap of two.

For two uses, triangular numbers modulo nine occupy

```math
T(n)\pmod9\ \in\{0,1,3,6\}.
```

The sum of two such residue sets misses both five and eight. Every run of six consecutive integers therefore contains a forbidden residue; the longest possible run has length at most five. The run $`0,1,2,3,4`$ is realized respectively by

```math
(0,0),\quad(2,0),\quad(2,2),\quad(3,0),\quad(3,2).
```

Every pair has total occupation at most five. Equation (L) and the sine probe give the exact risk $`2-\sqrt3`$ for $`N\geq5`$.

These are global estimation floors. They are not statements of exact nonidentifiability: an integer frequency gap of one is already present with one use.

### Three uses

Gauss's three-triangular-number theorem states that every nonnegative integer is the sum of three triangular numbers; see [Sun](../references/RELATED_WORK.md#sun2007) and [Mortenson](../references/RELATED_WORK.md#mortenson2017). For any representation $`g=\sum_{j=1}^3T(n_j)`$ and $`s=\sum_jn_j`$, Cauchy–Schwarz gives

```math
s^2\leq3\sum_jn_j^2=6g+3s.
\qquad\text{(T)}
```

Define

```math
M_N=\left\lfloor\frac{N(N-3)}6\right\rfloor.
```

For $`N\geq3`$ and $`0\leq g\leq M_N`$, inequality (T) forces $`s\leq N`$. Indeed, $`s\geq N+1`$ would give $`s(s-3)>N(N-3)\geq6g`$. Thus the entire band $`0,\ldots,M_N`$ is available within the total photon cap.

Choose one occupation triple $`\mathbf n(g)`$ for each $`g`$ and write $`s_g=\sum_jn_j(g)`$. A reference-counted version of (S) is

```math
|\psi_N\rangle
=\sqrt{\frac{2}{M_N+2}}
  \sum_{g=0}^{M_N}
  \sin\frac{(g+1)\pi}{M_N+2}
  |\mathbf n(g)\rangle_{\rm sense}
  |N-s_g\rangle_{\rm bypass}.
\qquad\text{(K3)}
```

Every component has exactly $`N`$ photons across the sensing and bypass modes. The bypass photons are part of the resource count. Distinct $`g`$ label orthogonal Fock states.

For a parallel total photon cap, all frequencies lie between zero and $`C_N=T(N)`$. Consequently the optimal risk within that class satisfies

```math
2\left[1-\cos\frac{\pi}{C_N+2}\right]
\leq R^*_{3,N}
\leq
2\left[1-\cos\frac{\pi}{M_N+2}\right].
\qquad\text{(K3R)}
```

Both sides are of order $`N^{-4}`$. For the broader adaptive class with occupation at most $`N`$ at each of three queries, replace $`C_N`$ by $`3T(N)`$ in the lower bound. The same parallel probe still supplies the upper bound, so the exponent is unchanged.

## One to three uses with an unknown common linear phase

The uniform nuisance average in (B) leaves coherence only between histories with equal cumulative occupation $`s`$. It is therefore the longest run in each fixed-$`s`$ frequency set that matters.

For one use, $`s=n_1`$ determines $`g=T(s)`$. Every block is a singleton and (L) gives $`R\geq2`$. A uniformly randomized estimate, or (M) on a one-dimensional code, has constant risk two.

For two uses, write the occupations as $`n,s-n`$. If $`s`$ is even,

```math
T(n)+T(s-n)
=\left(n-\frac s2\right)^2+\frac{s(s-2)}4.
```

The support is a subset of a translated square spectrum, whose longest consecutive run has length at most two. If $`s`$ is odd, successive values as $`n`$ changes differ by the even integer $`2n+1-s`$, so all frequencies have the same parity. At $`s=2`$, the pairs $`(1,1)`$ and $`(2,0)`$ realize frequencies zero and one. Hence the exact two-use risk is one.

For three uses, set $`u=n_1-n_3`$, $`v=n_2-n_3`$. Direct expansion gives the Eisenstein norm identity

```math
3g+\frac{3s-s^2}{2}
=u^2-uv+v^2.
\qquad\text{(E)}
```

The left hand shift is an integer. Modulo four, the form on the right takes only the values zero, one, and three: both coordinates even give zero, while every other parity pattern gives an odd value. Since three is invertible modulo four, every fixed-$`s`$ frequency set misses one residue class modulo four. Its longest run is at most three.

The total-$`s=4`$ occupation triples

```math
(2,1,1),\qquad(2,2,0),\qquad(3,1,0)
```

give $`g=1,2,3`$. A sine probe on these three Fock states therefore attains $`R=2-\sqrt2`$. All components have the same $`s`$, so the nuisance phase is a global phase. The bound is exact for total photon cap $`N\geq4`$, and it applies to arbitrary adaptive protocols by (F)–(L).

## Four uses with an unknown common linear phase

Four uses allow a fixed-occupation band of quadratic length. The parity of the exposed total matters: choose an odd integer $`s\leq N`$, for example the largest odd integer at most $`N`$.

Define the endpoints

```math
g_{\rm lo}=\frac{s^2-4s+3}{8},
\qquad
g_{\rm hi}=\left\lfloor\frac{s(s-3)}6\right\rfloor.
\qquad\text{(I)}
```

For every integer $`g`$ in this interval, put

```math
K=8g+4s-s^2.
```

The endpoint bounds imply $`3\leq K\leq s^2/3`$, and oddness of $`s`$ implies $`K\equiv3\pmod8`$. The Gauss–Legendre three-square criterion says that a nonnegative integer is a sum of three integer squares exactly when it is not of the form $`4^a(8b+7)`$; see [Sun](../references/RELATED_WORK.md#sun2007). It therefore supplies

```math
K=x^2+y^2+z^2.
```

All three coordinates are odd, since their squares sum to three modulo eight. Change the sign of one coordinate if necessary to arrange

```math
x+y+z\equiv-s\pmod4.
```

Such a sign change changes the odd sum by two modulo four. Now define

```math
\begin{aligned}
n_1&=(s+x+y+z)/4,\\
n_2&=(s+x-y-z)/4,\\
n_3&=(s-x+y-z)/4,\\
n_4&=(s-x-y+z)/4.
\end{aligned}
\qquad\text{(H)}
```

The first numerator is divisible by four by construction. The others differ from it by twice a sum of two odd integers, so they too are divisible by four. Moreover,

```math
|x|+|y|+|z|
\leq\sqrt{3K}
\leq s,
```

which makes every $`n_j`$ nonnegative. The inverse Hadamard map (H) gives

```math
\sum_jn_j=s,
\qquad
4\sum_jn_j^2=s^2+x^2+y^2+z^2,
\qquad
\sum_jT(n_j)=g.
```

Thus every integer in (I) has a four-mode representative of the same exposed total $`s`$. The number of frequencies is

```math
L_s=g_{\rm hi}-g_{\rm lo}+1
=\frac{s^2}{24}+O(s).
```

For sufficiently large odd $`s`$, the interval is nonempty and has length proportional to $`s^2`$. A sine state over one representative of each frequency, followed by (M), has pointwise risk

```math
R=2\left[1-\cos\frac{\pi}{L_s+1}\right]
=O(N^{-4}).
\qquad\text{(K4)}
```

The nuisance contributes the same phase $`e^{-is\beta}`$ to every component and is therefore irrelevant to this measurement. No bypass reference is needed; an unused fixed bypass occupation can be included if exactly $`N`$ initial photons are desired.

Under the parallel total photon cap, the frequency range is contained in $`[0,T(N)]`$; under the adaptive per-query occupation cap it is contained in $`[0,4T(N)]`$. Applying (L) to the full possible range gives an $`\Omega(N^{-4})`$ lower bound in either class. Together with (K4), this proves the four-use rate and the unknown-nuisance activation threshold.

The construction assumes permitted coherent preparation and readout on the specified Fock representatives. It does not itself establish a small optical circuit or a free representation oracle; the physical interface is discussed in [coherent preparation](coherent_preparation.md).

## Exactly even exposed photon totals

The cap theorem above permits odd $`s\leq N`$. A different constraint, exactly $`s`$ photons exposed across four parallel sensing modes, has a parity obstruction. The same obstruction applies to a fixed cumulative-exposure Fourier sector, but an even initial photon count in an arbitrary reuse protocol does not force that sector.

Let

```math
\begin{aligned}
x&=n_1+n_2-n_3-n_4,\\
y&=n_1-n_2+n_3-n_4,\\
z&=n_1-n_2-n_3+n_4.
\end{aligned}
```

Then $`x^2+y^2+z^2=8g+4s-s^2`$. If $`s=2a`$, the three coordinates are even. Writing them as $`2u,2v,2w`$ gives

```math
2g+2a-a^2=u^2+v^2+w^2.
\qquad\text{(P4)}
```

If $`s\equiv2\pmod4`$, then $`a`$ is odd. Three squares cannot sum to seven modulo eight, so (P4) removes one class of $`g`$ modulo four and forces longest run at most three. At $`s=6`$, the occupations

```math
(2,2,1,1),\qquad(3,1,1,1),\qquad(3,2,1,0)
```

give frequencies $`2,3,4`$. Adding one to all four occupations increases $`s`$ by four and translates every frequency by the old $`s`$. Hence the exact longest run is three and the exact sine risk is $`2-\sqrt2`$ for every $`s\geq6`$ with $`s\equiv2\pmod4`$.

If $`s\equiv0\pmod4`$, then $`a`$ is even. Three squares cannot sum to 28 modulo 32: a sum divisible by four forces every coordinate even, and division by four would give seven modulo eight. Equation (P4) therefore removes one class of $`g`$ modulo 16, forcing longest run at most 15.

This length is attained at $`s=24`$. With $`a=12`$, the following triples have squared norms $`30,32,\ldots,58`$, respectively:

| $`g`$ | $`(u,v,w)`$ |
|---:|---|
| 75 | $`(5,2,1)`$ |
| 76 | $`(4,4,0)`$ |
| 77 | $`(5,3,0)`$ |
| 78 | $`(6,0,0)`$ |
| 79 | $`(6,1,1)`$ |
| 80 | $`(6,2,0)`$ |
| 81 | $`(5,4,1)`$ |
| 82 | $`(6,2,2)`$ |
| 83 | $`(6,3,1)`$ |
| 84 | $`(4,4,4)`$ |
| 85 | $`(7,1,0)`$ |
| 86 | $`(6,4,0)`$ |
| 87 | $`(7,2,1)`$ |
| 88 | $`(6,4,2)`$ |
| 89 | $`(7,3,0)`$ |

Each triple has even coordinate sum and $`|u|+|v|+|w|\leq12`$. Therefore

```math
\left(
\frac{12+u+v+w}{2},
\frac{12+u-v-w}{2},
\frac{12-u+v-w}{2},
\frac{12-u-v+w}{2}
\right)
```

is a nonnegative integer occupation vector of total 24. Equation (P4) gives the listed frequencies. Adding one to every occupation extends the witness to every larger exposed total divisible by four. Thus

```math
R^*=2\left[1-\cos\frac{\pi}{16}\right]
```

for every $`s\geq24`$ divisible by four. This finite witness does not claim that 24 is the smallest possible exposed total with a 15-frequency run.

If exactly $`N`$ exposed photons are required for both budget parities, five uses suffice asymptotically. Put one photon through a fifth use when $`N`$ is even, and vacuum through it when $`N`$ is odd; the remaining four modes then have odd total. Since $`T(0)=T(1)=0`$, the fifth use adds no Kerr frequency. The even-total Haar floors above make five the smallest fixed query count for vanishing Haar risk, or equivalently here a full-circle minimax consistency guarantee, for both exact-exposure parities. The primary four-use theorem with a photon cap is unaffected.

A restricted target-phase prior can change this exact-exposure conclusion. For even $`s=2a`$, set $`r=2`$ when $`a`$ is even and $`r=3`$ when $`a`$ is odd. Every integer

```math
Q=r+8j\le\frac{a^2}{3},\qquad j\in\mathbb Z_{\ge0},
```

avoids the exclusions in the [three-square criterion](../references/RELATED_WORK.md#sun2007), so write $`Q=u^2+v^2+w^2`$. Since $`u+v+w\equiv Q\equiv a\pmod2`$ and $`|u|+|v|+|w|\le\sqrt{3Q}\le a`$, the occupations

```math
\left(
\frac{a+u+v+w}{2},
\frac{a+u-v-w}{2},
\frac{a-u+v-w}{2},
\frac{a-u-v+w}{2}
\right)
```

are nonnegative integers of total $`s`$. Equation (P4) gives

```math
g=\frac{a^2-2a+r}{2}+4j.
```

Thus each sufficiently large even total has a $`\Theta(s^2)`$-length band with frequency spacing four. The sine construction estimates $`\phi=4\theta\pmod{2\pi}`$ with pointwise risk $`O(s^{-4})`$. If $`\theta`$ is known to lie in a closed interval of width less than $`\pi/2`$, choose a phase cut outside its image under multiplication by four, with a fixed positive angular margin $`h`$. On the event $`d(\hat\phi,\phi)<h`$, lifting into this branch and dividing by four gives $`|\hat\theta-\theta|=d(\hat\phi,\phi)/4`$. The complementary event has probability at most $`R_\phi/[4\sin^2(h/2)]`$, which tends to zero. Since $`R_\phi\to0`$ and the target loss is bounded, four uses suffice for consistency for priors supported in such an interval. The five-use necessity retains its full-circle scope.

## Global scope of the threshold

The finite padded readout makes the attaining risks constant in the unknown phases. Thus the exact small-query Haar values also equal the corresponding minimax values, and the constructive rates hold for every phase pair.

For the primary thresholds under a photon cap, the converse is stronger than a nonzero sine-loss floor. The [global confidence theorem](global_confidence.md) applies to two or fewer uses with known linear phase and three or fewer with unknown common linear phase. In those cases, success in any shrinking angular window tends to zero uniformly over all finite photon budgets and all allowed protocols. It also removes the need for a full uniform prior: every fixed absolutely continuous prior has the same qualitative obstruction. [Timing and prior calibration](timing_and_priors.md) specifies which additional access and shrinking-prior assumptions preserve or escape that conclusion.
