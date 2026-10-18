# Coherent preparation and finite Fourier readout

The four-use construction admits a coherent preparation algorithm without a table of frequency representatives or quantum random-access memory. Its digital cost is polynomial in the photon budget, with a separately specified interface to the four sensing modes.

The [query and resource model](model.md) fixes what counts as a use of the unknown gate. Throughout this construction, the four sensing modes contain exactly an odd number $`s\le N`$ of photons when the unknown gates are applied. The frequency register, arithmetic work registers, and control ancilla do not pass through the unknown gate. All computational reflections, state transfers, and inverse preparation operations are known controls.

## Construction and resource statement

Let $`s\ge3`$ be odd and define

```math
g_{\mathrm{lo}}=\frac{s^2-4s+3}{8},
\qquad
g_{\mathrm{hi}}=\left\lfloor\frac{s(s-3)}6\right\rfloor,
\qquad
D=g_{\mathrm{hi}}-g_{\mathrm{lo}}+1.
```

The [four-use dense-band construction](query_thresholds.md#four-uses-with-an-unknown-common-linear-phase) gives every integer frequency in this interval at fixed total $`s`$. Choose $`K=2^m\le D`$ as the largest available power of two, and use $`g_j=g_{\mathrm{lo}}+j`$, $`0\le j<K`$. Taking $`s`$ as the largest odd integer at most $`N`$ gives $`K=\Theta(N^2)`$ as the cap grows.

The index amplitudes are

```math
a_j=\sqrt{\frac{2}{K+1}}\,
       \sin\frac{(j+1)\pi}{K+1}.
```

Their ideal pointwise sine risk is

```math
R_K=2-2\cos\frac{\pi}{K+1}=\Theta(N^{-4}).
```

Assume a reversible number-to-Fock interface that retains the digital occupation labels. For any $`0<\delta<1`$, the construction below uses four unknown-gate calls and

```math
O\!\left(N\log\frac{2}{\delta}\right)
```

calls to an arithmetic predicate. Each predicate evaluation and each additional computational reflection costs $`\mathrm{polylog}N`$ elementary digital operations. Conditioned on successful preparation of the query-free index state, the implemented pointwise risk obeys

```math
R(\theta)\le R_K+16\delta^2.
```

Consequently $`\delta=O(N^{-2})`$ gives $`O(N\mathrm{polylog}N)`$ digital operations while retaining $`O(N^{-4})`$ risk. This is polynomial in the photon number $`N`$, not in the input length $`\log N`$. It does not include an unstated physical cost for the number-to-Fock interface.

## Preparing the sine amplitudes without a table

Set $`\alpha=\pi/(K+1)`$. Prepare the index uniformly in $`K`$ states and a control qubit in $`|+\rangle`$. Apply the two conditional phases

```math
|0\rangle|j\rangle\longmapsto
e^{i\alpha(j+1)}|0\rangle|j\rangle,
\qquad
|1\rangle|j\rangle\longmapsto
e^{-i\alpha(j+1)}|1\rangle|j\rangle.
```

The binary expansion of $`j`$ expresses each phase as a product of $`O(\log K)`$ controlled one-bit rotations. A Hadamard on the control gives its $`|1\rangle`$ branch the index amplitude

```math
\frac{i}{\sqrt K}\sin[\alpha(j+1)].
```

The identity

```math
\sum_{j=0}^{K-1}\sin^2\frac{(j+1)\pi}{K+1}
=\frac{K+1}{2}
```

shows that the branch probability is $`(K+1)/(2K)>1/2`$. On this outcome the normalized index is the desired sine state, up to a global phase. No arbitrary-amplitude table is used.

The heralding occurs before loading photons or calling the unknown gate. Repeating it has fewer than two expected attempts. If a finite attempt cap is required, $`r=\lceil4\log_2N\rceil+O(1)`$ attempts give abort probability at most $`2^{-r}=O(N^{-4})`$. On abort, prepare the known Fock state $`|s,0,0,0\rangle`$, apply the same four unknown-gate calls, and return an arbitrary estimate. This retains both the four-use count and the exact exposed total $`s`$. Its contribution to the risk is at most $`4\,2^{-r}`$. Vacuum queries would retain a photon cap but would not retain an exact-$`s`$ exposure promise.

Each attempt uses $`O(\log N)`$ rotations; the finite cap therefore costs $`O(\log^2N)`$ such operations. All retries are query-free preparation, rather than postselection on a sensing outcome.

## A reversible representation predicate

For the frequency $`g`$, define

```math
Q_g=8g+4s-s^2.
```

Across the chosen band,

```math
Q_g\equiv3\pmod8,
\qquad
3\le Q_g\le\frac{s^2}{3}.
```

Choose $`B=2^{\lceil\log_2(s+1)\rceil}`$ and search the $`M=B^2=O(N^2)`$ pairs $`(x,y)\in\{0,\ldots,B-1\}^2`$. A pair is marked when $`x,y`$ are positive odd integers and

```math
r=Q_g-x^2-y^2\ge0,
\qquad
z=\lfloor\sqrt r\rfloor>0,
\qquad
z^2=r,
\qquad
z\equiv1\pmod2.
```

All integers have $`O(\log N)`$ bits. Fixed-length reversible circuits for squaring, signed subtraction, integer square root, comparison, and parity implement this predicate in $`\mathrm{polylog}N`$ elementary operations. Schoolbook arithmetic suffices; the square root can use a restoring algorithm with a number of iterations fixed by the register width. Compute the predicate into a flag and reverse its scratch computation. No data oracle is assumed.

Legendre's three-square theorem guarantees at least one marked pair. Since $`Q_g=3\pmod8`$, it is not of the excluded form $`4^a(8b+7)`$. Every three-square representation has three odd coordinates, because the only way three quadratic residues modulo eight sum to three is $`1+1+1`$. Taking absolute values makes all coordinates positive. Each is at most $`\sqrt{Q_g}<s+1\le B`$, so the search range contains a marked pair. Thus its marked fraction satisfies

```math
\lambda_g\ge\frac1M
```

uniformly over all frequencies in the coherent index register.

For a marked pair, choose the sign of $`z`$ so that $`s+x+y+z=0\pmod4`$. There is exactly one such sign: the residue before the choice is even, and changing the sign of odd $`z`$ changes it by two modulo four. Compute

```math
\begin{aligned}
n_1&=(s+x+y+z)/4,&
n_2&=(s+x-y-z)/4,\\
n_3&=(s-x+y-z)/4,&
n_4&=(s-x-y+z)/4.
\end{aligned}
```

All numerators are divisible by four. Moreover,

```math
|x|+|y|+|z|\le\sqrt{3Q_g}\le s,
```

so the occupations are nonnegative. They satisfy

```math
\sum_i n_i=s,
\qquad
\sum_i\binom{n_i}{2}=g.
```

For an unmarked candidate, define the output tuple to be $`(s,0,0,0)`$. This fallback is essential: residual search error must not violate the photon promise. Retaining the candidate registers makes the tuple computation reversible even when several candidates produce the same tuple.

## Coherent fixed-point amplification

The fixed-point search of [Yoder, Low and Chuang](../references/RELATED_WORK.md#yoder2014) prepares a marked component of squared norm at least $`1-\delta^2`$ whenever the marked fraction exceeds a supplied lower bound. It uses

```math
O\!\left(\lambda_{\min}^{-1/2}
          \log\frac{2}{\delta}\right)
```

predicate calls with explicitly determined generalized-reflection phases. Here $`\lambda_{\min}=1/M`$.

A finite choice can be made directly from their success polynomial. For odd sequence length $`L`$, the guaranteed width is

```math
w=1-T_{1/L}(1/\delta)^{-2}
 =\tanh^2\!\left(\frac{\mathrm{arcosh}(1/\delta)}{L}\right).
```

Choosing an odd $`L\ge\sqrt M\,\mathrm{arcosh}(1/\delta)`$ ensures $`w\le1/M`$. The predicate query count is $`L-1`$.

Use the same phase schedule in every frequency block. The reflection about the uniform candidate state acts on the candidate registers and leaves the frequency index untouched. The arithmetic marking operation is controlled by that index. Thus the full search has the form

```math
W=\sum_{j=0}^{K-1}|j\rangle\langle j|\otimes W_j.
```

It does not reflect about or measure the full sine superposition. The method therefore works coherently even though different frequencies have different numbers of representations.

Neither a canonical representation nor a common search phase is required. Within a frequency block, the marked component can be a superposition of all marked representations and can acquire a frequency-dependent phase. All marked representations receive the same unknown phase, and the later $`W_j^\dagger`$ reverses the known search.

The schedule is computed from $`N`$ and $`\delta`$; its angles need not be stored as a frequency-dependent table. Reversible arithmetic uses $`O(\log N)`$-bit logical registers and at most $`\mathrm{polylog}N`$ scratch. No assumption about an efficient classical three-square algorithm, the extended Riemann hypothesis, or QRAM enters the construction.

## Encoding, four queries, and decoding

Let $`V`$ denote a reversible, label-preserving interface from a digitally specified tuple to its Fock state:

```math
V:
|j,x,y,\boldsymbol n\rangle|0,0,0,0\rangle
\longmapsto
|j,x,y,\boldsymbol n\rangle
|n_1,n_2,n_3,n_4\rangle.
```

Other arithmetic registers are suppressed in this notation. Apply $`V`$ after computing the tuple, make one unknown-gate call on each sensing mode, apply $`V^\dagger`$, reverse the tuple computation, and apply $`W^\dagger`$. Every tuple, including an unmarked fallback, has total $`s`$. The unknown linear phase is therefore the same scalar $`e^{-i\beta s}`$ on every branch.

For each $`j`$, write $`|A_j\rangle=W_j|0\rangle`$. Its unmarked component has norm at most $`\delta`$. After factoring out $`e^{-ig_j\theta-i\beta s}`$, the induced diagonal operation $`D_j(\theta)`$ equals identity on every marked candidate. It is unitary on the unmarked candidates. Hence

```math
\|(D_j-I)|A_j\rangle\|\le2\delta.
```

After decoding, the output is, apart from a scalar phase,

```math
|\Psi_\theta\rangle
=\sum_{j=0}^{K-1}a_j e^{-ij\theta}
 |j\rangle|\chi_j(\theta)\rangle,
\qquad
|\chi_j\rangle=W_j^\dagger D_jW_j|0\rangle.
```

Each work state is normalized and satisfies

```math
\|\chi_j-|0\rangle\|\le2\delta.
```

No inverse of the unknown gate is used. The inverse operations are the same known computational and loading controls used before sensing.

## A finite readout with exact pointwise risk

For $`\phi_\ell=\pi\ell/K`$, $`0\le\ell<2K`$, define

```math
|e_{\phi_\ell}\rangle
=\sum_{j=0}^{K-1}e^{-ij\phi_\ell}|j\rangle,
\qquad
E_\ell=\frac1{2K}
       |e_{\phi_\ell}\rangle\langle e_{\phi_\ell}|.
```

The effects sum to identity. They can be implemented by a fair classical bit $`b\in\{0,1\}`$: set $`\alpha_b=b\pi/K`$, apply

```math
Z(\alpha_b)=\sum_j e^{ij\alpha_b}|j\rangle\langle j|,
```

then the Fourier transform with entries $`(F_K)_{mj}=e^{2\pi imj/K}/\sqrt K`$, followed by computational-basis measurement. Report

```math
\widehat\theta=\frac{2\pi m}{K}+\alpha_b\pmod{2\pi}.
```

For each fixed $`b`$, this is an orthonormal Fourier basis. Mixing the two bases gives exactly the $`2K`$ effects. This uses a single classical random bit and a known finite phase offset. Padding to a $`2K`$-dimensional quantum register and applying its Fourier transform is an alternative realization of the same POVM.

For the decoded joint state, the outcome probabilities are

```math
p_\ell=\frac1{2K}
\left\|
\sum_j a_j e^{ij(\phi_\ell-\theta)}\chi_j
\right\|^2.
```

Discrete Fourier orthogonality selects only adjacent index differences when multiplying by $`\cos(\phi_\ell-\theta)`$. The largest possible index difference is $`K-1`$, so no endpoint aliases into a first harmonic on the $`2K`$ grid. At every fixed $`\theta`$,

```math
\begin{aligned}
R(\theta)
&=2-2\mathrm{Re}
       \sum_{j=0}^{K-2}a_ja_{j+1}
       \langle\chi_{j+1}|\chi_j\rangle\\
&=R_K+\sum_{j=0}^{K-2}a_ja_{j+1}
          \|\chi_{j+1}-\chi_j\|^2.
\end{aligned}
```

The second equality uses normalization and

```math
\sum_{j=0}^{K-2}a_ja_{j+1}
=\cos\frac{\pi}{K+1}.
```

The identity remains valid when the work states depend on $`\theta`$, since all outcome summations are performed at that fixed parameter value. Their phases and distinguishability are both included in the norm difference. Using $`\|\chi_{j+1}-\chi_j\|\le4\delta`$ proves the stated error bound.

A single $`K`$-point Fourier PVM has an additional endpoint term in its pointwise risk. It has the same Haar-average risk but is not the pointwise measurement used here. The two offsets cancel that term exactly.

A digital power-of-two Fourier transform costs $`O(\log^2K)`$ ideal controlled-phase gates, and the offset costs $`O(\log K)`$ rotations. Inverse-polynomial errors in general digital operations can be assigned a total trace-distance budget $`O(N^{-4})`$; bounded loss then contributes $`O(N^{-4})`$. The sharper quadratic work-state estimate applies to errors that preserve the index structure. It is not a blanket quadratic bound on arbitrary hardware errors that mix indices or leak from the encoded system.

## A conditional physical loading lemma

The digital algorithm requires an actual bosonic interface, rather than a simulation of the unknown bosonic gate on qubits. The following ideal control set supplies one such interface with a linear number of transfer stages.

Assume a qutrit with an active pair of levels $`|u\rangle,|l\rangle`$, a third level $`|d\rangle`$ dark to the selected interaction, and mode-selectable Hamiltonians

```math
H_i=\gamma_i
\left(
 |l\rangle\langle u|\,a_i^\dagger+
 |u\rangle\langle l|\,a_i
\right).
```

Also assume coherent qutrit pulses conditioned on a predicate bit in the digital register. These Hamiltonians include the assumption that spectator-dependent detunings and unwanted phases are absent or compensated. Such compensation is not supplied by the arithmetic complexity bound.

For a mode initially in vacuum and qutrit in $`|d\rangle`$, repeat the following for $`k=1,\ldots,s`$. Compute the bit $`b=[n_i\ge k]`$. Conditioned on $`b=1`$, rotate $`|d\rangle`$ to $`|u\rangle`$. Apply $`H_i`$ for time

```math
t_{i,k}=\frac{\pi}{2\gamma_i\sqrt k}.
```

Then, conditioned on the same bit, rotate $`|l\rangle`$ back to $`|d\rangle`$ and uncompute the bit.

At the start of stage $`k`$, the branch with occupation label $`n_i`$ contains $`\min(n_i,k-1)`$ photons. If active, it contains exactly $`k-1`$ photons, so the pulse makes the same full transfer

```math
|u,k-1\rangle\longmapsto-i|l,k\rangle
```

on every active branch. All inactive branches remain dark. This induction proves coherent loading for an arbitrary superposition of digital labels. It avoids attempting to synchronize different $`\sqrt n`$ Rabi rates. The known phase accumulated by a branch can be included in the interface; its exact reverse cancels the phase after sensing.

Four modes require at most $`4s`$ JC stages for loading and another $`4s`$ for unloading, with $`O(s)`$ conditional qutrit pulses and $`O(N\mathrm{polylog}N)`$ comparator logic. Peak sensing-mode occupation is at most $`s`$, and the final loaded occupation is exactly $`s`$. The loader injects photons during preparation; it does not conserve the four-cavity photon number at every intermediate preparation step. The [finite four-photon protocol](four_photon_protocol.md) has the stronger conservation property.

For fixed nonzero couplings and negligible pulse overhead, the ideal JC dwell time is proportional to

```math
\sum_{k=1}^s\frac1{\sqrt k}=O(\sqrt s).
```

Finite-duration conditional pulses can instead give $`O(N)`$ elapsed control time. Neither estimate includes an unproved hardware accuracy scaling.

[Multimode sideband experiments](../references/RELATED_WORK.md#huang2026sideband) establish mode-selectable JC interactions, dark-state shelving, and selected encoding operations. They do not demonstrate a coherent arithmetic register controlling this entire four-mode interface. [Universal JC oscillator control](../references/RELATED_WORK.md#huang2026jc) establishes additional single-mode control capabilities and explicitly treats physical phase corrections; it likewise does not supply that complete interface. The distinction is material: the proven digital operation count, the conditional transfer-stage count, and a measured physical runtime or fidelity are different resource statements.
