"""Exact finite spectra and arithmetic constructions; no asymptotic inference."""

from itertools import product
import json
from math import isqrt


def triangular(n):
    return n * (n - 1) // 2


def spectrum(q, cap):
    """All (total occupation, Kerr frequency) pairs for q parallel modes."""
    pairs = {(0, 0)}
    for _ in range(q):
        pairs = {
            (s + n, g + triangular(n))
            for s, g in pairs
            for n in range(cap - s + 1)
        }
    sectors = {s: set() for s in range(cap + 1)}
    for s, g in pairs:
        sectors[s].add(g)
    return sectors


def longest(values):
    previous = None
    current = best = 0
    for value in sorted(values):
        current = current + 1 if previous is not None and value == previous + 1 else 1
        best = max(best, current)
        previous = value
    return best


def odd_sector_representative(s, g):
    """Independent bounded search followed by the four-occupation identity."""
    qform = 8 * g + 4 * s - s * s
    assert qform % 8 == 3 and 3 <= qform and 3 * qform <= s * s
    for x in range(1, isqrt(qform) + 1, 2):
        for y in range(1, isqrt(qform) + 1, 2):
            residual = qform - x * x - y * y
            if residual < 0:
                continue
            z = isqrt(residual)
            if z % 2 != 1 or z * z != residual:
                continue
            if (s + x + y + z) % 4:
                z = -z
            numerators = (s + x + y + z, s + x - y - z,
                          s - x + y - z, s - x - y + z)
            assert all(n >= 0 and n % 4 == 0 for n in numerators)
            occupations = tuple(n // 4 for n in numerators)
            assert sum(occupations) == s
            assert sum(map(triangular, occupations)) == g
            return occupations
    raise AssertionError((s, g, qform))


def verify():
    triangular_mod9 = {triangular(n) % 9 for n in range(9)}
    two_mod9 = {(a + b) % 9 for a in triangular_mod9 for b in triangular_mod9}
    assert triangular_mod9 == {0, 1, 3, 6}
    assert set(range(9)) - two_mod9 == {5, 8}
    norms_mod4 = {(u*u-u*v+v*v) % 4 for u, v in product(range(4), repeat=2)}
    assert norms_mod4 == {0, 1, 3}

    unknown_rows = []
    final_sectors = None
    for cap in (4, 7, 9, 15, 25, 39):
        runs = []
        for q in (1, 2, 3, 4):
            sectors = spectrum(q, cap)
            run = max(map(longest, sectors.values()))
            if q <= 3:
                assert run == q
            else:
                s = cap if cap % 2 else cap - 1
                lo = (s*s-4*s+3)//8
                hi = s*(s-3)//6
                assert set(range(lo, hi+1)) <= sectors[s]
                if cap == 39:
                    final_sectors = sectors
            runs.append(run)
        unknown_rows.append({"cap": cap, "longest_runs_q1_to_q4": runs})

    known_rows = []
    for cap in (2, 3, 4, 5, 6, 10, 20, 40):
        runs = []
        for q in (1, 2, 3):
            sectors = spectrum(q, cap)
            available = set().union(*sectors.values())
            run = longest(available)
            if q == 1:
                assert run == 2
            if q == 2 and cap >= 5:
                assert run == 5
            if q == 3:
                maximum = max(0, cap*(cap-3)//6)
                assert set(range(maximum+1)) <= available
            runs.append(run)
        known_rows.append({"cap": cap, "longest_runs_q1_to_q3": runs})

    band_rows = []
    for s in (3, 9, 15, 25, 39):
        lo, hi = (s*s-4*s+3)//8, s*(s-3)//6
        for g in range(lo, hi+1):
            odd_sector_representative(s, g)
        band_rows.append({"s": s, "lo": lo, "hi": hi, "representatives": hi-lo+1})

    parity_rows = []
    for s, frequencies in final_sectors.items():
        if s >= 6 and s % 4 == 2:
            assert longest(frequencies) == 3
            parity_rows.append({"s": s, "longest_run": 3})
        elif s >= 24 and s % 4 == 0:
            assert longest(frequencies) == 15
            parity_rows.append({"s": s, "longest_run": 15})
    triples = [(5,2,1),(4,4,0),(5,3,0),(6,0,0),(6,1,1),
               (6,2,0),(5,4,1),(6,2,2),(6,3,1),(4,4,4),
               (7,1,0),(6,4,0),(7,2,1),(6,4,2),(7,3,0)]
    for j, (u, v, w) in enumerate(triples):
        numerators = (12+u+v+w, 12+u-v-w, 12-u+v-w, 12-u-v+w)
        assert all(n >= 0 and n % 2 == 0 for n in numerators)
        occupations = [n//2 for n in numerators]
        assert sum(occupations) == 24
        assert sum(map(triangular, occupations)) == 75+j

    weighted_rows = []
    for a, b, c in ((1,1,1), (1,2,3), (2,3,5), (1,4,7), (3,3,6)):
        total_weight = a+b+c
        determinant = a*b*c*total_weight
        for occupations in product(range(7), repeat=3):
            s = sum(w*n for w, n in zip((a,b,c), occupations))
            g = sum(w*triangular(n) for w, n in zip((a,b,c), occupations))
            u, v = occupations[0]-occupations[2], occupations[1]-occupations[2]
            assert (2*total_weight*g+total_weight*s-s*s
                    == a*(b+c)*u*u-2*a*b*u*v+b*(a+c)*v*v)
        p = next(p for p in range(3, 80, 2)
                 if all(p % d for d in range(2, isqrt(p)+1))
                 and (2*determinant) % p
                 and pow((-determinant) % p, (p-1)//2, p) == p-1)
        modulus = p*p
        residues = {(a*(b+c)*u*u-2*a*b*u*v+b*(a+c)*v*v) % modulus
                    for u, v in product(range(modulus), repeat=2)}
        assert not residues.intersection(p*k for k in range(1, p))
        assert len(residues) <= modulus-p+1
        weighted_rows.append({"weights": [a,b,c], "prime": p,
                              "modulus": modulus, "occupied_residues": len(residues),
                              "bound": modulus-p+1, "identity_cases": 343})

    return {"known_phase_spectra": known_rows,
            "unknown_phase_spectra": unknown_rows,
            "odd_sector_bands": band_rows,
            "exact_exposure_parity": parity_rows,
            "s24_consecutive_witness": list(range(75,90)),
            "weighted_duration_forms": weighted_rows,
            "status": "passed"}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
