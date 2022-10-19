import json

def readJsonFile(filename):
    data = ""

    try:
        with open(filename) as fh:
            data = json.load(fh)
    except IOError: # file is not existed
        return False
    except json.decoder.JSONDecodeError:
        return ""
    
    return data
