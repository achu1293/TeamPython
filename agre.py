
'''
Created on Sep 26, 2018

@author: Archana
'''
class teacher:
    def __init__(self,dwages):
        self.dwages=dwages
    def salary(self):
        return(self.dwages*30)
class dept:
    def __init__(self,dwages,noofstaffs):
        self.dwages=dwages
        self.noofstaffs=noofstaffs
    def totalsalary(self):
        print("{}".format(self.dwages.salary()*self.noofstaffs))
        
obj=teacher(1000)
print(obj.salary())

obj1=dept(obj,5)
obj1.totalsalary()
#del obj1
#print(obj.salary())
