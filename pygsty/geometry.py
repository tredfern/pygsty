from pygsty.euclid import *

def rect_from_coordinates(left, top, right, bottom):
  return Rect(left, top , right-left, bottom-top)

class Rect():
    def __init__(self, x, y, width, height):
        if width < 0:
            self.x = x - abs(width)
            self.width = abs(width)
        else:
            self.x = x
            self.width = width

        if height < 0:
            self.y = y - abs(height)
            self.height = abs(height)
        else:
            self.y = y
            self.height = height

    @property
    def left(self):
        return self.x

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def right(self):
        return self.x + self.width

    @property
    def center(self):
        return Point2(self.x + self.width/2, self.y + self.height/2)

    @property
    def top(self):
        return self.y 

    def intersects(self, other):
        return not (self.x > other.right or
            self.right < other.left or
            self.y > other.top or
            self.top < other.y)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Rect( L:{}, T:{}, R:{}, B:{} )".format(self.left, self.top, self.right, self.bottom)
