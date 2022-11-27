from gui import View
from game.game import Game
from game.snake import Snake
from game.score import Score
import sqlite3
db = sqlite3.connect("src/database.db")
score=Score(db)
snake = Snake()
game = Game(snake, score)
view = View(game)

view.run()
