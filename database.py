import os
import json
from os.path import exists

class DataBase():
    def __init__(self, path):
        self.path = path
        self.exists = True
        try:
            if os.stat(self.path).st_size != 0:
                with open(self.path) as f:
                    self.current = json.load(f)
            else:
                self.current = {}
        except:
            print("File not found")
            self.exists = False
# Creates a table that can be added to our database
    def createTable(self,key,data):
        x = {str(key): data}
        self.current.update(x)
# Useful when new data is being created if you want to manipulate existing data then just access it via dictionary
# syntad (self.current[key][key] = new)
    def updateTable(self,key, data):
        self.current[key].update(data)
# Writes to the database    
    def write(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.current))
# Useful for my shell and CLI its probably easier to just use dictionary keys
# Readability may be a factor I guess
    def getTable(self, key):
        return self.current[key]

     
