import pygsty.euclid
import pygsty.graphics
import pyglet.graphics
from pygsty.utils import flatten

model_batch = pygsty.graphics.batches.create_batch()

def render_models():
    model_batch.draw()

def track_model(m):
    model_repository.add(m)

def remove_model(m):
    model_repository.remove(m)

def background():
    return pygsty.graphics.background_group

def middle():
    return pygsty.graphics.middleground_group

def foreground():
    return pygsty.graphics.foreground_group

def set_repository_size(width, height):
    model_repository.set_position_set_size(width, height)


class BaseModel():
    def __init__(self, position=(0,0)):
        self._sprite = None
        self.screen_offset_x = 1
        self.screen_offset_y = 1
        self._batch = model_batch

        self.moveTo(position[0], position[1])
        track_model(self)

    def kill(self):
        remove_model(self)
        if self.sprite:
            self.sprite.delete()

    def initSprite(self, image, group):
        self._sprite = pyglet.sprite.Sprite(
            image,
            x = self.screen_x,
            y = self.screen_y,
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

    @property
    def screen_x(self):
        return self._position.x * self.screen_offset_x

    @property
    def screen_y(self):
        return self._position.y * self.screen_offset_y

    def moveTo(self, x, y):
        self._position = pygsty.euclid.Point2(x, y)
        if self._sprite:
            self.sprite.x = self.screen_x
            self.sprite.y = self.screen_y

    def move_up(self):
        self.moveTo(self.x, self.y + 1)

    def move_down(self):
        self.moveTo(self.x, self.y - 1)

    def move_right(self):
        self.moveTo(self.x + 1, self.y)

    def move_left(self):
        self.moveTo(self.x - 1, self.y)

    @property
    def batch(self):
        return model_batch

class ModelRepository():
    def __init__(self):
        self._global_set = set()
        self.set_position_set_size(0, 0)

    def add(self, model):
        pygsty.logger.debug("Tracking model {}".format(model))

        self._global_set.add(model)
        self.update_model_position(model)

    def remove(self, model):
        self._global_set.remove(model)

    def get_neighbors(self, x, y):
        start_x = x-1
        start_y = y-1
        end_x = x + 2
        end_y = y +2
        neighbors = []
        for test_y in range(start_y, end_y):
            for test_x in range(start_x, end_x):
                if not test_x == x or not test_y == y:
                    n = self.find_by_position((test_x, test_y))
                    if n:
                        neighbors.append(n)

        return flatten(neighbors)

    def find_all(self, match_function):
        matches = []
        for test in self._global_set:
            if match_function(test):
                matches.append(test)
        return matches

    def find_nearest(self, location, search_radius, match_function=None):
        #Starting from location, search out until we find a match
        # By searching just the perimeter of the rectangle we are at
        start_x = location[0]
        start_y = location[1]
        end_x = start_x
        end_y = start_y
        search_level = 1
        found_object = None
        pygsty.logger.debug("Finding objects within {} of {}".format(search_radius, location))

        while(not found_object and search_level < search_radius):
            test_objects = []
            #Search top and bottom of rect
            for search_x in range(start_x, end_x + 1):
                test_objects += self.find_by_position((search_x, start_y))
                test_objects += self.find_by_position((search_x, end_y))

            for search_y in range(start_y, end_y + 1):
                test_objects += self.find_by_position((start_x, search_y))
                test_objects += self.find_by_position((end_x, search_y))

            test_objects = set(test_objects)
            matches = []
            if match_function:
                for t in test_objects:
                    if match_function(t):
                        matches.append(t)
            else:
                matches = test_objects

            search_level += 1
            start_x -= 1
            end_x += 1
            start_y -= 1
            end_y += 1

            if start_x < 0:
                start_x = 0
            if start_y < 0:
                start_y = 0
            if end_x > self.position_set_width:
                end_x = self.position_set_width
            if end_y > self.position_set_height:
                end_y = self.position_set_height

            if len(matches):
                found_object = list(matches)

        return found_object

    def find_by_position(self, location):
        pygsty.logger.debug("Getting objects at ({} , {})".format(location[0], location[1]))
        if location[1] < 0 or location[1] >= self.position_set_height:
            return []
        elif location[0] < 0 or location[0] >= self.position_set_width:
            return []
        else:
            return self.__position_set[location[1]][location[0]]

    def is_vacant(self, location):
        return not len(self.find_by_position(location))

    def __contains__(self, model):
        return model in self._global_set

    def update_model_position(self, model):
        if model.y > self.position_set_height or \
            model.y < 0 or \
            model.x > self.position_set_width or \
            model.x <0:
            raise Exception("Out of bounds: ({} {})".format(model.x, model.y))
        pygsty.logger.debug("Updating {} position to ({}, {})".format(model, model.x, model.y))
        self.__position_set[model.y][model.x].append(model)

    def set_position_set_size(self, width=0, height=0):
        self.__position_set = [
            [[] for x in range(width)] for y in range(height)
        ]

    def clear(self):
        self._global_set = set()
        self.set_position_set_size(self.position_set_width, self.position_set_height)

    @property
    def position_set_width(self):
        return len(self.__position_set[0])

    @property
    def position_set_height(self):
        return len(self.__position_set)

model_repository = ModelRepository()
