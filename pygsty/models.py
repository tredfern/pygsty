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

def background():
    return pygsty.graphics.background_group

def middle():
    return pygsty.graphics.middleground_group

def foreground():
    return pygsty.graphics.foreground_group

class BaseModel():
    def __init__(self, position=(0,0)):
        self.moveTo(position[0], position[1])
        track_model(self)
        self._batch = model_batch
        self._sprite = None

    def kill(self):
        remove_model(self)
        if self.sprite:
            self.sprite.delete()

    def initSprite(self, image, group):
        self._sprite = pyglet.sprite.Sprite(
            image,
            x = self.x,
            y = self.y,
            batch = self.batch,
            group = group
        )

    @property
    def sprite(self):
        return self._sprite

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
