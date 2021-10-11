import os
import json
from flask import jsonify

def readJsonFiles(dataType, moduleName = ""):
    cur_path = os.path.dirname(__file__)

    if dataType == 'messages':
        fileDir = cur_path + "/../static/messages.json"
    elif dataType == 'operations':
        fileDir = cur_path + "/../static/operations.json"
    elif dataType == 'results':
        fileDir = cur_path + "/../static/results.json"
    elif dataType == 'manifest':
        fileDir = cur_path + "/../static/manifest.json"
    else:
        return ''

    with open(fileDir, 'r') as jsonfile:
        dataJson = json.loads(jsonfile.read())

    if moduleName:
        return dataJson[moduleName]
    else:
        return dataJson

if __name__ == "__main__":
    pass