import datetime
from abc import ABC, abstractmethod

class SaveData(ABC):
    @abstractmethod
    def AddData(self, data:str):
        pass
    @abstractmethod
    def UpdateOrReplaceData(self, data:str):
        pass

class SaveToFile(SaveData):
    def __init__(self):
        self.file_name = "test.txt"
    def AddData(self, data): #file in append mode
        with open(self.file_name, "a") as myFile:
            myFile.write(data)
    def UpdateOrReplaceData(self, data): # file in write mode
        with open(self.file_name, "w") as myFile:
            myFile.write(data)

fileAcceesObj = SaveToFile()
conten_tosave = ["Hi today is wednes", "we tried numpy"]
fileAcceesObj.UpdateOrReplaceData(str(conten_tosave))
fileAcceesObj.AddData("This data does not overrides but gets appended")

# with open(file_name, "w") as myFile:
#     myFile.write(f"{datetime.datetime.now()}: starting to write\n")
#     for line in conten_tosave:
#         myFile.write(f"{datetime.datetime.now()}:{line}\n")
# try:
#     with open(file_name, "r") as myFile:
#         for line in myFile:
#             print(line)
# except FileNotFoundError:
#     print("file not found error")

