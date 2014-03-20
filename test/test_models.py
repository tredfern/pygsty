import unittest
import pygsty.models
import pyglet
from mock import MagicMock
from pygsty.models import *

class MockSprite():
    def __init__(self, image, x, y, batch, group):
        self.group = group

pyglet.sprite.Sprite = MockSprite

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

class TestModelRepository(unittest.TestCase):
    def test_it_can_track_a_model(self):
        m = BaseModel()
        repo = ModelRepository()
        repo.add(m)
        self.assertTrue(m in repo)
        repo.remove(m)
        self.assertTrue(m not in repo)
