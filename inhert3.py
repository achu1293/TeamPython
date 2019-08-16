'''
Created on Sep 12, 2018

@author: Archana
'''
"Multilevel"
class gp(object):
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(self.name,self.address)
class p(gp):
    def __init__(self,name,address,qualification):
        super().__init__(name, address)
        self.qualification=qualification
    def display(self):
        super().display()
        print(self.qualification)
class we(p):
    def __init__(self,name,address,qualification,chara):
        super().__init__(name,address,qualification)
        self.chara=chara
    def display(self):
        super().display()
        print(self.chara)
obj=we("achu","mas","ME","good girl")
#obj=p("achu","mas","ME")
obj.display()
    