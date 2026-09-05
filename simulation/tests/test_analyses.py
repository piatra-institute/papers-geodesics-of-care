"""Regression checks for the illustration, not empirical tests of care."""
import json
import unittest

import numpy as np
import analyses as a


class GeometryTests(unittest.TestCase):
    def test_probability_validation(self):
        for bad in ([0, 0, 0], [-1, 2, 0], [np.nan, 1], [np.inf, 1], [[1, 2]], [1]):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                a._norm(bad)
        np.testing.assert_allclose(a._norm([2, 3, 5]), [.2, .3, .5])
        with self.assertRaises(ValueError):
            a.fr_distance([1, 0], [1, 0, 0])

    def test_distance_boundary_identity_and_symmetry(self):
        self.assertEqual(a.fr_distance([.2, .3, .5], [.2, .3, .5]), 0)
        self.assertAlmostEqual(a.fr_distance([1, 0, 0], [0, 0, 1]), np.pi)
        p, q = [.7, .2, .1], [.1, .2, .7]
        self.assertAlmostEqual(a.fr_distance(p, q), a.fr_distance(q, p))
        self.assertAlmostEqual(a.fr_distance(p, q), 2*np.arccos(np.sqrt(p) @ np.sqrt(q)))

    def test_geodesic_endpoints_and_speed(self):
        p, q = [.7, .2, .1], [.1, .2, .7]
        np.testing.assert_array_equal(a.fr_geodesic(p, q, 0), a._norm(p))
        np.testing.assert_array_equal(a.fr_geodesic(p, q, 1), a._norm(q))
        for t in np.linspace(0, 1, 11):
            state = a.fr_geodesic(p, q, t)
            self.assertAlmostEqual(a.fr_distance(p, state), t*a.fr_distance(p, q), places=12)
            self.assertTrue((state >= 0).all())
            self.assertAlmostEqual(float(state.sum()), 1)
        for t in (-.1, 1.1, np.nan):
            with self.assertRaises(ValueError):
                a.fr_geodesic(p, q, t)

    def test_triangle_inequality_and_finite_difference_errors(self):
        result = a.study_manifold()
        self.assertTrue(result["triangle_inequality_holds"])
        self.assertEqual(result["triples_checked"], 125)
        errors = [row["max_abs_error"] for row in result["curvature_step_sensitivity"]]
        self.assertLess(errors[-1], 1e-5)
        self.assertGreater(errors[-1], 1e-9)  # not "machine precision"
        self.assertGreater(errors[0], errors[1])
        self.assertGreater(errors[1], errors[2])
        self.assertLess(result["geodesic_length"], result["straight_coordinate_path_length"])

    def test_constant_scaling_of_curvature(self):
        for multiplier in (1., 4., 9.):
            metric = lambda x, y: tuple(multiplier*v for v in a.fisher_EFG(x, y))
            self.assertAlmostEqual(a.gaussian_curvature(metric, .3, .25), .25/multiplier, delta=1e-6)

    def test_conformal_curvature_independent_formula(self):
        self.assertAlmostEqual(a.conformal_curvature_exact(.3, alpha=0), .25)
        result = a.study_effort()
        self.assertLess(result["curvature_max_abs_error"], 1e-5)
        self.assertGreater(result["curvature_max"] - result["curvature_min"], .1)

    def test_independent_area_and_flat_detour(self):
        result = a.study_routing()
        self.assertGreater(result["triangle_area"], 0)
        self.assertLess(result["gauss_bonnet_abs_residual"], 1e-12)
        self.assertGreater(result["routing_gap"], 0)
        self.assertGreater(result["flat_counterexample"]["gap"], 0)
        self.assertAlmostEqual(a.spherical_triangle_area([1, 0, 0], [0, 1, 0], [0, 0, 1]), 2*np.pi)

    def test_effort_multiplier_and_fixed_metric_symmetry(self):
        p, q = [.7, .22, .08], [.08, .22, .7]
        self.assertAlmostEqual(a._weighted_path_length(p, q, lambda _: 4., n=20),
                               2*a.fr_distance(p, q))
        f = lambda x: 1 + 3*x[0]
        self.assertAlmostEqual(a._weighted_path_length(p, q, f, n=100),
                               a._weighted_path_length(q, p, f, n=100), places=12)
        for f in (lambda _: 0., lambda _: -1., lambda _: np.inf):
            with self.assertRaises(ValueError):
                a._weighted_path_length(p, q, f, n=3)
        with self.assertRaises(ValueError):
            a._weighted_path_length(p, q, lambda _: 1., n=0)


class EntropyTests(unittest.TestCase):
    def test_endpoints_and_tied_maxima(self):
        np.testing.assert_array_equal(a.entropy_constrained_optimum([0, .5, 1], 0), [0, 0, 1])
        np.testing.assert_allclose(a.entropy_constrained_optimum([0, .5, 1], np.log(3)), [1/3]*3)
        np.testing.assert_array_equal(a.entropy_constrained_optimum([0, 1, 1], np.log(2)), [0, .5, .5])
        self.assertEqual(a.shannon_entropy([0, 0, 1]), 0)

    def test_interior_solution_and_weight_sensitivity(self):
        result = a.study_entropy()
        self.assertAlmostEqual(result["floor_entropy"], np.log(2), places=12)
        np.testing.assert_allclose(result["floor_distribution"],
                                   [.0527605806, .1987259545, .7485134649], atol=1e-10)
        self.assertAlmostEqual(result["utility_cost_of_floor"], .1521235579, places=9)
        self.assertEqual(result["alternative_score"]["cost_of_floor"], 0)

    def test_feasible_monotone_curve(self):
        curve = a.study_entropy()["utility_vs_entropy"]
        for row in curve:
            self.assertGreaterEqual(row["entropy"] + 1e-12, row["floor"])
        self.assertTrue(all(b["utility"] <= first["utility"] + 1e-12
                            for first, b in zip(curve, curve[1:])))

    def test_positive_affine_invariance_and_gibbs_stability(self):
        base = a.entropy_constrained_optimum([0, .5, 1], np.log(2))
        np.testing.assert_allclose(a.entropy_constrained_optimum([3, 8, 13], np.log(2)), base, atol=1e-12)
        np.testing.assert_array_equal(a._gibbs(np.array([0., .5, 1.]), 1e-12), [0, 0, 1])

    def test_invalid_optimization_inputs(self):
        for weights in ([1], [1, np.nan], [[0, 1]]):
            with self.assertRaises(ValueError):
                a.entropy_constrained_optimum(weights, 0)
        for floor in (-.1, np.log(3)+.001, np.nan):
            with self.assertRaises(ValueError):
                a.entropy_constrained_optimum([0, .5, 1], floor)


class PermissionTests(unittest.TestCase):
    def test_refusal_revocation_and_stale_target(self):
        p, q = [.7, .22, .08], [0, 0, 1]
        for permission in (a.Permission(), a.Permission(tuple(q), revoked=True),
                           a.Permission((0, 1, 0))):
            result = a.permitted_step(p, q, 1, permission)
            self.assertFalse(result["applied"])
            np.testing.assert_allclose(result["state"], p)

    def test_approved_step_is_capped(self):
        p, q = [.7, .22, .08], [0, 0, 1]
        result = a.permitted_step(p, q, 1, a.Permission(tuple(q), max_fraction=.2))
        self.assertTrue(result["applied"])
        self.assertEqual(result["fraction"], .2)
        self.assertAlmostEqual(a.fr_distance(p, result["state"]), .2*a.fr_distance(p, q))

    def test_permission_is_independent_of_entropy_and_score(self):
        result = a.study_permission()
        self.assertTrue(result["chosen_predictable_outcome"]["applied"])
        self.assertEqual(result["chosen_predictable_outcome"]["entropy"], 0)
        self.assertTrue(result["unapproved_high_entropy_proposal"]["entropy_floor_met"])
        self.assertFalse(result["unapproved_high_entropy_proposal"]["applied"])
        self.assertEqual(result["actions_after_revocation"], 0)
        self.assertFalse(result["changed_goal"]["stale_proposal"]["applied"])
        self.assertTrue(result["changed_goal"]["accepted_proposal"]["applied"])
        self.assertLess(result["changed_goal"]["assigned_utility"], 1)

    def test_permission_validation(self):
        for kwargs in ({"revoked": "false"}, {"max_fraction": -.1}, {"approved_target": (0, 0)}):
            with self.assertRaises(ValueError):
                a.Permission(**kwargs)
        with self.assertRaises(ValueError):
            a.permitted_step([.5, .5], [1, 0], .1, None)

    def test_all_results_serialize_without_nonfinite_values(self):
        parsed = json.loads(json.dumps(a.run(), allow_nan=False))
        self.assertEqual(set(parsed), {"manifold", "routing", "effort", "entropy", "permission"})


if __name__ == "__main__":
    unittest.main()
