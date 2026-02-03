import requests
import json

class DataUpdate:
    def makeRequest(self, url:str) -> str:
        # url = "https://jsonplaceholder.typicode.com/posts/"
        payload = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        return response.text

dataUpdate = DataUpdate()
res = dataUpdate.makeRequest("https://jsonplaceholder.typicode.com/posts/")
print(res)