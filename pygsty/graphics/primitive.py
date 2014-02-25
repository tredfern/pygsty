
import pyglet.gl
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

class Rectangle():
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    @property
    def left(self):
        return self.top_left[0]

    @property
    def top(self):
        return self.top_left[1]

    @property
    def right(self):
        return self.bottom_right[0]

    @property
    def bottom(self):
        return self.bottom_right[1]
    
    @property
    def width(self):
        return self.right - self.left
        
    @property
    def height(self):
        return self.bottom - self.top

    def to_primitive(self, color):
        verts = (self.left, self.top), (self.left, self.bottom),  \
                    (self.right, self.bottom), (self.right, self.top)
        return Primitive(verts, color, pyglet.gl.GL_TRIANGLE_STRIP)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

        def __ne__(self, other):
            return not self.__eq__(other)


class Shape():
    def __init__(self):
        self.primitives = []

    def add_primitive(self, p):
        self.primitives.append( p )

    def add_to_batch(self, batch, group=None):
        for p in self.primitives:
            p.add_to_batch(batch, group)
