import sqlite3
import datetime

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE IF NOT EXISTS alunos (matricula TEXT PRIMARY KEY, nome TEXT, senha TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS respostas (id INTEGER PRIMARY KEY autoincrement, matricula TEXT, exercicio TEXT, pontos INTEGER, data DATETIME)')

try:
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO alunos (matricula, nome, senha) VALUES (?,?,?)",('1234', 'Henrique', '123123') )
        con.commit()
        print("Record successfully added")
except Exception as ex:
    print(ex)
    con.rollback()
    print("error in insert operation")

finally:
    con.close()

try:
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO respostas (matricula, exercicio, pontos, data) VALUES (?,?,?,?)",('123', 'Ex1', '1', datetime.datetime.now()))
        con.commit()
        print("Record successfully added")
except Exception as ex:
    print(ex)
    con.rollback()
    print("error in insert operation")

finally:
    con.close()


con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row

cur = con.cursor()
cur.execute("select * from alunos")

rows = cur.fetchall(); 
for row in rows:
    print(row["nome"], row["matricula"], row["senha"])

con.close()

con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row

cur = con.cursor()
cur.execute("select * from respostas")

rows = cur.fetchall(); 
for row in rows:
    print(dict(row))

con.close()


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv

# for user in query_db('select * from users'):
#     print user['username'], 'has the id', user['user_id']

conn.close()