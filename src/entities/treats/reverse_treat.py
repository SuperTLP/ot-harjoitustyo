class ReverseTreat:
    """
    Class representing a single treat that reverses snake's direction.

    DIRECTIONS is a dict that gives opposite direction of the key.

    NUMERIC_DIRECTIONS is a dict that gives the numeric direction corresponding to
    given direction coordinates."""

    DIRECTIONS={
    0:2,
    1:3,
    2:0,
    3:1
    }

    NUMERIC_DIRECTIONS={
        "[-1, 0]":0,
        "[0, 1]":1,
        "[1, 0]":2,
        "[0, -1]":3
    }

    def __init__(self):
        pass

    def get_opposite_direction(self,position):
        """
        This method calculates what snake's direction should be
        after it's reversed and returns it.

        argument:
            position: position of snake class instance.
        """

        new_direction_y=position[0][0]-position[1][0]
        new_direction_x=position[0][1]-position[1][1]
        new_direction=str([new_direction_y,new_direction_x])
        new_numeric_direction=ReverseTreat.NUMERIC_DIRECTIONS[new_direction]
        return new_numeric_direction

    def consume(self, snake):
        """
        This method reverses snake's position
        and sets it's direction to opposite.

        argument:
            snake: snake class instance.
        """

        if len(snake.position)==1:
            snake.change_direction(ReverseTreat.DIRECTIONS[snake.direction])
            return

        new_numeric_direction=self.get_opposite_direction(snake.position)
        new_position = snake.position[::-1]
        snake.set_position(new_position)
        snake.change_direction(new_numeric_direction)
