from unicodedata import name 
import os
import json

class DataBase():
    def __init__(self, path):
        self.path = path
        self.current = open(self.path)
    #initializes a new table in the database 
    def addData(self,data):
       temp = json.dumps(data)
       print(temp)
       with open(self.path, 'w') as f:
           f.write(temp)
# Creates a table that can be added to our database
    def createTable(self,key,data):
        x = {str(key): data}
        jsonObj = json.dumps(x)
        return jsonObj
    
    def write(self,jsonObj):
        with open(self.path, 'w') as f:
            f.write(jsonObj)

    def removeData(key):
        pass
