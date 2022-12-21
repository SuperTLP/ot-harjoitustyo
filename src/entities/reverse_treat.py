direction_map={
    0:2,
    1:3,
    2:0,
    3:1
}
direction_from_coordinates={
    "[-1, 0]":2,
    "[0, 1]":3,
    "[1, 0]":0,
    "[0, -1]":1
}
class ReverseTreat:
    """Instance of this class reverses snake's position when consumed.
    This means the snake will continue in opposite direction."""
    def __init__(self):
        pass
    def consume(self, game,snake):
        """This method reverses snake's position list
        and sets game's direction to opposite."""
        if len(snake.position)==1:
            game.change_direction(direction_map[game.direction])
            return
        new_direction_y=snake.position[1][0]-snake.position[0][0]
        new_direction_x=snake.position[1][1]-snake.position[0][1]
        new_direction=str([new_direction_y,new_direction_x])
        new_position = snake.position[::-1]
        snake.set_position(new_position)
        game.change_direction(direction_from_coordinates[new_direction])
