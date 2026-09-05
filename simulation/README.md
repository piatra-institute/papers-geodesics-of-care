# Model — Geodesics of Care

Five deterministic illustrations. No participants, estimated action effects,
measured costs, training or stochastic simulations. NumPy and Matplotlib are the
only direct dependencies; uv.lock pins the environment. The recorded run used
Python 3.13.3, NumPy 2.4.6 and Matplotlib 3.10.9 on macOS ARM64.

## Run and test

With the existing environment, from this directory:

~~~sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -v
.venv/bin/python run_all.py
~~~

For a clean environment, run uv sync --frozen first. If Matplotlib's normal
cache is unwritable, set MPLCONFIGDIR to a task-specific writable temporary
directory.

From the collection root, record a run after changing scientific inputs:

~~~sh
python3 tooling/papers.py run geodesics-of-care --id model-checks \
  --cwd simulation \
  --artifact simulation/output/results.json \
  --artifact simulation/output/figures/geometry.png \
  --artifact simulation/output/figures/care.png \
  --artifact simulation/output/figures/entropy.png \
  --execution-result simulation/output/results.json \
  -- .venv/bin/python run_all.py
~~~

The receipt fingerprints code, tests, dependency declarations/lockfile and all
declared artifacts. PASS means the five calculations and three plots ran,
not that a hypothesis about care was confirmed. The child interpreter records
its actual library versions in results.json; the wrapper records its own
runtime separately.

## What is calculated

- **manifold:** Fisher-Rao distances use the radius-2 sphere convention and a
  stable half-angle expression. All 125 ordered triples of five points satisfy
  the triangle inequality. The coordinate-straight comparison uses 2,000
  segments. Brioschi curvature estimates use central differences on the declared
  interior grid at steps 1e-3, 3e-4 and 1e-4. The final maximum error is about
  6.01e-6, not zero.
- **routing:** three distributions p, q, r; angle excess and independently
  calculated solid-angle area. A separate flat-plane detour demonstrates that
  excess path cost needs no curvature. Neither calculation models delegation.
- **effort:** assigned constant efficiencies and variable conformal tensor
  multipliers. Length integrates sqrt(f), not f. The fixed Fisher arc is
  integrated by midpoint quadrature with 2,000 segments; no variable-metric
  shortest-path optimization is performed. Reverse costs agree for each fixed
  metric. For f=1+6*p1, finite-difference curvature is checked against
  K_f=(1/4 - Delta_F(log f)/2)/f, derived using
  Delta_F(p1)=(1-3*p1)/2 and |grad_F(p1)|^2=p1*(1-p1).
- **entropy:** maximize assigned expected utility under an outcome-entropy
  floor. Stable Gibbs weights and bracketed 120-step bisection handle interior
  optima; endpoint and tied-maximum cases are explicit. At ln(2), weights
  (0,.5,1) yield score .847876 and cost .152124; weights (0,1,1) yield score 1
  and cost 0. The plotted curve samples 26 floors. Entropy is not autonomy.
- **permission:** an exogenous valid instruction identifies an approved target,
  maximum arc fraction and revocation state. No permission, revocation or a
  target mismatch produces no applied action. Tests cover predictable approved
  outcomes, unapproved high-entropy proposals, revocation and changed goals
  that lower the assigned utility. There is no drift, manipulation, delegation,
  authentication, capacity assessment or safe-shutdown model.

These choices are declared, not fitted. Numerical consistency is distinct from
empirical or ethical validation. Eighteen regression tests cover mathematical
identities, boundary cases, sensitivity, permission handling and JSON validity.

## Current outputs

- output/results.json: full-precision results, execution status and child runtime.
- output/figures/geometry.png: Fisher arcs and conformal curvature.
- output/figures/care.png: assigned effort comparisons.
- output/figures/entropy.png: the outcome-entropy calculation.

Older autonomy.png / curvature.png, if present, are unreferenced historical
artifacts and are not regenerated. Do not use them for the current paper.
The former results keys directed and autonomy have been replaced by effort,
entropy and permission; callers of the old schema must migrate.
