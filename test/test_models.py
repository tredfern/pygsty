import unittest
import pygsty.models

class TestBaseModel(unittest.TestCase):
    def test_models_start_at_position_zero_zero(self):
        m = pygsty.models.BaseModel()
        self.assertEqual( m.position, pygsty.euclid.Point2(0, 0) )
        self.assertEqual( m.x, 0 )
        self.assertEqual( m.y, 0 )

    def test_you_can_move_the_model(self):
        m = pygsty.models.BaseModel()
        m.moveTo(40, 50)
        self.assertEqual( m.position.x, 40 )
        self.assertEqual( m.position.y, 50 )
        self.assertEqual( m.x, 40 )
        self.assertEqual( m.y, 50 )

    def test_you_can_instantiate_at_another_position(self):
        m = pygsty.models.BaseModel(position=(10, 32))
        self.assertEqual( m.position, (10, 32) )

    def test_models_are_added_to_the_global_repository(self):
        m = pygsty.models.BaseModel()
        self.assertTrue(m in pygsty.models.model_list)

    def test_killing_models_removes_them_from_the_list(self):
        m = pygsty.models.BaseModel()
        self.assertTrue(m in pygsty.models.model_list)
        m.kill()
        self.assertTrue(m not in pygsty.models.model_list)

class TestSpriteModel(unittest.TestCase):
    pass
