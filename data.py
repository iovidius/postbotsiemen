import json

# Get data from JSON file
def getData(attr):
    with open('data/data.json', 'r') as file:
        data = json.load(file)
        return data[attr]

def setData(attr, val):
    with open('data/data.json', 'r+') as file:
        data = json.load(file)
        data[attr] = val
        file.seek(0)  
        json.dump(data, file)
        file.truncate()