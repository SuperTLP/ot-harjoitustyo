class Score:
    """This class is responsible for saving and retreiving score-related data."""
    def __init__(self, database):
        """self.database is the database where scores are stored."""
        self.database=database

    def new(self, name, score, difficulty):
        """This method inserts new score into database with given name,score and difficulty."""
        cur = self.database.cursor()
        cur.execute("insert into scores (name, score, difficulty) values (?, ?, ?)",
        [name, score, difficulty])
        self.database.commit()

    def all(self):
        """This method fetches all scores from the database."""
        cur=self.database.cursor()
        data = cur.execute("select * from scores order by score desc;").fetchall()
        return data
