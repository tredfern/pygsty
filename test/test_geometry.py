import unittest
import pygsty.geometry

class TestRect(unittest.TestCase):
    def test_it_maps_x_y_height_width_properly(self):
        r = pygsty.geometry.Rect(1,1, 20, 20)
        self.assertEqual(r.top , 21)
        self.assertEqual(r.left , 1)
        self.assertEqual(r.width , 20)
        self.assertEqual(r.height , 20)
        self.assertEqual(r.bottom , 1)
        self.assertEqual(r.right , 21)
