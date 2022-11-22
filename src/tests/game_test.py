from game import Game
from snake import Snake
game_over=[[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0]]
class TestGame:
    import unittest
    class TestGame(unittest.TestCase):
        def setUp(self):
            print("Set up goes here")
        def test_right_out_of_bound(self):
            snake=Snake([[1, 11], [1, 12], [1, 13]])
            game = Game(snake)
            val = game.advance()
            print(val)
            self.assertEqual(val, game_over)

