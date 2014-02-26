import pyglet
from pyglet.window import key
import pygsty.camera
from math import pi

class BaseController():
    def prepare_draw(self):
        pass
   
    def draw(self):
        pass

    def draw_hud(self):
        pass

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifier):
        return False

class PerformanceController(BaseController):
  def __init__(self):
    self.fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load("Arial", 24))

  def draw_hud(self):
    self.fps_display.draw()
    
class CameraController(BaseController):
    def __init__(self, position, scale, angle=None):
        self.camera = pygsty.camera.Camera(position, scale, angle)
        
    def update(self, dt):
        self.camera.update()

    def prepare_draw(self):
        self.camera.focus(pygsty.window_resolution()[0], pygsty.window_resolution()[1])

    def draw_hud(self):
        self.camera.hud_mode(pygsty.window_resolution()[0], pygsty.window_resolution()[1])

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.camera.pan(self.camera.scale, -pi/2)
        elif symbol == key.RIGHT:
            self.camera.pan(self.camera.scale, pi/2)
        elif symbol == key.DOWN:
            self.camera.pan(self.camera.scale, pi)
        elif symbol == key.UP:
            self.camera.pan(self.camera.scale, 0)
        elif symbol == key.PAGEUP:
            self.camera.zoom(2)
        elif symbol == key.PAGEDOWN:
            self.camera.zoom(0.5)
        else:
            return False

        return True


