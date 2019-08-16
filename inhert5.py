'''
Created on Sep 14, 2018

@author: Archana
'''


class A:
    def __init__(self,name):
        self.name=name
       
class B(A):
    def __init__(self,name,age):
        
        super().__init__(name)
        self.age=age
        print(self.name,self.age)
class C(A):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept=dept
        print(self.name,self.dept)
obj=B("aaaa",25)
obj1=C("bbb","bca")        
    