from entities.default_treat import DefaultTreat
from entities.default_treat import DefaultTreat
from entities.matrix_element import MatrixElement
new_treat=MatrixElement(DefaultTreat(-2),"treat",1,1,-2)

class FloodTreat:
    #Instance of this class spawns a snake-length-reducing candy in every second
    #matrix position.
    def __init__(self):
        pass
    def consume(self, game):
        matrix_copy=[row[:] for row in game.game_matrix[:]]
        for row_index, row in enumerate(matrix_copy):
            new_row = list(enumerate(row))[::2]
            if row_index%2==0:
                new_row=list(enumerate(row))[1::2]
            for column_index, element in new_row:
                if element.type!="snake":
                    matrix_copy[row_index][column_index]=new_treat
        game.set_game_matrix(matrix_copy)



