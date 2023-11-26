import json
with open('configjson.json',encoding='utf-8') as f:
    data = json.load(f)
    print(data)