'''
Created on Oct 3, 2018

@author: Archana
'''
class room:
    def __init__(self,sqfeet):
        self.sqfeet=sqfeet
    def painting(self):
        return self.sqfeet*50
class home:
    def __init__(self,noofroom):
       
        self.noofroom=noofroom
        self.amt=room(300)
    def totalamt(self):
        print(self.amt.painting()*self.noofroom)
h=home(1)
h.totalamt()