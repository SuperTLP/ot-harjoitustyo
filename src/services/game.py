from random import choice
from entities.matrix_element import MatrixElement
from services.treat_factory import TreatFactory
from service_config.game_config import GAME_OVER,directions
treat_factory=TreatFactory()
snake_body=MatrixElement(None,"snake",0,0,0)
empty=MatrixElement(None,"empty",0,0,0)

START=[[empty]*14 for i in range(0, 9)]

class Game:
    """Game is class responsible for integrating entities, and producing the image
    supplied for gui."""
    def __init__(self, snake, score):
        """self.points is the current amount of points
        the player has collected.
        self.score is an instance of the Score class.
        self.game_matrix is the current position of the game.
        self.snake is an instance of the snake-class.
        self.direction is the direction given to the snake
        instance on advance.
        self.player_name is name of the player
        self.difficulty is the difficulty level chosen. Higher difficulty
        indicates lower refresh interval in gui.
        """
        self.difficulty="medium"
        self.points=0
        self.score=score
        self.player_name=""
        self.game_matrix=[x[:] for x in START]
        self.snake=snake
        self.direction=1
        self.game_over=True
        for i in snake.position:
            self.game_matrix[i[0]][i[1]]=snake_body
        self.coordinates = []
        for i in range(0, len(self.game_matrix)):
            for j in range(0, len(self.game_matrix[0])):
                self.coordinates.append([i, j])

    def start(self, name,difficulty):
        """this method resets game attributes. and returns initial image for gui"""
        self.points=0
        self.difficulty=difficulty
        self.game_matrix=[x[:] for x in START]
        self.player_name=name
        snake_position=self.snake.reset()
        for snake_block in snake_position:
            self.game_matrix[snake_block[0]][snake_block[1]]=snake_body
        self.direction=1
        self.game_over=False
        return self.game_matrix

    def set_game_matrix(self, matrix):
        """Sets self.game_matrix to custom matrix. used by special treats."""
        self.game_matrix=matrix

    def change_direction(self, direction, force=False):
        """Sets self.direction if snake does not turn on itself."""
        if len(self.snake.position)==1:
            self.direction=direction
            return
        snake_head=self.snake.position[-1]
        previous=self.snake.position[-2]
        next_head=[
        snake_head[0]+directions[direction][0],
        snake_head[1]+directions[direction][1]
        ]
        if len(self.snake.position)>1 and next_head==previous:
            return
        self.direction=direction

    def out_out_bounds(self, head):
        """This method tests whether the snake has hit wall"""
        return (head[1]<0 or head[0]>=len(self.game_matrix) or
        head[0]<0 or head[1]>=len(self.game_matrix[0]))

    def square_is_free(self, coordinates):
        """Checks if the first element (head) of the snake's position
        overlaps with some other snake_body element."""
        return self.game_matrix[coordinates[0]][coordinates[1]].type!="snake"

    def purge_candy(self):
        """This method removes all treats from the map. Used by the PurgeTreat
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
        """returns locations [y, x] on game_matrix where
        there are no snake_body or treat blocks."""
        return self.game_matrix[coordinate[0]][coordinate[1]].type=="empty"

    def no_snake_filter(self, coordinate):
        """Returns locations [y, x] on self.game_matrix where
        there are no snake_body blocks."""
        return self.game_matrix[coordinate[0]][coordinate[1]].type!="snake"

    def get_non_snake_coordinates(self):
        """This method is used to find squares on the game_matrix that are not snake body."""
        non_snake_coordinates=list(filter(self.no_snake_filter, self.coordinates))
        return non_snake_coordinates

    def get_empty_coordinates(self):
        """This method returns empty coordinates [y, x] on game_matrix. Empty
        coordinates means the element's type in that location is empty"""
        free_coordinates = list(filter(self.free_filter, self.coordinates))
        return free_coordinates

    def new_treat(self):
        """this method fetches new treat object from TreatFactory, adds
        it to game_matrix and updates free_coordinates accordingly."""
        new_treat=TreatFactory().new_random_treat()
        free_coordinates=self.get_non_snake_coordinates()
        if new_treat.tier==1:
            free_coordinates=self.get_empty_coordinates()
        if len(free_coordinates)==0:
            return
        coordinates=choice(free_coordinates)
        self.game_matrix[coordinates[0]][coordinates[1]]=new_treat

    def eat_treat(self, treat):
        """This method is called after is_treat method returns true, indicating
        snake has moved on top of a treat. the treat's consume function is called
        with argument snake, game or both depending on type of the treat."""
        self.points+=treat.points
        if treat.type=="treat":
            treat.action.consume(self.snake)
        if treat.type=="matrix_treat":
            treat.action.consume(self)
        if treat.type=="dual_treat":
            treat.action.consume(self, self.snake)

    def is_treat(self, head):
        """This method tests whether the snake has moved on a consumable
        element. Returns True or False accordingly."""
        if self.game_matrix[head[0]][head[1]].tier!=0:
            return True
        return False

    def update_game_matrix(self,snake):
        """This method renders snake's body on the game_matrix."""
        for block in snake:
            self.game_matrix[block[0]][block[1]]=snake_body

    def advance(self):
        """This method is the only method of game logic that is called by the GUI.
        This method initiates creation of a treat element, treat consumption
        and asks snake to update it's position given the direction. This method
        then updates the game_matrix and returns it to the GUI for rendering.
        """
        snake_image = self.snake.advance(self.direction)
        head = snake_image[len(snake_image)-1]
        if not self.game_over and (self.out_out_bounds(head) or not self.square_is_free(head)):
            self.game_over=True
            self.score.new(self.player_name, self.points,self.difficulty)
        if self.game_over:
            return GAME_OVER
        if self.is_treat(head):
            self.eat_treat(self.game_matrix[head[0]][head[1]])
        self.clear_game_matrix()
        self.update_game_matrix(snake_image)
        self.new_treat()
        return self.game_matrix
