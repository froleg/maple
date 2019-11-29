import sqlite3
conn = sqlite3.connect('E:/Users/Олег/Documents/hello/.vscode/dbase1.db')
curs = conn.cursor()
tblcmd = 'create table people (name char(30), job char(10), pay int(4))'
curs.execute(tblcmd)
curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
print(curs.rowcount)
print(sqlite3.paramstyle)
curs.executemany('insert into people values (?, ?, ?)', [ ('Sue', 'mus', '70000'),('Ann', 'mus', '60000')])