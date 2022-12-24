class ScoreRepository:
    """This class is responsible for saving and retreiving score-related data."""
    def __init__(self, database):
        """
        argument:
            database: the database where scores are stored."""
        self.database=database

    def new(self, name, score, difficulty):
        """
        This method inserts new score into database with given name,score and difficulty.

        Arguments:
            name: Name of the player
            score: The score the player got
            difficulty: the difficulty level the score was gotten on
        """

        cur = self.database.cursor()
        cur.execute("insert into scores (name, score, difficulty) values (?, ?, ?)",
        [name, score, difficulty])
        self.database.commit()

    def all(self):
        """
        This method fetches all scores from the database.

        returns:
            all scores from database as list of tuples.
        """

        cur=self.database.cursor()
        data = cur.execute("""select name, score, difficulty from scores
        order by score desc;""").fetchall()
        return data
