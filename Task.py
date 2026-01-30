class MyTask():
    __userId = 0
    id = 0
    __title = ""
    completed = False
    def setUser(self, userId):
        if userId > 0:
            self.__userId = userId
    def setTitle(self, title):
        self.__title = title
    # .. for other properties
