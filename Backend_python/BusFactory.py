from Buses.Bus19 import Bus19
from Buses.BusMA import BusMAA2

class BusFactory:
    @staticmethod
    def CreateBus(name):
        if name == "19":
            return Bus19()
        elif name == "MAA2":
            return BusMAA2()
