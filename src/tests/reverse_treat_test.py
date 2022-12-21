from entities.reverse_treat import ReverseTreat
from entities.matrix_element import MatrixElement
import unittest
from unittest.mock import MagicMock
class TestReverseTreat(unittest.TestCase):
    def setUp(self):
        self.snake=MagicMock()
        self.snake.position=[[1, 2], [1, 3], [1, 4]]
        self.snake.set_position=MagicMock()
        self.game=MagicMock()
        self.game.change_direction=MagicMock()
        pass
    def test_snake_longer_than_1(self):
        treat = MatrixElement(ReverseTreat(),"matrix_treat",2,20,"<-")
        treat.action.consume(self.game, self.snake)
        self.snake.set_position.assert_called_with([[1, 4], [1, 3], [1, 2]])
        self.game.change_direction.assert_called_with(3)
    def test_snake_length_1(self):
        treat = MatrixElement(ReverseTreat(),"matrix_treat",2,20,"<-")
        self.snake.position=[[1, 2]]
        self.game.direction=1
        treat.action.consume(self.game, self.snake)
        self.snake.set_position.assert_not_called()
        self.game.change_direction.assert_called_with(3)


