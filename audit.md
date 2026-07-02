# Audit

Dated log of editorial passes and verification runs. Newest first. See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-06-13 — voice reform

Editorial pass to remove AI-writing tells per tooling/docs/voice.md.

Pet-vocabulary: the only two gate-flagged tells. "no single contested formalism carries the weight" (§6) -> "the argument does not rest on any single contested formalism"; "where the geometry earns its keep" (§8) -> "what the geometry adds".

Structure: the gate flagged the formulaic skeleton (numbered sections + generic "Conclusion"). Limits are already folded into §9 ("three limits"), so no bolt-on section existed to fold. Retitled §10 "Conclusion" -> "What the geometry organizes and what it withholds", naming the substance of the closing.

Density: deleted one filler "exactly" in §1 ("is exactly what a theory should be built to state" -> "is what..."). The remaining "exactly"/"precisely" uses are genuine exact-computation language in §7 ("Computed Exactly", "solved exactly", "exact dynamic programming") and were left intact per scope (abstract/opening/closing only). Substantive enumerations and the abstract's three model-result claims were left alone.

Verification: voice 0 errors / 0 warns (structure advisory cleared); refs 34 cited / 34 bib, 0 missing, 0 unused (unchanged from baseline); build succeeds, 0 missing-character warnings; claims 17 decimal claims, 0 without a matching simulation value; check => PASS. No numbers, equations, figure values, or citations altered.

## 2026-06-08 — initial full build

Scope: first complete draft from the three seed chats. Wrote the simulation, the paper, and all provenance docs; brought the paper to a clean build.

Changes:

- simulation/: three exact, deterministic analyses (no seed) — care_quasimetric (asymmetry + triangle-inequality failure), price_of_autonomy (exact backward induction on a viability ladder under an option-entropy floor), care_curvature (closed-form Bernoulli-KL, nats per unit viability gain). Two publication figures (autonomy.png, curvature.png). One-command run_all.py.
- paper/PAPER.md: 10 sections. Care as directed viability-coupling; the care-distance and its quasi-metric failures (§3); the geometry's vocabulary (§4); the autonomy constraint as the ethical core, coincident with corrigibility (§5); active inference as one disciplined lens (§6); the exact model with both figures embedded (§7); moral psychology read as measured curvature and institutions as care-manifolds (§8); artificial care and the three limits — phenomenological gap, incommensurability, imperialism of viability (§9).
- metadata.yaml: has_simulation true, claims_target results.json, abstract filled, date "June 2026", status built.
- brief.md, research.md (tiered, T1/T2 traced), sources.md (34 frozen entries), README.md, simulation/README.md.

Headline numbers (all keys in simulation/output/results.json):

- quasi-metric: d(A→B)=1.2, d(B→A)=1.5 (asymmetry 0.3); direct d(A→C)=4.2 > routed 2.7 (triangle excess 1.5).
- price of autonomy: coercion V=1.0 (H=0), autonomy-preserving V=0.972 (H≥ln2), abandonment V=0.495 (death 0.088); price of autonomy 0.028.
- curvature: κ = 0.768 / 2.554 / 8.789 nats per unit (kin / stranger / distant); distant/kin 11.44×, stranger/kin 3.32×.

Verification:

- voice: 0 errors, 0 review-candidates.
- refs: 34 cited / 34 bib / 0 missing / 0 unused.
- claims: 17 decimal claims, 0 without a matching simulation value.
- build: 17 pages, both figures embedded, 0 missing-character warnings.
- check => PASS.

Notes / deferred:

- Dropped the seed's opening race provocation entirely; it is origin, not content.
- de Waal entry written "Waal, F. B. M. de (2008)" so the surname token parses for the refs gate (a leading lowercase particle would drop the bib line).
- Spin-ice / sheaf / optimal-transport extensions from the chats left out of scope.
- Status is `built`, not `published`: deploying to the web (sync + page.tsx) is the maintainer's pipeline.

---

## 2026-07-02 — reform pass (exemplar rebuild)

Scope: full rebuild of the paper as the corpus reference exemplar, addressing the audit's charge that "curvature" was decoration (a redefinition of help-inefficiency, with no metric tensor and an engineered triangle-inequality "violation"). The paper now rests on real information geometry.

What changed:

- simulation/analyses.py: rewritten from scratch. Four exact, deterministic studies on the Fisher-Rao manifold of the other's viability distribution (the 2-simplex). `fr_distance` = 2·arccos(Σ√(p·q)) (great-circle on the radius-2 sphere); `fr_geodesic` (slerp); `fisher_EFG` + `gaussian_curvature` (Brioschi formula from numerical metric partials). study_manifold (curvature self-test returns exactly 0.25, triangle inequality holds); study_routing (Gauss-Bonnet: spherical excess 0.1748 = 1/4 × area 0.6994; routed 2.34 > direct 1.8862); study_directed (control metric g_A = f·g_Fisher, directedness asymmetry 1.5879, kin gradient distant/kin 5.0, care-curvature varies 0.1395–0.2601); study_autonomy (entropy-floor optimum is a Gibbs/e-geodesic tilt; price of autonomy 0.1521 vs abandonment 0.5).
- simulation/figures.py + run_all.py: rewritten for the four studies. Three figures: geometry.png (geodesic care-triangle + care-metric curvature field), care.png (kin gradient + directedness), autonomy.png (viability-vs-entropy-floor + policy distributions). Old autonomy.png/curvature.png retired.
- paper/PAPER.md: full rewrite, 10 sections -> 7, de-templated (no "What the geometry organizes/withholds" ceremonial closer; ends on Ruyer's survol absolu as the phenomenological limit, folded into the argument rather than a bolt-on limits section). Corrected the quasi-metric error: care-distance IS a genuine metric, so the triangle inequality holds and the real obstruction is curvature (Gauss-Bonnet), not brokenness. Deep-cut bibliography woven substantively: Chentsov (metric uniqueness), Rao, Amari-Nagaoka, Ay et al.; Whitehead's "concern," Jonas (needful freedom, infant asymmetry), Canguilhem (single norm = pathological), Goldstein, Ruyer (absolute survey), Uexküll, Simondon, Rosen, Powers, Ashby, Aubin; care ethics (Noddings, Tronto, Ruddick, Kittay, Sen, Nussbaum), Murdoch/Weil (attention), Levinas.
- metadata.yaml + README.md: new title "Concern as Transport on the Manifold of Viability"; abstract rewritten to the information-geometry account.

Verified corrections applied: Weil "attention is the rarest and purest form of generosity" attributed to the 1942 letter to Bousquet (Seventy Letters, trans. Rees, 1965), not Gravity and Grace; Levinas softened to freedom "founded/invested," not "preceded"; Chentsov cited as the finite-case uniqueness with Ay et al. for the general manifold; Friston free-energy phrasing F = D_KL[q(s)‖p(s|o)] − ln p(o).

Verification:

- voice: 0 errors (6 review-candidate warns, all load-bearing contrasts the paper develops).
- refs: 32 cited / 32 bib / 0 missing / 0 unused.
- claims: 31 decimal claims, 0 without a matching simulation value.
- build: figures embedded, math and diacritics render; check => PASS. Synced to web public/.
