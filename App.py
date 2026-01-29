from WebManager import WebManager
from Parser import Parser
from FileManager import FileManager
webMan = WebManager()
resp = webMan.makeRequest(12)
fileMan = FileManager()
fileMan.SaveToFile(resp)
parser = Parser()
#res = parser.ParseText(resp)
res = parser.ParseToObject(resp)
print(res)