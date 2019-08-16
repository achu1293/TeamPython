'''
Created on Sep 3, 2018

@author: Archana
'''
class classA:
    __cvprivate=100
    _cvprotected=50
    cv=10
    def __init__(self,name):
        self.name=name
    def fun(self):
        print(classA.__cvprivate, classA._cvprotected,classA.cv,self.name)
    def _funpro(self):
                
        print("it is protected method")
    def __funpri(self):
        print("this is private method")
    def d(self):
        self.__funpri()
    #__funpri("f")
obj=classA("archana")
obj.fun()
obj._funpro()
obj.d()
#obj._classA__funpri()
'''class b(a):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def fun1(self):
        print(super().cv)        
        print("child")
        super().fun()
        super()._funpro()
       
        #print(obj.__cvprivate)
        print("hello",self.name,self.age)'''
'''obj=a("aa")
obj.fun()
obj._funpro()
obj._a__funpri()'''
#obj1=b("achu",23)
#obj1.fun1()
#print(obj._a__cvprivate)
