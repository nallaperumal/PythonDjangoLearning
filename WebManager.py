import requests
class WebManager():
    def makeRequest(self):
        resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        return resp.text