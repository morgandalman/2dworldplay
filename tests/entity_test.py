import unittest
from entity import Entity


class TestEntityClass(unittest.TestCase):
    def test_initialize(self):
        entity = Entity(15, 7, 99, (3, 330, 4))
        self.assertEqual(15, entity.x)
        self.assertEqual(7, entity.y)
        self.assertEqual(99, entity.identifier)
        self.assertEqual((3, 330, 4), entity.color)

    def test_serialize(self):
        entity = Entity(15, 7, 99, (3, 330, 4))
        self.assertEqual(
            '{"x": 15, "y": 7, "id": 99, "red": 3, "green": 330, "blue": 4}',
            entity.serialize())

    def test_deserialize(self):
        entity = Entity.deserialize('{"x": 15, "y": 7, "id": 99, "red": 3, "green": 330, "blue": 4}')
        self.assertEqual(15, entity.x)
        self.assertEqual(7, entity.y)
        self.assertEqual(99, entity.identifier)
        self.assertEqual((3, 330, 4), entity.color)