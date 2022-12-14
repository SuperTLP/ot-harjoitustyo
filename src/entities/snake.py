from service_config.service_config import START,DIRECTIONS

class Snake:
    """instance of this class is the snake controlled by the player."""
    def __init__(self, position=START):
        """
        argument:
            position: initial coordinates of snake's body. saved in self.start_position.

        self.pending_blocks is the number of times the snake will be extended
        in the future. Each advance reduces the value by one.
        self.position is the current position of snake.
        self.direction is numeric value of snake's current direction.
        """

        self.pending_blocks=0
        self.start_position=position[:]
        self.position=position[:]
        self.direction=1

    def reset(self):
        """
        This method resets snake's direction to 1, pending_blocks to 0
        and position to the given position when the class instance was created.

        Returns:
            snake's initial position
        """

        self.position=[row[:] for row in self.start_position[:]]
        self.pending_blocks=0
        self.direction=1
        return self.position

    def change_direction(self, direction):
        """
        This method sets self.direction if snake does not turn on itself.

        argument:
            direction: numeric direction for snake. values are:
            0: up, 1: right, 2: down, 3: left.
        """

        if len(self.position)==1:
            self.direction=direction
            return
        previous=self.position[-2]
        next_head=self.new_head(direction)
        if next_head!=previous:
            self.direction=direction

    def new_head(self, direction):
        """
        This method calculates what the next coordinates of snake's head
        are going to be.

        argument:
            direction: numeric direction where snake is going to advance

        returns:
            Coordinates [y, x] for snake's new head.
        """

        new_head=self.position[len(self.position)-1][:]
        new_head[0]+=DIRECTIONS[direction][0]
        new_head[1]+=DIRECTIONS[direction][1]

        return new_head

    def set_position(self, position):
        """
        This method sets the snakes position to custom list..
        This is used by special treats to alter the snake's behaviour.

        argument:
            position: 2-dimensional list that snake's position is to be set to.
        """

        self.position=[i[:] for i in position[:]]

    def set_pending_blocks(self, blocks):
        """
        This method sets snake's pending blocks to a given number.

        argument:
            blocks: number that snake's pending_blocks should be set to.
        """

        self.pending_blocks=blocks

    def advance(self):
        """
        This method moves the snake forward

        returns:
            snake's new position after moving forward.
        """

        new_head=self.new_head(self.direction)
        self.position.append(new_head)
        if self.pending_blocks<=0:
            del self.position[0]
        else:
            self.pending_blocks-=1
        return self.position
