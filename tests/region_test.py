import unittest
from region import Region


class TestYourClass(unittest.TestCase):
    def test_zero_region_min_max(self):
        region = Region(0, 10)
        self.assertEqual(0, region.min_y())
        self.assertEqual(0, region.min_x())
        self.assertEqual(9, region.max_x())
        self.assertEqual(9, region.max_y())

    def test_non_zero_region_min_max(self):
        region = Region(1, 10)
        self.assertEqual(0, region.min_y())
        self.assertEqual(10, region.min_x())
        self.assertEqual(19, region.max_x())
        self.assertEqual(9, region.max_y())

    def test_in_x_bounds_zero_index(self):
        region = Region(0, 10)
        self.assertTrue(region.in_x_bounds(0))
        self.assertTrue(region.in_x_bounds(1))
        self.assertTrue(region.in_x_bounds(9))
        self.assertFalse(region.in_x_bounds(-1))
        self.assertFalse(region.in_x_bounds(10))

    def test_in_x_bounds_one_index(self):
        region = Region(1, 10)
        self.assertFalse(region.in_x_bounds(0))
        self.assertFalse(region.in_x_bounds(1))
        self.assertFalse(region.in_x_bounds(9))
        self.assertFalse(region.in_x_bounds(-1))
        self.assertTrue(region.in_x_bounds(10))
        self.assertTrue(region.in_x_bounds(19))
        self.assertFalse(region.in_x_bounds(20))

    def test_in_y_bounds_zero_index(self):
        region = Region(0, 10)
        self.assertTrue(region.in_y_bounds(0))
        self.assertTrue(region.in_y_bounds(1))
        self.assertTrue(region.in_y_bounds(9))
        self.assertFalse(region.in_y_bounds(-1))
        self.assertFalse(region.in_y_bounds(10))

    def test_in_y_bounds_one_index(self):
        region = Region(1, 10)
        self.assertTrue(region.in_y_bounds(0))
        self.assertTrue(region.in_y_bounds(1))
        self.assertTrue(region.in_y_bounds(9))
        self.assertFalse(region.in_y_bounds(-1))
        self.assertFalse(region.in_y_bounds(10))