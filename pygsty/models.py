import pygsty.euclid
import pygsty.graphics
import pyglet.graphics

model_batch = pygsty.graphics.batches.create_batch()
model_list = set()

def render_models():
    model_batch.draw()

def track_model(m):
    model_list.add(m)

def remove_model(m):
    model_list.remove(m)

class BaseModel():
    def __init__(self, position=(0,0)):
        self.moveTo(position[0], position[1])
        track_model(self)
        self._batch = model_batch

    def kill(self):
        remove_model(self)

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

    @property
    def batch(self):
        return model_batch
