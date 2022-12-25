from services.game import Game
from entities.snake import Snake
from entities.treats.default_treat import DefaultTreat
from entities.treats.reverse_treat import ReverseTreat
from services.score_service import ScoreService

from entities.matrix_element import MatrixElement

from repositories.score_repository import ScoreRepository
import unittest
from unittest.mock import MagicMock
import sqlite3

class TestIntegration(unittest.TestCase):
    def setUp(self):
        db = sqlite3.connect("src/test_database.db")
        cur = db.cursor()
        cur.execute("drop table if exists scores")
        cur.execute("create table scores (id integer primary key autoincrement, name text, score int,difficulty text)")
        db.commit()
        self.snake=Snake([[3, 2], [3,3], [3, 4], [3, 5]])
        score_repository=ScoreRepository(db)
        self.score_service=ScoreService(score_repository)
        self.game=Game(snake=self.snake, score_service=self.score_service)

    def test_movement(self):
        self.game.start("Tester", "easy")
        self.snake.change_direction(1)
        for i in range(0, 20):
            self.game.advance()
        self.assertEqual(self.game.game_over, True)
        self.assertEqual(len(self.score_service.all()),1)

    def test_points_increase(self):
        candy=MatrixElement(DefaultTreat(1),"treat",1,1,1)
        self.game.start("Tester", "easy")
        for i in range(0, 5):
            snake_head=self.snake.position[-1]
            self.game.game_matrix[snake_head[0]][snake_head[1]+1]=candy
            self.game.advance()
        self.assertEqual(len(self.snake.position), 8)
        self.assertEqual(self.snake.pending_blocks,1)
        self.assertEqual(self.game.points, 5)
        self.snake.set_position([[1, 85]])
        self.game.advance()
        scores=self.score_service.all()
        self.assertEqual(
            (scores[0].name, scores[0].score, scores[0].difficulty), 
            ('Tester', 5, 'easy'))

    def test_points_blended(self):
        self.game.start("Tester", "easy")
        empty=MatrixElement(None,"empty",0,0,0)
        point_sequence=[-1, -2, 1, 1, 1, 1, 1, 1]

        for i in range(0, len(point_sequence)):
            snake_head=self.snake.position[len(self.snake.position)-1]
            self.game.game_matrix[snake_head[0]][snake_head[1]+1]=MatrixElement(DefaultTreat(point_sequence[i]),"treat",1,1,point_sequence[i])
            self.game.advance()

        self.game.game_matrix[snake_head[0]][snake_head[1]+1]=empty
        self.game.advance()

        self.game.game_matrix[snake_head[0]][snake_head[1]+1]=empty
        self.game.advance()
        scores = self.score_service.all()

        self.assertEqual(self.game.game_over, True)
        self.assertEqual(len(self.snake.position), 7)
        self.assertEqual(self.game.points, len(point_sequence))
        self.assertEqual((scores[0].name, scores[0].score, scores[0].difficulty), ('Tester', 8, 'easy'))

    def test_reverse_treat_consumption(self):
        treat = MatrixElement(ReverseTreat(),"treat",2,20,"<-")
        self.game.start("Riku", "easy")
        self.snake.set_position([[1, 2], [2, 2], [3,2], [3, 4], [3, 5]])
        self.game.game_matrix[3][6]=treat
        self.game.advance()
        self.assertEqual(self.game.points, 20)
        self.assertEqual(str(list(reversed([[2, 2], [3,2], [3, 4], [3, 5],[3, 6]]))),
        str(self.snake.position))
        self.assertEqual(self.snake.direction, 0)

    def test_reverse_treat_opposite_direction(self):
        treat = MatrixElement(ReverseTreat(),"treat",2,20,"<-")
        self.game.start("Riku", "easy")
        self.snake.set_position([[3, 1],[3,2]])
        self.game.game_matrix[3][3]=treat
        self.game.advance()
        self.assertEqual(self.game.points, 20)
        self.assertEqual(str(list(reversed([[3,2],[3,3]]))),
        str(self.snake.position))
        self.assertEqual(self.snake.direction, 3)
        self.assertEqual(self.game.game_over,False)

    def test_snake_length_increases_correctly(self):
        snake=Snake([[1, 3], [1, 4], [1, 5]])
        game=Game(snake,self.score_service)
        game.start("Tester","easy")
        for i in range(0, 4):
            candy=MatrixElement(DefaultTreat(1),"treat",1,1,1)
            snake_head=snake.position[-1]
            game.game_matrix[snake_head[0]][snake_head[1]+1]=candy
            game.advance()
        self.assertEqual(len(snake.position),6)
        self.assertEqual(snake.pending_blocks,1)


