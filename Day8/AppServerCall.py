import requests
import json
from SaveData import SaveData

class SaveToServer(SaveData):
    def AddData(self, params:str) -> str:
        url = "https://jsonplaceholder.typicode.com/posts/"
        payload = params
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.text
    def UpdateOrReplaceData(self, params:str) -> str:
        url = "https://jsonplaceholder.typicode.com/posts/3"
        payload = params
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
