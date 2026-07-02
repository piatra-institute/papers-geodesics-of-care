"""Orchestrator: reproduces every number and figure in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in the
paper is a key in the JSON file. All four studies are deterministic (exact
Fisher-Rao geometry, closed-form Gauss-Bonnet, exact entropy-constrained optimum);
there is no seed.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_geometry, plot_care, plot_autonomy

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_geometry(results, str(OUT / "figures" / "geometry.png"))
    plot_care(results, str(OUT / "figures" / "care.png"))
    plot_autonomy(results, str(OUT / "figures" / "autonomy.png"))

    m, r, d, a = (results["manifold"], results["routing"],
                  results["directed"], results["autonomy"])
    print(f"manifold: curvature self-test {m['curvature_mean']} "
          f"(expected 0.25, max dev {m['curvature_max_abs_dev_from_quarter']}); "
          f"triangle inequality holds={m['triangle_inequality_holds']}")
    print(f"routing:  excess {r['spherical_excess']} = 1/4 x area {r['triangle_area']}; "
          f"routed {r['d_A_to_C_routed']} > direct {r['d_A_to_C_direct']} "
          f"(gap {r['routing_gap']})")
    print(f"directed: asymmetry {d['directed']['asymmetry_ratio']}x; "
          f"distant/kin {d['distant_over_kin']}x; "
          f"care curvature {d['care_curvature_min']}–{d['care_curvature_max']}")
    print(f"autonomy: coercion V={a['viability_coercion']} (H=0) | floor "
          f"V={a['viability_autonomy_floor']} (H>=ln2) | abandon "
          f"V={a['viability_abandonment']}; price {a['price_of_autonomy']}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
