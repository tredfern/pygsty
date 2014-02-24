
import pygsty.utils

class Primitive():
    # Stores a list of vertices and color information 
    # This allows us to convert it into OpenGL batch information easily
    def __init__(self, verts, color, primitive_type):
        self.vertices = verts
        self.color = color
        self.primitive_type = primitive_type

    @property
    def vertices_length(self):
        return len(self.vertices)

    def flatten_vertices(self):
        return pygsty.utils.flatten(self.vertices)

    def add_to_batch(self, batch, group=None):
        return batch.add(
                self.vertices_length,
                self.primitive_type,
                group,
                ('v2f', self.flatten_vertices()),
                ('c4B', self.color * self.vertices_length) )


class Shape():
    def __init__(self):
        self.primitives = []

    def add_primitive(self, p):
        self.primitives.append( p )
