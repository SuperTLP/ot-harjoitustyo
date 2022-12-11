import unittest
from entities.purge_treat import PurgeTreat
from unittest.mock import MagicMock
class TestPurgeTreat(unittest.TestCase):
    def setUp(self):
        pass
    def test_consume(self):
        treat=PurgeTreat()
        game_mock=MagicMock()
        game_mock.purge_candy=MagicMock()
        treat.consume(game_mock)
        game_mock.purge_candy.assert_called()
    def ensure_setup(self):
        treat=PurgeTreat()
        self.assertEqual(treat.effect, "?")