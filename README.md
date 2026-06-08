# Geodesics of Care: A Scale-Free Geometry of Concern

Care is usually studied as an emotion or a virtue. This paper treats it as a measurable relation: system A cares for B when B's *viability* enters A's perception, model, valuation, and action. The least-cost admissible path by which A comes to reach B, the **care-distance**, is a *directed quasi-metric*, it is asymmetric and can violate the triangle inequality, so the moral world is a curved, broken manifold rather than a circle around the self. The paper gives the manifold's vocabulary (radius, diameter, depth, curvature, topology, singularity) working definitions, fixes the **autonomy constraint** that separates care from domination (and coincides, exactly, with the AI corrigibility requirement), and reads moral psychology as the measurement of curvature and institutions as engineered care-geometries. A minimal control model, solved exactly, makes three claims concrete: the quasi-metric; the **price of autonomy** (preserving B's option-entropy costs only 0.028 of B's viability, against the ~0.5 lost to abandonment); and **care-curvature** (a distant stranger costs 11.44× the policy deformation per unit of good done that kin cost). The account is organizational and bounded: it measures coupling, cost, and the preservation of agency, and it does not measure, or explain, what concern feels like.

## Contents

- `paper/PAPER.md` — the paper (10 sections); `paper/PAPER.pdf` — the build.
- `simulation/` — three exact, deterministic analyses behind §7, plus the two embedded figures. Entry point `run_all.py`; see `simulation/README.md`.
- `brief.md`, `research.md`, `sources.md`, `audit.md` — provenance: the pre-research brief, tiered findings, the frozen 34-entry bibliography, the dated pass log.
- `chats/` — the origin chats (gitignored, kept local).

## Build

```bash
papers build geodesics-of-care      # from the workspace root (or: uv run build.py)
```

Requires `pandoc` and `xelatex` on PATH. The figures resolve from `paper/PAPER.md` via pandoc's `--resource-path`, so the repo stays portable.

## Reproduce the numbers

```bash
cd simulation && uv run run_all.py   # -> output/results.json + output/figures/
```

Every decimal in §7 is a key in `simulation/output/results.json`. All three analyses are deterministic (exact arithmetic, exact dynamic programming, closed-form KL); there is no seed.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
