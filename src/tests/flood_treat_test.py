from entities.treats.flood_treat import FloodTreat
import unittest
from unittest.mock import MagicMock

class TestFloodTreat(unittest.TestCase):

    def setUp(self):
        self.set_matrix_called_with=None
        def return_args(arg):
            self.set_matrix_called_with=arg
        self.game_matrix=MagicMock()
        empty=MagicMock()
        empty.type="empty"
        matrix=[[empty]*14 for i in range(0, 9)]

        self.game_matrix.matrix=matrix
        self.game_matrix.set_matrix=return_args
        
    def test_every_second_is_treat(self):
        treat = FloodTreat()
        treat.consume(self.game_matrix)
        even_rows=self.set_matrix_called_with[::2]
        odd_rows=self.set_matrix_called_with[1::2]

        for row in odd_rows:
            for element in row[::2]:
                self.assertEqual(element.type, "treat")
                self.assertEqual(element.action.effect, -2)

        for row in even_rows:
            for element in row[1::2]:
                self.assertEqual(element.type, "treat")
                self.assertEqual(element.action.effect, -2)

    def test_every_second_is_not_changed(self):
        treat = FloodTreat()
        treat.consume(self.game_matrix)

        even_rows=self.set_matrix_called_with[::2]
        odd_rows=self.set_matrix_called_with[1::2]

        for row in odd_rows:
            for element in row[1::2]:
                self.assertEqual(element.type, "empty")

        for row in even_rows:
            for element in row[::2]:
                self.assertEqual(element.type, "empty")

    def test_snake_not_replaced(self):
        snake=MagicMock()
        snake.type="snake"
        self.game_matrix.matrix[0][1]=snake
        treat = FloodTreat()
        treat.consume(self.game_matrix)
        self.assertEqual(self.set_matrix_called_with[0][1].type,"snake")
