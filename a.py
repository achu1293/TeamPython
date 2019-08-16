'''
Created on Sep 11, 2018

@author: Archana
'''
class dog:
    def __init__(self,name,age,breed):
       self.name=name
       self.__age=age
       self._breed=breed
    def run(self):
        print(self.name," run well")
    def _bark(self):
        print(self._breed,"barks badly")
        print(self.__age)
    
name=input("enter the name")
age=int(input("Enter the age"))
breed=input("enter the breed")

pug=dog(name,age,breed)
#pug.run()
#pug._bark()
print(pug.name," run well")
print(pug._breed,"barks badly")
print(pug._dog__age)