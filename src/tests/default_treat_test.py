from game.default_treat import DefaultTreat
import unittest
from unittest import mock

class TestDefaultTreat(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.snake=mock.MagicMock()
        self.snake.set_pending_blocks=mock.MagicMock()
        self.snake.set_position=mock.MagicMock()

    def test_snake_length_too_small(self):
        treat = DefaultTreat(-10)
        self.snake.pending_blocks=2
        self.snake.position=[[1, 2], [1, 3]]
        treat.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(0)
        self.snake.set_position.assert_called_with([[1, 3]])

    def test_snake_length_grows(self):
        treat = DefaultTreat(5)
        self.snake.pending_blocks=2
        treat.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(7)


    def test_snake_length_equal_to_treat(self):
        self.snake.position=[[1, 2], [1, 3]]
        self.snake.pending_blocks=0
        treat = DefaultTreat(-2)
        treat.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(0)
        self.snake.set_position.assert_called_with([[1, 3]])
    