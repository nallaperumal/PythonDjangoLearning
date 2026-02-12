import time
class Bus19():
    def __init__(self):
        self.stops = ["ChennaiOne", "Karapakkam", "Sholinganallur", "Kilambakkam" ]
    def drive(self):
        for stop in self.stops:
            print(f"... next stop is: {stop}")
            time.sleep(1.2) # DO NOT use in production