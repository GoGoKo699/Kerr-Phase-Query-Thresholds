"""Run the documented finite checks and compare committed expected outputs."""

import importlib
import json
from math import isclose
from pathlib import Path


def compare(actual, expected, path="result"):
    if isinstance(expected, dict):
        assert isinstance(actual, dict) and actual.keys() == expected.keys(), path
        for key in expected:
            compare(actual[key], expected[key], path+"."+key)
    elif isinstance(expected, list):
        assert isinstance(actual, list) and len(actual) == len(expected), path
        for index, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, path+f"[{index}]")
    elif isinstance(expected, float):
        assert isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-10), (path, actual, expected)
    else:
        assert actual == expected, (path, actual, expected)


def main():
    base = Path(__file__).resolve().parent
    for name in ("verify_arithmetic", "verify_access", "verify_physical"):
        module = importlib.import_module(name)
        check = getattr(module, "verify", None) or module.run
        actual = json.loads(json.dumps(check()))
        expected = json.loads((base/"expected"/(name+".json")).read_text())
        compare(actual, expected, name)
        print(f"PASS {name}")
    print("All finite checks passed and matched committed outputs.")
    print("Universal and asymptotic claims rely on the written proofs and cited theorems.")


if __name__ == "__main__":
    main()
