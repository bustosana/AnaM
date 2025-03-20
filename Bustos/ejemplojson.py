import json 

with open('ejemplojson.py', 'w', encoding='utf-8') as json: 
    data = json.load(json)
    
print(data)
print(type(data))
