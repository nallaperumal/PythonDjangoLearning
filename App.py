import time 

class Travel:
    def drive(self):
        for stop in self.stops:
            print(f"...next stop is {stop}")
            time.sleep(1.2)
class Bus19(Travel):
    def __init__(self):
        self.stops = ["stop1", "stop2", "stop3"]
class BusMA(Travel):
    def __init__(self):
        self.stops = ["stopA", "stopB", "stopC"]

class BlueMetro(Travel):
    def __init__(self):
        self.stops = ["Wimco nagar", "nandanam", "Airport"]
    def drive(self): 
        print("doors will open on the left side")
        super().drive()
        print("doors are closing..")
myBus = Bus19()
myBus.drive()
myMetro = BlueMetro()
print("---------")
myMetro.drive()
# myBus.__Test1() #will not work
# myBus._TestProtected() #will not work