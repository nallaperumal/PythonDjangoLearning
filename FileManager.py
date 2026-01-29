class FileManager:
    def SaveToFile(self, txtToSave):
        try:
            with open("data.txt", "w") as myfile:
                myfile.write(txtToSave)            
        except IOError as e:
            print(f"error: {e}")

# https://meet.google.com/jaa-zuuf-snb            