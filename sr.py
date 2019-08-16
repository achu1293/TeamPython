'''
Created on Sep 19, 2018

@author: Archana
'''
class Item:
    def __init__(self, name):
        self._name = name;
    def __str__(self):
        return "Item: %s" % self._name
print(Item("car"))