import sqlite3

def get_users():
    with sqlite3.connect("untitled.db") as conn:
        cursor = conn.cursor()
        users = cursor.execute('''select * from users''')
        return users.fetchall()

def post_users():
    with sqlite3.connect("untitled.db") as conn:
        cursor = conn.cursor()
        users = cursor.execute('''insert into Users(?) values(?), **args''')
        return users.fetchall()


# conn = sqlite3.connect("untitled.db")
#
# # with conn:
# #     conn.execute('''insert into Users(username, email, password, age, city)
# #      values("kevin", "s@kevin.com", "12345", "10", "Berdyansk")''')
# # with conn:
# #     conn.execute('''insert into Users(username, email, password, age, city)
# #      values("phibi", "s@phibi.com", "12345", "60", "New York")''')
#
# with conn:
#     curs = conn.cursor()
#     # curs.execute('''select * from users where age between 25 and 60''')
#     # curs.execute('''select * from users limit 2''')
#     curs.execute('''select * from users''')
#     # curs.execute('''delete from users where email like "%i.com"''')
#     # curs.execute('''select * from users where email like "%.com"''')
#     # curs.execute('''select * from users where city = "Berdyansk" or age > 25''')
#     # curs.execute('''select * from users''')
#     # curs.execute('''select distinct username, email, age, city from users''')
#     print(curs.fetchall())