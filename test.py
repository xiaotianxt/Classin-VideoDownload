import json

with open("packages/1.json", "r") as f:
    jsonData = f.readline()

    text = json.loads(jsonData)
    print(text)

