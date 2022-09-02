from unicodedata import name 
import os
import json

class DataBase():
    def __init__(self, path):
        self.path = path
        if os.stat(self.path).st_size != 0:
            with open(self.path) as f:
                self.current = json.load(f)
        else:
            self.current = {}
# Creates a table that can be added to our database
    def createTable(self,key,data):
        x = {str(key): data}
        self.current.update(x)
# Writes to the database    
    def write(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.current))
# Converts the working dictionary to python    
    def convertToJson(self):
        jsonObj = json.dumps(self.current)
        return jsonObj
# Used to update a tables data (can only handle a table)
    def updateData(self, key, newData):
        self.current[key] = newData
     
