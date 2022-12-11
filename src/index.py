import sqlite3
from ui.gui import View
from services.game import Game
from services.snake import Snake
from repositories.score import Score
db = sqlite3.connect("src/database.db")
score=Score(db)
snake = Snake()
game = Game(snake, score)
view = View(game, score)

view.run()
