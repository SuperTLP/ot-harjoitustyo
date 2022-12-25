from entities.matrix_element import MatrixElement

class GameMatrix:

    """
    GameMatrix class is responsible for saving the location of treats and other elements
    on a matrix.

    START is empty matrix used to initialize game.
    """

    START=[[MatrixElement(None,"empty",0,0,0)]*14 for i in range(0, 9)]

    def __init__(self):
        """
        attributes:
            self.matrix is the situation of the game in matrix form.
            self.coordinates is list of coordinates [y, x] on the matrix.
        """

        self.matrix= [x[:] for x in GameMatrix.START[:]]
        self.coordinates=[]

        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                self.coordinates.append([i, j])

    def set_matrix(self, matrix):
        """
        this method sets self.matrix to custom matrix. used by special treats.

        argument:
            matrix: new value for self.matrix
        """

        self.matrix=matrix

    def reset(self):
        """
        Resets matrix
        """

        self.matrix=[x[:] for x in GameMatrix.START[:]]
