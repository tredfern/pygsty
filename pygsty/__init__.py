import pyglet
from math import pi
from pyglet.gl import *
from pyglet.window import key
import pygsty
import pygsty.rack
import pygsty.controllers
import pygsty.camera
import pygsty.utils

pygsty_globals = { 
    'rack' : None,
    'default_font' : 'Tahoma'
    } 

def start():
  pygsty_globals['rack'] = pygsty.rack.Rack()

def engine():
  return pygsty_globals['rack'];
  
def run():
  pyglet.clock.schedule_interval(pygsty_globals['rack'].update, 1/60.)
  pyglet.app.run()
