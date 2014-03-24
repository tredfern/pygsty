import unittest
import pygsty.models
import pyglet
from mock import MagicMock
from pygsty.models import *

class MockSprite():
    def __init__(self, image, x, y, batch, group):
        self.group = group
        self.x = x
        self.y = y

pyglet.sprite.Sprite = MockSprite
set_repository_size(100, 100)

class TestBaseModel(unittest.TestCase):
    def test_models_start_at_position_zero_zero(self):
        m = BaseModel()
        self.assertEqual( m.position, pygsty.euclid.Point2(0, 0) )
        self.assertEqual( m.x, 0 )
        self.assertEqual( m.y, 0 )

    def test_you_can_move_the_model(self):
        m = BaseModel()
        m.moveTo(40, 50)
        self.assertEqual( m.position.x, 40 )
        self.assertEqual( m.position.y, 50 )
        self.assertEqual( m.x, 40 )
        self.assertEqual( m.y, 50 )

    def test_you_can_instantiate_at_another_position(self):
        m = BaseModel(position=(10, 32))
        self.assertEqual( m.position, (10, 32) )

    def test_models_are_added_to_the_global_repository(self):
        m = BaseModel()
        self.assertTrue(m in pygsty.models.model_repository)

    def test_killing_models_removes_them_from_the_list(self):
        m = BaseModel()
        self.assertTrue(m in pygsty.models.model_repository)
        m.kill()
        self.assertTrue(m not in pygsty.models.model_repository)

    def test_you_can_set_the_image_and_the_layer_you_are_on(self):
        m = BaseModel()
        image = pyglet.image.AbstractImage(32, 32)
        m.initSprite(image, pygsty.models.background())
        self.assertEqual(m.sprite.group, pygsty.graphics.background_group)

    def test_it_removes_the_sprite_if_the_model_is_killed(self):
        m = BaseModel()
        m.initSprite("some image", pygsty.models.background())
        m.sprite.delete = MagicMock()
        m.kill()
        self.assertTrue(m.sprite.delete.called, "Sprite not cleaned up")

    def test_it_can_translate_screen_coordinates_based_on_multiplier(self):
        m = BaseModel()
        m.screen_offset_x = 10
        m.screen_offset_y = 20
        m.initSprite("some image", pygsty.models.background())

        m.moveTo(32, 12)

        self.assertEqual(320, m.screen_x)
        self.assertEqual(240, m.screen_y)
        self.assertEqual(320, m._sprite.x)
        self.assertEqual(240, m._sprite.y)

class TestModelRepository(unittest.TestCase):
    def test_it_can_track_a_model(self):
        m = BaseModel()
        repo = ModelRepository()
        repo.set_position_set_size(10, 10)
        repo.add(m)
        self.assertTrue(m in repo)
        repo.remove(m)
        self.assertTrue(m not in repo)

    def test_it_can_be_setup_with_a_specific_size(self):
        set_repository_size(2000, 3000)
        self.assertEqual(2000, model_repository.position_set_width)
        self.assertEqual(3000, model_repository.position_set_height)

    def test_it_tracks_the_position_of_elements(self):
        m1 = BaseModel(position=(10, 20))
        m2 = BaseModel(position=(10, 20))
        m3 = BaseModel(position=(25, 30))
        list1 = model_repository.find_by_position((10, 20))
        self.assertEqual([m1, m2], list1)
        list2 = model_repository.find_by_position((25, 30))
        self.assertEqual([m3], list2)
        empty = model_repository.find_by_position((8, 10))
        self.assertEqual([], empty)

    def test_it_can_the_closest_model_to_a_position(self):
        m = BaseModel(position=(10, 10))
        m2 = BaseModel(position=(50, 51))

        nearest = model_repository.find_nearest((20, 12), 20)
        self.assertEqual([m], nearest)

        nearest = model_repository.find_nearest(pygsty.euclid.Point2(20, 12), 20)
        self.assertEqual([m], nearest)

    def test_it_finds_the_following_location(self):
        model_repository.clear()
        m = BaseModel(position=(12,12))
        n = model_repository.find_nearest((10, 10), 10)

        self.assertEqual([m], n)

    def test_it_can_use_a_match_function_to_choose_object(self):
        m = BaseModel(position=(12,12))
        m2 = BaseModel(position=(12,12))

        def match_function(test_object):
            pygsty.logger.debug("calling match function")
            return test_object == m

        n = model_repository.find_nearest((10, 10), 10, match_function)
        self.assertEqual([m], n)
