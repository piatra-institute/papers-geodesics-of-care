"""Exact, deterministic analyses for *Geodesics of Care*.

Three computations, each an exact property of a defined model, no random seed:

  A. care_quasimetric — the direct-coupling cost d(X->Y) is a directed
     quasi-metric: it is asymmetric (d(A,B) != d(B,A)) and it violates the
     triangle inequality (d(A,C) > d(A,B)+d(B,C)) whenever the cost of modelling
     a more distant being grows faster than linearly. Plain arithmetic over the
     model; reported exactly.

  B. price_of_autonomy — a finite-horizon control problem (value iteration on a
     viability ladder) in which a carer A shapes the move-distribution of a
     target B. Maximising B's expected viability with no constraint drives B's
     per-step option-entropy to zero (the padded room). Requiring a floor on
     that entropy preserves B's options at a measurable cost in viability. The
     gap is the price of autonomy. Exact DP over a discretised action menu.

  C. care_curvature — kappa, the policy deformation (in nats of KL divergence
     from a baseline self-policy) required per unit of viability delivered to a
     target, as a function of relational curvature. Kin are geometrically cheap;
     distant strangers cost an order of magnitude more per unit of good done.
     Closed-form Bernoulli KL.

Every number cited in the paper's modelled section is a key in the dict
returned by run().
"""
from __future__ import annotations

import math
from itertools import product

# ---------------------------------------------------------------------------
# A. The care quasi-metric: asymmetry and triangle-inequality failure
# ---------------------------------------------------------------------------
# Direct-coupling cost for X to preserve/improve Y's viability:
#
#     d(X -> Y) = rep_weight * repcost(cat(X), cat(Y)) + act_weight * actcost(X)
#
# repcost is the representational burden of modelling Y from X's vantage; it
# grows with category distance and is CONVEX (super-additive), so modelling a
# being twice as far costs more than twice as much. actcost is set by the
# helper's own capability (a resource-rich agent intervenes cheaply). The two
# features that break the metric are exactly these: actcost(X) makes the cost
# direction-dependent; convex repcost makes it violate the triangle inequality.

# category coordinates on a line; B sits between A and C
_CAT = {"A": 0.0, "B": 1.0, "C": 2.0}
# per-agent action cost (capability): A is resource-rich, C resource-poor
_ACTCOST = {"A": 0.2, "B": 0.5, "C": 1.0}
_REP_WEIGHT = 1.0
_ACT_WEIGHT = 1.0


def _repcost(cx: float, cy: float) -> float:
    """Convex (squared) representational cost of modelling cy from cx."""
    return (cx - cy) ** 2


def _d_care(x: str, y: str) -> float:
    return _REP_WEIGHT * _repcost(_CAT[x], _CAT[y]) + _ACT_WEIGHT * _ACTCOST[x]


def care_quasimetric() -> dict:
    d_ab = _d_care("A", "B")
    d_ba = _d_care("B", "A")
    d_bc = _d_care("B", "C")
    d_ac = _d_care("A", "C")
    routed = d_ab + d_bc
    return {
        "d_A_to_B": round(d_ab, 6),
        "d_B_to_A": round(d_ba, 6),
        "asymmetry_gap": round(abs(d_ba - d_ab), 6),
        "d_B_to_C": round(d_bc, 6),
        "d_A_to_C_direct": round(d_ac, 6),
        "d_A_to_C_routed": round(routed, 6),       # d(A,B)+d(B,C)
        "triangle_excess": round(d_ac - routed, 6),  # > 0 means inequality fails
        "triangle_holds": bool(d_ac <= routed + 1e-9),
    }


# ---------------------------------------------------------------------------
# B. The price of autonomy: viability vs option-entropy on a control problem
# ---------------------------------------------------------------------------
# B lives on a viability ladder s in {0,...,N}. State 0 is absorbing death.
# Each step B makes a move delta in {-1, 0, +1}. The carer A sets the
# move-distribution p = (p_down, p_stay, p_up). A's objective is B's expected
# terminal viability s/N. The autonomy constraint is a floor H_min on the
# per-step Shannon entropy of p (in nats): A may bias B's options but may not
# collapse them. We solve exactly by backward induction over a discretised menu
# of distributions (denominator 12, so the floors ln 2 and ln 3 are hit exactly
# by (6,6,0)/12 and (4,4,4)/12).

_N = 8          # ladder height
_T = 8          # horizon (steps)
_S0 = 4         # B starts mid-ladder
_DENOM = 12     # action-menu resolution
_DELTAS = (-1, 0, +1)


def _entropy(p) -> float:
    return -sum(pi * math.log(pi) for pi in p if pi > 0.0)


def _action_menu():
    """All move-distributions on a denominator-12 grid, with their entropy."""
    menu = []
    for a, b in product(range(_DENOM + 1), repeat=2):
        c = _DENOM - a - b
        if c < 0:
            continue
        p = (a / _DENOM, b / _DENOM, c / _DENOM)
        menu.append((p, _entropy(p)))
    return menu


_MENU = _action_menu()


def _clip(s: int) -> int:
    return 0 if s < 0 else (_N if s > _N else s)


def _solve_ladder(h_min: float):
    """Backward induction. Returns (expected terminal viability from S0,
    optimal per-(t,s) distribution, the binding entropy floor in nats)."""
    feasible = [(p, h) for (p, h) in _MENU if h >= h_min - 1e-9]
    # terminal value: normalised viability; state 0 is dead
    V = [[0.0] * (_N + 1) for _ in range(_T + 1)]
    for s in range(_N + 1):
        V[_T][s] = s / _N
    policy = [[None] * (_N + 1) for _ in range(_T)]
    for t in range(_T - 1, -1, -1):
        for s in range(_N + 1):
            if s == 0:                      # absorbing death
                V[t][s] = 0.0
                continue
            best, best_p = -1.0, None
            for p, _h in feasible:
                ev = 0.0
                for pi, d in zip(p, _DELTAS):
                    if pi > 0.0:
                        ev += pi * V[t + 1][_clip(s + d)]
                if ev > best + 1e-12:
                    best, best_p = ev, p
            V[t][s] = best
            policy[t][s] = best_p
    return V[0][_S0], policy, h_min


def _terminal_distribution(policy):
    """Propagate the start mass through the optimal policy; exact, no sampling.
    Returns (terminal distribution over states, death probability)."""
    dist = [0.0] * (_N + 1)
    dist[_S0] = 1.0
    for t in range(_T):
        nxt = [0.0] * (_N + 1)
        for s in range(_N + 1):
            m = dist[s]
            if m == 0.0:
                continue
            if s == 0:
                nxt[0] += m
                continue
            p = policy[t][s]
            for pi, d in zip(p, _DELTAS):
                if pi > 0.0:
                    nxt[_clip(s + d)] += m * pi
        dist = nxt
    return dist, dist[0]


def price_of_autonomy() -> dict:
    floors = {
        "coercion": 0.0,            # may collapse B's options entirely
        "autonomy": math.log(2),    # at least two live options each step
        "freedom": math.log(3),     # full option set (uniform): pure random walk
    }
    out = {}
    dists = {}
    for name, h in floors.items():
        v, policy, _ = _solve_ladder(h)
        term, death = _terminal_distribution(policy)
        out[name] = {
            "entropy_floor_nats": round(h, 6),
            "expected_viability": round(v, 6),
            "death_probability": round(death, 6),
        }
        dists[name] = term
    out["price_of_autonomy"] = round(
        out["coercion"]["expected_viability"] - out["autonomy"]["expected_viability"], 6
    )
    out["price_of_freedom"] = round(
        out["coercion"]["expected_viability"] - out["freedom"]["expected_viability"], 6
    )
    out["_terminal_distributions"] = {k: [round(x, 6) for x in v] for k, v in dists.items()}
    out["_ladder"] = {"height": _N, "horizon": _T, "start": _S0}
    # sweep the entropy floor for the figure: viability falls as B keeps options
    sweep = []
    steps = 40
    for i in range(steps + 1):
        h = math.log(3) * i / steps
        v, _, _ = _solve_ladder(h)
        sweep.append((round(h, 6), round(v, 6)))
    out["_sweep_floor_viability"] = sweep
    return out


# ---------------------------------------------------------------------------
# C. Care-curvature: nats of policy deformation per unit viability gain
# ---------------------------------------------------------------------------
# A's baseline self-policy helps with probability q. Delivering a viability gain
# Delta to a target requires raising the help-probability to p = q + Delta/eff,
# where eff is the per-unit efficacy of A's help toward that target. Efficacy
# falls with relational curvature: kin are well modelled and cheaply helped,
# strangers less so. The cost of the shift is KL(Bernoulli(p) || Bernoulli(q))
# in nats; kappa divides it by the gain delivered.

_Q_BASELINE = 0.1     # baseline help-probability of the self-policy
_DELTA = 0.2          # fixed viability gain to deliver
_RELATIONS = {        # relational efficacy (viability gain per unit help-prob)
    "kin": 1.0,
    "stranger": 0.5,
    "distant_stranger": 0.25,
}


def _bernoulli_kl(p: float, q: float) -> float:
    def term(a, b):
        return a * math.log(a / b) if a > 0 else 0.0
    return term(p, q) + term(1 - p, 1 - q)


def _kappa(eff: float, delta: float = _DELTA, q: float = _Q_BASELINE):
    p = q + delta / eff
    if p > 1.0:                      # cannot be reached by a single agent's act
        return None, p
    return _bernoulli_kl(p, q) / delta, p


def care_curvature() -> dict:
    out = {"baseline_help_prob": _Q_BASELINE, "viability_gain": _DELTA}
    rel = {}
    for name, eff in _RELATIONS.items():
        k, p = _kappa(eff)
        rel[name] = {
            "efficacy": eff,
            "required_help_prob": round(p, 6),
            "kappa_nats_per_unit": None if k is None else round(k, 6),
        }
    out["relations"] = rel
    k_kin = rel["kin"]["kappa_nats_per_unit"]
    k_str = rel["stranger"]["kappa_nats_per_unit"]
    k_dist = rel["distant_stranger"]["kappa_nats_per_unit"]
    out["stranger_over_kin"] = round(k_str / k_kin, 6)
    out["distant_over_kin"] = round(k_dist / k_kin, 6)
    # a continuous sweep of efficacy for the figure
    sweep = []
    e = 0.18
    while e <= 1.01:
        k, p = _kappa(e)
        if k is not None:
            sweep.append((round(e, 4), round(k, 6)))
        e += 0.01
    out["_sweep_eff_kappa"] = sweep
    return out


# ---------------------------------------------------------------------------

def run() -> dict:
    return {
        "quasimetric": care_quasimetric(),
        "autonomy": price_of_autonomy(),
        "curvature": care_curvature(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
