class PurgeTreat:
    #Instance of this class removes all treats from the game matrix.
    def __init__(self):
        pass

    def consume(self, game):
        """
        argument:
            game: instance of game class."""

        game.purge_candy()
    