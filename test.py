import json

file = open('test.json','w')
dict = {'Test22':'Test'}

data = json.dumps(dict,indent = 4)
file.write(data)

file.close()
