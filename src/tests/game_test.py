from services.game import Game
from services.snake import Snake
import unittest
from unittest.mock import MagicMock

class TestGame(unittest.TestCase):
    def setUp(self):
        self.db=MagicMock()
        self.db.new=MagicMock()
    def test_right_out_of_bound(self):
        snake=MagicMock()
        snake.advance=MagicMock()
        snake.advance.return_value=[[1, 12], [1, 13], [1, 14]]
        game = Game(snake, self.db)
        game.start("Riku")
        game.advance()
        self.db.new.assert_called_with("Riku", 0)
        self.assertEqual(game.game_over, True)
    def test_normal_advance(self):
        snake=MagicMock()
        snake.advance=MagicMock()
        snake.advance.return_value=[[1, 5], [1, 6], [1, 7]]
        game = Game(snake, self.db)
        game.start("Riku")
        game.advance()
        expected_snake_coordinates=[[1, 5], [1, 6], [1, 7]]
        for element in expected_snake_coordinates:
            self.assertEqual(game.game_matrix[element[0]][element[1]].type, "snake")

