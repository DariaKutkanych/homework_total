import sqlite3


def get_statistics():
    with sqlite3.connect("dec17.db") as conn:
        users = conn.execute('''SELECT users.username, COUNT(posts.data) FROM users INNER JOIN posts
         ON users.id = posts.userid GROUP BY users.username ORDER BY COUNT(posts.data) DESC
                ''')
        return users.fetchall()


def get_comments(id_):
    with sqlite3.connect("dec17.db") as conn:
        users = conn.execute('''SELECT data FROM comments where userid=?''', str(id_))
    return users.fetchall()


def get_post_comments(id_):
    with sqlite3.connect("dec17.db") as conn:
        users = conn.execute('''SELECT data FROM comments where postid=?''', str(id_))
    return users.fetchall()


def get_posts_with_data(word):
    with sqlite3.connect("dec17.db") as conn:
        result = f'''SELECT data FROM posts where data LIKE "%{word}%"'''
        posts = conn.execute(result)
        return posts.fetchall()


def get_data(table, data=None):
    with sqlite3.connect("dec17.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = f'''select * from {table}'''
        if data:
            query = f'''select * from Posts where user_id = {str(data)}'''
        users = cursor.execute(query)
        result = users.fetchall()
        k = []

        for row in result:
            k.append(dict(row))

        return k


def post_data(table, data):

    v = tuple(data.values())
    k = tuple(data.keys())

    with sqlite3.connect('dec17.db') as conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        query = f'''insert into {table} {k} values {v}'''
        curs.execute(query)
