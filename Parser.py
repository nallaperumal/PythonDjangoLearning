import json

class Parser:
    def ParseText(self, respText):
        todoDict = json.loads(respText)
        return todoDict["title"]