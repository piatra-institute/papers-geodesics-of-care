"""Run five deterministic illustrations and render their three figures.

Numerical methods use finite differences, midpoint quadrature and bisection.
PASS denotes completed execution, not empirical confirmation of a theory.
"""
from __future__ import annotations

import json
import platform
import sys
from pathlib import Path

import matplotlib
import numpy as np

from analyses import run
from figures import plot_geometry, plot_effort, plot_entropy

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    plot_geometry(results, OUT / "figures" / "geometry.png")
    plot_effort(results, OUT / "figures" / "care.png")
    plot_entropy(results, OUT / "figures" / "entropy.png")
    results["execution"] = {"status": "PASS", "exit_code": 0}
    results["runtime"] = {"python": platform.python_version(), "executable": sys.executable,
                          "numpy": np.__version__, "matplotlib": matplotlib.__version__,
                          "platform": platform.platform(), "stochastic": False}
    (OUT / "results.json").write_text(json.dumps(results, indent=2, allow_nan=False) + "\n")
    print("Five deterministic illustrations completed; no empirical hypothesis tested.")
    print("Base curvature max absolute error:", results["manifold"]["curvature_max_abs_error"])
    print("Conformal curvature max absolute error:", results["effort"]["curvature_max_abs_error"])
    print("Assigned utility cost of the entropy floor:", results["entropy"]["utility_cost_of_floor"])
    print("Actions after revocation:", results["permission"]["actions_after_revocation"])
    print("Wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
