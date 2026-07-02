"""Publication figures for *Geodesics of Care*. The plotters recompute geometry
from analyses (geodesics, curvature field) and read scalar results from the
results dict. Deterministic; no seed."""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import (
    _norm, fr_geodesic, fisher_EFG, gaussian_curvature, shannon_entropy,
)

INK = "#1e1e2e"
MUTED = "#6c7086"
ACCENT = "#8839ef"
WARM = "#d20f39"
COOL = "#1e66f5"


# barycentric (p1,p2,p3) -> 2D coordinates of an equilateral triangle
_V = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]])


def _bary(p):
    p = _norm(p)
    return p @ _V


def _frame(ax):
    tri = np.vstack([_V, _V[0]])
    ax.plot(tri[:, 0], tri[:, 1], color=MUTED, lw=1.0)
    for xy, lab, dx, dy in [(_V[0], "failing", -0.02, -0.06),
                            (_V[1], "coping", 0.02, -0.06),
                            (_V[2], "flourishing", 0.0, 0.03)]:
        ax.annotate(lab, xy, xytext=(xy[0] + dx, xy[1] + dy),
                    ha="center", fontsize=8, color=MUTED)
    ax.set_aspect("equal")
    ax.axis("off")


def plot_geometry(results, path):
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.6))

    # --- left: the geodesic care-triangle, with the spherical excess ---
    _frame(axL)
    A = _norm([0.75, 0.20, 0.05]); B = _norm([0.20, 0.60, 0.20]); C = _norm([0.05, 0.20, 0.75])
    for P, Q in [(A, B), (B, C), (A, C)]:
        arc = np.array([_bary(fr_geodesic(P, Q, t)) for t in np.linspace(0, 1, 200)])
        axL.plot(arc[:, 0], arc[:, 1], color=ACCENT, lw=2.0)
    # the Euclidean chord A-C, to show the geodesic bows away from it
    chord = np.array([_bary(A), _bary(C)])
    axL.plot(chord[:, 0], chord[:, 1], color=MUTED, lw=1.0, ls=(0, (4, 3)))
    for P, lab in [(A, "A"), (B, "B"), (C, "C")]:
        xy = _bary(P)
        axL.scatter(*xy, color=INK, s=36, zorder=5)
        axL.annotate(lab, xy, xytext=(xy[0] + 0.02, xy[1] + 0.02), fontsize=11, color=INK)
    rt = results["routing"]
    axL.set_title("A geodesic care-triangle", fontsize=10, color=INK)
    axL.text(0.5, -0.16,
             f"angle sum {rt['angle_sum']} > $\\pi$   ·   excess {rt['spherical_excess']} = "
             f"(1/4) × area {rt['triangle_area']}\n"
             f"routed A→B→C {rt['d_A_to_C_routed']} > direct A→C {rt['d_A_to_C_direct']} "
             f"(gap {rt['routing_gap']})",
             transform=axL.transAxes, ha="center", va="top", fontsize=8, color=MUTED)

    # --- right: the care-metric curvature field (varies; base Fisher is 1/4) ---
    def f_field(x, y):
        return 1.0 + 6.0 * x
    def care_EFG(x, y):
        E, F, G = fisher_EFG(x, y)
        f = f_field(x, y)
        return f * E, f * F, f * G
    xs, ys, ks = [], [], []
    for x in np.linspace(0.08, 0.84, 60):
        for y in np.linspace(0.08, 0.84, 60):
            if min(x, y, 1 - x - y) > 0.08:   # stay off the boundary (edge artefacts)
                xy = _bary([x, y, 1 - x - y])
                xs.append(xy[0]); ys.append(xy[1])
                ks.append(gaussian_curvature(care_EFG, x, y))
    _frame(axR)
    sc = axR.scatter(xs, ys, c=ks, s=16, cmap="viridis", marker="s",
                     vmin=0.13, vmax=0.27)
    cb = fig.colorbar(sc, ax=axR, fraction=0.046, pad=0.04)
    cb.set_label("Gaussian curvature of the care metric", fontsize=8, color=INK)
    cb.ax.tick_params(labelsize=7)
    axR.set_title("Curvature bends with legibility", fontsize=10, color=INK)
    dc = results["directed"]
    axR.text(0.5, -0.16,
             f"base Fisher curvature $\\equiv$ 1/4; care-metric curvature ranges "
             f"{dc['care_curvature_min']}–{dc['care_curvature_max']}",
             transform=axR.transAxes, ha="center", va="top", fontsize=8, color=MUTED)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_care(results, path):
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.3))
    dc = results["directed"]

    # --- left: the kin gradient, care-cost vs legibility ---
    rel = dc["relations"]
    order = ["kin", "friend", "stranger", "distant_stranger"]
    labs = ["kin", "friend", "stranger", "distant\nstranger"]
    ls = [rel[k]["legibility"] for k in order]
    cs = [rel[k]["care_cost"] for k in order]
    ll = np.linspace(0.16, 1.0, 200)
    axL.plot(ll, dc["geodesic_length_fisher"] / ll, color=MUTED, lw=1.2, zorder=1)
    axL.scatter(ls, cs, color=ACCENT, s=60, zorder=3)
    for l, c, lab in zip(ls, cs, labs):
        axL.annotate(lab, (l, c), xytext=(l + 0.02, c + 0.15), fontsize=8, color=INK)
    axL.set_xlabel("legibility of the other  $\\ell$", fontsize=9)
    axL.set_ylabel("care-cost  (geodesic length under $g_A$)", fontsize=9)
    axL.set_title(f"The kin gradient: distant costs {dc['r_distant_over_kin']}× kin",
                  fontsize=10, color=INK)
    axL.invert_xaxis()
    axL.spines[["top", "right"]].set_visible(False)

    # --- right: directedness, two carers on the same geodesic ---
    d = dc["directed"]
    bars = axR.bar(["reader A", "blind D"], [d["cost_reader_A"], d["cost_blind_D"]],
                   color=[COOL, WARM], width=0.55)
    for b, v in zip(bars, [d["cost_reader_A"], d["cost_blind_D"]]):
        axR.text(b.get_x() + b.get_width() / 2, v + 0.05, f"{v}",
                 ha="center", fontsize=9, color=INK)
    axR.set_ylabel("care-cost of the same restoration", fontsize=9)
    axR.set_title(f"Directedness: {d['asymmetry_ratio']}× by who reads the other",
                  fontsize=10, color=INK)
    axR.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_autonomy(results, path):
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.3))
    a = results["autonomy"]

    # --- left: viability vs the entropy floor ---
    curve = np.array(a["viability_vs_entropy"])
    axL.plot(curve[:, 0], curve[:, 1], color=ACCENT, lw=2.0)
    axL.scatter([0.0], [a["viability_coercion"]], color=WARM, s=55, zorder=5)
    axL.annotate("coercion\n(single norm)", (0.0, a["viability_coercion"]),
                 xytext=(0.05, 0.97), fontsize=8, color=WARM)
    axL.scatter([a["autonomy_floor_nats"]], [a["viability_autonomy_floor"]],
                color=COOL, s=55, zorder=5)
    axL.annotate("autonomy floor\n$H\\geq\\ln 2$", (a["autonomy_floor_nats"],
                 a["viability_autonomy_floor"]), xytext=(0.72, 0.9), fontsize=8, color=COOL)
    axL.scatter([np.log(3)], [a["viability_abandonment"]], color=MUTED, s=55, zorder=5)
    axL.annotate("abandonment\n(uniform)", (np.log(3), a["viability_abandonment"]),
                 xytext=(0.7, 0.52), fontsize=8, color=MUTED)
    axL.set_xlabel("floor on the other's option-entropy  (nats)", fontsize=9)
    axL.set_ylabel("attained viability", fontsize=9)
    axL.set_title(f"The price of autonomy is {a['price_of_autonomy']}", fontsize=10, color=INK)
    axL.spines[["top", "right"]].set_visible(False)

    # --- right: the three distributions over the viability states ---
    states = ["failing", "coping", "flourishing"]
    coercion = [0.0, 0.0, 1.0]
    auto = a["autonomy_distribution"]
    uniform = [1 / 3, 1 / 3, 1 / 3]
    x = np.arange(3); w = 0.26
    axR.bar(x - w, coercion, w, label="coercion", color=WARM)
    axR.bar(x, auto, w, label="autonomy-preserving", color=COOL)
    axR.bar(x + w, uniform, w, label="abandonment", color=MUTED)
    axR.set_xticks(x); axR.set_xticklabels(states, fontsize=9)
    axR.set_ylabel("probability mass", fontsize=9)
    axR.set_title("Where each policy leaves the other", fontsize=10, color=INK)
    axR.legend(fontsize=8, frameon=False)
    axR.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
