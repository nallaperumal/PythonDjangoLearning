from WebManager import WebManager
from Parser import Parser
webMan = WebManager()
resp = webMan.makeRequest()
parser = Parser()
res = parser.ParseText(resp)
print(res)