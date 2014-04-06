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
    def setUp(self):
        model_repository.clear()

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

    def test_there_are_basic_move_controls_to_make_things_easier(self):
        m = BaseModel(position=(20, 20))
        m.move_up()
        self.assertEqual(21, m.y)
        m.move_down()
        self.assertEqual(20, m.y)
        m.move_right()
        self.assertEqual(21, m.x)
        m.move_left()
        self.assertEqual(20, m.x)

class TestModelRepository(unittest.TestCase):
    def setUp(self):
        model_repository.clear()

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

    def test_find_by_position_returns_empty_list_for_negative_values(self):
        self.assertEqual([], model_repository.find_by_position((-1, 2)))
        self.assertEqual([], model_repository.find_by_position((2, -1)))

    def test_find_by_position_returns_empty_list_for_out_of_range_values(self):
        self.assertEqual([], model_repository.find_by_position((20000, 2)))
        self.assertEqual([], model_repository.find_by_position((2, 20000)))
        self.assertEqual([], model_repository.find_by_position((model_repository.position_set_width, model_repository.position_set_height)))

    def test_it_can_the_closest_model_to_a_position(self):

        m = BaseModel(position=(10, 10))
        m2 = BaseModel(position=(50, 51))

        nearest = model_repository.find_nearest((20, 12), 20)
        self.assertEqual([m], nearest)

        nearest = model_repository.find_nearest(pygsty.euclid.Point2(20, 12), 20)
        self.assertEqual([m], nearest)

    def test_it_finds_the_following_location(self):
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

    def test_it_can_return_neighbors_of_a_location(self):
        m = BaseModel(position=(10, 9))
        m2 = BaseModel(position=(11, 11))
        m3 = BaseModel(position=(9,11))
        missing = BaseModel(position=(12, 12))
        target_loc = BaseModel(position=(10, 10))
        neighbors = model_repository.get_neighbors(10, 10)
        self.assertTrue(m in neighbors)
        self.assertTrue(m2 in neighbors)
        self.assertTrue(m3 in neighbors)
        self.assertFalse(missing in neighbors)
        self.assertFalse(target_loc in neighbors)

    def test_it_returns_if_a_location_is_empty(self):
        m = BaseModel(position=(20, 20))
        self.assertTrue(model_repository.is_vacant((21, 21)))
        self.assertFalse(model_repository.is_vacant((20, 20)))

    def test_it_does_not_blow_up_finding_edge_neighbors(self):
        n = model_repository.get_neighbors(20000,20000)
        self.assertEqual([], n)

    def test_it_can_find_any_by_a_matching_function(self):
        m = BaseModel(position=(10, 20))
        m2 = BaseModel(position=(11, 22))
        m3 = BaseModel(position=(14, 11))

        def test_match(test_obj):
            return test_obj == m

        matches = model_repository.find_all(test_match)
        self.assertEqual([m], matches)
