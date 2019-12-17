import sqlite3


def get_data(table, data=None):
    with sqlite3.connect("untitled.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = '''select * from {}'''.format(table)
        if data:
            query = '''select * from Posts where user_id = {}'''.format(str(data))
        users = cursor.execute(query)
        result = users.fetchall()
        k = []

        for row in result:
            k.append(dict(row))

        return k


def post_data(table, data):

    v = tuple(data.values())
    k = tuple(data.keys())

    with sqlite3.connect('untitled.db') as conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        query = '''insert into {} {} values {}'''.format(table, k, v)
        curs.execute(query)
