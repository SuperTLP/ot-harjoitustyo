from random import choice, randint
from entities.default_treat import DefaultTreat
from entities.matrix_element import MatrixElement
from services.treat_factory import TreatFactory
treat_factory=TreatFactory()
treat_1=MatrixElement(DefaultTreat(3), "treat", 1,1,3)
snake_body=MatrixElement(None,"snake",0,0,0)
empty=MatrixElement(None,"empty",0,0,0)

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
    """Game is class responsible for integrating entities, and producing the image
    supplied for gui."""
    def __init__(self, snake, score, game_matrix=START):
        """self.points is the current amount of points
        the player has collected."""
        self.points=0
        """self.score is an instance of the Score class."""
        self.score=score
        self.player_name=""
        """self.start_position is the initial position
        of the game. This never changes."""
        self.start_position=[x[:] for x in game_matrix]
        """self.game_matrix is the current position of the game."""
        self.game_matrix=[x[:] for x in game_matrix]
        """self.snake is an instance of the snake-class."""
        self.snake=snake
        """self.direction is the direction given to the snake
        instance on advance."""
        self.direction=1
        self.game_over=True
        for i in snake.position:
            self.game_matrix[i[0]][i[1]]=snake_body
        self.coordinates = []
        for i in range(0, len(game_matrix)):
            for j in range(0, len(game_matrix[0])):
                self.coordinates.append([i, j])

    def start(self, name):
        """this method resets the game"""
        self.points=0
        self.game_matrix=[x[:] for x in self.start_position]
        self.player_name=name
        self.snake.reset()
        self.direction=1
        self.game_over=False

    def set_game_matrix(self, matrix):
        """This method allows high customization of special treat functionality
        in the future."""
        self.game_matrix=matrix

    def change_direction(self, direction):
        self.direction=direction

    def out_out_bounds(self, head):
        """This method tests whether the snake has hit wall"""
        return (head[1]<0 or head[0]>=len(self.game_matrix) or
        head[0]<0 or head[1]>=len(self.game_matrix[0]))

    def square_is_free(self, coordinates):
        """This tests whether the square that snake's head is currently on its body.
        Returns true if snake blocks do not overlap and false otherwise."""
        return self.game_matrix[coordinates[0]][coordinates[1]].type!="snake"

    def purge_candy(self):
        """This method removes all candies from the map. Used by the PurgeTreat class's
        consume method."""
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type!="snake":
                    i[j]=empty

    def clear_game_matrix(self):
        """This clears previous snake blocks. Used before rendering new snake position."""
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type=="snake":
                    i[j]=empty

    def free_filter(self, coordinate):
        return self.game_matrix[coordinate[0]][coordinate[1]].type=="empty"

    def no_snake_filter(self, coordinate):
        return self.game_matrix[coordinate[0]][coordinate[1]].type!="snake"

    def get_non_snake_coordinates(self):
        """This method is used to find squares on the game_matrix that are not snake body."""
        non_snake_coordinates=list(filter(self.no_snake_filter, self.coordinates))
        return non_snake_coordinates

    def get_empty_coordinates(self):
        """This is used to find free squares systematically to reduce overhead caused
        by random polling"""
        free_coordinates = list(filter(self.free_filter, self.coordinates))
        return free_coordinates

    def new_treat(self):
        new_treat=TreatFactory().new_random_treat()
        free_coordinates=self.get_non_snake_coordinates()
        if new_treat.tier==1:
            free_coordinates=self.get_empty_coordinates()
        if len(free_coordinates)==0:
            return
        coordinates=choice(free_coordinates)
        self.game_matrix[coordinates[0]][coordinates[1]]=new_treat

    def eat_treat(self, treat):
        """This method is called when snake's head is on any consumable element.
        It assures the consume function of the element is called with a correct argument."""
        self.points+=treat.points
        if treat.type=="treat":
            treat.action.consume(self.snake)
        if treat.type=="matrix_treat":
            treat.action.consume(self)
        if treat.type=="dual_treat":
            print("ny consumee")
            treat.action.consume(self, self.snake)

    def is_treat(self, head):
        """This method tests whether the snake's head is currently on a consumable element.
        Returns true if yes, false otherwise."""
        if self.game_matrix[head[0]][head[1]].tier!=0:
            return True
        return False

    def update_game_matrix(self,snake):
        """This method renders snake's body on the game_matrix."""
        for block in snake:
            self.game_matrix[block[0]][block[1]]=snake_body

    def advance(self):
        """This is the game's tick method. It manages everything that is needed to produce
        the next image supplied to GUI, and then returns it."""
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
