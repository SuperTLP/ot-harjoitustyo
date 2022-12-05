from random import choice, randint
from entities.matrix_element import MatrixElement
from entities.default_treat import DefaultTreat
from entities.purge_treat import PurgeTreat
empty = MatrixElement()
treat_1=MatrixElement(DefaultTreat(3), "treat", 1, 1)
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

    def set_game_matrix(self, matrix):
        self.game_matrix=matrix

    def change_direction(self, direction):
        self.direction=direction

    def out_out_bounds(self, head):
        return (head[1]<0 or head[0]>=len(self.game_matrix) or
        head[0]<0 or head[1]>=len(self.game_matrix[0]))

    def square_is_free(self, coordinates):
        return self.game_matrix[coordinates[0]][coordinates[1]].type!="snake"

    def purge_candy(self):
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type!="snake":
                    i[j]=empty

    def clear_game_matrix(self):
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type=="snake":
                    i[j]=empty

    def free_filter(self, coordinate):
        return self.game_matrix[coordinate[0]][coordinate[1]].type=="empty"

    def no_snake_filter(self, coordinate):
        return self.game_matrix[coordinate[0]][coordinate[1]].type!="snake"

    def get_non_snake_coordinates(self):
        non_snake_coordinates=list(filter(self.no_snake_filter, self.coordinates))
        return non_snake_coordinates

    def get_empty_coordinates(self):
        free_coordinates = list(filter(self.free_filter, self.coordinates))
        return free_coordinates

    def generate_default_treat(self):
        free_coordinates=self.get_empty_coordinates()
        if len(free_coordinates)==0:
            return
        new_effect=choice([-1, -2, 1, 1, 1, 1, 1, 1, 1])
        treat_coordinates = choice(free_coordinates)
        x_coordinate=treat_coordinates[0]
        y_coordinate=treat_coordinates[1]
        new_element=MatrixElement(DefaultTreat(new_effect), "treat", 1, 1)
        self.game_matrix[x_coordinate][y_coordinate]=new_element

    def generate_matrix_treat(self):
        coordinates=choice(self.get_non_snake_coordinates())
        new_element=MatrixElement(PurgeTreat("?"), "matrix_treat", 5, 20)
        self.game_matrix[coordinates[0]][coordinates[1]]=new_element

    def new_treat(self):
        lottery = randint(1, 90)
        if lottery==90:
            self.generate_matrix_treat()
            return
        self.generate_default_treat()

    def eat_treat(self, treat):
        self.points+=treat.points
        if treat.type=="treat":
            treat.action.consume(self.snake)
        if treat.type=="matrix_treat":
            print("täs")
            treat.action.consume(self)

    def is_treat(self, head):
        if self.game_matrix[head[0]][head[1]].type in ["treat", "matrix_treat"]:
            return True
        return False

    def update_game_matrix(self,snake):
        for block in snake:
            self.game_matrix[block[0]][block[1]]=snake_body

    def advance(self):
        snake_image = self.snake.advance(self.direction)
        head = snake_image[len(snake_image)-1]
        if not self.game_over and (self.out_out_bounds(head) or not self.square_is_free(head)):
            self.game_over=True
            self.score.new(self.player_name, self.points)
        if self.game_over:
            return GAME_OVER
        if self.is_treat(head):
            self.eat_treat(self.game_matrix[head[0]][head[1]])
        self.clear_game_matrix()
        self.update_game_matrix(snake_image)
        self.new_treat()
        return self.game_matrix
