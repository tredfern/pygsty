import unittest
import pygsty.geometry

class TestRect(unittest.TestCase):
    def test_it_maps_x_y_height_width_properly(self):
        r = pygsty.geometry.Rect(1,1, 20, 20)
        self.assertEqual(r.top , 1)
        self.assertEqual(r.left , 1)
        self.assertEqual(r.width , 20)
        self.assertEqual(r.height , 20)
        self.assertEqual(r.bottom , 21)
        self.assertEqual(r.right , 21)

    def test_it_marks_two_triangles_in_the_same_spot_as_equal(self):
        r1 = pygsty.geometry.Rect(1,1, 5, 5)
        r2 = pygsty.geometry.Rect(1, 1, 5, 5)
        r3 = pygsty.geometry.Rect(400, 400, 3200, 3020)

        self.assertEqual(r1, r2)
        self.assertNotEqual(r1, r3)

    def test_it_shows_a_good_representation_of_itself(self):
        r = pygsty.geometry.Rect(1,3, 8, 10)
        self.assertEqual(repr(r), "Rect( L:1, T:3, R:9, B:13 )")

