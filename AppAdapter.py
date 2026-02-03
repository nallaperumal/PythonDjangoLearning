from abc import ABC, abstractmethod

class USBCPhone(ABC):
    @abstractmethod
    def recharge(self):
        pass

class ACPowerSocket:
    def provide_220V_power(self) -> str:
        return "Supply 220v AC power"

class ACPowerToUSBCAdapter(USBCPhone):    
    def __init__(self, powerSrc:ACPowerSocket):
        self.powerSrc = powerSrc

    def recharge(self):
        power = self.powerSrc.provide_220V_power()
        print(f"converting the {power} to DC")    

ACPower = ACPowerSocket()
adapter = ACPowerToUSBCAdapter(ACPower)
adapter.recharge()        