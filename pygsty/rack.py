import pyglet
from math import pi
from pyglet.gl import *
from pyglet.window import key
import pygsty.camera

class Rack(pyglet.window.Window):
  def __init__(self):
    super(Rack, self).__init__(800, 600)
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
