---
title: |
  Geodesics of Care:\
  Concern as Transport on the Manifold of Viability
author: PIATRA . INSTITUTE
date: June 2026
---

## Abstract

Care is usually studied as a feeling, a virtue, or a practice, and studied that way it is hard to see what a hospital and a mother have in common, or why good intentions so often miscarry. This paper takes a colder primitive and follows it further than sentiment allows. One system cares for another, in the minimal sense, when the other's viability enters its perception, model, and choice of action; the ethical senses add valence, an explicit model, and a submission to the other's consent, but they do not discard the minimal one. The claim is that this relation has a geometry, and that the geometry is not a metaphor but the information geometry of the other's viability. Represent the cared-for as a distribution over the states in which it can persist. The space of such distributions is a statistical manifold, and Chentsov's theorem fixes its metric: on a finite state space the Fisher-Rao metric is the only one invariant under the sufficient statistics, so the distances are forced, not chosen. On the three-state simplex that metric is a sphere of radius 2, of constant curvature a quarter, and a differential-geometry routine built from scratch returns that quarter to machine precision, which certifies the machinery the rest of the paper runs on. Care is then transport: the carer moves the other along a geodesic toward the viable region, and the care-distance is the geodesic's length. Three results follow from the construction rather than from any tuning of it. The care-distance is a genuine metric, so it obeys the triangle inequality and the older claim that concern could reach a stranger more cheaply by routing through a friend was an artefact; the real obstruction is curvature, and a care-triangle has a measurable spherical excess of 0.1748, a quarter of its area, by Gauss-Bonnet. Direction enters not through the base metric, which is symmetric, but through the carer's control metric, a conformal reweighting whose curvature is no longer constant, and under which a distant stranger costs 5.0 times what kin cost to reach along the same path. And the ethical constraint that separates care from domination becomes a boundary fact: total coercion drives the other to a vertex of the simplex, a distribution of zero entropy, which is Canguilhem's definition of the pathological, a life reduced to a single norm; holding the other off that boundary at a modest entropy floor costs only 0.1521 of attained viability, while abandoning it to an unguided drift costs 0.5. What the geometry cannot reach is the inside of the relation, and the paper ends there, with Ruyer, on the one region that has no distance because it is present to itself without survey, and which a geometry of distances is therefore built to miss.

## 1. Concern Before Feeling

Whitehead needed a word for the relation an experience has to the world it takes up, and he refused the obvious one.
The relation of a subject to its object is not, at bottom, that of a knower to a thing known; it is affective before it is cognitive, and he borrowed from the Quakers the word for it.
"The occasion as subject has a 'concern' for the object," he wrote, and the concern "at once places the object as a component in the experience of the subject, with an affective tone drawn from this object and directed towards it" (Whitehead, 1933).
Concern, in this technical use, is older and wider than the feeling that shares its name.
It is the bare fact that one center of activity has taken another's condition into itself and been altered by it, and the feeling, where there is feeling, is something that happens on top of that fact.

This paper builds on the wide sense and works back toward the narrow one.
A system cares for another, in the minimal and purely functional sense, when variables tracking the other's viability enter its perception, its internal model, its valuation, and its selection of action, so that what happens to the other changes what it does.
Nothing here is yet kindness, and calling it care is a claim about control architecture, not about virtue.
It is the relation Ashby's homeostat would have to a second homeostat whose essential variables it had begun to defend, keeping them inside the bounds outside which the other cannot persist (Ashby, 1952), and it is also, at the far end of the same relation, what a parent is to a child.
A theory is worth having only if it states the difference between those two rather than assuming it, and the layered vocabulary comes first.
Affective care adds valence, so the other's distress registers as the carer's problem.
Cognitive care adds an explicit model of the other's states and point of view.
Ethical care subjects the coupling to the other's consent and standing, so that helping is bounded by what the other wants and is owed.
Institutional care implements the coupling at a scale no nervous system reaches, through rules, budgets, and records.
Most of the confusions in this area come from reading one layer as another, calling bacterial quorum-sensing compassion or calling a warm feeling an obligation, and the layers are kept apart here precisely so that the geometry can be built on the layer they share.

That there is a shared layer is not obvious, and the reason to believe it is that the same coupling appears where feeling is certainly absent and appears in a form continuous with the human case.
Jonas located the root of the continuity in metabolism itself.
A living thing is not a stable lump but a form that must continuously exchange its matter to persist, and in that dependence it is, in his phrase, a "needful freedom": free of any particular material instantiation, and for that very reason exposed to need, so that its own continuation is the first thing that can matter to anything at all (Jonas, 1966).
Value does not wait for minds; it enters the world with the first system whose persistence is conditional on what it does.
Care is what happens when one such system's conditional persistence is taken up into another's regulation, and Jonas saw that the clearest human instance is also the most asymmetric: the infant, whose mere breathing, he wrote, addresses an unanswerable ought to the world, and whose helplessness is the archetype from which the idea of responsibility is drawn (Jonas, 1984).
The thesis of this paper is that when one system's regulation bends around another's viability, the bending has a shape, that the shape is a real geometry rather than a figure of speech, and that the geometry is the information geometry of the other's viability.
The account is organizational and formal.
It does not tell anyone whom to care for, and its last section is about the precise thing it cannot see.

## 2. The Other's Viability as a Manifold

To make viability a place one can move through, it has to be made a quantity, and the natural quantity is a distribution.
Fix, for a target $B$, a small set of states that matter to its persistence: below its norm, within it, above it, or however the essential variables of the case are coarsened.
Ashby's essential variables are the physiological quantities a system must hold within limits to survive, and Aubin's viability theory studies the trajectories that can be kept inside such a constraint set by available controls, characterizing the viability kernel, the largest region from which the system can be kept viable at all (Aubin, 1991).
What matters here is not a point in that set but $B$'s standing across it, and that is a probability distribution: the chance, at a given moment, that $B$ is failing, coping, or flourishing.
Which states even count as viable is not given from outside.
Uexküll showed that each animal inhabits its own Umwelt, a world carved into significance by its own functional cycles, so that what viability consists in is species-relative and, past the animal case, person-relative (Uexküll, 2010); Canguilhem made the same point for medicine, that health is not a single objective set-point but a living being's own capacity to set and revise its norms (Canguilhem, 1991).
The carer therefore acts not on $B$'s viability but on its own model of it, and that gap is where the whole ethical difficulty will later live.

Grant the distribution and the geometry is no longer optional.
The space of distributions over a finite set of states is a simplex, and a simplex of distributions is a statistical manifold, an object with its own intrinsic notion of distance.
The notion is not up to us.
Rao observed in 1945 that the Fisher information could be read as a Riemannian metric on a family of distributions, giving a geodesic distance between them (Rao, 1945), and Chentsov proved the fact that removes the arbitrariness: on a finite sample space the Fisher-Rao metric is, up to scale, the only Riemannian metric invariant under the transformations that carry one statistical model into another by a sufficient statistic (Chentsov, 1982; the general-manifold version is Ay, Jost, Lê, and Schwachhöfer, 2017).
Any other choice of distance between viability distributions would smuggle in structure that the statistics does not contain.
The metric is compulsory.

On the three-state simplex the metric has a concrete shape worth seeing.
The map $p \mapsto 2\sqrt{p}$ carries the simplex isometrically onto a piece of a sphere of radius 2, on which the Fisher-Rao geodesic distance between two distributions is
$$
d(p,q) \;=\; 2\arccos\!\Big(\textstyle\sum_i \sqrt{p_i\,q_i}\Big),
$$
the great-circle distance, running from 0 for identical distributions to $\pi$ for distributions on disjoint supports (Amari and Nagaoka, 2000).
A sphere of radius 2 has constant Gaussian curvature a quarter, and the simulation computes that quarter rather than assuming it.
A curvature routine built only from the metric components and the Brioschi formula, fed the Fisher metric on a grid across the simplex interior, returns 0.25 with a maximum deviation of 0.0 over the grid.
The instrument works before it is trusted.
That the machinery recovers the known curvature to machine precision is the license to trust it later, where the curvature is not known in advance.
The care-distance the paper will use is a distance on this manifold, and its geodesics are great-circle arcs; a representative arc runs 1.5074 while the straight chord across the simplex, measured in the same metric, runs 1.5171, longer, because the straight line in the coordinates is not the shortest path in the geometry.

## 3. Care as Transport

With the manifold fixed, care has a formal shape.
$B$ sits at some distribution over its viability states, displaced from the region where it flourishes.
A carer $A$ acts to move $B$ along the manifold toward that region, and the care-distance from $A$ to $B$ is the length of the path $A$ must drive $B$ through to secure a target improvement, measured in the metric the last section forced.
This is transport, and it presumes of $A$ the two capacities the older cybernetics isolated.
Rosen argued that a system able to act on the future rather than merely react to the present must contain an internal predictive model of itself and its world and steer by the model's forecast, which is what anticipation is (Rosen, 1985); Powers argued that organisms do not control their outputs but their perceptions, holding a sensed variable near a reference by whatever action the disturbance requires (Powers, 1973).
A carer is an anticipatory controller pointed at a second system: it holds a model of $B$, predicts where $B$ is drifting, and acts to hold $B$'s viability near a reference that is not its own.
Active inference gives one explicit way to write this, an agent minimizing a variational free energy $F = D_{\mathrm{KL}}[q(s)\,\Vert\,p(s\mid o)] - \ln p(o)$ that scores its model against its world, with a caring agent carrying a second such term, weighted, for another agent's viability (Friston, 2010; Parr, Pezzulo, and Friston, 2022).
The formalism is useful where its pieces are written down and empty where they are not, a looseness its own critics have pressed (Biehl, Pollock, and Kanai, 2021), and it is used here as one chart on the manifold rather than as the manifold itself.

A first correction falls out immediately, and it corrects an earlier version of this very framework.
Because care-distance is a length in a Riemannian metric, it is a metric quantity in the strict sense, and a metric obeys the triangle inequality: the distance from $A$ to $C$ is never more than the distance from $A$ to $B$ plus the distance from $B$ to $C$.
It had been tempting to say that concern is broken, that a carer might reach a distant stranger more cheaply by routing through an intermediary who is close to both, so that the direct distance could exceed the sum of the two hops.
On the manifold this cannot happen, and checking a grid of triangles confirms it: the largest violation of the triangle inequality found over the sampled triples is 0, to numerical tolerance.
The intuition that routing through a friend does not discharge one's own concern for a stranger is real, but it is not a failure of the triangle inequality.
It is a fact about who holds which path, and the geometry behind it is curvature.

## 4. Why Concern Does Not Route

Put three viability positions on the simplex, $A$ failing, $B$ coping, $C$ flourishing, and read the geometry of the triangle their geodesics bound.
The direct care-distance from $A$ to $C$ is 1.8862.
The routed distance, $A$ to $B$ at 1.17 followed by $B$ to $C$ at 1.17, is 2.34, longer than the direct path by 0.4539.
Routing is a detour, and the detour is geometric rather than incidental.
The three geodesics meet at interior angles whose sum is 3.3164, greater than the $\pi$ that a flat triangle would give, and the surplus, the spherical excess of 0.1748, is by the Gauss-Bonnet theorem exactly the curvature times the enclosed area, a quarter of an area of 0.6994.
The excess is the invariant the old vocabulary was reaching for.
A positively curved manifold focuses geodesics, bending initially parallel paths of concern toward one another, and it is the reason a carer cannot compose its reach out of others' reaches: the paths do not add, they curve, and the curving is measurable in the one number the triangle's angles already contain.

This is what the claim that the moral world is not flat comes to.
Distances do not misbehave.
The surface on which concern is transported has a shape, and the shape has consequences a carer pays whether or not anyone names them.
Figure 1 draws the care-triangle with its geodesic sides bowing away from the straight chords, and beside it the curvature of the metric across the whole simplex, which the next section makes vary.

![The curved manifold of care. Left: a geodesic care-triangle with vertices at a failing, a coping, and a flourishing distribution; the sides are Fisher-Rao geodesics, and the dashed line is the straight coordinate chord the geodesic departs from. The interior angles sum to 3.3164, above $\pi$, and the spherical excess of 0.1748 equals a quarter of the enclosed area, 0.6994, by Gauss-Bonnet; routing $A\to B\to C$ costs 2.34 against the direct 1.8862. Right: the Gaussian curvature of the carer's control metric across the simplex, which departs from the base Fisher value of a quarter and ranges from 0.14 near the failing corner to 0.26, because legibility is not uniform.](../simulation/output/figures/geometry.png){width=100%}

## 5. Directed Care and the Shape of Nearness

The base metric is symmetric, and care is not.
A parent reaches a child far more cheaply than the child reaches the parent, and a state reaches a citizen through instruments the citizen has no counterpart for.
Direction does not come from the manifold of the other's viability, which is a fact about the other and the same for everyone; it comes from the carer, and specifically from how legibly the carer can read and move the other.
Write the carer's control metric as a conformal reweighting of the base, $g_A = f_A\, g_{\text{Fisher}}$, where $f_A$ is the cost per unit of manifold length that $A$ pays to drive $B$ along it, high where $B$ is opaque to $A$ and low where $B$ is transparent.
Because $f_A$ belongs to $A$ and $f_B$ to $B$, the care-cost is directed: two carers moving the same target along the same geodesic pay different amounts, and one reader who is well attuned to a distressed target pays 2.3283 for a restoration that costs a carer blind to distress 3.6972, an asymmetry of 1.5879 on identical work.
Reweighting the metric also breaks the constant curvature.
Under a legibility field that dims toward the failing corner, where a system in crisis is hardest to read, the control metric's Gaussian curvature is no longer a flat quarter everywhere but ranges from 0.1395 to 0.2601 across the simplex, computed by the same routine that returned the exact quarter for the base.
Curvature here is the curvature of the metric care is transported in, an intrinsic quantity of the surface itself, and it varies because legibility varies.

The gradient this produces is the one moral psychology has mapped from the other side.
Hold the target's condition fixed and vary only the carer's legibility of it, $\ell$ running from 1 for kin, whom the carer models transparently, down toward 0 for a stranger who is barely read, with control cost $f = 1/\ell^2$.
The care-cost of the same restoration is then the geodesic length divided by legibility, and it climbs from 1.6095 for kin to 2.6825 for a friend, 4.0238 for a stranger, and 8.0476 for a distant stranger, so that the distant stranger costs 5.0 times what kin cost to reach along the identical path.
Hamilton's rule explains why the gradient runs this way, since alleles promoting aid to relatives are favored when the weighted benefit exceeds the cost (Hamilton, 1964), and the framework does not compete with that explanation but restates its consequence as geometry: kin are not more deserving, they are cheaper to model, and the steep rise of cost with relational distance is the curvature that keeps unaided concern parochial.
Compassion fade, the shrinking of concern as the number needing it grows, and the pull of the single identifiable victim over the statistical many, are the same effect seen along the axis of number rather than kinship: a determinate person is cheap to model and sits close, a population is expensive to represent and recedes, whatever the viability at stake.
Simondon's word for what the low-legibility relation lacks is instructive.
He held that individuals are constituted in part by their relations, that a relation can have the status of being rather than merely connecting two prior terms (Simondon, 2020), and legibility is the degree to which the carer has let the other become such a constitutive relation rather than an object at distance.
Institutions are the technology a species with this curvature uses to care past the reach of its feelings.
A welfare office reaches millions of strangers precisely because it does not love any of them; it flattens the legibility field into a uniform low resolution, a rule that reads everyone equally badly, and buys reach with the same flattening that produces its characteristic cruelty, the eligible case the form cannot see.
Figure 2 shows the kin gradient and the directedness together.

![The shape of nearness. Left: care-cost, the geodesic length under the carer's control metric, against the legibility of the other; kin at legibility 1 cost 1.6095, a friend 2.6825, a stranger 4.0238, a distant stranger 8.0476, so the distant stranger is 5.0 times as costly as kin along the same path. Right: directedness, two carers driving the same target along the same geodesic, the one attuned to distress paying 2.3283 and the one blind to it 3.6972, an asymmetry of 1.5879 on identical work.](../simulation/output/figures/care.png){width=100%}

## 6. The Price of Autonomy and the Single Norm

Everything so far is a theory of moving another toward viability, and read as nothing more it would license the worst thing done in care's name, because the most reliable way to secure a system's viability is to remove its freedom to be otherwise.
The constraint that forbids this is not an addition to the geometry; it is a fact about where on the manifold the geometry is allowed to go.
Let $B$'s viability be scored by the mass its distribution places on coping and flourishing, so that driving all of $B$'s mass onto the flourishing state gives the maximal viability of 1.0.
That maximal state is a vertex of the simplex, a distribution of zero entropy, and it is not a healthy endpoint but a pathological one.
Canguilhem defined the pathological as precisely this: not the absence of norms but their collapse to one, the sick organism being sick in its "incapacity to tolerate more than a single norm," able to live only in a shrunken and unvarying milieu (Canguilhem, 1991).
Goldstein had described the same collapse from the clinic, the brain-injured patient driven to a rigid, constricted order because any disturbance it cannot meet brings on a catastrophic reaction, its world narrowed to what it can still master (Goldstein, 1995).
Total coercion, in the geometry, drives $B$ to that vertex.
It maximizes the score and destroys the thing the score was standing in for, and the manifold makes this visible: the vertex is on the boundary, where the metric degenerates and $B$'s interior room to be otherwise has gone to zero.

The autonomy constraint is a floor on how far toward the boundary care may push.
Require that $B$ retain live options, a Shannon entropy at or above a floor, and the viability-maximizing feasible distribution is no longer the vertex but an exponential-family tilt of the uniform distribution toward the flourishing direction, a Gibbs distribution sitting on the exponential geodesic that information geometry draws from the center of the simplex (Amari, 2016).
At a floor of $\ln 2$ nats, the guarantee of at least two live options, that optimum is the distribution placing 0.7485 on flourishing, 0.1987 on coping, and 0.0528 on failing, and it attains a viability of 0.8479.
The price of autonomy, the viability that total coercion buys over this free-but-guided care, is therefore 0.1521, and the shape of the trade-off is the argument.
A carer who refuses to guide at all abandons $B$ to an unguided drift, the uniform distribution, whose viability is only 0.5 and which leaves a full 0.3333 of the mass on failing; abandonment costs $B$ more than three times what respecting its freedom costs.
The supportive carer captures 0.8479 of the attainable good while leaving the other its options, coercion buys back the last 0.1521 by emptying them, and the refusal to act at all forfeits half.
This is the formal residue of what the care-ethics tradition has held without formalizing it.
Noddings made the carer's reception of the cared-for, on the cared-for's own terms, constitutive of care rather than incidental to it (Noddings, 1984); Tronto made responsiveness to the recipient's response one of care's defining phases (Tronto, 1993); Ruddick found in maternal practice not a mood but a discipline of thought, organized by the demands of preservation, growth, and the child's acceptability (Ruddick, 1989); Kittay insisted that dependency is inescapable and asymmetric and that a theory built for independent equals will misdescribe most of a life (Kittay, 1999); and the capability approach named the proper end of such help not utility or bare survival but the protection and widening of a person's real freedoms to be and do (Sen, 1999; Nussbaum, 2000).
Figure 3 shows the price of autonomy and the distributions each policy leaves.

![The price of autonomy. Left: attained viability against the floor on the other's option-entropy. Coercion drives all mass to the flourishing vertex, viability 1.0 at zero entropy, a single norm; the autonomy floor at $\ln 2$ nats reaches viability 0.8479; unguided abandonment at maximal entropy falls to 0.5. The price of autonomy, the viability coercion buys over free-but-guided care, is 0.1521. Right: where each policy leaves the other across the failing, coping, and flourishing states, coercion massing entirely at the vertex while the autonomy-preserving policy keeps the other high without emptying its options.](../simulation/output/figures/autonomy.png){width=100%}

The same constraint returns, stripped of any sentiment, in the engineering of artificial carers, which is the framework's evidence that it has isolated something structural rather than something humane.
An agent that models a person's viability, updates the model from the person's own corrections, acts to keep the person viable, and preserves the person's power to halt and redirect it is, in every functional sense defined here, caring, and it is caring without any of the affect the human case carries.
The corrigibility problem, how to build an agent that permits itself to be corrected or shut down even when its objective would give it reason to resist, is the autonomy floor written as a design requirement (Soares, Fallenstein, Armstrong, and Yudkowsky, 2015), and its known failure modes are deformations of this geometry: the paternalistic optimizer that meets the viability target while closing the options is the coercive vertex built at scale; the manipulative one that reshapes the person's preferences to be easier to satisfy corrupts the feedback the constraint depends on; the indifferent one is capability at legibility zero.
Wiener saw the shape of the problem at the outset, that a powerful automaton acting on a person is safe only where the person keeps meaningful control of it (Wiener, 1954), and Levinas gave the demand its sharpest statement from the other direction, that the face of the other resists being reduced to a theme the self masters, calling the self's freedom to a responsibility that founds it rather than the reverse (Levinas, 1969).
Both come to the same constraint the geometry names, the refusal to let the carer's model of the other stand in for the other, and the same requirement, that the other keep the power to refuse.
The refusal is the one Murdoch, taking the word from Weil, called attention: the just and patient regard for a reality other than oneself, an unselfing, against which Weil set the warning that attention is the rarest and purest form of generosity (Murdoch, 1970; Weil, 1965).

## 7. The Interior That Has No Distance

Everything the geometry measures is exterior.
It reads the coupling, the cost, the fidelity of the model, the preservation of the other's options, and every one of these is a fact about the relation seen from outside, a distance on a manifold that an observer with the right instruments could in principle map.
The relation also has an inside, and the inside is what a geometry of distances cannot contain, for a reason that is not a limitation of this construction but a feature of what distance is.
Ruyer spent a career on the point.
A true form, a field of consciousness, an organism surveying its own activity, is present to itself, he argued, without any distance inside it, from no particular point within it, and with nothing standing outside it to do the seeing; he called this immediate self-possession the "absolute survey," the *survol absolu*, and held that it is the mark of a true unity as against a mere aggregate observed from without (Ruyer, 2016).
Whatever is surveyed absolutely is surveyed at no distance.
A geometry, by its nature, is the science of distances, and so the felt interior of care, the "what it is like" to be concerned, falls through the geometry's net by construction: the one thing it is built to measure is the one thing that interior does not have.

This is why coupling is not yet care in the sense that finally matters, and the standing reminder is a machine.
A guided missile is coupled to the viability of its target with great fidelity and acts continuously to change it, scoring well on every exterior quantity the framework defines, and there is nothing it is like to be the missile and no one the target is to it.
The geometry cannot tell the missile from the mother by any measurement it takes, because the difference between them is not a distance.
Two further cautions are the same point in other registers.
The framework's currencies, energy and risk and information and viability and the preservation of options, do not collapse into a single scalar that would rank a child, a forest, a stranger, and an unborn generation on one axis, and any construction that pretended they did would have quietly supplied the ethics it claims only to give a shape.
And the deepest danger lives in the definition itself: the carer acts on its model of the other's viability, and if the model is wrong, or if what the carer takes to be the other's flourishing is not the other's own, then the entire apparatus becomes the most efficient possible engine of harm, delivered at least cost under the sincere description of help.
The autonomy floor and the open feedback channel are the only guard against this, and they are a discipline, not a guarantee, because the model can always be confident and mistaken at once.
A geometry of concern can find the region of need no one's path reaches, price the geodesic that would reach it, and name the curvature that keeps the stranger far.
Whether the concern that arrives has become its opposite is a question about the inside of the relation, and the inside is the one place, Ruyer would say, that no survey from outside was ever going to see.

## References

Amari, S., and Nagaoka, H. (2000). *Methods of Information Geometry* (D. Harada, Trans.). Translations of Mathematical Monographs 191. American Mathematical Society and Oxford University Press.

Amari, S. (2016). *Information Geometry and Its Applications*. Applied Mathematical Sciences 194. Springer.

Ashby, W. R. (1952). *Design for a Brain: The Origin of Adaptive Behaviour*. Chapman and Hall.

Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser.

Ay, N., Jost, J., Lê, H. V., and Schwachhöfer, L. (2017). *Information Geometry*. Ergebnisse der Mathematik und ihrer Grenzgebiete, 3. Folge, 64. Springer.

Biehl, M., Pollock, F. A., and Kanai, R. (2021). A technical critique of some parts of the free energy principle. *Entropy*, 23(3), 293.

Canguilhem, G. (1991). *The Normal and the Pathological* (C. R. Fawcett, Trans.; intro. M. Foucault). Zone Books. (Original work published 1966.)

Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference* (Translations of Mathematical Monographs 53). American Mathematical Society. (Original work published 1972.)

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Goldstein, K. (1995). *The Organism: A Holistic Approach to Biology Derived from Pathological Data in Man* (foreword O. Sacks). Zone Books. (Original work published 1934.)

Hamilton, W. D. (1964). The genetical evolution of social behaviour, I and II. *Journal of Theoretical Biology*, 7(1), 1–52.

Jonas, H. (1966). *The Phenomenon of Life: Toward a Philosophical Biology*. Harper and Row.

Jonas, H. (1984). *The Imperative of Responsibility: In Search of an Ethics for the Technological Age* (H. Jonas with D. Herr, Trans.). University of Chicago Press. (Original work published 1979.)

Kittay, E. F. (1999). *Love's Labor: Essays on Women, Equality, and Dependency*. Routledge.

Levinas, E. (1969). *Totality and Infinity: An Essay on Exteriority* (A. Lingis, Trans.). Duquesne University Press. (Original work published 1961.)

Murdoch, I. (1970). *The Sovereignty of Good*. Routledge and Kegan Paul.

Noddings, N. (1984). *Caring: A Feminine Approach to Ethics and Moral Education*. University of California Press.

Nussbaum, M. C. (2000). *Women and Human Development: The Capabilities Approach*. Cambridge University Press.

Parr, T., Pezzulo, G., and Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.

Powers, W. T. (1973). *Behavior: The Control of Perception*. Aldine.

Rao, C. R. (1945). Information and the accuracy attainable in the estimation of statistical parameters. *Bulletin of the Calcutta Mathematical Society*, 37, 81–91.

Rosen, R. (1985). *Anticipatory Systems: Philosophical, Mathematical, and Methodological Foundations*. Pergamon.

Ruddick, S. (1989). *Maternal Thinking: Toward a Politics of Peace*. Beacon Press.

Ruyer, R. (2016). *Neofinalism* (A. Edlebi, Trans.). University of Minnesota Press. (Original work published 1952.)

Sen, A. (1999). *Development as Freedom*. Oxford University Press.

Simondon, G. (2020). *Individuation in Light of Notions of Form and Information* (T. Adkins, Trans.). University of Minnesota Press. (Original work published 1958.)

Soares, N., Fallenstein, B., Armstrong, S., and Yudkowsky, E. (2015). Corrigibility. In *Artificial Intelligence and Ethics: Papers from the 2015 AAAI Workshop*.

Tronto, J. C. (1993). *Moral Boundaries: A Political Argument for an Ethic of Care*. Routledge.

Uexküll, J. von (2010). *A Foray into the Worlds of Animals and Humans* (J. D. O'Neil, Trans.). University of Minnesota Press. (Original work published 1934.)

Weil, S. (1965). *Seventy Letters* (R. Rees, Trans.). Oxford University Press. (Letter to Joë Bousquet, 13 April 1942.)

Whitehead, A. N. (1933). *Adventures of Ideas*. Macmillan.

Wiener, N. (1954). *The Human Use of Human Beings: Cybernetics and Society* (2nd ed.). Houghton Mifflin.
