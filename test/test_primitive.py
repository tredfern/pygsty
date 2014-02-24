import unittest
import pygsty.graphics
import pyglet.gl

class TestPrimitive(unittest.TestCase):
    def setUp(self):
        self.verts = (20, 30), (30, 20), (40, 30)
        self.color = (255, 128, 128, 128)
        self.primitive = pygsty.graphics.Primitive(self.verts, self.color, pyglet.gl.GL_POINTS)

    def test_it_has_a_list_of_verts(self):
        self.assertEqual( self.primitive.vertices, self.verts )

    def test_it_tracks_the_color(self):
        self.assertEqual( self.primitive.color, self.color)

    def test_it_tracks_the_primitive_type(self):
        self.assertEqual( self.primitive.primitive_type, pyglet.gl.GL_POINTS)


