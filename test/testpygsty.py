from mock import *
import unittest
import pygsty

@patch("pygsty.rack.Rack")
class TestPork(unittest.TestCase):
  def test_start_creates_and_starts_the_rack(self, mock_rack):
    r = mock_rack.return_value
    pygsty.start()
    self.assertEqual(pygsty.engine(), r)
    mock_rack.assert_called_with()
