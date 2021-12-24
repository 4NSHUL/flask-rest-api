import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

crete_table = "create table Users (id int,username text,password text)"
cursor.execute(crete_table)

user = (1, "anshul", 'qwerty')
insert_q = "insert into Users values (?,?,?)"

users = [(2, "hey", 'zed'),
         (3, "too", 'ded'),
         (4, "kite", 'pep')]
cursor.executemany(insert_q,users)
select_q = "select * from Users"
result = cursor.execute(select_q)
for _ in result:
    print(_)
connection.commit()
connection.close()

