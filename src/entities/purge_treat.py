class PurgeTreat:
    #Class representing a single treat that deletes all treats from game matrix.
    def __init__(self):
        pass

    def consume(self, game):
        """
        argument:
            game: instance of game class."""

        game.purge_candy()
    