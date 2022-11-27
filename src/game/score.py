class Score:
    def __init__(self, database):
        self.database=database
    def new(self, score, name):
        cur = self.database.cursor()
        cur.execute("insert into scores (name, score) values (?, ?)", [name, score])
        self.database.commit()
    