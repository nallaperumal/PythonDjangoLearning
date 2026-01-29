import requests

resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(resp.text)