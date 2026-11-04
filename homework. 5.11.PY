class acount:
    def __init__(self):
        self.__pin=12345
    def store(self):
        print("please store the pin: {}".format (self.__pin))
    def setpin(self,pin):
        self.__pin = pin

c= acount()
c.store()

c.__pin=12543
c.setpin(123543)
c.store

