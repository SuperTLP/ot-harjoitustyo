class Score:
    def __init__(self, database):
        self.database=database
    def new(self, name, score):
        cur = self.database.cursor()
        cur.execute("insert into scores (name, score) values (?, ?)", [name, score])
        self.database.commit()
    def all(self):
        cur=self.database.cursor()
        data = cur.execute("select * from scores order by score desc;").fetchall()
        return data

    