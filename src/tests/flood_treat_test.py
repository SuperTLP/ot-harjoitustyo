from entities.flood_treat import FloodTreat
import unittest
from unittest.mock import MagicMock

class TestFloodTreat(unittest.TestCase):
    def setUp(self):
        self.returned=None
        def return_args(arg):
            self.returned=arg
        self.game=MagicMock()
        empty=MagicMock()
        empty.type="empty"
        game_matrix=[[empty]*14 for i in range(0, 9)]
        self.game.game_matrix=game_matrix
        self.game.set_game_matrix=return_args
        
    def test_every_second_is_treat(self):
        treat = FloodTreat()
        treat.consume(self.game)
        even_rows=self.returned[::2]
        odd_rows=self.returned[1::2]
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
        treat.consume(self.game)
        even_rows=self.returned[::2]
        odd_rows=self.returned[1::2]
        for row in odd_rows:
            for element in row[1::2]:
                self.assertEqual(element.type, "empty")
        for row in even_rows:
            for element in row[::2]:
                self.assertEqual(element.type, "empty")

    def test_snake_not_replaced(self):
        snake=MagicMock()
        snake.type="snake"
        self.game.game_matrix[0][1]=snake
        treat = FloodTreat()
        treat.consume(self.game)
        self.assertEqual(self.returned[0][1].type,"snake")
