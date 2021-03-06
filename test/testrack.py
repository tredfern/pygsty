import unittest
from mock import * 
import pygsty

# Need to mock the init method so it doesn't create the window
# this is flawed since we need to know about the rack initializer
# but it does prevent windows from opening up and allows us
# to test the rack class methods that are important

mock_cam = Mock()

def mock_init(self, width, height, fullscreen):
  self._controllers = []
  self.camera = mock_cam.return_value

pygsty.rack.Rack.__init__ = mock_init

class TestRackControllerManagement(unittest.TestCase):
  def setUp(self):
    self.rack = pygsty.rack.Rack(800, 600, False)

  def test_you_can_push_controllers_onto_the_stack(self):
    c1 = pygsty.controllers.BaseController()
    c2 = pygsty.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    self.assertEqual(len(self.rack._controllers), 2)
    self.assertEqual(self.rack._controllers[0], c1)
    self.assertEqual(self.rack._controllers[1], c2)

  def test_you_can_pop_a_controller_off_the_stack(self):
    c1 = pygsty.controllers.BaseController()
    c2 = pygsty.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    popped = self.rack.pop_controller()
    self.assertEqual(popped, c2)
    self.assertEqual(len(self.rack._controllers), 1)

  def test_it_draws_all_controllers_in_stack(self):
    c1 = pygsty.controllers.BaseController()
    c2 = pygsty.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    c1.draw = Mock()
    c2.draw = Mock()
    c1.draw_hud = Mock()
    c2.draw_hud = Mock()
    self.rack.on_draw()
    c1.draw.assert_called_with()
    c1.draw_hud.assert_called_with()
    c2.draw.assert_called_with()
    c2.draw_hud.assert_called_with()

  def test_it_updates_all_the_controllers(self):
    c1 = pygsty.controllers.BaseController()
    c2 = pygsty.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    c1.update = Mock()
    c2.update = Mock()
    self.rack.update(1234)
    c1.update.assert_called_with(1234)
    c2.update.assert_called_with(1234)

