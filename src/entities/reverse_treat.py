direction_map={
    0:2,
    1:3,
    2:0,
    3:1
}
numeric_direction_from_coordinates={
    "[-1, 0]":2,
    "[0, 1]":3,
    "[1, 0]":0,
    "[0, -1]":1
}
class ReverseTreat:
    """Instance of this class reverses snake's position and direction
    when consumed. This means the snake will continue in opposite direction."""
    def __init__(self):
        pass

    def get_opposite_direction(self,position):
        """This method calculates what the snake's direction should be
        after it's reversed"""
        new_direction_y=position[1][0]-position[0][0]
        new_direction_x=position[1][1]-position[0][1]
        new_direction=str([new_direction_y,new_direction_x])
        new_numeric_direction=numeric_direction_from_coordinates[new_direction]
        return new_numeric_direction

    def consume(self, snake):
        """This method reverses snake's position list
        and sets it's direction to opposite."""
        if len(snake.position)==1:
            snake.change_direction(direction_map[snake.direction])
            return
        new_numeric_direction=self.get_opposite_direction(snake.position)
        new_position = snake.position[::-1]
        snake.set_position(new_position)
        snake.change_direction(new_numeric_direction)
