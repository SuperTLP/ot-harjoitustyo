START=[[3, 1], [3, 2], [3, 3], [3, 4]]

class Snake:
    """instance of this class is the snake controlled by the player."""
    def __init__(self, position=START):
        """pending_blocks is the number of times the snake will be extended
        in the future. Each tick of the game reduces the value by one."""
        self.pending_blocks=0
        """start_position is a list containing original coordinates
        of the snake. This is never changed."""
        self.start_position=position[:]
        """self.position is a list containing the current coordinates
        of the snake."""
        self.position=position[:]
        """self.directions is a map that converts direction to coordinates
        that will be added to the previous head coordinate, producing
        new head location."""
        self.directions={
            0: [-1, 0],
            1: [0, 1],
            2: [1, 0],
            3: [0, -1]
        }
    def reset(self):
        """This method resets the snake's position to the given position
        when the class instance was created."""
        self.position=self.start_position[:]
        self.pending_blocks=0

    def new_head(self, direction):
        """This calculates what the next coordinates of snake's head
        are going to be."""
        new_head=self.position[len(self.position)-1][:]
        new_head[0]+=self.directions[direction][0]
        new_head[1]+=self.directions[direction][1]
        return new_head
    def set_position(self, position):
        """This set's the snakes position to given list.
        This is used by special treats to alter the snake's behaviour."""
        self.position=[i[:] for i in position[:]]
    def set_pending_blocks(self, blocks):
        """This method sets snake's pending blocks to a given number."""
        self.pending_blocks=blocks
    def advance(self, direction):
        """This method changes the snake's position depending on
        given direction. This method returns the snake's position
        to the game."""
        new_head=self.new_head(direction)
        self.position.append(new_head)
        if self.pending_blocks<=0:
            del self.position[0]
        else:
            self.pending_blocks-=1
        return self.position
