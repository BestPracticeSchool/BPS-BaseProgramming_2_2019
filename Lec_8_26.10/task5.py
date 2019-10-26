#JSON --- JavaScriptObjectNotation
import json 
data = {
    "passengerId":"152",
    "uniqueNumber": "1996",
    "words" : [
        "lol",
        "kek",
        "python"
    ]
}

with open("my_data.json", "w") as md:
    json.dump(data, md)

with open("my_data.json", "r") as rd:
    inside = json.load(rd)
    
print(inside)
