import json
from Task import MyTask

class Parser:
    def ParseText(self, respText):
        todoDict = json.loads(respText)
        return todoDict["title"]
    def ParseToObject(self, respText):
        todoDict = json.loads(respText)
        myTask = MyTask()        
        myTask.setTitle(todoDict["title"])
        myTask.setUser(todoDict["userId"])
        myTask.id = todoDict["id"]
        myTask.completed = todoDict["completed"]        
        return myTask