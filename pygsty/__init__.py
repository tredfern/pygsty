import pyglet
from math import pi
from pyglet.gl import *
from pyglet.window import key
import pygsty
import pygsty.rack
import pygsty.controllers
import pygsty.models
import pygsty.camera
import pygsty.utils

from pygsty.utils import logger

pygsty_globals = {
    'rack' : None,
    'default_font' : 'Tahoma'
    }

def start(width=800, height=600, fullscreen=False):
  pygsty_globals['rack'] = pygsty.rack.Rack(width, height, fullscreen)

def engine():
  return pygsty_globals['rack'];

def window_resolution():
    return (engine().width, engine().height)

def stop():
    engine().close()


def run():
  pyglet.clock.schedule_interval(pygsty_globals['rack'].update, 1/60.)
  pyglet.app.run()
