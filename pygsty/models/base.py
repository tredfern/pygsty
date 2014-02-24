import pygsty.euclid
import pyglet.graphics


default_batch = pyglet.graphics.Batch()

def render_models():
    default_batch.draw()

class BaseModel():
    def __init__(self):
        self.moveTo(0, 0)
        self._rotation = 0

    @property
    def rotation(self):
        return self._rotation

    @property
    def position(self):
        return self._position

    def moveTo(self, x, y):
        self._position = pygsty.euclid.Point2(x, y)
    

class VisibleModelGroup(pyglet.graphics.Group):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def set_state(self):
        pyglet.gl.glPushMatrix()
        pyglet.gl.glTranslatef(self.model.position.x, self.model.position.y, 0)
        pyglet.gl.glRotatef(self.model.rotation, 0, 0, 1)
       
    def unset_state(self):
        pyglet.gl.glPopMatrix()

class VisibleModel(BaseModel):
    def __init__(self):
        super().__init__()
        self._render_group = VisibleModelGroup(self)
        self._batch = default_batch

    @property
    def render_group(self):
        return self._render_group

    @property
    def batch(self):
        return self._batch
