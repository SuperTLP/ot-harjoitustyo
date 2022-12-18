import sqlite3
db = sqlite3.connect("src/database.db")
cur = db.cursor()
cur.execute("drop table if exists scores")
cur.execute("create table scores (id integer primary key autoincrement, name text, score int,difficulty text)")
db.commit()