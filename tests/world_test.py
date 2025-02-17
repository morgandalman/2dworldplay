import unittest
from world import World


class TestWorldClass(unittest.TestCase):
    def test_one_region_min_max(self):
        world = World(size=10, region_count=1)
        self.assertEqual(0, world.min_y())
        self.assertEqual(0, world.min_x())
        self.assertEqual(9, world.max_x())
        self.assertEqual(9, world.max_y())

    def test_two_region_min_max(self):
        world = World(size=10, region_count=2)
        self.assertEqual(0, world.min_y())
        self.assertEqual(0, world.min_x())
        self.assertEqual(19, world.max_x())
        self.assertEqual(9, world.max_y())

    def test_region_for(self):
        self.assertEqual(0, World(size=10, region_count=1).region_for(5, 7))
        self.assertEqual(0, World(size=10, region_count=1).region_for(0, 7))
        self.assertEqual(0, World(size=10, region_count=1).region_for(9, 7))
        self.assertEqual(1, World(size=10, region_count=2).region_for(19, 7))