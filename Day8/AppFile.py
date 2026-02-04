import datetime
file_name = "test.txt"
conten_tosave = ["Hi today is wednes", "we tried numpy"]
with open(file_name, "w") as myFile:
    myFile.write(f"{datetime.datetime.now()}: starting to write\n")
    for line in conten_tosave:
        myFile.write(f"{datetime.datetime.now()}:{line}\n")
with open(file_name, "a") as myFile:
    myFile.write("new line appended NOT REPLACED old one\n")
try:
    with open(file_name, "r") as myFile:
        for line in myFile:
            print(line)
except FileNotFoundError:
    print("file not found error")

# class SaveToFile:
#     def AddData(self, data): #file in append mode
#         ...
#     def UpdateData(self, data): # file in write mode
#         ...