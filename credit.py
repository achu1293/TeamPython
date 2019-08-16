class cc:
    def __init__(self):
        newcardholder=input("name")
        limit=int(input("limit"))
    def getBal(self):
        return self.__bal
    def getCredit(self):
        return self.__climit
    def setBal(self):
        self.__bal=int(input("Enter the balance"))
    def setCredit(self):
        self.__climit=int(input("Enter the limit"))
obj=cc()
obj.setBal()
obj.setCredit()
print(obj.getBal())
print(obj.getCredit())
