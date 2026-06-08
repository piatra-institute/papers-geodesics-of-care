"""Publication figures for *Geodesics of Care*. Pure plotters: every value is
read from the results dict produced by analyses.run(). Deterministic."""
from __future__ import annotations

import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

INK = "#1a1a1a"
ACCENT = "#b3202c"   # red
COOL = "#2a5b8c"     # blue
MUTE = "#8a8a8a"
GOLD = "#c98a1a"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 0.8,
})


# ---------------------------------------------------------------------------
def plot_autonomy(results: dict, path: str) -> None:
    aut = results["autonomy"]
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.4))

    # --- left: viability vs the entropy floor (the price of autonomy) --------
    sweep = aut["_sweep_floor_viability"]
    xs = [h for h, _ in sweep]
    ys = [v for _, v in sweep]
    axL.plot(xs, ys, color=INK, lw=1.8, zorder=3)
    axL.fill_between(xs, ys, min(ys) - 0.02, color=COOL, alpha=0.06, zorder=0)

    pts = {
        "coercion": (0.0, aut["coercion"]["expected_viability"], ACCENT, "coercion\n(H=0, options collapsed)"),
        "autonomy": (math.log(2), aut["autonomy"]["expected_viability"], COOL, "autonomy-preserving\n(H ≥ ln 2)"),
        "freedom": (math.log(3), aut["freedom"]["expected_viability"], MUTE, "abandonment\n(H = ln 3, no guidance)"),
    }
    for _, (x, y, c, lab) in pts.items():
        axL.scatter([x], [y], s=46, color=c, zorder=5, edgecolor="white", linewidth=0.8)
    # annotate the price of autonomy: the tiny gap between the coercive optimum
    # (H=0, V=1) and the autonomy-preserving optimum (H>=ln2)
    yc = pts["coercion"][1]
    ya = pts["autonomy"][1]
    axL.annotate(
        f"price of autonomy = {aut['price_of_autonomy']:.3f}\n"
        f"(coercion buys only this much\nmore viability than free-but-guided B)",
        xy=(math.log(2), ya), xytext=(0.30, 0.66),
        fontsize=8.5, color=GOLD, va="center", ha="left",
        arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.2))
    axL.text(0.02, yc + 0.015, "coercion", fontsize=8.5, color=ACCENT, ha="left")
    axL.text(math.log(2) + 0.03, ya + 0.012, "autonomy-preserving", fontsize=8.5, color=COOL, ha="left")
    axL.text(math.log(3), pts["freedom"][1] + 0.035, "abandonment", fontsize=8.5, color=MUTE, ha="right")
    axL.set_xlabel("per-step option-entropy floor on B  (nats)")
    axL.set_ylabel("B's expected terminal viability")
    axL.set_xticks([0, math.log(2), math.log(3)])
    axL.set_xticklabels(["0", "ln 2", "ln 3"])
    axL.set_ylim(min(ys) - 0.03, 1.03)
    axL.set_title("Viability bought by collapsing options", fontsize=10.5)

    # --- right: terminal viability distributions -----------------------------
    td = aut["_terminal_distributions"]
    states = list(range(aut["_ladder"]["height"] + 1))
    w = 0.27
    axR.bar([s - w for s in states], td["coercion"], width=w, color=ACCENT, label="coercion", alpha=0.9)
    axR.bar(states, td["autonomy"], width=w, color=COOL, label="autonomy-preserving", alpha=0.9)
    axR.bar([s + w for s in states], td["freedom"], width=w, color=MUTE, label="abandonment", alpha=0.85)
    axR.set_xlabel("B's terminal state on the viability ladder  (0 = death, 8 = flourishing)")
    axR.set_ylabel("probability")
    axR.set_xticks(states)
    axR.legend(frameon=False, fontsize=8.5, loc="upper left")
    axR.set_title("Where B lands", fontsize=10.5)

    fig.suptitle("The price of autonomy: an exact care-control problem", fontsize=12, y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
def plot_curvature(results: dict, path: str) -> None:
    cur = results["curvature"]
    qm = results["quasimetric"]
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.4))

    # --- left: kappa vs relational curvature ---------------------------------
    sweep = cur["_sweep_eff_kappa"]
    # plot against curvature = 1/efficacy so the axis reads "harder to the right"
    xs = [1.0 / e for e, _ in sweep]
    ys = [k for _, k in sweep]
    axL.plot(xs, ys, color=INK, lw=1.8, zorder=3)
    rel = cur["relations"]
    marks = {
        "kin": (rel["kin"], COOL),
        "stranger": (rel["stranger"], GOLD),
        "distant_stranger": (rel["distant_stranger"], ACCENT),
    }
    labels = {"kin": "kin", "stranger": "stranger", "distant_stranger": "distant stranger"}
    for name, (r, c) in marks.items():
        x = 1.0 / r["efficacy"]
        y = r["kappa_nats_per_unit"]
        axL.scatter([x], [y], s=48, color=c, zorder=5, edgecolor="white", linewidth=0.8)
        axL.annotate(f"{labels[name]}\nκ = {y:.2f}", (x, y),
                     textcoords="offset points", xytext=(8, -2), fontsize=8.5, color=c,
                     va="top")
    axL.set_xlabel("relational curvature  (1 / efficacy)")
    axL.set_ylabel("κ : nats of policy deformation per unit viability gain")
    axL.set_title("Kin are geometrically cheap to reach", fontsize=10.5)

    # --- right: the quasi-metric (asymmetry + triangle failure) --------------
    # asymmetry pair
    axR.bar([0.0, 0.7], [qm["d_A_to_B"], qm["d_B_to_A"]], width=0.6,
            color=[COOL, GOLD], alpha=0.9)
    axR.text(0.0, qm["d_A_to_B"] + 0.06, f"d(A→B)\n{qm['d_A_to_B']}", ha="center", fontsize=8.5, color=COOL)
    axR.text(0.7, qm["d_B_to_A"] + 0.06, f"d(B→A)\n{qm['d_B_to_A']}", ha="center", fontsize=8.5, color=GOLD)
    axR.text(0.35, max(qm["d_A_to_B"], qm["d_B_to_A"]) + 0.5, "asymmetry", ha="center", fontsize=9, color=INK)

    # triangle: direct vs routed
    axR.bar([2.0, 2.7], [qm["d_A_to_C_direct"], qm["d_A_to_C_routed"]], width=0.6,
            color=[ACCENT, MUTE], alpha=0.9)
    axR.text(2.0, qm["d_A_to_C_direct"] + 0.06, f"direct\nd(A→C)\n{qm['d_A_to_C_direct']}", ha="center", fontsize=8.5, color=ACCENT)
    axR.text(2.7, qm["d_A_to_C_routed"] + 0.06, f"d(A→B)+d(B→C)\n{qm['d_A_to_C_routed']}", ha="center", fontsize=8.5, color=MUTE)
    axR.annotate("", xy=(2.0, qm["d_A_to_C_direct"]), xytext=(2.0, qm["d_A_to_C_routed"]),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.2))
    axR.text(1.3, (qm["d_A_to_C_direct"] + qm["d_A_to_C_routed"]) / 2,
             f"triangle excess\n+{qm['triangle_excess']}", fontsize=8.5, color=INK, va="center")
    axR.text(2.35, qm["d_A_to_C_direct"] + 0.7, "triangle inequality fails", ha="center", fontsize=9, color=INK)

    axR.set_xticks([0.35, 2.35])
    axR.set_xticklabels(["same pair,\nopposite direction", "reaching C:\ndirect vs routed"])
    axR.set_ylabel("care-distance  (model units)")
    axR.set_ylim(0, qm["d_A_to_C_direct"] + 1.4)
    axR.set_title("Care-distance is a directed quasi-metric", fontsize=10.5)

    fig.suptitle("Curvature and the quasi-metric of concern", fontsize=12, y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
