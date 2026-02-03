from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass
class SilverPrice:
    def __init__(self):
        self._observers = []
        self._price = 0
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)    
    def notify(self):
        for observer in self._observers:
            observer.update(self._price)
    def setPrice(self, value):
        self._price = value
        self.notify()
class PotentialBuyer(Observer):
    def update(self, price):
        print(f"new price of silver is {price}")
silverPrice = SilverPrice()
srinivas = PotentialBuyer()
sriShankari = PotentialBuyer()
silverPrice.attach(srinivas)
silverPrice.attach(sriShankari)
silverPrice.setPrice(300)
silverPrice.detach(sriShankari)
silverPrice.setPrice(400)