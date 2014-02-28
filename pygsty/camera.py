"""
Camera tracks a position, orientation and zoom level, and applies openGL
transforms so that subsequent renders are drawn at the correct place, size
and orientation on screen

Found this code from:
http://tartley.com/files/stretching_pyglets_wings/presentation/
"""
from __future__ import division
from math import sin, cos

from pyglet.gl import (
    glLoadIdentity, glMatrixMode, gluLookAt, gluOrtho2D, glDepthFunc,
    GL_MODELVIEW, GL_PROJECTION, GL_NEVER
)

import pygsty.geometry

glDepthFunc(GL_NEVER)

class Target(object):

    def __init__(self, camera):
        self.x, self.y = camera.x, camera.y
        self.scale = camera.scale
        self.angle = camera.angle


class Camera(object):

    def __init__(self, position=None, scale=None, angle=None):
        if position is None:
            position = (0, 0)
        self.x, self.y = position
        if scale is None:
            scale = 1
        self.scale = scale
        if angle is None:
            angle = 0
        self.angle = angle
        self.target = Target(self)
        self.bounding_rect = pygsty.geometry.Rect(0,0,0,0)
        self.aspect = 0;


    def zoom(self, factor):
        self.target.scale *= factor

    def pan(self, length, angle):
        self.target.x += length * sin(angle + self.angle)
        self.target.y += length * cos(angle + self.angle)

    def tilt(self, angle):
        self.target.angle += angle


    def update(self):
        self.x += (self.target.x - self.x) * 0.1
        self.y += (self.target.y - self.y) * 0.1
        self.scale += (self.target.scale - self.scale) * 0.1
        self.angle += (self.target.angle - self.angle) * 0.1
        self.bounding_rect = pygsty.geometry.rect_from_coordinates(self.x + (-self.scale * self.aspect),
                                  self.x + self.scale * self.aspect,
                                  self.y -self.scale,
                                  self.y + self.scale)


    def focus(self, width, height):
        "Set projection and modelview matrices ready for rendering"

        # Set projection matrix suitable for 2D rendering"
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = width / height
        self.aspect = aspect
        gluOrtho2D(
            -self.scale * aspect,
            +self.scale * aspect,
            -self.scale,
            +self.scale)

        # Set modelview matrix to move, scale & rotate to camera position"
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.x, self.y, +1.0,
            self.x, self.y, -1.0,
            sin(self.angle), cos(self.angle), 0.0)


    def hud_mode(self, width, height):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, width, 0, height)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def inspect(self):
      return "Camera: x={}, y={}, scale={}, aspect={}".format(self.x, self.y, self.scale, self.aspect)
