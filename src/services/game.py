from random import choice
from entities.matrix_element import MatrixElement
from services.treat_factory import TreatFactory
from service_config.service_config import GAME_OVER
treat_factory=TreatFactory()
snake_body=MatrixElement(None,"snake",0,0,0)
empty=MatrixElement(None,"empty",0,0,0)

START=[[empty]*14 for i in range(0, 9)]

class Game:
    """Game is class responsible for integrating entities, and producing the image
    supplied for gui."""
    def __init__(self, snake, score):
        """
        self.score is an instance of the Score class.
        self.snake is an instance of the snake-class.
        self.game_matrix is the current position of the game.
        indicates lower refresh interval in gui.
        self.coordinates is 2 dimensional list of game coordinates.
        This reduces overhead caused by searching free coordinates.
        """
        self.points=0
        self.difficulty="medium"
        self.player_name=""
        self.score=score
        self.snake=snake
        self.game_matrix=[x[:] for x in START]
        self.coordinates = []
        for i in range(0, len(self.game_matrix)):
            for j in range(0, len(self.game_matrix[0])):
                self.coordinates.append([i, j])
        self.game_over=True

    def start(self, name,difficulty):
        """this method initializes game attributes and returns initial image for gui
        - self.points is the current amount of points
        the player has collected.
        - self.difficulty is the difficulty level chosen. Higher difficulty
        - self.player_name is name of the player"""
        self.points=0
        self.difficulty=difficulty
        self.game_matrix=[x[:] for x in START]
        self.player_name=name
        snake_position=self.snake.reset()
        for snake_block in snake_position:
            self.game_matrix[snake_block[0]][snake_block[1]]=snake_body
        self.game_over=False
        return self.game_matrix

    def set_game_matrix(self, matrix):
        """Sets self.game_matrix to custom matrix. used by special treats."""
        self.game_matrix=matrix

    def out_out_bounds(self, head):
        """This method tests whether the snake has hit wall"""
        return (head[1]<0 or head[0]>=len(self.game_matrix) or
        head[0]<0 or head[1]>=len(self.game_matrix[0]))

    def snake_collision(self, position):
        """Checks if the first element (head) of the snake's position
        overlaps with some other snake_body element."""
        return position[-1] in position[:-1]

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
        """returns true if given coordinates are empty on game_matrix."""
        return self.game_matrix[coordinate[0]][coordinate[1]].type=="empty"

    def no_snake_filter(self, coordinate):
        """Returns true if given coordinates are not coordinates of a
        snake body block"""
        return self.game_matrix[coordinate[0]][coordinate[1]].type!="snake"

    def get_non_snake_coordinates(self):
        """This method is used to find coordinates [y,x] where there are no
        snake_body blocks."""
        non_snake_coordinates=list(filter(self.no_snake_filter, self.coordinates))
        return non_snake_coordinates

    def get_empty_coordinates(self):
        """This method returns empty coordinates [y, x] on game_matrix. Empty
        coordinates mean the element's type in that location is empty"""
        free_coordinates = list(filter(self.free_filter, self.coordinates))
        return free_coordinates

    def new_treat(self):
        """this method fetches new treat object from TreatFactory and adds
        it to game_matrix"""
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
        with argument self.snake or self depending on type of the treat."""
        self.points+=treat.points
        if treat.type=="treat":
            treat.action.consume(self.snake)
        if treat.type=="matrix_treat":
            treat.action.consume(self)

    def is_treat(self, head):
        """This method tests whether the snake has moved on a consumable
        element. Returns True or False accordingly."""
        if self.game_matrix[head[0]][head[1]].tier!=0:
            return True
        return False

    def update_snake_position(self,snake):
        """This method renders snake's body on the game_matrix."""
        for block in snake:
            self.game_matrix[block[0]][block[1]]=snake_body

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
        self.clear_game_matrix()
        self.update_snake_position(snake_image)
        self.new_treat()
        return self.game_matrix
