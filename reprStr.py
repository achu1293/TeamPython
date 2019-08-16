class A:
    def setName(self,name):
        self.__name=name
    def setAge(self):
        self.__age=int(input("Enter the age"))
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def __str__(self):
        print("str")
        return self.getName()+str(self.getAge())
    '''def __repr__(self):
        print("repr")
        return self.getName()+str(self.getAge())'''
if __name__=="__main__":
    obj=A()
    obj.setName("achu")
    obj.setAge()
    print(obj)