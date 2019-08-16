'''
Created on Sep 19, 2018

@author: Archana
'''
class mo:
    def handling(self,sub1=None,sub2=None,sub3=None):
        if sub1 is None and sub2 is None and sub3 is None:
            print("no subjects")
        elif sub2 is None and sub3 is None:
            print(sub1)
        elif sub3 is None:
            print(sub1,sub2)
        else:
            print(sub1,sub2,sub3)
obj=mo()
obj.handling()
obj.handling('python','ap','aj')
obj.handling('python')
obj.handling('python','ap')
        