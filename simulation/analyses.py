"""Geodesics of Care — the viability manifold as genuine information geometry.

Care is modelled as transport on the statistical manifold of a target's
viability distribution. The manifold carries the Fisher-Rao metric, which
Chentsov's theorem singles out (on a finite sample space) as the unique metric
invariant under sufficient statistics, so the geometry is not a chosen analogy.
On the (n-1)-simplex the Fisher-Rao metric is isometric, via p -> 2*sqrt(p), to
the positive orthant of a sphere of radius 2: constant curvature 1/4, geodesic
distance d(p,q) = 2*arccos(sum_i sqrt(p_i q_i)), maximal distance pi.

Four studies, all deterministic and exact (no seed):

  A. The manifold. Validate that care-distance is a genuine metric and that a
     from-scratch Gaussian-curvature routine (Brioschi) returns 1/4 on the
     Fisher metric, which certifies the differential-geometry machinery used
     downstream.
  B. Routing. A geodesic care-triangle: the triangle inequality HOLDS (the old
     "triangle violation" was an artefact of a non-metric cost), and the real
     invariant is the spherical excess, angle-sum minus pi = curvature x area
     (Gauss-Bonnet). Concern routed through an intermediary is never cheaper.
  C. Directed care. Directedness comes from the carer's control metric, a
     conformal reweighting g_A = f_A * g_Fisher of the base geometry: f_A
     differs by carer, so the cost is asymmetric, and where legibility falls
     the metric's curvature departs from 1/4. Kin/stranger/distant costs are
     geodesic lengths under this metric.
  D. The price of autonomy. Viability is w.p on the 3-state simplex. Total
     coercion drives the target to a vertex (a delta, zero entropy: Canguilhem's
     single norm). The autonomy floor caps the entropy loss; the constrained
     optimum is an exponential-family (Gibbs) tilt, a point on the e-geodesic
     from the uniform distribution. The price of autonomy is the viability
     coercion buys over that floor.

    cd simulation && uv run run_all.py
"""
from __future__ import annotations

import numpy as np

# --------------------------------------------------------------------------- #
# Fisher-Rao geometry on the simplex (convention: p -> 2*sqrt(p), radius-2
# sphere, curvature 1/4, d = 2*arccos(sum sqrt(p q)), max distance pi).
# --------------------------------------------------------------------------- #

def _norm(p):
    p = np.asarray(p, float)
    return p / p.sum()


def fr_distance(p, q):
    """Fisher-Rao geodesic distance between two distributions."""
    p, q = _norm(p), _norm(q)
    c = np.clip(np.sqrt(p * q).sum(), -1.0, 1.0)
    return 2.0 * np.arccos(c)


def sphere_point(p):
    """Unit-sphere embedding u = sqrt(p) (angles here match the radius-2 model)."""
    return np.sqrt(_norm(p))


def fr_geodesic(p, q, t):
    """Point a fraction t along the Fisher-Rao geodesic from p to q (slerp)."""
    u, v = sphere_point(p), sphere_point(q)
    omega = np.arccos(np.clip(u @ v, -1.0, 1.0))
    if omega < 1e-12:
        w = u
    else:
        w = (np.sin((1 - t) * omega) * u + np.sin(t * omega) * v) / np.sin(omega)
    return _norm(w ** 2)


def triangle_angle(vertex, a, b):
    """Interior angle at `vertex` of the geodesic triangle, between the great
    circles to a and to b (computed on the unit-sphere embedding)."""
    u, ua, ub = sphere_point(vertex), sphere_point(a), sphere_point(b)
    ta = ua - (ua @ u) * u
    tb = ub - (ub @ u) * u
    ta /= np.linalg.norm(ta)
    tb /= np.linalg.norm(tb)
    return np.arccos(np.clip(ta @ tb, -1.0, 1.0))


def shannon_entropy(p):
    p = _norm(p)
    nz = p[p > 0]
    return float(-(nz * np.log(nz)).sum())


# --------------------------------------------------------------------------- #
# Gaussian curvature of a 2D metric from its components, by the Brioschi
# formula with numerical partials. Fed the Fisher metric it must return 1/4;
# that self-test certifies the routine before it is used on the care metric.
# Coordinates: (x, y) = (p1, p2), with p3 = 1 - p1 - p2.
# --------------------------------------------------------------------------- #

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


# --------------------------------------------------------------------------- #
# Study A — the manifold, the metric, and the curvature self-test.
# --------------------------------------------------------------------------- #

def study_manifold():
    # care-distance is a genuine metric: sample triples, check the triangle
    # inequality holds (the earlier claim that it could be violated was wrong).
    pts = [
        _norm([0.6, 0.3, 0.1]), _norm([0.2, 0.5, 0.3]), _norm([0.1, 0.2, 0.7]),
        _norm([0.4, 0.4, 0.2]), _norm([0.33, 0.34, 0.33]),
    ]
    worst = 0.0
    for a in pts:
        for b in pts:
            for c in pts:
                slack = fr_distance(a, c) - (fr_distance(a, b) + fr_distance(b, c))
                worst = max(worst, slack)  # must stay <= 0
    triangle_ok = worst <= 1e-9

    # curvature self-test: Brioschi on the Fisher metric over the interior grid
    ks = []
    for x in np.linspace(0.12, 0.76, 9):
        for y in np.linspace(0.12, 0.76, 9):
            if x + y < 0.88:
                ks.append(gaussian_curvature(fisher_EFG, x, y))
    ks = np.array(ks)
    curv_mean = float(ks.mean())
    curv_max_dev = float(np.abs(ks - 0.25).max())

    # a geodesic is genuinely non-Euclidean: compare its length to the straight
    # simplex chord's Fisher length for one representative pair.
    p, q = _norm([0.7, 0.2, 0.1]), _norm([0.1, 0.2, 0.7])
    geo_len = fr_distance(p, q)
    ts = np.linspace(0, 1, 2001)
    chord = np.array([(1 - t) * p + t * q for t in ts])
    chord_len = 0.0
    for i in range(len(ts) - 1):
        chord_len += fr_distance(chord[i], chord[i + 1])
    return {
        "triangle_inequality_holds": bool(triangle_ok),
        "max_triangle_slack": float(worst),
        "curvature_mean": round(curv_mean, 4),
        "curvature_expected": 0.25,
        "curvature_max_abs_dev_from_quarter": round(curv_max_dev, 4),
        "geodesic_length": round(geo_len, 4),
        "straight_chord_length": round(chord_len, 4),
        "chord_excess_percent": round(100 * (chord_len - geo_len) / geo_len, 2),
        "r_curv_mean": round(curv_mean, 2),
    }


# --------------------------------------------------------------------------- #
# Study B — routing and Gauss-Bonnet (the honest replacement for the old,
# impossible, "triangle violation").
# --------------------------------------------------------------------------- #

def study_routing():
    A = _norm([0.75, 0.20, 0.05])   # three viability states / positions
    B = _norm([0.20, 0.60, 0.20])
    C = _norm([0.05, 0.20, 0.75])

    dAB, dBC, dAC = fr_distance(A, B), fr_distance(B, C), fr_distance(A, C)
    routed = dAB + dBC
    gap = routed - dAC                      # >= 0 by the triangle inequality

    ang_A = triangle_angle(A, B, C)
    ang_B = triangle_angle(B, A, C)
    ang_C = triangle_angle(C, A, B)
    excess = (ang_A + ang_B + ang_C) - np.pi   # = K * area
    area = excess / 0.25                        # curvature is 1/4

    return {
        "d_A_to_B": round(dAB, 4),
        "d_B_to_C": round(dBC, 4),
        "d_A_to_C_direct": round(dAC, 4),
        "d_A_to_C_routed": round(routed, 4),
        "routing_gap": round(gap, 4),
        "triangle_inequality_holds": bool(gap >= -1e-9),
        "angle_sum": round(ang_A + ang_B + ang_C, 4),
        "spherical_excess": round(excess, 4),
        "triangle_area": round(area, 4),
        "r_excess": round(excess, 2),
        "r_gap": round(gap, 2),
    }


# --------------------------------------------------------------------------- #
# Study C — directed care: the carer's control metric g_A = f_A * g_Fisher.
# --------------------------------------------------------------------------- #

def _weighted_path_length(p, q, f, n=2000):
    """Length of the Fisher geodesic p->q measured under the conformal metric
    g = f * g_Fisher, i.e. integral of sqrt(f) ds along the geodesic. f(point)
    is the carer's per-length control cost (illegibility). For constant f this
    is exactly sqrt(f) * d_FR."""
    ts = np.linspace(0, 1, n + 1)
    ptsg = [fr_geodesic(p, q, t) for t in ts]
    total = 0.0
    for i in range(n):
        ds = fr_distance(ptsg[i], ptsg[i + 1])
        fmid = 0.5 * (f(ptsg[i]) + f(ptsg[i + 1]))
        total += np.sqrt(fmid) * ds
    return total


def study_directed():
    start = _norm([0.70, 0.22, 0.08])    # target in distress (low flourishing)
    goal = _norm([0.08, 0.22, 0.70])     # target restored to viability
    base = fr_distance(start, goal)

    # (i) directedness: two carers with different legibility fields pay
    # different costs to traverse the SAME geodesic. Carer A reads distress
    # well (low cost near the failing corner); carer D does not.
    def f_A(p):  # good at reaching a distressed target
        return 1.0 + 3.0 * p[0]          # cost rises with the target's failing-mass
    def f_D(p):  # blind to distress
        return 1.0 + 12.0 * p[0]
    cost_A = _weighted_path_length(start, goal, f_A)
    cost_D = _weighted_path_length(start, goal, f_D)

    # (ii) the kin gradient: legibility l in (0,1], control cost f = 1/l^2, so
    # the care-cost is d_FR / l. Kin are transparent (l=1); distance dims them.
    relations = {}
    for name, l in [("kin", 1.0), ("friend", 0.6),
                    ("stranger", 0.4), ("distant_stranger", 0.2)]:
        cost = _weighted_path_length(start, goal, lambda p, l=l: 1.0 / l ** 2)
        relations[name] = {"legibility": l, "care_cost": round(cost, 4)}
    ratio = (relations["distant_stranger"]["care_cost"]
             / relations["kin"]["care_cost"])

    # (iii) curvature of the care metric is no longer constant. With a
    # legibility field that dims toward the failing corner, g_A = f * g_Fisher
    # has curvature that departs from 1/4; report the field.
    def f_field(x, y):
        return 1.0 + 6.0 * x              # x is the failing-state mass
    def care_EFG(x, y):
        E, F, G = fisher_EFG(x, y)
        f = f_field(x, y)
        return f * E, f * F, f * G
    ks = []
    for x in np.linspace(0.12, 0.76, 9):
        for y in np.linspace(0.12, 0.76, 9):
            if x + y < 0.88:
                ks.append(gaussian_curvature(care_EFG, x, y))
    ks = np.array(ks)

    return {
        "geodesic_length_fisher": round(base, 4),
        "directed": {
            "cost_reader_A": round(cost_A, 4),
            "cost_blind_D": round(cost_D, 4),
            "asymmetry_ratio": round(cost_D / cost_A, 4),
        },
        "relations": relations,
        "distant_over_kin": round(ratio, 4),
        "care_curvature_min": round(float(ks.min()), 4),
        "care_curvature_max": round(float(ks.max()), 4),
        "care_curvature_is_variable": bool(ks.max() - ks.min() > 1e-3),
        "r_distant_over_kin": round(ratio, 2),
        "r_asym": round(cost_D / cost_A, 2),
    }


# --------------------------------------------------------------------------- #
# Study D — the price of autonomy: entropy-floored viability on the 3-simplex.
# --------------------------------------------------------------------------- #

def _gibbs(w, tau):
    """Exponential-family tilt p_i ~ exp(w_i / tau): the max-viability
    distribution at fixed entropy, a point on the e-geodesic from uniform."""
    z = np.exp(np.asarray(w, float) / tau)
    return z / z.sum()


def study_autonomy():
    w = np.array([0.0, 0.5, 1.0])         # viability of failing/coping/flourishing
    uniform = _norm([1, 1, 1])

    # coercion: drive the target to the flourishing vertex. Maximal viability,
    # zero entropy, a single norm.
    coercion = np.array([0.0, 0.0, 1.0])
    v_coercion = float(w @ coercion)

    # sweep the entropy floor. At each floor the viability-maximising feasible
    # distribution is the Gibbs tilt whose entropy equals the floor (entropy
    # decreases monotonically as tau falls), found by bisection on tau.
    def v_at_floor(h_floor):
        lo, hi = 1e-3, 50.0               # tau: small=coercive, large=uniform
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if shannon_entropy(_gibbs(w, mid)) < h_floor:
                lo = mid
            else:
                hi = mid
        p = _gibbs(w, 0.5 * (lo + hi))
        return float(w @ p), p

    floor_2opt = np.log(2)                # "keep at least two live options"
    v_auto, p_auto = v_at_floor(floor_2opt)
    price = v_coercion - v_auto

    v_abandon = float(w @ uniform)        # no guidance: uniform, maximal entropy
    death_abandon = float(uniform[0])     # mass on the failing state

    # geometry: coercion drives the target a finite Fisher distance to a
    # boundary vertex where the metric degenerates; autonomy-preserving care
    # stops in the interior.
    d_to_vertex = fr_distance(uniform, coercion)
    d_to_auto = fr_distance(uniform, p_auto)

    curve = []
    for h in np.linspace(0.02, np.log(3) - 1e-6, 25):
        v, _ = v_at_floor(h)
        curve.append((round(float(h), 4), round(v, 4)))

    return {
        "viability_coercion": round(v_coercion, 4),
        "entropy_coercion": 0.0,
        "viability_autonomy_floor": round(v_auto, 4),
        "autonomy_floor_nats": round(float(floor_2opt), 4),
        "autonomy_distribution": [round(float(x), 4) for x in p_auto],
        "price_of_autonomy": round(price, 4),
        "viability_abandonment": round(v_abandon, 4),
        "death_prob_abandonment": round(death_abandon, 4),
        "fr_distance_uniform_to_vertex": round(d_to_vertex, 4),
        "fr_distance_uniform_to_autonomy": round(d_to_auto, 4),
        "viability_vs_entropy": curve,
        "r_price": round(price, 3),
        "r_v_auto": round(v_auto, 3),
        "r_v_abandon": round(v_abandon, 3),
    }


def run():
    return {
        "manifold": study_manifold(),
        "routing": study_routing(),
        "directed": study_directed(),
        "autonomy": study_autonomy(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
