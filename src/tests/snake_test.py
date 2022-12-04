
from entities.snake import Snake
import unittest


class TestSnake(unittest.TestCase):
    def setUp(self):
        pass
    def test_snake_length_does_not_go_to_zero(self):
        snake = Snake([[2, 3]])
        snake.advance(1)
        self.assertEqual(str(snake.position), str([[2, 4]]))
    def test_snake_tail_pops_on_advance(self):
        snake = Snake([[2, 3], [2, 4]])
        snake.advance(1)
        self.assertEqual(str(snake.position),str([[2, 4], [2, 5]]))
    def test_pending_blocks_get_consumed(self):
        snake = Snake([[2, 3], [2, 4]])
        snake.set_pending_blocks(1)
        snake.advance(1)
        self.assertEqual(str(snake.position), str([[2, 3], [2, 4], [2, 5]]))
    def test_reset_resets_values(self):
        snake = Snake([[2, 3], [2, 4]])
        snake.set_pending_blocks(15)
        snake.reset()
        self.assertEqual(str(snake.position), str([[2, 3], [2, 4]]))
        self.assertEqual(snake.pending_blocks, 0)
    def test_position_setter(self):
        snake = Snake([[2, 3], [2, 4]])
        snake.set_position([[5, 5]])
        self.assertEqual(str(snake.position), str([[5, 5]]))



