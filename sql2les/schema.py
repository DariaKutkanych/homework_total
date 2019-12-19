import sqlite3

conn = sqlite3.connect("dec17.db")

with conn:
    conn.execute('''INSERT INTO comments (data, userid, postid)
    values("hot", 2, 3)
    ''')
# #     conn.execute('''create table Users (
# #     id integer unique primary key autoincrement,
# #     username varchar(50) not null,
# #     email varchar(50) not null
# #     )
# # ''')

#     conn.execute('''create table posts (
#     id integer unique primary key autoincrement,
#     data TEXT,
#     userid INTEGER,
#     FOREIGN KEY (userid) REFERENCES users (id)
#     )
# ''')
#     conn.execute('''CREATE TABLE comments (
#     id integer primary key autoincrement,
#     data TEXT,
#     userid INTEGER,
#     postid INTEGER,
#     FOREIGN KEY (userid) REFERENCES users (id),
#     FOREIGN KEY (postid) REFERENCES posts (id)
#   ) ''')