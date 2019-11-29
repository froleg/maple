
  
from ZODB import FileStorage, DB
for key in root.keys():
  print('%s => %s' % (key.ljust(10), root[key]))
  
storage = FileStorage.FileStorage(r'E:\Users\Олег\Documents\hello\.vscode\mydb.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
object1 = (1, 'spam', 4, 'YOU')
object2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
object3 = {'name': ['Bob', 'Doe'],'age': 42,'job': ('dev', 'mgr')}
root['mystr'] = 'spam' * 3
root['mylist'] = object2
root['mydict'] = object3
print( root['mydict'])
import transaction
transaction.commit()
storage.close()