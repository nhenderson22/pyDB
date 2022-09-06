from database import DataBase

db = DataBase('./test.json')
db.createTable('test', {'tes1': 'test2'})
db.write()
