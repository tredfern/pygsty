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

    def test_it_adds_all_the_primitives_to_a_batch(self):
        v = (20, 30), (40, 10)
        p = pygsty.graphics.Primitive(v, (255, 255, 255, 255), pyglet.gl.GL_POINTS)
        self.shape.add_primitive(p)

        p2 = pygsty.graphics.Primitive(v, (255, 255, 255, 255), pyglet.gl.GL_POINTS)
        self.shape.add_primitive(p2)

        batch = pyglet.graphics.Batch()
        self.shape.add_to_batch(batch)


class TestRectangle(unittest.TestCase):
    def test_it_is_set_up_by_two_points(self):
        r = pygsty.graphics.Rectangle((20, 30), (50, 50))
        self.assertEqual(r.right, 50)
        self.assertEqual(r.bottom, 50)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 20)

    def test_it_can_generate_a_primitive_from_its_location(self):
        r = pygsty.graphics.Rectangle((1, 1), (2, 2))
        p = r.to_primitive((255, 255, 255, 255))
        self.assertEqual(p.vertices, ((1, 1), (1, 2), (2, 2), (2, 1)) )

    def test_two_rectangles_in_the_same_spot_and_size_are_equal(self):
        r1 = pygsty.graphics.Rectangle((1, 1), (2, 2))
        r2 = pygsty.graphics.Rectangle((1, 1), (2, 2))
        self.assertEqual(r1, r2)

    def test_two_rectangles_in_different_spots_are_not_equal(self):
        r1 = pygsty.graphics.Rectangle((1, 1), (2, 2))
        r2 = pygsty.graphics.Rectangle((2, 2), (1, 1))
        self.assertNotEqual(r1, r2)
