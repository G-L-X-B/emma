import unittest

from emma.points import *


class PointCreationTests(unittest.TestCase):
    def test_correct_creation(self):
        p = Point(x = 1, y = 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_axes_name_validation(self):
        with self.assertRaises(ValueError, msg='Given invalid axis name should raise ValueError.'):
            Point(**{' ': 23})
        with self.assertRaises(ValueError, msg='Trying to name axis as with a reserved name should result in ValueError raise.'):
            Point(dimensions = 4)

    def test_axes_values_validation(self):
        with self.assertRaises(ValueError, msg='Given invalid axis value should raise ValueError.'):
            Point(x = 'x')

    def test_copy_creation(self):
        p1 = Point(x = 1)
        p2 = Point(p1)
        p2.x = 4
        self.assertNotEqual(p1.x, p2.x, msg='Copy creation should create an independent copy.')

    def test_creation_with_overwrite(self):
        p1 = Point(x = 1, y = 1)
        p2 = Point(p1, y = 2)
        self.assertEqual(p2.y, 2)


class PointAttributesAccessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.point = Point(x = 1, y = 2)
        return super().setUp()

    def test_axes_reassignment(self):
        self.point.x = 3
        self.assertEqual(self.point.x, 3)

    def test_reserved_attributes_access(self):
        self.assertEqual(self.point.dimensions, 2)
        self.assertEqual(self.point.axes, ['x', 'y'])

    def test_reserved_attributes_assignment(self):
        with self.assertRaises(AttributeError, msg='When trying to assign to reserved attributes should raise AttributeError.'):
            self.point.dimensions = 3
        with self.assertRaises(AttributeError, msg='When trying to assign to reserved attributes should raise AttributeError.'):
            self.point.axes = ['x', 'y', 'z']


class PointIsSameSpaceTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(x = 1, y = 2, z = 3)

    def test_with_same(self):
        same = Point(self.point)
        self.assertTrue(same.is_same_space(self.point))

    def test_with_different(self):
        diff = Point(self.point, t = 3)
        self.assertFalse(diff.is_same_space(self.point))
