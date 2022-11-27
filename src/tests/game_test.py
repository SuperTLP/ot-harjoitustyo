from services.game import Game
from entities.snake import Snake
import unittest
from unittest.mock import MagicMock
game_over=[[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0]]
class TestGame:
    class TestGame(unittest.TestCase):
        def setUp(self):
            self.db=MagicMock()
        def test_right_out_of_bound(self):
            snake=Snake([[1, 11], [1, 12], [1, 13]])
            game = Game(snake, self.db)
            val = game.advance()
            self.assertEqual(val, game_over)

