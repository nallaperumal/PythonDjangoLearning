import time 
from BusFactory import BusFactory

# busFact = BusFactory()
# busFact.CreateBus("19")

bus19 = BusFactory.CreateBus("19")
bus19.drive()

maabus = BusFactory.CreateBus("MAA2")
maabus.drive()

# aReal19RandonBus = bus19()
# aReal19RandonBus.drive()
# print("....")
# maa2Bus = busMAA2()
# maa2Bus.drive()