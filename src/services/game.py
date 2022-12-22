from random import choice
from entities.matrix_element import MatrixElement
from services.treat_factory import TreatFactory
from service_config.service_config import GAME_OVER

class Game:
    """Game is class responsible for integrating entities, and producing the image
    supplied for gui.
    snake_body is used to mark snake location in game.
    empty is used to mark empty locations in game.
    START is empty matrix used to initialize game.
    """
    snake_body=MatrixElement(None,"snake",0,0,0)
    empty=MatrixElement(None,"empty",0,0,0)
    START=[[MatrixElement(None,"empty",0,0,0)]*14 for i in range(0, 9)]

    def __init__(self, snake, score):
        """
        Arguments:
        -score is an instance of the Score class.
        -snake is an instance of the snake-class.

        self.points is the number of points the player has collected
        self.difficulty is the difficulty level selected by player.
        self.player_name is the name of the player.
        self.game_matrix is the current position of the game.
        self.coordinates is 2 dimensional list of game coordinates.
        This reduces overhead caused by searching free coordinates.
        self.game_over indicates whether the game is currently running. Is
        False until game is started with .start method.
        """
        self.points=0
        self.difficulty="medium"
        self.player_name=""
        self.score=score
        self.snake=snake
        self.game_matrix=[x[:] for x in Game.START]
        self.coordinates = []

        for i in range(0, len(self.game_matrix)):
            for j in range(0, len(self.game_matrix[0])):
                self.coordinates.append([i, j])
        self.game_over=True

    def start(self, name,difficulty):
        """
        arguments:
        -name: name of the player
        -difficulty: difficulty level the game is played on

        this method initializes game attributes and returns initial image for gui
        """
        self.points=0
        self.difficulty=difficulty
        self.game_matrix=[x[:] for x in Game.START]
        self.player_name=name
        snake_position=self.snake.reset()
        for snake_block in snake_position:
            self.game_matrix[snake_block[0]][snake_block[1]]=self.snake_body
        self.game_over=False
        return self.game_matrix

    def set_game_matrix(self, matrix):
        """
        argument:
        -matrix: new value for self.game_matrix

        this method sets self.game_matrix to custom matrix. used by special treats.
        """
        self.game_matrix=matrix

    def out_out_bounds(self, head):
        """
        argument:
        -head: snake's current head coordinates.

        This method tests whether the snake has hit wall
        """
        return (head[1]<0 or head[0]>=len(self.game_matrix) or
        head[0]<0 or head[1]>=len(self.game_matrix[0]))

    def snake_collision(self, position):
        """
        argument:
        -position: snake's position

        Checks if the first element (head) of the snake's position
        overlaps with some other snake_body element. Returns True or False
        accordingly.
        """
        return position[-1] in position[:-1]

    def purge_candy(self):
        """
        This method removes all treats from game_matrix. Used by the PurgeTreat
        consume method.
        """
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type!="snake":
                    i[j]=self.empty

    def remove_previous_snake(self):
        """
        This clears previous snake blocks. Used before rendering new snake position.
        """
        for i in self.game_matrix:
            for j, elem in enumerate(i):
                if elem.type=="snake":
                    i[j]=self.empty

    def get_non_snake_coordinates(self):
        """
        This method is used to find coordinates [y,x] where there are no
        snake_body blocks. It then returns those coordinates.
        """
        non_snake_coordinates=[
        x[:] for x in self.coordinates if
        self.game_matrix[x[0]][x[1]].type!="snake"]
        return non_snake_coordinates

    def get_empty_coordinates(self):
        """
        This method returns empty coordinates [y, x] on game_matrix. Empty
        coordinates mean the element's type in that location is empty. Those
        Coordinates are then returned.
        """
        free_coordinates = [x[:] for x in self.coordinates if
        self.game_matrix[x[0]][x[1]].type=="empty"]
        return free_coordinates

    def new_treat(self):
        """
        this method fetches new treat object from TreatFactory and adds
        it to game_matrix
        """
        new_treat=TreatFactory().new_random_treat()
        free_coordinates=self.get_non_snake_coordinates()
        if new_treat.tier==1:
            free_coordinates=self.get_empty_coordinates()
        if len(free_coordinates)==0:
            return
        coordinates=choice(free_coordinates)
        self.game_matrix[coordinates[0]][coordinates[1]]=new_treat

    def eat_treat(self, treat):
        """
        argument:
        -treat: the treat that is to be consumed

        This method is called after is_treat method returns true, indicating
        snake has moved on top of a treat. the treat's consume function is called
        with argument self.snake or self depending on type of the treat."""

        self.points+=treat.points
        if treat.type=="treat":
            treat.action.consume(self.snake)
        if treat.type=="matrix_treat":
            treat.action.consume(self)

    def is_treat(self, head):
        """
        argument:
        -head: coordinates of snake's head.

        This method tests whether the snake has moved on a consumable
        element. Returns True or False accordingly.
        """
        if self.game_matrix[head[0]][head[1]].tier!=0:
            return True
        return False

    def draw_snake(self,snake):
        """
        argument:
        -snake: instance of snake class.

        This method renders snake's body on the game_matrix.
        """
        for block in snake:
            self.game_matrix[block[0]][block[1]]=self.snake_body

    def advance(self):
        """
        This method initiates creation of a treat element, treat consumption
        and asks snake to update it's position given the direction. This method
        then updates the game_matrix and returns it to the GUI for rendering.
        """
        snake_image = self.snake.advance()
        head = snake_image[len(snake_image)-1]
        if not self.game_over and (self.out_out_bounds(head) or self.snake_collision(snake_image)):
            self.game_over=True
            self.score.new(self.player_name, self.points,self.difficulty)
        if self.game_over:
            return GAME_OVER
        if self.is_treat(head):
            self.eat_treat(self.game_matrix[head[0]][head[1]])
        self.remove_previous_snake()
        self.draw_snake(snake_image)
        self.new_treat()
        return self.game_matrix
