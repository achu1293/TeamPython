'''
Created on Oct 5, 2018

@author: Archana
'''


class students:    
    def __init__(self,name,age,dept,mark1,mark2,mark3):
        self.name=name
        self.__age=age
        self._dept=dept
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def __average(self):
        self.average=(self.mark1+self.mark2+self.mark3)//3
        
    def display(self):
        self.__average()
        #print(self.name,self.__age,self._dept,self.average)
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age=age   
    def __repr__(self):
        return self.name+" "+str(self.__age)+self._dept+str(self.average)
    def __del__(self):
        print("object is deleted")
if __name__=="__main__":
    obj=students("harini",20,"CSE",78,98,80)
    obj.setage(21)   
    obj.display()
    del obj
    obj.display()

print(obj)
print(obj._dept)
print(obj.getage())
       
       
       
       

    