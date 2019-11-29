import ZODB, ZODB.FileStorage, zo2, BTrees.OOBTree

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root
root.accounts = BTrees.OOBTree.BTree()
root.accounts['account-1']=zo2.Account()
ac2=zo2.Account()
ac2.deposit(30)
root.accounts['account-2']=ac2
print(root.accounts["account-2"].balance)
ac2.deposit(40)
print(root.accounts["account-2"].balance)