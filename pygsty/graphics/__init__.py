import pygsty.graphics.primitive
import pygsty.graphics.batches

from pygsty.graphics.primitive import *

#
# Setup ordered groups to divide up the layers
#
background_group = pyglet.graphics.OrderedGroup(0)
middleground_group = pyglet.graphics.OrderedGroup(5)
foreground_group = pyglet.graphics.OrderedGroup(10)
