import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_tbl = "create table if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_tbl)
create_tbl = "create table if not exists items (id INTEGER PRIMARY KEY, name text, price int)"
cursor.execute(create_tbl)
cursor.execute("insert into items values (NULL,?,?)",('pen',30))

connection.commit()
connection.close()
