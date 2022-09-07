import unittest

from emma.points import *


class PointTest(unittest.TestCase):
    def test_correct_creation(self):
        p = Point(x = 1, y = 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_axes_name_validation(self):
        with self.assertRaises(ValueError, msg='Given invalid axis name should raise ValueError.'):
            Point(**{' ': 23})

    def test_axes_values_validation(self):
        with self.assertRaises(ValueError, msg='Given invalid axis value should raise ValueError.'):
            Point(**{'x': 'x'})
