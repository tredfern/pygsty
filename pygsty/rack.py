import pyglet
from math import pi
from pyglet.gl import *
from pyglet.window import key

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

class Rack(pyglet.window.Window):
  def __init__(self, width, height, fullscreen):
    super().__init__(width=width, height=height, fullscreen=fullscreen)
    self._controllers = []

  def push_controller(self, c):
    self._controllers.append(c)

  def pop_controller(self):
    return self._controllers.pop()

  def update(self, dt):
    for c in self._controllers:
      c.update(dt)


  def on_draw(self):
    self.clear()

    for c in self._controllers:
      c.prepare_draw()

    for c in self._controllers:
      c.draw()

    for c in self._controllers:
      c.draw_hud()

  def on_key_press(self, symbol, modifiers):
      for c in self._controllers:
          if c.on_key_press(symbol, modifiers):
              break
