"""Figures for the declared geometry, costs and uncertainty calculation.

Neutral labels distinguish assigned parameters from measured social relations.
Plot markers come from results.json; continuous curves illustrate the formulas.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import _norm, fr_geodesic, conformal_curvature_exact

INK, MUTED = "#222222", "#727272"
ACCENT, WARM, COOL = "#713D73", "#B6603B", "#2A7183"
_V = np.array([[0., 0.], [1., 0.], [.5, np.sqrt(3) / 2]])


def _bary(p):
    return _norm(p) @ _V


def _frame(ax):
    tri = np.vstack([_V, _V[0]])
    ax.plot(tri[:, 0], tri[:, 1], color=MUTED, lw=1)
    for xy, label, dy in [(_V[0], "failing", -.055),
                           (_V[1], "coping", -.055),
                           (_V[2], "flourishing", .035)]:
        ax.text(xy[0], xy[1] + dy, label, ha="center", fontsize=10, color=MUTED)
    ax.set_aspect("equal")
    ax.set_xlim(-.13, 1.13)
    ax.set_ylim(-.1, 1.03)
    ax.axis("off")


def _finish(fig, path):
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_geometry(results, path):
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 4.3), layout="constrained")
    _frame(left)
    points = results["routing"]["points"]
    for a, b in [("p", "q"), ("q", "r"), ("p", "r")]:
        arc = np.array([_bary(fr_geodesic(points[a], points[b], t))
                        for t in np.linspace(0, 1, 201)])
        left.plot(arc[:, 0], arc[:, 1], color=ACCENT, lw=2)
    for name, point in points.items():
        xy = _bary(point)
        left.scatter(*xy, color=INK, s=28, zorder=3)
        left.annotate(name, xy, xytext=(5, 7), textcoords="offset points", fontsize=12)
    left.set_title("Three distributions, Fisher arcs", fontsize=11)
    samples = results["effort"]["curvature_samples"]
    xs = np.linspace(min(row["x"] for row in samples), max(row["x"] for row in samples), 201)
    right.plot(xs, [conformal_curvature_exact(x) for x in xs],
               color=ACCENT, lw=2, label="analytic, $f=1+6p_1$")
    right.scatter([row["x"] for row in samples], [row["numerical"] for row in samples],
                  color=INK, s=20, label="finite differences", zorder=3)
    right.axhline(.25, color=MUTED, ls="--", label="base Fisher metric")
    right.set_xlabel("Failing probability  $p_1$", fontsize=10)
    right.set_ylabel("Gaussian curvature", fontsize=10)
    right.set_title("A chosen effort field changes curvature", fontsize=11)
    right.spines[["top", "right"]].set_visible(False)
    right.legend(fontsize=9, frameon=False, loc="lower left")
    _finish(fig, path)


def plot_effort(results, path):
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 4.1), layout="constrained")
    effort = results["effort"]
    ell = np.linspace(.2, 1, 201)
    left.plot(ell, effort["base_distance"] / ell, color=MUTED, lw=1.5)
    rows = effort["constant_factors"]
    left.scatter([row["efficiency"] for row in rows], [row["path_length"] for row in rows],
                 color=ACCENT, s=42, zorder=3)
    left.set_xlabel("Assigned efficiency  $\\ell$", fontsize=10)
    left.set_ylabel("Length with $f=1/\\ell^2$", fontsize=10)
    left.set_title("Constant effort multiplier", fontsize=11)
    fields = effort["variable_fields"]
    values = [row["path_length"] for row in fields]
    bars = right.bar([f"$\\alpha={row['alpha']:g}$" for row in fields], values,
                     color=[COOL, WARM], width=.5)
    for bar, value in zip(bars, values):
        right.text(bar.get_x() + bar.get_width()/2, value + .06, f"{value:.3f}", ha="center")
    right.set_ylim(0, max(values) * 1.2)
    right.set_ylabel("Length of the fixed Fisher arc", fontsize=10)
    right.set_title("Variable field  $f=1+\\alpha p_1$", fontsize=11)
    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
    _finish(fig, path)


def plot_entropy(results, path):
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 4.1), layout="constrained")
    entropy = results["entropy"]
    curve = entropy["utility_vs_entropy"]
    left.plot([row["floor"] for row in curve], [row["utility"] for row in curve],
              color=ACCENT, lw=2)
    left.scatter([entropy["floor_nats"]], [entropy["floor_utility"]],
                 color=COOL, s=42, zorder=3)
    left.annotate("$H\\geq\\ln 2$", (entropy["floor_nats"], entropy["floor_utility"]),
                  xytext=(.76, .9), fontsize=10)
    left.set_xlabel("Required outcome entropy  (nats)", fontsize=10)
    left.set_ylabel("Maximum assigned expected utility", fontsize=10)
    left.set_title("Weights $(0,\\,0.5,\\,1)$", fontsize=11)
    x, width = np.arange(3), .25
    for shift, key, label, color in [
        (-1, "vertex", "vertex", WARM), (0, "floor_distribution", "floor optimum", COOL),
        (1, "uniform", "uniform", MUTED),
    ]:
        right.bar(x + shift*width, entropy[key], width, label=label, color=color)
    right.set_xticks(x, ["failing", "coping", "flourishing"])
    right.set_ylabel("Probability", fontsize=10)
    right.set_title("Distributions, not permissions", fontsize=11)
    right.set_ylim(0, 1.2)
    right.legend(fontsize=9, frameon=False, loc="upper left")
    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
    _finish(fig, path)
