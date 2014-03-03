import pygsty.euclid
import pyglet.graphics


default_batch = pyglet.graphics.Batch()

def render_models():
    default_batch.draw()

class BaseModel():
    def __init__(self, position=(0,0)):
        self.moveTo(position[0], position[1])
        self.rotation = 0

    @property
    def position(self):
        return self._position

    @property
    def x(self):
        return self._position.x

    @property
    def y(self):
        return self._position.y

    def moveTo(self, x, y):
        self._position = pygsty.euclid.Point2(x, y)
    

class VisibleModelGroup(pyglet.graphics.Group):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def set_state(self):
        pyglet.gl.glPushMatrix()
        pyglet.gl.glTranslatef(self.model.screen_x, self.model.screen_y, 0)
        pyglet.gl.glRotatef(self.model.rotation, 0, 0, 1)
       
    def unset_state(self):
        pyglet.gl.glPopMatrix()

class VisibleModel(BaseModel):
    def __init__(self, position=(0, 0)):
        super().__init__(position = position)
        self._render_group = VisibleModelGroup(self)
        self._batch = default_batch

    @property
    def render_group(self):
        return self._render_group

    @property
    def batch(self):
        return self._batch

    @property
    def screen_x(self):
        return self.x

    @property
    def screen_y(self):
        return self.y
