# Geodesics of Care

Distance, Effort and Permission in a Model of Help

A prognosis, the effort needed to change it, and permission to act are different
objects. This essay uses Fisher-Rao geometry to keep them separate. Its strongest
counterexample concerns entropy: a chosen predictable outcome can have none,
while an imposed lottery can have plenty. An entropy floor is not recipient
authority.

The September revision replaces claims of compulsory geometry, measured kinship
costs and a general “price of autonomy” with an explicit, conditional model.
It implements a recipient instruction channel with refusal, revocation and
changed targets. These are illustrative calculations, not data about people.

## Read and reproduce

- [Manuscript](paper/PAPER.md) and [PDF](paper/PAPER.pdf).
- [Model and numerical methods](simulation/README.md).
- [Primary-source inspection record](source-checks.md) and
  [structured bibliography](paper/references.json).
- [Claim bindings](claims.yaml), [execution receipt](verification/model-checks.json),
  [editorial decisions](editorial.md), and [dated history](audit.md).

From this repository, with its existing environment:

~~~sh
cd simulation
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -v
.venv/bin/python run_all.py
~~~

A clean environment can be created with uv sync --frozen in simulation.
The pinned lockfile identifies dependencies. See the simulation guide for the
versioned recording command; a direct rerun changes artifacts and requires a new
receipt.

From the paper repository, python3 build.py builds the PDF using Pandoc and
XeLaTeX. The shared tooling command is available from the archive root:

~~~sh
python3 tooling/papers.py check geodesics-of-care --stage local --json
~~~

Build logs and manifests stay local and are ignored by Git. Historical briefs,
reviews and unreferenced legacy figures are retained as provenance; they are not
evidence for the revised paper. The metadata's existing published status refers
to the prior deployment. This revision has not been published or pushed.
