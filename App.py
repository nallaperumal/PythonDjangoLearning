import time 

class bus19():
    def __init__(self):
        self.stops = ["ChennaiOne", "Karapakkam", "Sholinganallur", "Kilambakkam" ]
    def drive(self):
        for stop in self.stops:
            print(f"... next stop is: {stop}")
            time.sleep(1.2) # DO NOT use in production

class busMAA2():
    def __init__(self):
        self.stops = ["Airport", "Chromepet", "Vels University", "Thoraipakkam" ,"PTC" ]
    def drive(self):
        for stop in self.stops:
            print(f"... next stop is: {stop}")
            time.sleep(1.2) # DO NOT use in production

aReal19RandonBus = bus19()
aReal19RandonBus.drive()
print("....")
maa2Bus = busMAA2()
maa2Bus.drive()