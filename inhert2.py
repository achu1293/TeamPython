'''
Created on Sep 12, 2018

@author: Archana
'''

"MULTIPLE"
class SavingAcc:
    def __init__(self,accno,minbal):
        self.Saccno=accno
        self.Sminbal=minbal
    def display1(self):
        print("saving")
        print(self.Saccno,self.Sminbal)
class CurrentAcc:
    def __init__(self,accno,minbal):
        super().__init__(accno,minbal)
        super().display1()
        self.Caccno=accno
        self.Cminbal=minbal
    def display1(self):
        print("current")
        print(self.Caccno,self.Cminbal)
class Person(CurrentAcc,SavingAcc):
    def __init__(self,name,accno,minbal):
        super().__init__(accno,minbal)
    def display(self):
        super().display1()
obj=Person("shameer",1234,1000)
obj.display()