---
title: "Geodesics of Care: Distance, Effort and Permission in a Model of Help"
author: PIATRA . INSTITUTE
date: June 2026
bibliography: references.json
---

## Abstract

A system can improve its forecast of a person's welfare while losing track of what that person wants. We use a small geometric model to separate three questions: how a represented condition changes, what an intervention costs, and who may authorize it. A prognosis over failing, coping and flourishing is placed on a probability simplex with the Fisher-Rao metric, which statistical invariance motivates but does not make compulsory for care. Worked calculations show how a conformal effort field changes path costs and curvature, and a flat counterexample shows that a costly detour carries no information by itself about delegating responsibility. The central ethical distinction concerns outcome entropy and recipient permission. A freely chosen predictable outcome can have zero entropy, and an imposed lottery can have high entropy, so an entropy floor constrains uncertainty and leaves autonomy unaddressed. With assigned utility weights, the floor's calculated cost is 0.1521, and a different choice of weights removes the cost entirely. A separate permission rule lets the recipient refuse, revoke or change a target, including when the new target scores worse for the controller. All results are deterministic illustrations and implementation checks with no observations of caring practice. They make the model's commitments inspectable and prevent a welfare score from standing in for the recipient's own instruction.

## 1. Introduction

Consider a device that helps someone organize a day: when to rest, when to walk, when to ask for help. It carries a model of the user's condition and predicts how each proposed change will affect it. Suppose it becomes very good at keeping the user inside its preferred range. The forecast still cannot answer whether the user asked it to do so.

This difficulty persists under perfect prediction. A person might knowingly choose an exhausting visit over a quiet afternoon; the device could predict the cost correctly and still be wrong to prevent the visit. Conversely, a device that leaves every outcome uncertain has not thereby left its user free, since the user may have no say in the matter.

A geometric model can keep these differences visible by separating a distribution over outcomes, a field of intervention costs, and an instruction from the recipient. The separation matters whenever a description of help is taken to authorize it.

Whitehead supplies a starting term, though not an engineering definition. In *Adventures of Ideas* he writes that “The occasion as subject has a ‘concern’ for the object.” Concern describes how something enters experience with affective significance, prior to any reduction of the relation to knowledge of an object [@whitehead1967, pp. 175–177]. The account should not be reduced to an input-output connection: a sensor can respond to a body without experiencing concern and without helping it.

We call the weaker relation *functional coupling*: information about a recipient changes a system's action. In a practical helping relation, those actions are directed toward improving or sustaining the recipient's condition. Ethical care adds questions of standing, need, permission and the recipient's response. These distinctions allow a machine to assist in care without settling whether it feels anything, and they prevent a tracking system directed toward harm from qualifying as helpful because it has an accurate model.

The recipient's role is already central in care ethics. Noddings treats the cared-for's reception and response as part of a caring relation; over successive encounters, those responses help the carer revise what they do [@noddings2002, pp. 18–20]. The permission rule developed here is narrower. It implements an explicit instruction channel in a toy controller and does not define every caring relationship. It assumes a recipient able to communicate a valid instruction; infancy, impaired decision-making, conflicting duties and emergency intervention require judgments the example does not supply.

## 2. The Fisher-Rao simplex of prognoses

Let $p=(p_1,p_2,p_3)$ represent a model's probabilities that the recipient will be failing, coping or flourishing at a specified horizon. The names are placeholders for an assessment that would have to be agreed and validated in an application, and they compress many ways of living into three categories. Probability theory supplies neither the categories nor their ranking.

The model must also state what kind of change it represents. Learning that a person was healthier than expected can move $p$ without improving their health, and an intervention can improve their condition without the model registering it. Interpreting a path from $p$ to $q$ as practical help would require an action-dependent causal model connecting interventions to outcomes. No such model is estimated here; the paths are stipulated changes in prognosis, used to examine the consequences of the representation.

For positive probabilities summing to one, take the Fisher metric
$$
g_F(v,v)=\sum_{i=1}^{3}\frac{v_i^2}{p_i},
\qquad \sum_i v_i=0.
$$
The choice has a statistical justification. In Chentsov's finite-model characterization, a continuous metric family preserved by congruent Markov embeddings is a constant multiple of the Fisher metric; these embeddings correspond to information-preserving statistical transformations [@ay2015, Proposition 3.19 and its preceding discussion]. The requirement applies across statistical models and is stronger than invariance under a change of coordinates on this simplex.

Accepting that invariance requirement selects a statistical geometry. It does not establish that the resulting distance measures suffering, effort or obligation. Costs of action, time and inaccessible transitions may justify additional structure; the conformal fields introduced below are one explicit addition, and their choice needs separate justification.

Set $z_i=2\sqrt{p_i}$. Then
$$
\sum_i z_i^2=4,
\qquad
\sum_i dz_i^2=\sum_i\frac{dp_i^2}{p_i}.
$$
The simplex interior becomes the positive part of a sphere of radius $2$, with Gaussian curvature $1/4$, and the shortest arc has length
$$
d_F(p,q)=2\arccos\!\left(\sum_i\sqrt{p_iq_i}\right).
$$
The completed space includes distributions with zero coordinates, and distributions with disjoint supports are a finite distance $\pi$ apart. The divergent coordinate coefficients at a vertex do not make the vertex infinitely distant, and they do not mark it as an ethical or medical pathology.

For $p=(0.7,0.2,0.1)$ and $q=(0.1,0.2,0.7)$, the Fisher arc has length $1.5074$. Linear interpolation in probability coordinates, measured with the same metric using $2{,}000$ segments, has length $1.5171$. The comparison verifies that a path straight in a chart need not be shortest in the metric.

The code also estimates curvature from the metric components using central finite differences and the Brioschi formula. On the declared interior grid, at difference step $10^{-4}$, the largest absolute error from $1/4$ is about $6.01\times10^{-6}$. This is a numerical consistency check; it neither attains machine precision nor validates the care interpretation. Step-size sensitivity and an independent conformal-curvature formula provide further checks.

## 3. Path costs and conformal effort fields

Take three distributions,
$$
p=(0.75,0.20,0.05),\quad
q=(0.20,0.60,0.20),\quad
r=(0.05,0.20,0.75).
$$
The route through $q$ has length $2.3400$, against $1.8862$ for the direct Fisher arc from $p$ to $r$, a gap of $0.4539$. The angles of the geodesic triangle sum to $3.3164$ radians, with spherical excess $0.1748$ and area $0.6994$. An independent computation of the area from the spherical solid angle agrees with the Gauss-Bonnet relation
$$
\theta_p+\theta_q+\theta_r-\pi=\frac14\,\operatorname{Area}.
$$

These are properties of three distributions. They do not represent three people, and the triangle does not model a parent asking a nurse to help a child. A routing gap does not require curvature: in the flat plane, the path $(0,0)\to(1,1)\to(2,0)$ has length $2\sqrt2$ and the direct distance is $2$. In both examples the detour is longer because it is not a shortest route between its endpoints.

Delegation requires a different description: which agent can perform which action, with what information, resources and responsibility. An intermediary might make an otherwise unavailable action possible or perform it at lower cost, and none of these possibilities contradicts a triangle inequality on a fixed statistical manifold. Curvature cannot decide whether transferring a task discharges an obligation.

Effort can nevertheless be represented explicitly. For a carer $A$, assign a positive field $f_A(p)$ and define
$$
g_A=f_Ag_F,
\qquad
L_A(\gamma)=\int_\gamma\sqrt{f_A(p)}\,ds_F.
$$
The tensor is multiplied by $f_A$ and length is multiplied locally by its square root. A constant efficiency parameter $\ell$ is therefore represented by $f_A=1/\ell^2$, giving length $d_F/\ell$ along a Fisher geodesic.

On the path from $(0.70,0.22,0.08)$ to $(0.08,0.22,0.70)$, the base distance is $1.6095$. Assigning $\ell=1,0.6,0.4,0.2$ gives costs $1.6095,2.6825,4.0238,8.0476$. The final cost is five times the first because the efficiencies were chosen in that ratio. Labeling the endpoints of this parameter list “kin” and “distant stranger” would add an empirical claim for which the calculation supplies no evidence.

For the variable field $f_A(p)=1+\alpha p_1$, the same Fisher arc costs $2.3283$ at $\alpha=3$ and $3.6972$ at $\alpha=12$. These are lengths of a fixed path under two different metrics, and with variable $f_A$ that path need not minimize effort. Each metric remains symmetric, so reversing the path gives the same cost; different agents may have different fields without either field becoming direction-dependent.

![Fisher arcs between three distributions, projected into probability coordinates (left). Analytic and finite-difference curvature for the assigned field $f=1+6p_1$ (right); repeated markers at a common $p_1$ correspond to different $p_2$ values on the same interior grid.](../simulation/output/figures/geometry.png){width=100%}

The effort metric also has different curvature. For $f=1+6p_1$, numerical values on the sampled grid range from $0.1395$ to $0.2601$. The independent formula
$$
K_{f g_F}=\frac{1}{f}\left(\frac14-\frac12\Delta_F\log f\right)
$$
uses $\Delta_Fp_1=(1-3p_1)/2$ and
$\lVert\nabla_Fp_1\rVert^2=p_1(1-p_1)$. Its maximum absolute disagreement with the finite-difference estimates is about $2.68\times10^{-6}$. Because the formula depends on $p_1$ alone, the exact range over the grid's interval $0.12\le p_1\le0.68$ follows by one-dimensional search: the minimum, $0.1395$, lies at the upper endpoint, and the maximum is $0.2607$ at $p_1\approx0.211$, slightly above the largest grid value, which falls at $p_1=0.20$. The curvature describes the chosen field and has not been measured in any family, hospital or institution.

![Path cost of a fixed improvement under assigned constant efficiencies (left) and under two variable fields (right). The parameters have no empirical kinship or psychological interpretation.](../simulation/output/figures/care.png){width=100%}

## 4. Entropy floors and assigned utility

Suppose the controller assigns utilities $w=(0,0.5,1)$ to failing, coping and flourishing. Its expected score is
$$
U(p)=w^\top p.
$$
Without further constraints it prefers the vertex $(0,0,1)$. One proposed safeguard is a lower bound on Shannon entropy,
$$
\max_p U(p)
\quad\text{subject to}\quad
H(p)=-\sum_i p_i\log p_i\ge h.
$$
For an interior solution, the Lagrange multiplier $\tau>0$ gives
$$
p_i(\tau)=
\frac{\exp(w_i/\tau)}{\sum_j\exp(w_j/\tau)}.
$$
The implementation brackets and bisects $\tau$ until the entropy constraint is met and handles the endpoints and tied utility maxima separately; the optimization is numerical.

At $h=\ln2$, the resulting distribution is approximately
$(0.0528,0.1987,0.7485)$, with expected utility $0.8479$, a loss of $0.1521$ against the maximum score. Uniform probability gives utility $0.5$ and maximum entropy $\ln3$. These values follow from the assigned weights. If the score is instead the probability of coping *or* flourishing, with weights $(0,1,1)$, then $(0,0.5,0.5)$ meets the same entropy floor with maximum utility $1$, and the floor costs nothing.

$H(p)$ measures uncertainty over outcomes. It contains no information about which actions the recipient can choose or whose decision produced the distribution. A recipient might freely select a highly predictable outcome, and another person might impose a lottery over all three states. Zero entropy does not establish coercion, and high entropy does not establish freedom. The uniform distribution is also no model of abandonment, since the example contains no unattended drift process.

![Entropy-floor calculation with utility weights $(0,0.5,1)$. A higher floor lowers the attainable score (left); the vertex, the floor optimum and the uniform distribution allocate probability differently (right). None of the distributions records who chose it.](../simulation/output/figures/entropy.png){width=100%}

Canguilhem's account of health locates the error. His discussion of disease and normative capacity concerns an organism's ability to meet changed conditions and establish new ways of living [@canguilhem1991, pp. 181–187]. That capacity cannot be read from uncertainty among three assessor-defined labels. A person might have many practicable ways to flourish while the model confidently assigns all probability to “flourishing,” and a person with little control over anything might face a very uncertain future. The capacity to revise a norm and entropy within a fixed classification are different quantities.

The distinction precedes any calculation of what autonomy costs. A person's chosen activities may conflict with another party's welfare assessment, but this model has not measured such conflicts. It has calculated the cost of a constraint on a forecast.

## 5. A recipient permission rule

An instruction can be represented separately from the forecast. Let a permission record contain an approved target $q_B$, a maximum step fraction $\delta_B$, and a revocation flag. The controller proposes target $q$ and fraction $\eta$. In the toy rule,
$$
p_{t+1}=
\begin{cases}
\operatorname{Geo}_F(p_t,q;\min(\eta,\delta_B)),
& \text{if }q=q_B\text{ and permission remains valid},\\
p_t, & \text{otherwise}.
\end{cases}
$$
Here $\operatorname{Geo}_F(p,q;s)$ is the fraction $s$ of the shortest Fisher arc. A missing permission record authorizes no action. The equality test is numerical, and all target distributions are normalized before comparison.

The rule is deliberately simple. It assumes a truthful, usable instruction channel and a fixed action whose only modeled attribute is movement toward the target. Real permission concerns means, timing, risk and circumstances as well as ends, so a target match alone would be insufficient. The example also has no autonomous dynamics: when an action is rejected, the modeled state stays fixed, whereas a real recipient continues to change when assistance stops.

Four checks separate permission from entropy:

| Recipient instruction | Proposed target | Rule's response |
|:--|:--|:--|
| Approves predictable flourishing | $(0,0,1)$ | Applies it despite zero outcome entropy |
| Approves only that target | Uniform lottery | Rejects it despite maximum entropy |
| Revokes earlier permission | Earlier approved target | Applies no further action |
| Changes the approved target | Old target, then new target | Rejects the old; accepts the new |

In the revocation trace, two permitted steps of fraction $0.25$ occur before revocation, and the remaining three proposals produce zero applied actions. When the recipient instead approves $(0,0.9,0.1)$, the rule accepts it although its assigned utility, $0.55$, is below the controller's maximum. The recipient's instruction changes what may be done; it functions as an authorization and not as one more observation for predicting what the controller already intends.

The check is a property of a programmed gate. It does not show that an optimizing system will preserve the gate, refrain from manipulating the instruction channel, or pass the same constraint to systems it creates. These are among the harder problems studied in corrigibility research, which concerns agents' responses to correction and shutdown [@soares2015, §§2, 4–5]. Even stopping may require a safe transition in place of an immediate halt. The present rule leaves incentives, self-modification and shutdown dynamics outside its scope.

A permission channel also does not settle whose wishes should prevail when several people are affected, or whether a particular refusal relieves others of a duty. The normative commitment is specific: in the non-emergency, single-recipient case modeled, an assessed improvement does not override a valid refusal. The commitment enters the model as a constraint and is not derived from the geometry.

## 6. Requirements for application

A quantitative account of care should identify the recipient, the outcome categories, the assessment horizon, the effects of actions, the cost field and the source of permission. Where two of these are represented by the same quantity, the identification needs an argument; the entropy example shows how readily a convenient number acquires an ethical meaning it does not contain.

An empirical extension would need validated forecasts, causal evidence about interventions, and observed measures of effort. Recipient authority would require a usable means of refusing and revising assistance, including arrangements for people unable to use a simple instruction channel. Fitting the geometry to outcomes would not validate all of these relations at once.

The code, full-precision results, regression tests and a versioned execution receipt are published in the repository. The calculations are deterministic and use no observations of recipients or caring institutions.

The model leaves the experience of caring undescribed and establishes no general limit on formal accounts of experience. Its practical conclusion is that a predicted improvement does not replace the recipient's instruction: when the device forecasts a better afternoon, the person whose afternoon it is retains the authority to accept or refuse the change, and that answer enters the next decision.

## References
