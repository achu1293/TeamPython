'''
Created on Sep 26, 2018

@author: Archana
'''
class room:
    def __init__(self,sqfeet):
        self.sqfeet=sqfeet
    def painting(self):
        return self.sqfeet*100
class home:
    def __init__(self,sqfeet,noofrooms):
        self.sqfeet=sqfeet
        self.noofrooms=noofrooms
        self.calc=room(self.sqfeet)
    def totallyprice(self):
        print(self.calc.painting()*self.noofrooms)
obj=home(50,2)
obj.totallyprice()()
