'''
Created on Jul 24, 2017

@author: Archana
'''
from admin import admin
from register import register
class menu:
    def __init__(self):
        print("hiii")
    def menudrive(self):
        print("1. Admin \n 2. register")
        choice=int(input("enter the choice"))
        if choice==1:
            admin().adetails()
        if choice==2:
            register().reg()
menu().menudrive()
