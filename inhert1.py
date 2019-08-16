'''
Created on Sep 12, 2018

@author: Archana
'''
#Single Inheritance
class fruits:
    def __init__(self,name,colour):
        
        self.__name=name
        self.colour=colour
    
    def display(self):
        print(self.__name,self.colour)
        
class apple(fruits):
    def __init__(self,name,colour,acid):
        fruits.__init__(self,name,colour)
        self.acid=acid
    def display1(self):
        super().display()
        print(self.acid)
        
obj=apple("fugi","red","malic")
obj.display1()


print(isinstance(obj,fruits))
print(issubclass(apple,fruits))
        
        