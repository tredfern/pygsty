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


class TestVisibleModel(unittest.TestCase):
    def test_each_model_gets_its_own_group(self):
        model1 = pygsty.models.VisibleModel()
        model2 = pygsty.models.VisibleModel()

        self.assertNotEqual( model1.render_group, model2.render_group)


    def test_model_group_is_set_to_the_model_in_question(self):
        model = pygsty.models.VisibleModel()
        self.assertEqual( model.render_group.model, model)

    def test_models_start_in_the_default_batch(self):
        model = pygsty.models.VisibleModel()
        self.assertEqual( model.batch, pygsty.models.default_batch )


    def test_screen_coordinates_default_to_standard_position(self):
        model = pygsty.models.VisibleModel(position=(30, 40) )
        self.assertEqual(model.screen_x, 30 )
        self.assertEqual(model.screen_y, 40 )

class TestSpriteModel(unittest.TestCase):
    pass
