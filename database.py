from unicodedata import name


import os

class DataBase():
    def __init__(self, name):
        self.name = name
    
    def addKey(self, key, value):
        with open(str(key) + '.txt' , 'w') as f:
            f.write(str(value))
    
    def getKey(self, key):
        with open(str(key) + '.txt','r') as f:
            print(f.read())