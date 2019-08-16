'''
Created on Sep 26, 2018

@author: Archana
'''
from abc import ABC,abstractmethod
class fish(ABC):
    @abstractmethod
    def fun(self):
        print("this is fish")
class shark(fish):
    def fun(self):
        super().fun()
        print("this is shark")
f=shark()
f.fun()
                               






