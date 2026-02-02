import inspect
import requests

# print(dir(requests))
# print(callable(requests.get))
print(inspect.signature(requests.get))
result = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(result)
# print(dir(result))
print(result.text)
print(result.json)