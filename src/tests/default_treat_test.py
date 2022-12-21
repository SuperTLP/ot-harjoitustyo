from entities.default_treat import DefaultTreat
from entities.matrix_element import MatrixElement
import unittest
from unittest import mock

class TestDefaultTreat(unittest.TestCase):
    def setUp(self):
        self.snake=mock.MagicMock()
        self.snake.set_pending_blocks=mock.MagicMock()
        self.snake.set_position=mock.MagicMock()

    def test_snake_length_too_small(self):
        treat = MatrixElement(DefaultTreat(-10),"treat",1,1,-10)
        self.snake.pending_blocks=2
        self.snake.position=[[1, 2], [1, 3]]
        treat.action.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(0)
        self.snake.set_position.assert_called_with([[1, 3]])

    def test_snake_length_grows(self):
        treat = MatrixElement(DefaultTreat(5),"treat",1,1,5)
        self.snake.pending_blocks=2
        treat.action.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(7)


    def test_snake_length_equal_to_treat(self):
        self.snake.position=[[1, 2], [1, 3]]
        self.snake.pending_blocks=0
        treat = MatrixElement(DefaultTreat(-2),"treat",1,1,-2)
        treat.action.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(0)
        self.snake.set_position.assert_called_with([[1, 3]])
    
    def test_pending_blocks_does_not_change(self):
        self.snake.position=[[1, 2], [1, 3], [1, 4], [1, 5]]
        self.snake.pending_blocks=5
        treat = MatrixElement(DefaultTreat(-2),"treat",1,1,-2)
        treat.action.consume(self.snake)
        self.snake.set_pending_blocks.assert_not_called()
        self.snake.set_position.assert_called_with([[1, 4], [1, 5]])

    def test_pending_blocks_decrease_correctly(self):
        self.snake.position=[[1, 2], [1, 3], [1, 4]]
        treat = MatrixElement(DefaultTreat(-5),"treat",1,1,-2)
        self.snake.pending_blocks=16
        treat.action.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(13)

    def test_pending_blocks_increase_correctly(self):
        self.snake.position=[[1, 2]]
        treat = MatrixElement(DefaultTreat(2),"treat",1,1,2)
        self.snake.pending_blocks=4
        treat.action.consume(self.snake)
        self.snake.set_pending_blocks.assert_called_with(6)
