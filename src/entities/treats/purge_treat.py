from entities.matrix_element import MatrixElement


class PurgeTreat:
    #Class representing a single treat that deletes all treats from game matrix.

    def __init__(self):
        self.empty=[[MatrixElement(None, "empty", 0, 0, "")]*14 for i in range(0,9)]

    def consume(self, game_matrix):
        """
        This method removes all treats from game_matrix.

        args:
            game_matrix: Instance of GameMatrix class.
        """

        new_matrix=[row[:] for row in self.empty[:]]
        game_matrix.set_matrix(new_matrix)
