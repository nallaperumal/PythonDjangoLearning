class Processor:
    def __init__(self, model:str, cores:str):
        self.model = model
        self.cores = cores
    def process_data(self):
        print(f"Process the data with {self.cores}")
class Storage:    
    def __init__(self, capcity:int):
        self.capacity = capcity
    def save_data(self):
        print(f"saving the data {self.capacity} GB")    
class Computer:
    def __init__(self, model_name:str, cpu:Processor, disk:Storage):
        self.model_name = model_name
        self.cpu = cpu
        self.disk = disk
    def work(self) -> str:
        print(f"system with cpu {self.cpu.cores} and memory {self.disk.capacity}") 
        return "work is going on"   
cpu = Processor("intel i5", "4")
myStorage = Storage(500) 
myComp = Computer("Programming laptop",cpu, myStorage)
myComp.work()
