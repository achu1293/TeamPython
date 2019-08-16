
class myclass:
    cv=100
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def display(self):
        #for i in l:
            #print(i.name,i.age,i.dept)
        for i in l:
            if i.age==25:
                print(i.name)
                
l=[]
for i in range(2):
    obj=myclass(input("Enter the name"),int(input("Enter the age")),input("Enter the dept"))
    l.append(obj)
    
obj.display()
print(getattr(obj,"cv"))
print(hasattr(obj,"cv"))
#print(delattr(myclass,"cv"))
print(setattr(obj,"cv","180"))
print(obj.cv)