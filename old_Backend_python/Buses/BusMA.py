import time
class BusMAA2():
    def __init__(self):
        self.stops = ["Airport", "Chromepet", "Vels University", "Thoraipakkam" ,"PTC" ]
    def drive(self):
        for stop in self.stops:
            print(f"... next stop is: {stop}")
            time.sleep(1.2) # DO NOT use in production