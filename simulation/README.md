# Simulation — Geodesics of Care

Three exact, deterministic analyses behind §7 of the paper. No random seed: every number is exact arithmetic, exact dynamic programming, or a closed-form KL.

```bash
cd simulation
uv run run_all.py      # writes output/results.json and output/figures/*.png
```

Every decimal cited in §7 is a key in `output/results.json` (the `papers claims` gate checks the paper's prose decimals against it).

## What it computes

`analyses.py`

- **`care_quasimetric`** — the direct-coupling cost `d(X→Y) = repcost + actcost`, with representational cost convex (squared) in category distance and action cost set by the helper's capability. Yields the asymmetry `d(A→B)=1.2 ≠ d(B→A)=1.5` and the triangle-inequality failure `d(A→C)=4.2 > d(A→B)+d(B→C)=2.7`. Care-distance is a directed quasi-metric.
- **`price_of_autonomy`** — a finite-horizon control problem on a 9-state viability ladder (death absorbing at the bottom), horizon 8, start mid-ladder. A carer sets the distribution over B's move at each state to maximise B's expected terminal viability, subject to a floor on the Shannon entropy of that distribution (the autonomy constraint). Solved by exact backward induction over a denominator-12 menu of distributions, so the floors `ln 2` and `ln 3` are hit exactly. Coercion (H=0) reaches viability 1.0 with zero options; autonomy-preserving care (H≥ln2) reaches 0.972; abandonment (H=ln3, unguided random walk) falls to 0.495 with death probability 0.088. Price of autonomy = 0.028.
- **`care_curvature`** — κ, the policy deformation in nats (Bernoulli KL from a baseline help-probability 0.1) required per unit of viability delivered (gain 0.2), as relational efficacy falls. Kin 0.768, stranger 2.554, distant stranger 8.789; distant/kin = 11.44×.

`figures.py` (pure plotters, read the results dict)

- `output/figures/autonomy.png` — viability vs the option-entropy floor (the price of autonomy), and the terminal-state distributions under each regime.
- `output/figures/curvature.png` — κ vs relational curvature with kin/stranger/distant marked, and the quasi-metric (asymmetry bars + triangle-failure bars).

## Status

Complete and minimal. The model is a fact about itself: it shows the structural features claimed for care-distance are realizable and coherent, not that any empirical agent exhibits these particular magnitudes (the "calibration is not fitting" discipline). Dependencies: `matplotlib` only (see `pyproject.toml`).
