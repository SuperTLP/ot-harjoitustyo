from gui import View
from game import Game
from snake import Snake
snake = Snake()
game = Game(snake)
view = View(game)

view.run()