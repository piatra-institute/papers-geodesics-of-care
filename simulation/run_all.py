"""Orchestrator: reproduces every number in the paper's modelled section (§7).

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in the
modelled section is a key in the JSON file. All three analyses are deterministic
(exact arithmetic, exact dynamic programming, closed-form KL); there is no seed.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_autonomy, plot_curvature

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_autonomy(results, str(OUT / "figures" / "autonomy.png"))
    plot_curvature(results, str(OUT / "figures" / "curvature.png"))

    q, a, c = results["quasimetric"], results["autonomy"], results["curvature"]
    print(f"quasi-metric: d(A->B)={q['d_A_to_B']} vs d(B->A)={q['d_B_to_A']} "
          f"(asymmetry {q['asymmetry_gap']}); direct d(A->C)={q['d_A_to_C_direct']} "
          f"> routed {q['d_A_to_C_routed']} (triangle excess {q['triangle_excess']})")
    print(f"autonomy: coercion V={a['coercion']['expected_viability']} (H=0) | "
          f"autonomy-preserving V={a['autonomy']['expected_viability']} (H>=ln2) | "
          f"abandonment V={a['freedom']['expected_viability']} (death "
          f"{a['freedom']['death_probability']}); price of autonomy "
          f"{a['price_of_autonomy']}")
    print(f"curvature: kappa kin={c['relations']['kin']['kappa_nats_per_unit']} "
          f"stranger={c['relations']['stranger']['kappa_nats_per_unit']} "
          f"distant={c['relations']['distant_stranger']['kappa_nats_per_unit']} "
          f"(distant/kin {c['distant_over_kin']}x)")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
