class PurgeTreat:
    def __init__(self, effect):
        self.effect=effect
    def consume(self, game):
        game.purge_candy()

