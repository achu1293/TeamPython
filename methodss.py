'''
Created on Sep 2, 2018

@author: Archana
'''
import encap
class myclass:
    cv=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b,myclass.cv)
    @classmethod
    def c(cls,name):
        c=20
        print(name)
    @staticmethod
    def s(age):
        sa=10
        print(age)
obj=myclass(10,20)
obj.a=100
print(obj.a,obj.b)
myclass.c("achu")
obj.s(25)
myclass.cv=100
obj.a=150
print(myclass.cv,obj.a,sep="-------")
print(obj.c)