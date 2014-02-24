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

    def test_it_has_the_length_of_the_vertices(self):
        self.assertEqual( self.primitive.vertices_length, 3 )

    def test_it_can_flatten_the_verticies_into_a_single_tuple(self):
        self.assertEqual( self.primitive.flatten_vertices(), [20, 30, 30, 20, 40, 30] )

    def test_it_can_append_the_primitive_to_a_batch(self):
        batch = pyglet.graphics.Batch()
        vertex_list = self.primitive.add_to_batch(batch)
        self.assertIsInstance( vertex_list, pyglet.graphics.vertexdomain.VertexList )

class TestShape(unittest.TestCase):
    def setUp(self):
        self.shape = pygsty.graphics.Shape()

    def test_it_initializes_with_no_primitives(self):
        self.assertEqual( self.shape.primitives, [] )

    def test_can_add_primitives_to_shape(self):
        v = (20, 30), (40, 10), (30, 10)
        p = pygsty.graphics.Primitive(v, (255, 255, 255, 255), pyglet.gl.GL_POINTS)
        self.shape.add_primitive(p)
        self.assertEqual( self.shape.primitives, [ p ] )

