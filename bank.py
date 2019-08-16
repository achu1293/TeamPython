'''
Created on Sep 11, 2018

@author: Archana
'''
class bank:
    balance=1000
    def __init__(self,name,type,id):
        self.name=name
        self.type=type
        self._id=id
    def deposit(self,damt):
        self.__damt=damt
        self.balance+=self.__damt
        print("balance is",self.balance)
    def withdrawl(self,wamt):
        self.__wamt=wamt
        self.balance-=self.__wamt
        print("balance is",self.balance)
obj=bank("achu","saving",232434)
obj.deposit(2000)
obj.withdrawl(500)