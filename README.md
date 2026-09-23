# Geodesics of Care

Distance, Effort and Permission in a Model of Help.

A system can improve its forecast of a person's welfare while losing track of what that person wants. We use a small geometric model to separate three questions: how a represented condition changes, what an intervention costs, and who may authorize it. A prognosis over failing, coping and flourishing is placed on a probability simplex with the Fisher-Rao metric, which statistical invariance motivates but does not make compulsory for care. Worked calculations show how a conformal effort field changes path costs and curvature, and a flat counterexample shows that a costly detour carries no information by itself about delegating responsibility. The central ethical distinction concerns outcome entropy and recipient permission. A freely chosen predictable outcome can have zero entropy, and an imposed lottery can have high entropy, so an entropy floor constrains uncertainty and leaves autonomy unaddressed. With assigned utility weights, the floor's calculated cost is 0.1521, and a different choice of weights removes the cost entirely. A separate permission rule lets the recipient refuse, revoke or change a target, including when the new target scores worse for the controller. All results are deterministic illustrations and implementation checks with no observations of caring practice. They make the model's commitments inspectable and prevent a welfare score from standing in for the recipient's own instruction.

## Read and reproduce

- [Manuscript](paper/PAPER.md) and [PDF](paper/PAPER.pdf).
- [Model and numerical methods](simulation/README.md).
- [Primary-source inspection record](source-checks.md) and
[structured bibliography](paper/references.json).
- [Claim bindings](claims.yaml), [execution receipt](verification/model-checks.json),
[editorial decisions](editorial.md), and [dated history](audit.md).

From this repository, with its existing environment:

~~~sh cd simulation PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -v .venv/bin/python run_all.py ~~~

A clean environment can be created with uv sync --frozen in simulation. The pinned lockfile identifies dependencies. See the simulation guide for the versioned recording command; a direct rerun changes artifacts and requires a new receipt.

From the paper repository, python3 build.py builds the PDF using Pandoc and XeLaTeX. The shared tooling command is available from the archive root:

~~~sh python3 tooling/papers.py check geodesics-of-care --stage local --json ~~~

Build logs and manifests stay local and are ignored by Git. Historical briefs, reviews and unreferenced legacy figures are retained as provenance; they are not evidence for the revised paper. The metadata's existing published status refers to the prior deployment. This revision has not been published or pushed.
