"""Illustrative Fisher-Rao geometry, assigned effort and recipient permission.

The representation, metric invariance requirement, utilities and effort fields
are modeling choices. Numerical consistency checks do not validate a theory of
care. Outcome entropy is independent of who may authorize a transition.

Distances use the radius-2 sphere convention. Curvature and path integrals are
numerical; results retain full precision rather than rounding error to zero.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


def _norm(p):
    """Normalize finite nonnegative weights; reject invalid distributions."""
    p = np.asarray(p, float)
    if p.ndim != 1 or len(p) < 2 or not np.isfinite(p).all() or (p < 0).any():
        raise ValueError("expected a finite nonnegative vector of at least two weights")
    total = p.sum()
    if not np.isfinite(total) or total <= 0:
        raise ValueError("distribution must have positive finite mass")
    return p / total


def sphere_point(p):
    return np.sqrt(_norm(p))


def fr_distance(p, q):
    """Radius-2 great-circle distance, using a stable half-angle expression."""
    u, v = sphere_point(p), sphere_point(q)
    if u.shape != v.shape:
        raise ValueError("distributions must have the same state space")
    return float(4.0 * np.arctan2(np.linalg.norm(u - v), np.linalg.norm(u + v)))


def fr_geodesic(p, q, t):
    """Fraction t of the shortest Fisher-Rao arc; no actuation model is implied."""
    if not np.isfinite(t) or not 0 <= t <= 1:
        raise ValueError("geodesic fraction must be between zero and one")
    u, v = sphere_point(p), sphere_point(q)
    omega = fr_distance(p, q) / 2
    if t == 0:
        return _norm(p)
    if t == 1:
        return _norm(q)
    if omega < 1e-12:
        return _norm(p)
    w = (np.sin((1 - t) * omega) * u + np.sin(t * omega) * v) / np.sin(omega)
    return _norm(w ** 2)


def triangle_angle(vertex, a, b):
    u, ua, ub = sphere_point(vertex), sphere_point(a), sphere_point(b)
    ta, tb = ua - (ua @ u) * u, ub - (ub @ u) * u
    na, nb = np.linalg.norm(ta), np.linalg.norm(tb)
    if min(na, nb) < 1e-12:
        raise ValueError("triangle angle requires distinct vertices")
    return float(np.arccos(np.clip((ta @ tb) / (na * nb), -1.0, 1.0)))


def spherical_triangle_area(p, q, r):
    """Independent solid-angle formula, scaled by radius squared (four)."""
    u, v, w = sphere_point(p), sphere_point(q), sphere_point(r)
    numerator = abs(np.linalg.det(np.stack([u, v, w])))
    denominator = 1 + u @ v + v @ w + w @ u
    return float(8.0 * np.arctan2(numerator, denominator))


def shannon_entropy(p):
    p = _norm(p)
    nz = p[p > 0]
    return max(0.0, float(-(nz * np.log(nz)).sum()))


def fisher_EFG(x, y):
    """Fisher-Rao metric components in simplex coordinates (p1, p2)."""
    p3 = 1.0 - x - y
    E = 1.0 / x + 1.0 / p3          # g_11
    F = 1.0 / p3                     # g_12
    G = 1.0 / y + 1.0 / p3          # g_22
    return E, F, G


def gaussian_curvature(EFG, x, y, h=1e-4):
    """Brioschi formula for K from a metric callable EFG(x, y) -> (E, F, G)."""
    def E(a, b): return EFG(a, b)[0]
    def F(a, b): return EFG(a, b)[1]
    def G(a, b): return EFG(a, b)[2]

    E0, F0, G0 = EFG(x, y)
    # first derivatives (central differences)
    Ex = (E(x + h, y) - E(x - h, y)) / (2 * h)
    Ey = (E(x, y + h) - E(x, y - h)) / (2 * h)
    Fx = (F(x + h, y) - F(x - h, y)) / (2 * h)
    Fy = (F(x, y + h) - F(x, y - h)) / (2 * h)
    Gx = (G(x + h, y) - G(x - h, y)) / (2 * h)
    Gy = (G(x, y + h) - G(x, y - h)) / (2 * h)
    # second derivatives needed by Brioschi
    Eyy = (E(x, y + h) - 2 * E0 + E(x, y - h)) / h ** 2
    Gxx = (G(x + h, y) - 2 * G0 + G(x - h, y)) / h ** 2
    Fxy = (F(x + h, y + h) - F(x + h, y - h)
           - F(x - h, y + h) + F(x - h, y - h)) / (4 * h ** 2)

    m1 = np.array([
        [-0.5 * Eyy + Fxy - 0.5 * Gxx, 0.5 * Ex, Fx - 0.5 * Ey],
        [Fy - 0.5 * Gx,                E0,       F0],
        [0.5 * Gy,                     F0,       G0],
    ])
    m2 = np.array([
        [0.0,       0.5 * Ey, 0.5 * Gx],
        [0.5 * Ey,  E0,       F0],
        [0.5 * Gx,  F0,       G0],
    ])
    denom = (E0 * G0 - F0 ** 2) ** 2
    return float((np.linalg.det(m1) - np.linalg.det(m2)) / denom)



def conformal_curvature_exact(x, alpha=6.0):
    """For f=1+alpha*x: K_f=(1/4 - (1/2) Delta_F log(f))/f.

    On the three-state Fisher simplex, Delta_F x=(1-3x)/2 and
    squared norm of grad_F x=x(1-x). This is independent of finite differences.
    """
    f = 1.0 + alpha * x
    lap_log_f = alpha * (1 - 3 * x) / (2 * f) - alpha ** 2 * x * (1 - x) / f ** 2
    return float((0.25 - 0.5 * lap_log_f) / f)


def _interior_grid():
    return [(float(x), float(y))
            for x in np.linspace(0.12, 0.76, 9)
            for y in np.linspace(0.12, 0.76, 9) if x + y < 0.88]


def study_manifold():
    points = [[0.6, 0.3, 0.1], [0.2, 0.5, 0.3], [0.1, 0.2, 0.7],
              [0.4, 0.4, 0.2], [0.33, 0.34, 0.33]]
    slacks = [fr_distance(a, c) - fr_distance(a, b) - fr_distance(b, c)
              for a in points for b in points for c in points]
    sensitivity = []
    for h in (1e-3, 3e-4, 1e-4):
        estimates = [gaussian_curvature(fisher_EFG, x, y, h) for x, y in _interior_grid()]
        sensitivity.append({"step": h, "mean": float(np.mean(estimates)),
                            "max_abs_error": float(np.max(np.abs(np.array(estimates) - 0.25)))})
    p, q = np.array([0.7, 0.2, 0.1]), np.array([0.1, 0.2, 0.7])
    ts = np.linspace(0, 1, 2001)
    chord = [(1 - t) * p + t * q for t in ts]
    chord_length = sum(fr_distance(a, b) for a, b in zip(chord[:-1], chord[1:]))
    return {
        "points": points, "triples_checked": len(slacks),
        "max_positive_triangle_slack": float(max(0.0, max(slacks))),
        "triangle_inequality_holds": bool(max(slacks) <= 1e-9),
        "curvature_expected": 0.25, "grid": _interior_grid(),
        "curvature_step_sensitivity": sensitivity,
        "curvature_mean": sensitivity[-1]["mean"],
        "curvature_max_abs_error": sensitivity[-1]["max_abs_error"],
        "path_start": p.tolist(), "path_goal": q.tolist(), "path_segments": 2000,
        "geodesic_length": fr_distance(p, q),
        "straight_coordinate_path_length": float(chord_length),
    }


def study_routing():
    p, q, r = [0.75, 0.20, 0.05], [0.20, 0.60, 0.20], [0.05, 0.20, 0.75]
    pq, qr, pr = fr_distance(p, q), fr_distance(q, r), fr_distance(p, r)
    angles = [triangle_angle(p, q, r), triangle_angle(q, p, r), triangle_angle(r, p, q)]
    excess = sum(angles) - np.pi
    area = spherical_triangle_area(p, q, r)
    # A flat counterexample: a detour can cost more without any curvature.
    flat_p, flat_q, flat_r = np.array([0., 0.]), np.array([1., 1.]), np.array([2., 0.])
    flat_direct = float(np.linalg.norm(flat_r - flat_p))
    flat_routed = float(np.linalg.norm(flat_q - flat_p) + np.linalg.norm(flat_r - flat_q))
    return {
        "points": {"p": p, "q": q, "r": r},
        "d_pq": pq, "d_qr": qr, "d_pr": pr,
        "routed_length": pq + qr, "routing_gap": pq + qr - pr,
        "angles": angles, "angle_sum": float(sum(angles)),
        "spherical_excess": float(excess), "triangle_area": area,
        "gauss_bonnet_abs_residual": float(abs(excess - 0.25 * area)),
        "flat_counterexample": {"direct": flat_direct, "routed": flat_routed,
                                "gap": flat_routed - flat_direct},
    }


def _weighted_path_length(p, q, f, n=2000):
    """Midpoint quadrature of sqrt(f) ds along the fixed Fisher geodesic.

    A variable f generally changes the shortest path; this routine does not
    optimize it. The tensor factor is f, the per-length multiplier is sqrt(f).
    """
    if type(n) is not int or n < 1:
        raise ValueError("quadrature requires a positive number of segments")
    factors = [float(f(fr_geodesic(p, q, (i + 0.5) / n))) for i in range(n)]
    if not np.isfinite(factors).all() or min(factors) <= 0:
        raise ValueError("metric multipliers must be positive and finite")
    return float(fr_distance(p, q) * np.sqrt(factors).mean())


def study_effort():
    start, goal = [0.70, 0.22, 0.08], [0.08, 0.22, 0.70]
    base = fr_distance(start, goal)
    constants = [{"efficiency": ell, "tensor_factor": 1 / ell ** 2,
                  "path_length": base / ell} for ell in (1.0, 0.6, 0.4, 0.2)]
    variable = []
    for alpha in (3.0, 12.0):
        f = lambda p, alpha=alpha: 1.0 + alpha * p[0]
        forward = _weighted_path_length(start, goal, f)
        reverse = _weighted_path_length(goal, start, f)
        variable.append({"alpha": alpha, "path_length": forward,
                         "reversed_path_length": reverse,
                         "symmetry_abs_residual": abs(forward - reverse)})
    def conformal_EFG(x, y):
        return tuple((1 + 6 * x) * value for value in fisher_EFG(x, y))
    samples = [{"x": x, "y": y,
                "numerical": gaussian_curvature(conformal_EFG, x, y),
                "analytic": conformal_curvature_exact(x)} for x, y in _interior_grid()]
    return {
        "start": start, "goal": goal, "base_distance": base,
        "constant_factors": constants,
        "lowest_over_highest_efficiency_cost": constants[-1]["path_length"] / constants[0]["path_length"],
        "variable_fields": variable,
        "variable_field_cost_ratio": variable[1]["path_length"] / variable[0]["path_length"],
        "curvature_alpha": 6.0, "curvature_samples": samples,
        "curvature_min": min(row["numerical"] for row in samples),
        "curvature_max": max(row["numerical"] for row in samples),
        "curvature_max_abs_error": max(abs(row["numerical"] - row["analytic"]) for row in samples),
    }


def _gibbs(w, tau):
    if not np.isfinite(tau) or tau <= 0:
        raise ValueError("temperature must be positive and finite")
    w = np.asarray(w, float)
    z = np.exp((w - w.max()) / tau)
    return z / z.sum()


def entropy_constrained_optimum(weights, floor):
    """Maximize an assigned expected utility subject to H(p) >= floor.

    No authority, action menu or welfare interpretation follows from entropy.
    Endpoints and tied maxima are handled directly; interior solutions use a
    stable Gibbs tilt and bracketed bisection.
    """
    w = np.asarray(weights, float)
    if w.ndim != 1 or len(w) < 2 or not np.isfinite(w).all():
        raise ValueError("expected a finite utility vector")
    maximum_entropy = float(np.log(len(w)))
    if not np.isfinite(floor) or not 0 <= floor <= maximum_entropy:
        raise ValueError("entropy floor must be between zero and log(state count)")
    maxima = (w == w.max()).astype(float)
    top = maxima / maxima.sum()
    if floor <= shannon_entropy(top) + 1e-12:
        return top
    if maximum_entropy - floor <= 1e-12:
        return np.full(len(w), 1 / len(w))
    lo, hi = 0.0, max(float(np.ptp(w)), 1.0)
    for _ in range(100):
        if shannon_entropy(_gibbs(w, hi)) >= floor:
            break
        hi *= 2
    else:
        raise ArithmeticError("could not bracket entropy-constrained optimum")
    for _ in range(120):
        mid = (lo + hi) / 2
        if shannon_entropy(_gibbs(w, mid)) < floor:
            lo = mid
        else:
            hi = mid
    return _gibbs(w, hi)


def study_entropy():
    weights = np.array([0.0, 0.5, 1.0])
    uniform, vertex = np.full(3, 1 / 3), np.array([0., 0., 1.])
    floor = float(np.log(2))
    optimum = entropy_constrained_optimum(weights, floor)
    # The former prose used coping+flourishing probability: a different utility.
    alternative_weights = np.array([0.0, 1.0, 1.0])
    alternative = entropy_constrained_optimum(alternative_weights, floor)
    curve = []
    for h in np.linspace(0, np.log(3), 26):
        p = entropy_constrained_optimum(weights, float(h))
        curve.append({"floor": float(h), "utility": float(weights @ p),
                      "entropy": shannon_entropy(p), "distribution": p.tolist()})
    return {
        "weights": weights.tolist(), "floor_nats": floor,
        "vertex": vertex.tolist(), "vertex_utility": float(weights @ vertex),
        "vertex_entropy": shannon_entropy(vertex),
        "floor_distribution": optimum.tolist(), "floor_utility": float(weights @ optimum),
        "floor_entropy": shannon_entropy(optimum),
        "utility_cost_of_floor": float(weights @ vertex - weights @ optimum),
        "uniform": uniform.tolist(), "uniform_utility": float(weights @ uniform),
        "uniform_entropy": shannon_entropy(uniform),
        "uniform_failing_mass": float(uniform[0]),
        "distance_uniform_to_vertex": fr_distance(uniform, vertex),
        "distance_uniform_to_floor": fr_distance(uniform, optimum),
        "utility_vs_entropy": curve,
        "alternative_score": {"weights": alternative_weights.tolist(),
                              "distribution": alternative.tolist(),
                              "utility": float(alternative_weights @ alternative),
                              "cost_of_floor": float(alternative_weights.max() - alternative_weights @ alternative)},
    }


@dataclass(frozen=True)
class Permission:
    """Exogenous recipient instruction, not inferred from outcome probabilities.

    This toy assumes a valid instruction channel. It models neither consent
    capacity nor resistance, manipulation, authentication or emergency duties.
    """
    approved_target: tuple[float, ...] | None = None
    max_fraction: float = 0.25
    revoked: bool = False

    def __post_init__(self):
        if type(self.revoked) is not bool:
            raise ValueError("revoked must be a boolean")
        if not np.isfinite(self.max_fraction) or not 0 <= self.max_fraction <= 1:
            raise ValueError("permission fraction must be between zero and one")
        if self.approved_target is not None:
            object.__setattr__(self, "approved_target", tuple(_norm(self.approved_target)))


def permitted_step(current, proposed_target, fraction, permission):
    """Apply only an authorized bounded transition; otherwise apply no action.

    Transitions are stipulated Fisher arcs. With no autonomous drift in this
    example, no action leaves the modeled distribution unchanged. Actual
    shutdown may require a safe transition rather than immediately doing nothing.
    """
    p, target = _norm(current), _norm(proposed_target)
    if p.shape != target.shape:
        raise ValueError("target and current state spaces differ")
    if not isinstance(permission, Permission):
        raise ValueError("an explicit Permission record is required")
    if not np.isfinite(fraction) or not 0 <= fraction <= 1:
        raise ValueError("proposed fraction must be between zero and one")
    reason = "authorized"
    if permission.revoked:
        reason = "revoked"
    elif permission.approved_target is None:
        reason = "no permission"
    elif (len(permission.approved_target) != len(target) or
          not np.allclose(target, permission.approved_target, rtol=0, atol=1e-12)):
        reason = "unapproved target"
    applied_fraction = min(float(fraction), permission.max_fraction) if reason == "authorized" else 0.0
    state = fr_geodesic(p, target, applied_fraction) if applied_fraction else p
    return {"state": state.tolist(), "applied": applied_fraction > 0,
            "fraction": applied_fraction, "reason": reason}


def study_permission():
    initial, vertex, uniform = [0.70, 0.22, 0.08], [0., 0., 1.], [1/3, 1/3, 1/3]
    consent = Permission(tuple(vertex), max_fraction=1.0)
    chosen = permitted_step(initial, vertex, 1.0, consent)
    rejected = permitted_step(initial, uniform, 1.0, consent)
    missing = permitted_step(initial, vertex, 1.0, Permission())
    trace, state = [], initial
    for step in range(5):
        authority = Permission(tuple(vertex), max_fraction=0.25, revoked=step >= 2)
        before = list(state)
        decision = permitted_step(state, vertex, 0.25, authority)
        state = decision["state"]
        trace.append({"step": step, "before": before, **decision})
    changed_target = [0., 0.9, 0.1]
    changed_permission = Permission(tuple(changed_target), max_fraction=1.0)
    old_goal = permitted_step(initial, vertex, 1.0, changed_permission)
    new_goal = permitted_step(initial, changed_target, 1.0, changed_permission)
    return {
        "chosen_predictable_outcome": {**chosen, "entropy": shannon_entropy(chosen["state"])},
        "unapproved_high_entropy_proposal": {
            "proposed_distribution": uniform, "proposed_entropy": shannon_entropy(uniform),
            "entropy_floor_met": bool(shannon_entropy(uniform) >= np.log(2)), **rejected},
        "no_permission": missing, "revocation_trace": trace,
        "actions_after_revocation": sum(row["applied"] for row in trace[2:]),
        "changed_goal": {"stale_proposal": old_goal, "accepted_proposal": new_goal,
                         "assigned_utility": float(np.array([0., 0.5, 1.]) @ changed_target)},
    }


def run():
    return {"manifold": study_manifold(), "routing": study_routing(),
            "effort": study_effort(), "entropy": study_entropy(),
            "permission": study_permission()}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, allow_nan=False))
