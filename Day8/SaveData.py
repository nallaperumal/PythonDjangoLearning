from abc import ABC, abstractmethod
class SaveData(ABC):
    @abstractmethod
    def AddData(self, data:str):
        pass
    @abstractmethod
    def UpdateOrReplaceData(self, data:str):
        pass