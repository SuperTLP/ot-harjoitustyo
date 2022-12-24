class Score:

    #Class representing a single score gotten by a player.

    def __init__(self, name, score, difficulty):
        """
        arguments:
            name: name of the player
            score: the score gotten by the player
            difficulty: the difficulty level the score was gotten on.
        """

        self.name=name
        self.score=score
        self.difficulty=difficulty
