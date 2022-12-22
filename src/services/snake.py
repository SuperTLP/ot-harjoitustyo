from service_config.service_config import START,directions

class Snake:
    """instance of this class is the snake controlled by the player."""
    def __init__(self, position=START):
        """
        self.pending_blocks is the number of times the snake will be extended
        in the future. Each advance of the game reduces the value by one.
        self.start_position is a list containing original coordinates
        of the snake. This is never changed.
        self.position is a list containing the current coordinates
        of the snake.
        self.direction is numeric value of snake's current direction."""
        self.pending_blocks=0
        self.start_position=position[:]
        self.position=position[:]
        self.direction=1

    def reset(self):
        """This method resets snake's direction to 1, pending_blocks to 0
        and position to the given position when the class instance was created.
        Position is returned to game for initial rendering."""
        self.position=[x[:] for x in self.start_position[:]]
        self.pending_blocks=0
        self.direction=1
        return self.position

    def change_direction(self, direction):
        """Sets self.direction if snake does not turn on itself."""
        if len(self.position)==1:
            self.direction=direction
            return
        previous=self.position[-2]
        next_head=self.new_head(direction)
        if next_head!=previous:
            self.direction=direction

    def new_head(self, direction):
        """This calculates what the next coordinates of snake's head
        are going to be given direction."""
        new_head=self.position[len(self.position)-1][:]
        new_head[0]+=directions[direction][0]
        new_head[1]+=directions[direction][1]
        return new_head
    
    def set_position(self, position):
        """This sets the snakes position to given list.
        This is used by special treats to alter the snake's behaviour."""
        self.position=[i[:] for i in position[:]]
        
    def set_pending_blocks(self, blocks):
        """This method sets snake's pending blocks to a given number."""
        self.pending_blocks=blocks
        
    def advance(self):
        """This method moves the snake forward every time the game advances."""
        new_head=self.new_head(self.direction)
        self.position.append(new_head)
        if self.pending_blocks<=0:
            del self.position[0]
        else:
            self.pending_blocks-=1
        return self.position
