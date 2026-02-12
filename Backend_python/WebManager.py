import requests
class WebManager():
    def makeRequest(self, taskID):
        resp = requests.get(f"https://jsonplaceholder.typicode.com/todos/{taskID}")
        return resp.text