from entities.treats.default_treat import DefaultTreat
from entities.matrix_element import MatrixElement

class FloodTreat:
    """
    class representing a single treat that spawns snake length reducing treats
    """

    new_treat=MatrixElement(DefaultTreat(-2),"treat",1,1,-2)

    def __init__(self):
        pass

    def consume(self, game):
        """
        This method replaces every second element on every row of the game's
        game_matrix with defaultTreat element with effect of -2.

        argument:
            game: Instance of Game class.
        """

        matrix_copy=[row[:] for row in game.game_matrix[:]]
        for row_index, row in enumerate(matrix_copy):

            new_row = list(enumerate(row))[::2]
            if row_index%2==0:
                new_row=list(enumerate(row))[1::2]

            for column_index, element in new_row:
                if element.type!="snake":
                    matrix_copy[row_index][column_index]=FloodTreat.new_treat
        game.set_game_matrix(matrix_copy)
