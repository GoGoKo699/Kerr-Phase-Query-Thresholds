"""Finite checks of the four-photon selected-pair Kerr protocol.

The matrices act on the complete 35-state four-photon Fock sector.
This checks finite formulas and circuit composition, not hardware accuracy
or an asymptotic law inferred from numerical data. Requires NumPy only.
"""
import json
import math

import numpy as np


def run():
    """Return a deterministic JSON-compatible verification report."""
    basis = [
        (a, b, c, 4 - a - b - c)
        for a in range(5)
        for b in range(5 - a)
        for c in range(5 - a - b)
    ]
    index = {state: j for j, state in enumerate(basis)}
    dimension = len(basis)
    logical = [(1, 1, 1, 1), (2, 1, 1, 0), (0, 2, 2, 0), (3, 1, 0, 0)]
    code = np.eye(dimension)[:, [index[state] for state in logical]]
    identity = np.eye(dimension, dtype=complex)
    tolerance = 1e-12

    def selected_pair_hamiltonian(p, q, left, right):
        """i|right><left|-i|left><right|, identity on spectators.

        Modes are zero based. This is a selected nonlinear pair operation,
        not an ordinary beamsplitter and not a projection onto the code.
        """
        assert sum(left) == sum(right)
        H = np.zeros((dimension, dimension), dtype=complex)
        for j, state in enumerate(basis):
            if (state[p], state[q]) == left:
                target = list(state)
                target[p], target[q] = right
                k = index[tuple(target)]
                H[k, j] = 1j
                H[j, k] = -1j
        return H

    def rotate(H, angle):
        # H is a direct sum of Pauli-Y blocks and zero blocks, so H^3=H.
        return identity - 1j * math.sin(angle) * H + (math.cos(angle) - 1) * (H @ H)

    def logical_diagonal(phases):
        # Occupations n1=1,2,0,3 uniquely identify logical states 0,1,2,3.
        by_occupation = {state[0]: phase for state, phase in zip(logical, phases)}
        return np.diag([
            np.exp(1j * by_occupation.get(state[0], 0.0))
            for state in basis
        ])

    H14 = selected_pair_hamiltonian(0, 3, (2, 0), (1, 1))
    H12 = selected_pair_hamiltonian(0, 1, (3, 1), (2, 2))
    H23 = selected_pair_hamiltonian(1, 2, (2, 0), (1, 1))
    H13 = selected_pair_hamiltonian(0, 2, (2, 0), (0, 2))
    S = rotate(H13, math.pi / 2)
    C = np.diag([complex((-1) ** (state[0] * state[1])) for state in basis])

    def logical_rotation(edge, angle):
        """Canonical adjacent logical rotation, implemented physically."""
        if edge == 0:
            return rotate(H14, -angle)
        if edge == 1:
            echo = rotate(H23, angle / 2) @ C @ rotate(H23, angle / 2) @ C.conj().T
            return S.conj().T @ echo @ S
        if edge == 2:
            return S.conj().T @ rotate(H12, angle) @ S
        raise ValueError("Logical edge must be 0, 1, or 2.")

    a = math.sqrt((5 - math.sqrt(5)) / 20)
    b = math.sqrt((5 + math.sqrt(5)) / 20)
    amplitudes = np.array([a, b, b, a])
    angles = [
        math.acos(a),
        math.acos(b / math.sqrt(1 - a * a)),
        math.pi / 2,
        math.atan(a / b),
    ]
    prepared = identity[:, index[logical[3]]]
    for H, angle in zip([H12, H23, H13, H14], angles):
        prepared = rotate(H, angle) @ prepared
    amplitude_error = np.max(np.abs(code.conj().T @ prepared - amplitudes))
    preparation_leakage = np.linalg.norm(prepared - code @ (code.conj().T @ prepared))
    assert amplitude_error < tolerance
    assert preparation_leakage < tolerance

    edge_checks = {}
    angle = 0.371
    for edge in range(3):
        U = logical_rotation(edge, angle)
        expected = np.eye(4, dtype=complex)
        expected[edge, edge] = expected[edge + 1, edge + 1] = math.cos(angle)
        expected[edge + 1, edge] = math.sin(angle)
        expected[edge, edge + 1] = -math.sin(angle)
        restricted = code.conj().T @ U @ code
        error = np.max(np.abs(restricted - expected))
        leakage = np.linalg.norm(U @ code - code @ restricted)
        assert error < tolerance
        assert leakage < tolerance
        edge_checks[str(edge)] = {
            "matrix_error": float(error),
            "leakage_norm": float(leakage),
        }
    conjugated = C @ H23 @ C.conj().T
    commutator_error = np.linalg.norm(H23 @ conjugated - conjugated @ H23)
    assert commutator_error < tolerance

    # Compile F4 by adjacent-row QR elimination, each complex Givens factor
    # being made from the physical pair circuit and a mode-1 SNAP.
    K = 4
    logical_indices = np.arange(K)
    F4 = np.exp(2j * math.pi * np.outer(logical_indices, logical_indices) / K) / math.sqrt(K)
    reduced = F4.copy()
    eliminations = []
    compilation_angles = []
    for column in range(K - 1):
        for row in range(K - 1, column, -1):
            edge = row - 1
            x, y = reduced[edge, column], reduced[row, column]
            if abs(y) < 1e-14:
                continue
            angle = math.atan2(abs(y), abs(x))
            phi = float(np.angle(y) - (np.angle(x) if abs(x) > 1e-14 else 0.0))
            G = np.eye(K, dtype=complex)
            G[edge, edge] = G[row, row] = math.cos(angle)
            G[edge, row] = np.exp(-1j * phi) * math.sin(angle)
            G[row, edge] = -np.exp(1j * phi) * math.sin(angle)
            phases = np.zeros(K)
            phases[row] = phi
            phase_gate = logical_diagonal(phases)
            G_physical = phase_gate @ logical_rotation(edge, -angle) @ phase_gate.conj().T
            assert np.max(np.abs(code.conj().T @ G_physical @ code - G)) < tolerance
            reduced = G @ reduced
            eliminations.append(G_physical)
            compilation_angles.append({
                "column": column,
                "edge": edge,
                "angle": angle,
                "phase": phi,
            })
    assert len(eliminations) <= 6
    assert np.linalg.norm(reduced - np.diag(np.diag(reduced))) < tolerance
    compiled_F4 = logical_diagonal(np.angle(np.diag(reduced)))
    for G_physical in reversed(eliminations):
        compiled_F4 = G_physical.conj().T @ compiled_F4
    compiled_error = np.max(np.abs(code.conj().T @ compiled_F4 @ code - F4))
    compiled_leakage = np.linalg.norm(compiled_F4 @ code - code @ F4)
    assert compiled_error < tolerance
    assert compiled_leakage < tolerance

    J = 2 * K
    phases = 2 * math.pi * np.arange(J) / J
    E = np.exp(-1j * np.outer(phases, logical_indices))
    resolution_error = np.linalg.norm(E.conj().T @ E / J - np.eye(K))
    assert resolution_error < tolerance
    theta_values = [0.0, 0.1, math.pi / 7, 1.0, 2.9, math.pi, 2 * math.pi - 0.003]
    pointwise_risks = []
    ideal_risk = (3 - math.sqrt(5)) / 2
    physical_risk_error = 0.0
    for theta in theta_values:
        state = amplitudes * np.exp(-1j * theta * logical_indices)
        probabilities = np.abs(E.conj() @ state) ** 2 / J
        risk = float(np.dot(probabilities, 2 - 2 * np.cos(phases - theta)))
        assert abs(probabilities.sum() - 1) < tolerance
        assert abs(risk - ideal_risk) < tolerance
        # Explicit equal mixture of the two compiled physical PVMs.
        physical_risk = 0.0
        physical_state = code @ state
        for bit in [0, 1]:
            offset = bit * math.pi / K
            Z = logical_diagonal(logical_indices * offset)
            outcomes = code.conj().T @ compiled_F4 @ Z @ physical_state
            p = np.abs(outcomes) ** 2 / 2
            estimates = 2 * math.pi * logical_indices / K + offset
            physical_risk += float(np.dot(p, 2 - 2 * np.cos(estimates - theta)))
        physical_risk_error = max(physical_risk_error, abs(physical_risk - risk))
        pointwise_risks.append({"theta": float(theta), "risk": risk})
    assert physical_risk_error < tolerance

    cubic_risks = []
    for kappa in [0.0, 0.3, 0.99, 1.2]:
        target = ideal_risk + (1 - math.cos(kappa)) / math.sqrt(5)
        observed = []
        for theta in theta_values:
            state = amplitudes * np.exp(-1j * theta * logical_indices)
            state[3] *= np.exp(-1j * kappa)
            probabilities = np.abs(E.conj() @ state) ** 2 / J
            risk = float(np.dot(probabilities, 2 - 2 * np.cos(phases - theta)))
            assert abs(risk - target) < tolerance
            observed.append(risk)
        cubic_risks.append({
            "kappa": kappa,
            "formula": target,
            "maximum_error": max(abs(value - target) for value in observed),
        })

    # The exact readout identity allows normalized residual work states.
    rng = np.random.default_rng(619)
    work = rng.normal(size=(K, 7)) + 1j * rng.normal(size=(K, 7))
    work /= np.linalg.norm(work, axis=1)[:, None]
    work_target = ideal_risk + sum(
        amplitudes[j] * amplitudes[j + 1] * np.linalg.norm(work[j + 1] - work[j]) ** 2
        for j in range(K - 1)
    )
    work_identity_error = 0.0
    for theta in theta_values:
        state = (amplitudes * np.exp(-1j * theta * logical_indices))[:, None] * work
        outcome_work = E.conj() @ state / math.sqrt(J)
        probabilities = np.sum(np.abs(outcome_work) ** 2, axis=1)
        risk = float(np.dot(probabilities, 2 - 2 * np.cos(phases - theta)))
        work_identity_error = max(work_identity_error, abs(risk - work_target))
    assert work_identity_error < tolerance

    # Check the cubic identity exactly in integer arithmetic.
    cubic_identity_checks = 0
    for s in [3, 5, 7, 9, 13]:
        for n1 in range(s + 1):
            for n2 in range(s - n1 + 1):
                for n3 in range(s - n1 - n2 + 1):
                    n4 = s - n1 - n2 - n3
                    ns = (n1, n2, n3, n4)
                    x = n1 + n2 - n3 - n4
                    y = n1 - n2 + n3 - n4
                    z = n1 - n2 - n3 + n4
                    Q = x * x + y * y + z * z
                    h = sum(n * (n - 1) * (n - 2) // 6 for n in ns)
                    assert 96 * h == s**3 + 3 * (s - 4) * Q - 12 * s * s + 32 * s + 6 * x * y * z
                    cubic_identity_checks += 1

    # Finite oracle witnesses. Legendre's theorem supplies the all-N result.
    arithmetic_checks = 0
    for s in [5, 7, 9, 15, 25, 39]:
        lo = (s * s - 4 * s + 3) // 8
        hi = s * (s - 3) // 6
        for g in range(lo, hi + 1):
            Q = 8 * g + 4 * s - s * s
            found = False
            for x in range(1, math.isqrt(Q) + 1, 2):
                for y in range(1, math.isqrt(max(0, Q - x * x)) + 1, 2):
                    residual = Q - x * x - y * y
                    if residual < 0:
                        continue
                    z = math.isqrt(residual)
                    if z * z != residual or z % 2 == 0:
                        continue
                    if (s + x + y + z) % 4:
                        z = -z
                    nums = (s + x + y + z, s + x - y - z,
                            s - x + y - z, s - x - y + z)
                    assert all(value >= 0 and value % 4 == 0 for value in nums)
                    occupations = [value // 4 for value in nums]
                    assert sum(occupations) == s
                    assert sum(n * (n - 1) // 2 for n in occupations) == g
                    found = True
                    break
                if found:
                    break
            assert found
            arithmetic_checks += 1

    return {
        "numpy_version": np.__version__,
        "dimension": dimension,
        "logical_states": logical,
        "amplitudes": [float(value) for value in (code.conj().T @ prepared).real],
        "preparation_amplitude_error": float(amplitude_error),
        "preparation_leakage_norm": float(preparation_leakage),
        "logical_edge_checks": edge_checks,
        "echo_commutator_norm": float(commutator_error),
        "fourier_eliminations": compilation_angles,
        "compiled_fourier_error": float(compiled_error),
        "compiled_fourier_leakage_norm": float(compiled_leakage),
        "two_physical_grids_risk_error": float(physical_risk_error),
        "povm_resolution_error": float(resolution_error),
        "pointwise_risks": pointwise_risks,
        "cubic_perturbation_checks": cubic_risks,
        "general_work_state_identity_error": float(work_identity_error),
        "finite_cubic_identity_checks": cubic_identity_checks,
        "finite_arithmetic_oracle_checks": arithmetic_checks,
        "cubic_threshold_radians": math.acos((2 * math.sqrt(10) - math.sqrt(5) - 3) / 2),
        "status": "All finite checks passed; analytical arguments establish general claims.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

