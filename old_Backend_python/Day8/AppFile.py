from SaveData import SaveData
from AppServerCall import SaveToServer
import json
class SaveToFile(SaveData):
    def __init__(self):
        self.file_name = "test.txt"
    def AddData(self, data):
        with open(self.file_name, "a") as myFile:
            myFile.write(data)
    def UpdateOrReplaceData(self, data):
        with open(self.file_name, "w") as myFile:
            myFile.write(data)
paramsToInsert =  {
        "title": "foo",
        "body": "bar",
        "userId": 1        }
dictionStr = json.dumps(paramsToInsert)
fileAcceesObj = SaveToFile()
fileAcceesObj.AddData(dictionStr)
serverAccessObj = SaveToServer()
serverAccessObj.AddData(dictionStr)
