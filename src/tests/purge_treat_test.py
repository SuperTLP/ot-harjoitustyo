import unittest
from entities.treats.purge_treat import PurgeTreat
from unittest.mock import MagicMock

class TestPurgeTreat(unittest.TestCase):

    def setUp(self):
        pass
        self.empty=[[MagicMock()]*14 for i in range(0,9)]
        for row in self.empty:
            for element in row:
                element.type="empty"
        self.set_matrix_called_with=""

        def return_args(arg):
            self.set_matrix_called_with=arg

        self.game_matrix=MagicMock()
        self.game_matrix.set_matrix=return_args

    def test_matrix_cleared(self):
        self.game_matrix.matrix=self.empty
        self.game_matrix[0][1].type="snake"
        treat=PurgeTreat()
        treat.consume(self.game_matrix)
        called_matrix=[row[:] for row in self.set_matrix_called_with]
        for row in called_matrix:
            for element in row:
                self.assertEqual(element.type, "empty")


