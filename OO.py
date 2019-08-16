class oo:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("this is constructor")
    def __sub__(self,other):
        x=self.num1+self.num2
        print(self.num1,self.num2)
        y=other.num1+other.num2
        print(other.num1,other.num2)
        return x-y
    def __eq__(self,other):
        print("equal than")
    def __ge__(self,other):
        print("greater than")
obj1=oo(10,20)
obj2=oo(100,200)
print(obj1>=obj2)
        