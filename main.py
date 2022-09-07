from database import DataBase

db = DataBase('./test.json')
db.createTable('test', {'tes1': 'test2'})
db.updateTable('students',{'pass':'1234'})
db.write()
