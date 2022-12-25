from services.game import Game
from entities.snake import Snake
import unittest
from unittest.mock import MagicMock

class TestGame(unittest.TestCase):
    def setUp(self):
        self.set_matrix_called_with=""
        self.score_service=MagicMock()
        self.score_service.new=MagicMock()
        self.game_matrix=MagicMock()
        self.game_matrix.matrix=[[MagicMock()]*14 for i in range(0, 9)]

        def return_args(args):
            self.set_matrix_called_with=args
        
        self.game_matrix.set_matrix=return_args

        for row in self.game_matrix.matrix:
            for element in row:
                element.type="empty"

        snake=MagicMock()
        snake.advance=MagicMock()
        self.snake=snake

    def test_right_out_of_bound(self):
        self.snake.advance.return_value=[[1, 12], [1, 13], [1, 14]]
        game = Game(self.snake, self.game_matrix, self.score_service)
        game.start("Riku", "easy")
        game.advance()
        self.score_service.new.assert_called_with("Riku", 0, "easy")
        self.assertEqual(game.game_over, True)

    def test_normal_advance(self):
        self.snake.advance.return_value=[[1, 5], [1, 6], [1, 7]]
        game = Game(self.snake, self.game_matrix, self.score_service)
        game.start("Riku", "easy")
        game.advance()
        expected_snake_coordinates=[[1, 5], [1, 6], [1, 7]]
        arg_matrix = self.set_matrix_called_with
        for element in expected_snake_coordinates:
            self.assertEqual(arg_matrix[element[0]][element[1]].type, "snake")

    def test_consume_gives_points(self):
        self.snake.advance.return_value=[[1, 4], [1, 5], [1, 6]]
        game=Game(self.snake, self.game_matrix, self.score_service)
        game.start("Riku","hard")
        treat=MagicMock()
        treat.consume=MagicMock()
        treat.points=15
        treat.type="treat"
        game.game_matrix.matrix[1][6]=treat
        game.advance()
        self.assertEqual(game.points,15)

    
    




