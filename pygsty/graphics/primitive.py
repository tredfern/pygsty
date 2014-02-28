import pyglet.gl
import pygsty.utils

def rect_to_primitive(rect, color):
    verts = (rect.left, rect.bottom), (rect.right, rect.bottom),  \
                (rect.left, rect.top), (rect.right, rect.top)
    return IndexedPrimitive(verts, [0,1,2,1,2,3], color, pyglet.gl.GL_TRIANGLES)

class Primitive():
    # Stores a list of vertices and color information 
    # This allows us to convert it into OpenGL batch information easily
    def __init__(self, verts, color, primitive_type):
        self._vertices = verts
        self._color = color
        self._primitive_type = primitive_type

    @property
    def vertices_length(self):
        return len(self.vertices)

    @property
    def vertices(self):
        return self._vertices

    @property
    def color(self):
        return self._color

    @property
    def primitive_type(self):
        return self._primitive_type

    def flatten_vertices(self):
        return pygsty.utils.flatten(self.vertices)

    def add_to_batch(self, batch, group=None):
        return batch.add(
                self.vertices_length,
                self.primitive_type,
                group,
                ('v2f', self.flatten_vertices()),
                ('c4B', self.color * self.vertices_length) )

class IndexedPrimitive(Primitive):
    def __init__(self, verts, indices, color, primitive_type):
        super().__init__(verts, color, primitive_type)
        self.indices = indices

    def add_to_batch(self, batch, group=None):
        return batch.add_indexed(
                self.vertices_length,
                self.primitive_type,
                group,
                self.indices,
                ('v2f', self.flatten_vertices()),
                ('c4B', self.color * self.vertices_length) )
