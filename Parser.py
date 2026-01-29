import json
from Task import MyTask

class Parser:
    def ParseText(self, respText):
        todoDict = json.loads(respText)
        return todoDict["title"]
    def ParseToObject(self, respText):
        todoDict = json.loads(respText)
        myTask = MyTask()
        myTask.id = todoDict["id"]
        myTask.title = todoDict["title"]
        myTask.completed = todoDict["completed"]
        myTask.userId = todoDict["userId"]
        return myTask