# A four-photon protocol with selected pair controls

Four photons suffice for a strict improvement over the optimal three-use uniform-prior risk. The construction uses four sensing modes, a four-dimensional code, and known one- and two-mode controls that preserve the total photon number. The controls are nonlinear, number-selected operations; their action is specified on the entire fixed-photon sector, not only on the intended code words.

## Code and risk

Use the ordered code

| Index | Fock state | Kerr frequency $`\sum_i\binom{n_i}{2}`$ | Cubic frequency $`\sum_i\binom{n_i}{3}`$ |
|---|---|---:|---:|
| $`0`$ | $`\lvert1,1,1,1\rangle`$ | $`0`$ | $`0`$ |
| $`1`$ | $`\lvert2,1,1,0\rangle`$ | $`1`$ | $`0`$ |
| $`2`$ | $`\lvert0,2,2,0\rangle`$ | $`2`$ | $`0`$ |
| $`3`$ | $`\lvert3,1,0,0\rangle`$ | $`3`$ | $`1`$ |

Write these states as $`|e_j\rangle`$. Define

```math
a=\sqrt{\frac{5-\sqrt5}{20}},
\qquad
b=\sqrt{\frac{5+\sqrt5}{20}},
\qquad
|\psi\rangle=a|e_0\rangle+b|e_1\rangle+b|e_2\rangle+a|e_3\rangle.
```

One call to the unknown gate on each mode produces

```math
|\psi_{\theta,\beta}\rangle
=e^{-4i\beta}\sum_{j=0}^{3}a_j e^{-ij\theta}|e_j\rangle,
\qquad
(a_0,a_1,a_2,a_3)=(a,b,b,a).
```

The common unknown linear phase is a scalar. The finite Fourier measurement below gives, for every $`\theta,\beta`$,

```math
R_4=2-2\cos\frac\pi5
=\frac{3-\sqrt5}{2}
\simeq0.3819660113.
```

This is less than $`2-\sqrt2\simeq0.5857864376`$, the [three-use lower bound](query_thresholds.md#one-to-three-uses-with-an-unknown-common-linear-phase). That comparison uses the same common-phase model and includes arbitrary adaptive three-use protocols.

## The selected pair primitive

For ordered participating modes $`p,q`$ and pair occupations $`L=(l_1,l_2)`$, $`R=(r_1,r_2)`$ with equal total occupation, define

```math
H_{pq}^{L\to R}
=i|R\rangle\langle L|-i|L\rangle\langle R|,
\qquad
R_{pq}^{L\to R}(t)=e^{-itH_{pq}^{L\to R}}.
```

The Hamiltonian is tensored with identity on all spectator modes and is zero on all other pair occupations. Thus

```math
\begin{aligned}
|L\rangle&\longmapsto
\cos t\,|L\rangle+\sin t\,|R\rangle,\\
|R\rangle&\longmapsto
-\sin t\,|L\rangle+\cos t\,|R\rangle.
\end{aligned}
```

The selection refers only to the two participating modes. It acts for every allowed spectator occupation, so unwanted transitions cannot be removed merely by projecting the gate definition onto the code. Since $`l_1+l_2=r_1+r_2`$, the primitive conserves the total cavity photon number.

An ordinary beamsplitter has many occupation-dependent matrix elements and does not implement this selected primitive. In particular, the selected $`|20\rangle\leftrightarrow|02\rangle`$ swap below is a nonlinear control.

## Four-gate preparation

Initialize the four modes in $`|e_3\rangle=|3,1,0,0\rangle`$. Introduce the temporary state $`|e_2^{\mathrm{old}}\rangle=|2,2,0,0\rangle`$ and the parking operation

```math
S=R_{13}^{20\to02}(\pi/2).
```

Apply these four operations in the listed order:

| Step | Operation | Effect on the occupied support |
|---|---|---|
| 1 | $`R_{12}^{31\to22}(\arccos a)`$ | Leaves amplitude $`a`$ on $`e_3`$ and transfers the remaining amplitude to $`e_2^{\mathrm{old}}`$. |
| 2 | $`R_{23}^{20\to11}(\arccos[b/\sqrt{1-a^2}])`$ | Leaves amplitude $`b`$ on $`e_2^{\mathrm{old}}`$ and transfers amplitude $`1/\sqrt2`$ to $`e_1`$. |
| 3 | $`S`$ | Maps $`e_2^{\mathrm{old}}`$ to $`e_2`$ and fixes the other occupied states. |
| 4 | $`R_{14}^{20\to11}(\arctan(a/b))`$ | Splits the $`e_1`$ amplitude into $`b e_1+a e_0`$. |

The spectator checks make the sequence exact. In step 2, $`e_3`$ has pair occupation $`(n_2,n_3)=(1,0)`$ and is unaffected. In step 3, $`e_3`$ and $`e_1`$ have pair occupations $`(n_1,n_3)=(3,0)`$ and $`(2,1)`$, neither selected. In step 4, the parked state $`e_2`$ has $`(n_1,n_4)=(0,0)`$ and $`e_3`$ has $`(3,0)`$, so both are fixed.

The amplitudes follow from $`a^2+b^2=1/2`$. After step 2 the remaining tail has norm

```math
\sqrt{1-a^2-b^2}=\frac1{\sqrt2},
```

and the last rotation has cosine $`\sqrt2b`$ and sine $`\sqrt2a`$. Three variable-angle selected pair rotations and one selected swap therefore prepare the sine state exactly. The four sensing modes contain exactly four photons throughout the sequence.

## Logical rotations from one- and two-mode gates

Define the adjacent logical rotations

```math
\mathcal R_j(t)
=\exp\!\left[
t\bigl(|e_{j+1}\rangle\langle e_j|
      -|e_j\rangle\langle e_{j+1}|\bigr)
\right],
\qquad j=0,1,2.
```

The first edge is direct:

```math
\mathcal R_0(t)
=R_{14}^{20\to11}(-t)
\quad\text{on the code}.
```

The third edge uses parking:

```math
\mathcal R_2(t)
=S^\dagger R_{12}^{31\to22}(t)S
\quad\text{on the code}.
```

Under the stated real-rotation convention, $`S|e_2\rangle=-|e_2^{\mathrm{old}}\rangle`$ and $`S^\dagger|e_2^{\mathrm{old}}\rangle=-|e_2\rangle`$. These signs produce the logical orientation in the displayed formula. The other code states are fixed by $`S`$.

### A parity echo for the middle edge

After un-parking, the Hamiltonian

```math
H=H_{23}^{20\to11}
```

couples the desired pair $`e_2^{\mathrm{old}}\leftrightarrow e_1`$. It also couples

```math
|e_0\rangle=|1,1,1,1\rangle
\longleftrightarrow
|u\rangle=|1,2,0,1\rangle.
```

The latter transition must be canceled. Use the known two-mode cross-Kerr phase

```math
C=e^{i\pi n_1n_2}.
```

In each selected $`H`$ doublet, $`n_2`$ changes by one and $`n_1`$ is a spectator. Consequently,

```math
CHC^\dagger=(-1)^{n_1}H
```

block by block. The desired doublet has $`n_1=2`$ and keeps its sign; the unwanted doublet has $`n_1=1`$ and changes sign. The two Hamiltonians commute because each doublet is multiplied only by a scalar sign. Therefore

```math
\begin{aligned}
\mathcal E(t)
&=e^{-itH/2}C e^{-itH/2}C^\dagger\\
&=\exp\!\left[-\frac{it}{2}(H+CHC^\dagger)\right]
\end{aligned}
```

performs the desired rotation and cancels the unwanted one exactly. The state $`e_3`$ has pair occupation $`(n_2,n_3)=(1,0)`$ and does not participate. Hence

```math
\mathcal R_1(t)=S^\dagger\mathcal E(t)S
\quad\text{on the code}.
```

The echo can act on other states outside the code; its restriction to the code has no leakage. All gates in the sequence preserve the total photon number.

### Logical phases and an explicit Fourier compilation

The mode-1 occupations of $`e_0,e_1,e_2,e_3`$ are $`1,2,0,3`$, respectively. A single-mode number-dependent phase gate

```math
P=\sum_{n=0}^4 e^{i\varphi_n}|n\rangle\langle n|
```

on mode 1 therefore supplies any diagonal logical phase. This is a finite SNAP control. [SNAP-based oscillator control](../references/RELATED_WORK.md#krastanov2015) gives a relevant single-mode control framework; it does not by itself implement the selected two-mode exchanges or the cross-Kerr echo above.

These diagonal gates and the three adjacent rotations give a constructive compilation of the logical Fourier transform

```math
(F_4)_{mj}=\frac12 e^{2\pi imj/4}.
```

To specify the compilation, apply adjacent-row QR elimination to $`F_4`$. For columns $`c=0,1,2`$, eliminate rows $`r=3,\ldots,c+1`$ in descending order, using the adjacent rows $`r-1,r`$. If their column entries are $`x,y`$, choose $`t,\phi`$ with

```math
\cos t=\frac{|x|}{\sqrt{|x|^2+|y|^2}},
\qquad
\sin t=\frac{|y|}{\sqrt{|x|^2+|y|^2}},
\qquad
\phi=\arg y-\arg x.
```

Take $`\arg0=0`$ for this prescription; a zero $`y`$ needs no rotation. The corresponding two-level elimination matrix is

```math
G=
\begin{pmatrix}
\cos t & e^{-i\phi}\sin t\\
-e^{i\phi}\sin t & \cos t
\end{pmatrix}
=
\begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix}
\mathcal R_{r-1}(-t)
\begin{pmatrix}1&0\\0&e^{-i\phi}\end{pmatrix}.
```

The displayed factors are their restrictions to the two selected logical rows; they fix the other code words. The matrix removes $`y`$. There are at most $`3+2+1=6`$ adjacent eliminations. The remaining upper-triangular unitary is diagonal, so reversing the eliminations and applying this diagonal reconstructs $`F_4`$. The preceding formulas compile each factor into the specified physical pair gates and mode-1 SNAP phases. No rotation is selected on the occupations of all four modes.

## Two offset Fourier grids

For any $`K`$ consecutive frequencies, let

```math
|e_\phi\rangle=\sum_{j=0}^{K-1}e^{-ij\phi}|j\rangle,
\qquad
E_\ell=\frac1{2K}|e_{\pi\ell/K}\rangle
                     \langle e_{\pi\ell/K}|,
\quad 0\le\ell<2K.
```

A fair classical bit chooses between the Fourier grids

```math
\phi_m=\frac{2\pi m}{K},
\qquad
\phi_m=\frac{2\pi m}{K}+\frac\pi K.
```

For each grid the normalized vectors $`|e_{\phi_m}\rangle/\sqrt K`$ form an orthonormal basis. The equally weighted union is exactly the displayed $`2K`$-outcome POVM. It can be realized by a phase offset $`Z(\alpha)=\operatorname{diag}(e^{ij\alpha})`$ before the same $`F_K`$ and ordinary basis measurement.

For $`K=4`$, choose $`\alpha=0`$ or $`\pi/4`$, apply the corresponding mode-1 SNAP and compiled $`F_4`$, measure the final Fock word, and report $`2\pi m/4+\alpha`$. This gives eight outcomes using one classical random bit.

The [finite Fourier risk identity](coherent_preparation.md#a-finite-readout-with-exact-pointwise-risk) gives, for real amplitudes and an ideal frequency encoding,

```math
R(\theta)=2-2\sum_{j=0}^{K-2}a_ja_{j+1}
```

at every $`\theta`$. A single $`K`$-point PVM has pointwise risk

```math
2-2\sum_{j=0}^{K-2}a_ja_{j+1}
-2a_0a_{K-1}\cos[K(\theta-\alpha)].
```

The second offset reverses the endpoint term, and the fair mixture cancels it. The calculation also follows directly from discrete Fourier orthogonality: after multiplication by the loss's first harmonic, the $`2K`$ grid has no unintended endpoint alias. Thus the finite eight-outcome realization attains $`R_4`$ pointwise, rather than only after averaging over the prior.

## Control resources and verification

The protocol uses four unknown-gate calls. Preparation uses three variable-angle selected rotations and one selected swap after initialization in $`|3,1,0,0\rangle`$. Readout uses a constant number of selected pair rotations, parking swaps, cross-Kerr phases, and mode-1 SNAP phases through the explicit six-elimination compilation, followed by one Fock measurement. Every one of these ideal gates preserves the four-mode photon total.

The pair-selective rotations and the calibrated cross-Kerr gate are assumptions of this finite control construction. Published [multimode sideband control](../references/RELATED_WORK.md#huang2026sideband) and [single-oscillator JC control](../references/RELATED_WORK.md#huang2026jc) support physical ingredients for nonlinear bosonic control, but do not establish the fidelity or duration of this complete network.

The reproducible [physical verification](../verification/verify_physical.py) constructs each pair primitive on all $`\binom{7}{3}=35`$ four-photon Fock states. It checks the prepared amplitudes, spectator cancellation, the compiled logical Fourier transform, and the eight-outcome risk. The analytical block arguments establish the control identities; the full-sector computation checks their indexing, signs, and composition. Coherent cubic-phase effects are treated separately in [robustness](robustness.md).

