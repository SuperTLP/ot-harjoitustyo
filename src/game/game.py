from random import choice
from .matrix_element import MatrixElement
from .default_treat import DefaultTreat
empty = MatrixElement()
treat_1=MatrixElement(DefaultTreat(3), "treat", 1)
snake_body=MatrixElement(_type="snake")
START=[
[empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, treat_1, empty,
empty, empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,
empty, empty, empty, empty]]

GAME_OVER=[[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0]]

class Game:
    def __init__(self, snake, score, game_matrix=START):
        self.points=0
        self.score=score
        self.player_name=""
        self.start_position=[x[:] for x in game_matrix]
        self.game_matrix=[x[:] for x in game_matrix]
        self.snake=snake
        self.direction=1
        self.game_over=True
        for i in snake.position:
            self.game_matrix[i[0]][i[1]]=snake_body
        self.coordinates = []
        for i in range(0, len(game_matrix)):
            for j in range(0, len(game_matrix[0])):
                self.coordinates.append([i, j])

    def start(self, name):
        self.points=0
        self.game_matrix=[x[:] for x in self.start_position]
        self.player_name=name
        self.snake.reset()
        self.direction=1
        self.game_over=False

    def change_direction(self, direction):
        self.direction=direction

    def out_out_bounds(self, head):
        return (head[1]<0 or head[0]>=len(self.game_matrix) or
        head[0]<0 or head[1]>=len(self.game_matrix[0]))

    def square_is_free(self, coordinates):
        return self.game_matrix[coordinates[0]][coordinates[1]].type!="snake"

    def clear_game_matrix(self):
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type=="snake":
                    i[j]=empty

    def free_filter(self, coordinate):
        return self.game_matrix[coordinate[0]][coordinate[1]].type=="empty"

    def get_empty_coordinates(self):
        free_coordinates = list(filter(self.free_filter, self.coordinates))
        return free_coordinates

    def new_treat(self):
        new_effect=choice([-1, -2, 1, 1, 1, 1, 1, 1, 1])
        free_coordinates=self.get_empty_coordinates()
        if len(free_coordinates)==0:
            return
        treat_coordinates = choice(free_coordinates)
        x_coordinate=treat_coordinates[0]
        y_coordinate=treat_coordinates[1]
        new_element=MatrixElement(DefaultTreat(new_effect), "treat", 1)
        self.game_matrix[x_coordinate][y_coordinate]=new_element

    def eat_treat(self, head):
        self.points+=self.game_matrix[head[0]][head[1]].points
        self.game_matrix[head[0]][head[1]].action.consume(self.snake)

    def is_treat(self, head):
        if self.game_matrix[head[0]][head[1]].type=="treat":
            return True
        return False
    def update_game_matrix(self,snake):
        for block in snake:
            self.game_matrix[block[0]][block[1]]=snake_body

    def advance(self):
        print(self.get_empty_coordinates())
        snake_image = self.snake.advance(self.direction)
        head = snake_image[len(snake_image)-1]
        if not self.game_over and (self.out_out_bounds(head) or not self.square_is_free(head)):
            self.game_over=True
            self.score.new(self.player_name, self.points)
        if self.game_over:
            return GAME_OVER
        if self.is_treat(head):
            self.eat_treat(head)
        self.clear_game_matrix()
        self.update_game_matrix(snake_image)
        self.new_treat()
        return self.game_matrix
