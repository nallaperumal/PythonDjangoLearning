from WebManager import WebManager
from Parser import Parser
from FileManager import FileManager
webMan = WebManager()
fileMan = FileManager()
parser = Parser()

for i in range(1,10):
    resp = webMan.makeRequest(i)
    fileMan.SaveToFile(resp)
    #res = parser.ParseText(resp)
    res = parser.ParseToObject(resp)
    print(res.title)