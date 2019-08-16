'''
Created on Sep 2, 2018

@author: Archana
'''
class classA:
    name="archana"
    a=10
    def __init__(self,b,name,age,dept="cse"):
        classA.a+=10
        self.b=b
        self.b+=10
        self.name=name
        self.age=age
        self.dept=dept
        print("this is my constructor")
    def fun1(self):
        #self.name=name
        print("1","name:",self.name,"age: ",self.age,"dept: ",self.dept,self.a,self.b)
    def fun2(self):
        
        print(classA.name)
        print("2","name:",self.name,"age: ",self.age,"dept: ",self.dept,self.a,self.b)
    '''def __del__(self):
        print("deleted")'''
    print("clss variable",name)
obj=classA(10,"achu",25)
obj.fun1()
print("before",obj.a)
#del obj.a
print(obj.a)
del obj
#obj1=classA(20,"kanna",28,"bca")
obj1=classA(10,"achu",25)



obj1.fun1()
#obj1.fun2()