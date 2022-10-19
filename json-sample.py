import json

user = ""

try:
    with open("sample.json","r") as fh:
        user = json.load(fh)
        
except IOError:
    pass

print("old user: ",user)

try:
    with open("sample.json","w") as fh:
        user["name"] = "Cloud"
        json.dump(user,fh)
        
except IOError:
    pass

print("new user: ",user)
