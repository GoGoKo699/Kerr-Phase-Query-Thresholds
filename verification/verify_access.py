"""Finite Fourier probabilities for the shortened-call and inverse examples."""

import json
from math import isqrt
import numpy as np


def verify():
    shortened = []
    largest_normalization_error = 0.0
    largest_formula_error = 0.0
    for cap in (9, 25, 101, 401, 1601):
        odd = cap if cap % 2 else cap-1
        n0 = (odd+1)//2
        length = isqrt(odd)
        k = np.arange(-length, length+1, dtype=float)
        occupations = n0+k
        dimension = len(k)
        j = np.arange(dimension, dtype=float)
        assert min(occupations) >= 0 and max(occupations) <= cap
        coefficients = np.sqrt(2/(dimension+1))*np.sin((j+1)*np.pi/(dimension+1))
        grid = np.pi*np.arange(2*dimension)/dimension
        readout = np.exp(1j*grid[:,None]*j[None,:])/np.sqrt(2*dimension)
        ideal_risk = 2*(1-np.cos(np.pi/(dimension+1)))
        risk_values = []
        for theta, beta in ((0.,0.), (.123,1.234), (np.pi,2*np.pi-.01), (2*np.pi-.001,.5)):
            amplitudes = coefficients*np.exp(-1j*(2/odd)*(
                theta*occupations*(occupations-1)/2+beta*occupations))
            probabilities = abs(readout @ amplitudes)**2
            measured = float(np.dot(probabilities, 4*np.sin((grid-theta)/2)**2))
            formula = float(ideal_risk+2*np.sum(coefficients[:-1]*coefficients[1:]
                *(1-np.cos((theta*(2*k[:-1]+1)+2*beta)/odd))))
            norm_error = abs(float(sum(probabilities))-1)
            formula_error = abs(measured-formula)
            assert norm_error < 1e-11 and formula_error < 1e-10
            largest_normalization_error = max(largest_normalization_error, norm_error)
            largest_formula_error = max(largest_formula_error, formula_error)
            risk_values.append(round(measured, 12))
        shortened.append({"cap": cap, "duration_multiplier": 2/odd,
                          "logical_dimension": dimension, "risks": risk_values})

    inverse = []
    for cap in (9, 25, 101):
        dimension = (cap-1)//2+1
        k = np.arange(dimension, dtype=float)
        coefficients = np.sqrt(2/(dimension+1))*np.sin((k+1)*np.pi/(dimension+1))
        grid = np.pi*np.arange(2*dimension)/dimension
        readout = np.exp(1j*grid[:,None]*k[None,:])/np.sqrt(2*dimension)
        for theta, beta in ((.123,1.234), (np.pi,.3)):
            phase = theta*((k+1)*k/2-k*(k-1)/2)+beta*((k+1)-k)
            probabilities = abs(readout @ (coefficients*np.exp(-1j*phase)))**2
            risk = float(np.dot(probabilities,4*np.sin((grid-theta)/2)**2))
            expected = float(2*(1-np.cos(np.pi/(dimension+1))))
            assert abs(float(sum(probabilities))-1) < 1e-11
            assert abs(risk-expected) < 1e-10
        inverse.append({"cap": cap, "logical_dimension": dimension,
                        "risk": round(expected,12)})
    return {"shortened_call": shortened, "inverse_pair": inverse,
            "normalization_tolerance": 1e-11, "risk_formula_tolerance": 1e-10,
            "shortened_cases": 20, "inverse_cases": 6, "status": "passed"}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
