import requests
import json

class DataUpdate:
    def AddData(self, params) -> str:
        url = "https://jsonplaceholder.typicode.com/posts/"
        payload = json.dumps(params)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        return response.text
    def UpdateData(self, params) -> str:
        url = "https://jsonplaceholder.typicode.com/posts/"
        payload = json.dumps(params)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        # print(response.text)
        return response.text

class MongoDataUpdate:
    def AddData(self, param):
        print("insert data into mongo")
    def UpdateData(self, param):
        print("update data into mongo")    
dataUpdate = DataUpdate()
# dataUpdate = MongoDataUpdate()
paramsToInsert =  {
        "title": "foo",
        "body": "bar",
        "userId": 1
        }
res = dataUpdate.AddData(paramsToInsert)
print(res)
res = dataUpdate.UpdateData(paramsToInsert)
# res = dataUpdate.DeleatData(2)
print(res)