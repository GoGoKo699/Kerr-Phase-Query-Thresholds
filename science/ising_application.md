# One fixed-time interrogation of an all-to-all Ising coupling

The cyclic-frequency obstruction also applies to a spin system with a quadratic collective generator. This is a separate one-interrogation corollary. It does not transfer the Kerr three- and four-use thresholds to spin controls.

## Physical model

Fix a known register of $`N`$ spins and the Hamiltonian

```math
H_N(J)=J\sum_{1\le i\lt j\le N}Z_iZ_j.
```

The pair coupling $`J`$ has a fixed absolutely continuous prior on the real line. Prepare any $`J`$-independent input, possibly entangled with arbitrary parameter-independent ancillas, apply one uninterrupted evolution for a fixed time $`t>0`$, and perform any final joint POVM. The time and the definition of the pair coupling do not vary with $`N`$.

[Belliardo, Gardner, Jiang and Clerk, Section IV.1 and Appendix H](../references/RELATED_WORK.md#belliardo2026), examine this fixed-time model for the prescribed input $`|+\rangle^{\otimes N}`$. The argument below removes that input restriction and proves a uniform asymptotic confidence obstruction. It complements their finite-precision bounds rather than identifying their lower performance guarantee with the unknown optimum.

## Spectrum and the two parity subsequences

With $`S_z=\frac12\sum_i Z_i`$,

```math
\sum_{i\lt j}Z_iZ_j=2S_z^2-\frac N2 I.
```

For fixed known $`N`$, the identity term contributes only a global phase and may be dropped. The remaining frequencies depend on the parity of $`N`$.

For even $`N`$, the magnetic quantum number $`m`$ is an integer. In the phase variable $`\theta=2Jt`$, the frequencies are squares $`m^2`$. For $`N\ge2`$, the projective period in $`J`$ is $`\pi/t`$.

For odd $`N`$, write $`m=k+1/2`$. Then

```math
2m^2=4T(k+1)+\frac12.
```

Dropping another global phase and setting $`\theta=4Jt`$ gives triangular frequencies. Negative integer arguments fold into the same set by $`T(n)=T(1-n)`$. For $`N\ge3`$, the projective period in $`J`$ is $`\pi/(2t)`$. The one-spin Hamiltonian encodes no coupling at all.

Degenerate eigenspaces and ancillas can supply arbitrary vectors at a frequency; they do not add new frequencies. The [cyclic confidence lemma](global_confidence.md) therefore applies to every allowed input and POVM.

## Uniform confidence bound

For every odd prime $`p`$, squares occupy exactly $`(p+1)/2`$ residue classes modulo $`p`$. The triangular-number image has the same size because

```math
8T(n)+1=(2n-1)^2
```

and both the input affine map and multiplication by $`8`$ are invertible modulo an odd prime. Given any finite set of odd primes $`\mathcal P`$, let $`M=\prod_{p\in\mathcal P}p`$. The Chinese remainder theorem bounds the fraction of available residues by

```math
\frac{D}{M}
\le\prod_{p\in\mathcal P}\frac{p+1}{2p}.
```

For a uniform phase prior, every protocol thus satisfies

```math
\Pr\!\left\{d(\hat\theta,\theta)<\frac\pi M\right\}
\le\prod_{p\in\mathcal P}\frac{p+1}{2p},
```

uniformly in $`N`$. The product tends to zero along a growing set of odd primes. First fix enough primes to make it smaller than any prescribed tolerance; then shrink the error window below $`\pi/M`$. This proves vanishing success probability in every shrinking phase window, uniformly over the input and the register size within either parity subsequence.

## Transfer to a real coupling prior

Let $`f(J)`$ be the fixed prior density. For even $`N`$, push it forward by $`J\mapsto2tJ\bmod2\pi`$; for odd $`N`$, use $`J\mapsto4tJ\bmod2\pi`$. Each pushforward is an absolutely continuous phase distribution. More explicitly, for either fixed factor $`c\in\{2t,4t\}`$, its density with respect to ordinary phase Lebesgue measure is

```math
\widetilde f_c(\theta)
=\frac1c\sum_{r\in\mathbb Z}
f\!\left(\frac{\theta+2\pi r}{c}\right)
```

almost everywhere. It is nonnegative and integrates to one. Truncation of an integrable density, as proved in [global confidence](global_confidence.md), transfers the uniform-prior result to this fixed density.

If a real-valued estimator satisfies $`|\hat J-J|<\delta`$, its phase report $`c\hat J\bmod2\pi`$ has wrapped error less than $`c\delta`$. Therefore, for every $`\delta_N\to0`$,

```math
\sup_{\text{allowed inputs and POVMs}}
\Pr\{|\hat J-J|<\delta_N\}\longrightarrow0.
```

Both parity subsequences have the same vanishing conclusion, so it holds along the complete sequence of register sizes. Restricting the prior to one projective period is unnecessary.

## What the corollary says operationally

The rapidly growing quadratic generator does not by itself make one uninterrupted fixed-time interrogation globally consistent. Choosing a different input or adding a final collective measurement cannot fill the missing cyclic frequencies. The theorem does not imply that the exact optimum becomes monotonically worse with each additional spin; it rules out nonvanishing confidence in a shrinking window.

The fixed Hamiltonian family is essential. Controls during the evolution, multiple exposures, a duration $`t_N\to0`$, or an $`N`$-dependent normalization such as $`J/N`$ change its frequencies or resource scaling. Coherent selection among different interacting particle numbers also changes the family: $`-JN/2`$ is then no longer one scalar phase on the whole coherent state. None of these changes is included in this corollary.
