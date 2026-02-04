conten_tosave = ["Hi today is wednes", "we tried numpy"]

with open("test.txt", "w") as myFile:
    myFile.write("starting to write\n")
    for line in conten_tosave:
        myFile.write(line + "\n")

with open("test.txt", "a") as myFile:
    myFile.write("new line appended NOT REPLACED old one\n")

try:
    with open("test.txt", "r") as myFile:
        for line in myFile:
            print(line)
except FileNotFoundError:
    print("file not found error")