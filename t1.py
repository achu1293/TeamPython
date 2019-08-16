'''
Created on Jul 28, 2018

@author: Archana
'''
#global a
#a=100
'''def fun(a):
    if a*2>20:
        return a
      
print(list(map(fun,[4,10,3,15])))

print("-------------------")'''
def fun1(a):
    if a*2>20:
        return a

print(list(filter(fun1,[4,10,3,15])))

print(list(map(lambda a:a*2,[2,4,6])))
print(list(filter(lambda a:a*2,[2,4,6])))
from functools import reduce
#print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))
print(reduce((lambda x,y:x+y),[1,2,3,4]))




   


