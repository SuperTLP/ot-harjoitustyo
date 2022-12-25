import sqlite3
from ui.gui import View
from repositories.score_repository import ScoreRepository
from entities.snake import Snake
from entities.game_matrix import GameMatrix
from services.game import Game
from services.score_service import ScoreService

db = sqlite3.connect("src/database.db")
score_repository=ScoreRepository(db)
score_service=ScoreService(score_repository)
game_matrix=GameMatrix()
snake = Snake()
game = Game(snake, game_matrix, score_service)
view = View(game, score_service)
view.run()
