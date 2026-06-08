# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2. T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only). A claim that reaches the paper rests on a T1 or T2 source.

Origin: three seed chats in `chats/` (one ChatGPT ideation, one ChatGPT Pro deep research, one Gemini deep research), which proposed "Geodesics of Care" and the viability-coupling reading. The chats are leads only; every claim below was traced to a primary or authoritative source and frozen in `sources.md`.

## Findings

### Scale-free biology and the boundary of the self

- [T1] The self is a *computational boundary* set by the size of goals a system can represent and pursue (the "cognitive light cone"); multicellularity is held by bioelectric coordination toward anatomical targets, and cancer is a contraction of that boundary — Levin (2019), *Front. Psychol.* 10:2688. Supports §2's anchor: a boundary that can expand to enclose another's viability or contract to exclude it.
- [T1] Life defined as a self-producing, self-maintaining (autopoietic) unity, making viability and boundary the defining features of the living — Maturana & Varela (1980). Supports §2's philosophical antecedent for using viability/boundary as primitives.
- [T2] Care argued as the *driver* of intelligence across basal cognition and AI — Doctor, Witkowski, Solomonova, Duane & Levin (2022), *Entropy* 24:710. The closest adjacent proposal; §2 cites it and takes the narrower "what shape" path.
- [T1] Quorum sensing: diffusible signals let cells estimate density and switch collective behaviors (biofilm, virulence) at threshold — Waters & Bassler (2005), *Annu. Rev. Cell Dev. Biol.* 21:319. Supports §2's "weak functional care" at the bacterial scale.
- [T1] Danger model: immune response keyed to damage/distress signals rather than mere foreignness; the viable self is negotiated and context-sensitive — Matzinger (2002), *Science* 296:301. Supports §2's "boundary as active process."
- [T1] Rats free a trapped cagemate absent reward/contact — Bartal, Decety & Mason (2011), *Science* 334:1427. [T2] Primate empathy/consolation better attested — de Waal (2008), *Annu. Rev. Psychol.* 59:279. §2 uses both, holding the layer line.

### The formal object

- [T1] Viability theory: dynamics constrained to a set; viability kernels are the controlled-invariant subsets from which the system can be kept inside — Aubin (1991). Supports §3: care = keeping B in its viability kernel via A's controls.
- [T1] Information as a measurable quantity; relative entropy (KL) as the cost of using one distribution for another — Shannon (1948); Cover & Thomas (2006). Supports the "nats of policy deformation" currency in §3 and §7.3.
- [T2] Statistical manifold with relative entropy as local distance — Amari (2016), *Information Geometry and Its Applications*. Supports the information-geometric reading.
- [T1] Active inference: agents minimize expected free energy (pragmatic + epistemic) — Friston (2010), *Nat. Rev. Neurosci.* 11:127; Parr, Pezzulo & Friston (2022), MIT Press. Supports §6's coupled-objective bridge.
- [T1] Technical critique: the Markov-blanket formalism does not support strong interpretations — Biehl, Pollock & Kanai (2021), *Entropy* 23:293. Supports §6's discipline: active inference as one lens, not a unifier.

### The autonomy constraint

- [T2] Capability approach: the end is real freedoms to be and do, beyond utility or survival — Sen (1999); Nussbaum (2000). Supports §5's target "viability under preserved agency."
- [T2] Care ethics: reception of the cared-for on their own terms (Noddings 1984) and responsiveness to the recipient's response (Tronto 1993) are constitutive — also Gilligan (1982), Held (2006). Supports the consent/feedback channels as constraints.
- [T1] The Other exceeds the self's comprehension; responsibility precedes mastery — Levinas (1969), *Totality and Infinity*. Supports §5's refusal to let A's model of B stand in for B.
- [T1] Corrigibility: an agent that cooperates with shutdown/modification despite contrary incentives — Soares, Fallenstein, Armstrong & Yudkowsky (2015), AAAI Workshop. §5/§9: the autonomy constraint for an artificial carer.
- [T1] Cybernetics: powerful automata are safe only where the human retains meaningful control — Wiener (1954). §9 antecedent.

### Curvature in the human case

- [T1] Inclusive fitness: aid to relatives favored when relatedness-weighted benefit exceeds cost — Hamilton (1964), *J. Theor. Biol.* 7:1. The kin discount of §7.3/§8.
- [T1] Reciprocal altruism under repeated interaction — Trivers (1971), *Q. Rev. Biol.* 46:35. Second low-cost channel.
- [T1] Coevolution of parochial altruism and war: in-group care and out-group hostility evolve together — Choi & Bowles (2007), *Science* 318:636. Tight radius + hard boundary as one adaptation.
- [T1] Compassion fade: affect/giving peak for one identified victim, decline with number — Västfjäll, Slovic, Mayorga & Peters (2014), *PLOS ONE* 9:e100115. [T1] Identifiable-victim effect — Small & Loewenstein (2003), *J. Risk Uncertain.* 26:5. §8: curvatures of representational cost.
- [T2] Dehumanization: denial of the traits by which agency/mind are recognized — Haslam (2006), *Pers. Soc. Psychol. Rev.* 10:252. §8: removal from the manifold.
- [T1] Moral Expansiveness Scale: breadth of moral concern as a measurable trait — Crimston, Bain, Hornsey & Bastian (2016), *JPSP* 111:636. Closest instrument to radius/diameter; marks the empirical frontier (no path-cost yet).
- [T2] Against empathy / rational compassion — Bloom (2016). §8: affective care's curvature is severe enough to need institutional correction.
- [T1] Mutual aid as a real factor in evolution — Kropotkin (1902). §8 counterweight.
- [T2] Moral progress as expansion of the circle — Singer (1981). §1/§8: supplies the radius, lacks path-cost/asymmetry/institutions.

### Institutions

- [T3] People-centred care: services organized around persons and stated needs — World Health Organization (2016), Framework on Integrated, People-Centred Health Services (A69/39). §8: the deliberate lowering of institutional curvature.

## What was deliberately left out

- The seed's opening race provocation ("kindness races") is the origin of the idea and not its content; the paper drops it entirely and never frames care as ancestry.
- No empirical effect sizes are quoted in prose (they are not this paper's to audit); the only decimals in the modelled section are outputs of the shipped simulation.
- Spin-ice / sheaf-theoretic and optimal-transport extensions noted in the chats are out of scope; the formal core stays viability-theory + information-geometry + control.
