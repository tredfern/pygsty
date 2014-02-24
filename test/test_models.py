import unittest
import pygsty.models

class TestBaseModel(unittest.TestCase):
    def test_models_start_at_position_zero_zero(self):
        m = pygsty.models.BaseModel()
        self.assertEqual( m.position, pygsty.euclid.Point2(0, 0) )

    def test_models_start_with_no_rotation(self):
        m = pygsty.models.BaseModel()
        self.assertEqual( m.rotation, 0)

    def test_you_can_move_the_model(self):
        m = pygsty.models.BaseModel()
        m.moveTo(40, 50)
        self.assertEqual( m.position.x, 40 )
        self.assertEqual( m.position.y, 50 )


class TestVisibleModel(unittest.TestCase):
    def test_each_model_gets_its_own_group(self):
        model1 = pygsty.models.VisibleModel()
        model2 = pygsty.models.VisibleModel()

        self.assertNotEqual( model1.render_group, model2.render_group)


    def test_model_group_is_set_to_the_model_in_question(self):
        model = pygsty.models.VisibleModel()
        self.assertEqual( model.render_group.model, model)
        



