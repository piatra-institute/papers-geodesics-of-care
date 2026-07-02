# Simulation — Geodesics of Care

Four exact, deterministic information-geometry studies behind the paper. No random seed: every number is exact Fisher-Rao geometry, a closed-form Gauss-Bonnet quantity, or an exact entropy-constrained optimum.

```bash
cd simulation
uv run run_all.py      # writes output/results.json and output/figures/*.png
```

Every decimal cited in the paper is a key in `output/results.json` (the `papers claims` gate checks the paper's prose decimals against it).

## The manifold

The cared-for is a distribution over three viability states (failing, coping, flourishing), a point on the 2-simplex. Chentsov's theorem forces the Fisher-Rao metric, under which the map `p -> 2*sqrt(p)` is an isometry onto a sphere of radius 2. The geodesic distance is `d(p,q) = 2*arccos(sum_i sqrt(p_i q_i))`, the great-circle distance, and the constant Gaussian curvature is 1/4.

## What it computes

`analyses.py`

- **`study_manifold`** — the self-test. `gaussian_curvature`, built from the metric components and the Brioschi formula with numerical partials, is fed the Fisher metric on a grid and returns 0.25 with maximum deviation 0.0. Confirms the triangle inequality holds (largest slack 0). This certifies the differential-geometry machinery the other studies rely on.
- **`study_routing`** — Gauss-Bonnet on a care-triangle (failing / coping / flourishing vertices). Interior angles sum to 3.3164; the spherical excess 0.1748 equals 1/4 times the enclosed area 0.6994. Routing `A->B->C` costs 2.34 against the direct `A->C` 1.8862 (gap 0.4539): concern does not route, because the manifold is curved, not because any metric axiom fails.
- **`study_directed`** — direction from the carer's control metric `g_A = f_A * g_Fisher`, a conformal reweighting by legibility. Two carers on the same geodesic pay 2.3283 (attuned) vs 3.6972 (blind), asymmetry 1.5879. The kin gradient (cost = geodesic length / legibility) runs 1.6095 (kin) to 8.0476 (distant stranger), a factor of 5.0. Under the reweighting the curvature is no longer constant, ranging 0.1395 to 0.2601.
- **`study_autonomy`** — the viability-maximizing distribution subject to a Shannon-entropy floor is an exponential-family (Gibbs) tilt, a point on the e-geodesic. Coercion (H=0) reaches viability 1.0 at a zero-entropy vertex; the autonomy floor (H>=ln2) reaches 0.8479; abandonment (uniform) falls to 0.5. Price of autonomy = 0.1521.

`figures.py` (pure plotters, recompute geometry and read scalars from the results dict)

- `output/figures/geometry.png` — the geodesic care-triangle with its spherical excess, and the care-metric curvature field across the simplex.
- `output/figures/care.png` — the kin gradient (cost vs legibility) and directedness (two carers on one geodesic).
- `output/figures/autonomy.png` — viability vs the option-entropy floor (the price of autonomy), and the distribution each policy leaves the other in.

## Status

Complete. The geometry is not stipulated: the metric is forced by Chentsov's theorem and the curvature self-test recovers the known value exactly, so the results are facts about the Fisher-Rao manifold rather than about tuned parameters. Dependencies: `numpy` and `matplotlib` (see `pyproject.toml`).
