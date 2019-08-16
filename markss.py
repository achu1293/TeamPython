'''
Created on Sep 14, 2018

@author: Archana
'''

class mark:
    def __init__(self,name,age,dept,mark1,mark2,mark3):
        self.name=name
        self.age=age
        self.dept=dept
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3     
    #def average(self):
        #self.avg=(self.mark1+self.mark2+self.mark3)//3
        
    def display(self):
        for i in l:
            print(i.name,i.age,i.dept,i.mark1,i.mark2,i.mark3)
        for i in l:
            if i.mark2>90:
                print(i.name)
    
l=[]
for i in range(2):
    m=mark(input("Enter the name"),int(input("Enter the age")),input("Enter the dept"),int(input("Enter the mark1")),int(input("Enter the mark2")),int(input("Enter the mark3")))
    l.append(m)
   
m.display()