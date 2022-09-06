from database import DataBase
import json

dbase = input("Please input patch to database: ")
db = DataBase(dbase)
running = True

while running:
    x=input("Command:")
    if x == "getTable":
        y = input("Key:")
        db.getTable(y)
    elif x == "createTable":
        y = input("key: ")
        z = json.loads(input("Dictionary: "))
        db.createTable(y,z)
        db.write()
    elif x == "quit":
        running = False
    
