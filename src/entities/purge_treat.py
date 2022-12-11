class PurgeTreat:
    #Instance of this class removes all treats from the game matrix.
    def __init__(self):
        self.effect="?"
        self.tier=2
        self.type="matrix_treat"
        self.points=20
    def consume(self, game):
        game.purge_candy()
    