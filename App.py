import time 
from abc import ABC, abstractmethod
class Travel(ABC):
    @abstractmethod
    def LastStop():
        pass
    def drive(self):
        for stop in self._stops:
            print(f"...next stop is {stop}")
            time.sleep(1.2)
        self.LastStop()    
class Bus19(Travel):
    def __init__(self):
        self._stops = ["stop1", "stop2", "stop3"]
    def LastStop(self):
        print("last stop is stop3")
class BusMA(Travel):
    def __init__(self):
        self._stops = ["stopA", "stopB", "stopC"]
    def LastStop(self):
        print("last stop is stopC")
class BlueMetro(Travel):
    def __init__(self):
        self._stops = ["Wimco nagar", "nandanam", "Airport"]
    def drive(self): 
        print("doors will open on the left side")
        super().drive()
        print("doors are closing..")
    def LastStop(self):
        print("last stop is Airport")    
myBus = Bus19()
myBus.drive()
myMetro = BlueMetro()
print("---------")
myMetro.drive()
# myBus.__Test1() #will not work
# myBus._TestProtected() #will not work