import datetime

class SaveToFile:
    def __init__(self):
        self.file_name = "test.txt"
    def AddData(self, data): #file in append mode
        with open(self.file_name, "a") as myFile:
            myFile.write(data)
    def UpdateData(self, data): # file in write mode
        with open(self.file_name, "w") as myFile:
            myFile.write(data)

fileAcceesObj = SaveToFile()
conten_tosave = ["Hi today is wednes", "we tried numpy"]
fileAcceesObj.UpdateData(str(conten_tosave))
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

