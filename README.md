# Geodesics of Care: Concern as Transport on the Manifold of Viability

Care is usually studied as a feeling, a virtue, or a practice. This paper takes a colder primitive: system A cares for B when B's *viability* enters A's perception, model, and choice of action. The claim is that this relation has a genuine geometry, and that the geometry is the **information geometry** of the other's viability. Represent B as a distribution over the states in which it can persist; the space of such distributions is a statistical manifold whose metric is not chosen but forced, since Chentsov's theorem makes the **Fisher-Rao metric** the only one invariant under sufficient statistics. On the three-state simplex it is a sphere of radius 2 with constant curvature a quarter, a value a from-scratch Brioschi curvature routine recovers to machine precision. Care is then *transport*: moving B along a geodesic toward the viable region, with the **care-distance** the geodesic's length. Three results follow from the construction. Care-distance is a genuine metric, so it obeys the triangle inequality (correcting an earlier quasi-metric framing) and the real obstruction is **curvature**: a care-triangle carries a measurable spherical excess, a quarter of its area, by Gauss-Bonnet. Direction enters through the carer's **control metric**, a conformal reweighting whose curvature is no longer constant and under which a distant stranger costs 5× what kin cost along the same path. And the **autonomy constraint** becomes a boundary fact: total coercion drives B to a zero-entropy vertex, which is Canguilhem's definition of the pathological, a life reduced to a single norm; holding B off that boundary costs little viability, while abandonment costs half. What the geometry cannot reach is the inside of the relation, and the paper ends there, with Ruyer's *survol absolu*.

## Contents

- `paper/PAPER.md` — the paper (7 sections); `paper/PAPER.pdf` — the build.
- `simulation/` — four exact, deterministic information-geometry studies (manifold self-test, Gauss-Bonnet routing, directed care, the price of autonomy), plus three embedded figures. Entry point `run_all.py`; see `simulation/README.md`.
- `brief.md`, `research.md`, `sources.md`, `audit.md` — provenance: the pre-research brief, tiered findings, the frozen bibliography, the dated pass log.
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

Every decimal in the paper is a key in `simulation/output/results.json`. All four studies are deterministic (exact Fisher-Rao geometry, closed-form Gauss-Bonnet, exact entropy-constrained optimum); there is no seed. The curvature routine's recovery of the exact value 0.25 for the base Fisher metric is the self-test that certifies the differential-geometry machinery.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
