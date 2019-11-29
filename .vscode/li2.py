import sqlite3
conn = sqlite3.connect('E:/Users/Олег/Documents/hello/.vscode/dbase1.db')
curs = conn.cursor()
rows = [['Tom', 'mgr', 100000],['Kim', 'adm', 30000],['pat', 'dev', 90000]]
for row in rows:
    curs.execute('insert into people values (? , ?, ?)', row)
conn.commit()
curs.execute('select * from people')
print(curs.fetchall())
