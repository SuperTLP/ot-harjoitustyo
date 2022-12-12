import unittest
from entities.purge_treat import PurgeTreat
from unittest.mock import MagicMock
from entities.matrix_element import MatrixElement
class TestPurgeTreat(unittest.TestCase):
    def setUp(self):
        pass
    def test_consume(self):
        treat=MatrixElement(PurgeTreat(),"matrix_treat",2,20,"X")
        game_mock=MagicMock()
        game_mock.purge_candy=MagicMock()
        treat.action.consume(game_mock)
        game_mock.purge_candy.assert_called()
    def ensure_setup(self):
        treat=MatrixElement(PurgeTreat(),"matrix_treat",2,20,"X")
        self.assertEqual(treat.effect, "?")