from services.game import Game
from entities.snake import Snake
import unittest
from unittest.mock import MagicMock

class TestGame(unittest.TestCase):
    def setUp(self):
        self.score_service=MagicMock()
        self.score_service.new=MagicMock()
        snake=MagicMock()
        snake.advance=MagicMock()
        self.snake=snake

    def test_right_out_of_bound(self):
        self.snake.advance.return_value=[[1, 12], [1, 13], [1, 14]]
        game = Game(self.snake, self.score_service)
        game.start("Riku", "easy")
        game.advance()
        self.score_service.new.assert_called_with("Riku", 0, "easy")
        self.assertEqual(game.game_over, True)

    def test_normal_advance(self):
        self.snake.advance.return_value=[[1, 5], [1, 6], [1, 7]]
        game = Game(self.snake, self.score_service)
        game.start("Riku", "easy")
        game.advance()
        expected_snake_coordinates=[[1, 5], [1, 6], [1, 7]]
        for element in expected_snake_coordinates:
            self.assertEqual(game.game_matrix[element[0]][element[1]].type, "snake")

    def test_consume_gives_points(self):
        self.snake.advance.return_value=[[1, 4], [1, 5], [1, 6]]
        game=Game(self.snake,self.score_service)
        game.start("Riku","hard")
        treat=MagicMock()
        treat.consume=MagicMock()
        treat.points=15
        treat.type="treat"
        game.game_matrix[1][6]=treat
        game.advance()
        self.assertEqual(game.points,15)

    
    




