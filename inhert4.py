'''
Created on Sep 14, 2018

@author: Archana
'''
class A(object):
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B")
class C(A):
    def __init__(self):
        super().__init__()
        print("C")
class D(B,C):
    def __init__(self):
        super().__init__()
        print("D")
obj=D()

    

'''class A:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class B(A):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept=dept
    def display(self):
        super().display()
        print(self.dept)
class C(A):
    def __init__(self,name,section):
        super().__init__(name)
        #super().display()
        self.section=section
    def display(self):
        super().display()
        print(self.section)
class D(C,B):
    def __init__(self,name,dept,section,coll):
        super().__init__(name,section)
        self.coll=coll
    def display(self):
        super().display()
        print(self.coll)
obj=D("achu","CSE","A","KCE")
obj.display()'''
        
    
