from database import DataBase

db = DataBase('./test.json')
db.createTable('students', {'username':'nhenderson22'})
db.write()
