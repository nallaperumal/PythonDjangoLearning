from WebManager import WebManager
from Parser import Parser
from FileManager import FileManager
webMan = WebManager()
resp = webMan.makeRequest()
fileMan = FileManager()
fileMan.SaveToFile(resp)
parser = Parser()
res = parser.ParseText(resp)
print(res)