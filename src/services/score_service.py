from entities.score import Score

class ScoreService:
    def __init__(self,score_repository):
        """
        arguments:
            score_repository: instance of ScoreRepository class.
        """

        self.score_repository=score_repository

    def new(self, name, points, difficulty):
        """
        creates new score

        arguments:
            name: name of the player
            points: points the player achieved
            difficulty: difficulty level the score was gotten on.
        """

        self.score_repository.new(name, points, difficulty)

    def all(self):
        """
        returns:
            Score class instances for all scores in highest to lowest order.
        """

        data = self.score_repository.all()
        scores = [Score(x[0],x[1],x[2]) for x in data]
        return scores
