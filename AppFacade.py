class IrctctClass:
    def PerformLogin(self):
        print("login using name and pass")
    def LookForTrain(self, src, dst, type):
        print(f"Look for train from {src} to {dst} of type: {type}")
    def BookTicket(self, isTicketAvailable):
        if isTicketAvailable:
            print("Book Ticket")
        else:
            print("sorry go by bus")

class RedBus:
    def BookTickets(self):
        irctcProxy = IrctctClass()
        irctcProxy.PerformLogin()
        irctcProxy.LookForTrain("MAS","Vizag", "2nd ac")
        irctcProxy.BookTicket(True)

redBusFacadeInstance = RedBus()
redBusFacadeInstance.BookTickets()
#  irctcTrainObj = IrctctClass()
# irctcTrainObj.PerformLogin()
# irctcTrainObj.LookForTrain("MAS", "Vizag","3rd AC")
# irctcTrainObj.BookTicket(True)