
class Primitive():
    # Stores a list of vertices and color information 
    # This allows us to convert it into OpenGL batch information easily
    def __init__(self, verts, color, primitive_type):
        self.vertices = verts
        self.color = color
        self.primitive_type = primitive_type
