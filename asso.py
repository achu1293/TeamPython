'''
Created on Sep 26, 2018

@author: Archana
'''
class teacher:
    cv=100
    def __init__(self,name):
        self.name=name
    def fun(self):
        print("this is teacher")
class student:
    def __init__(self,dept):
        self.dept=dept
    def fun1(self):
        print("this is student")
class person:
    def __init__(self,age,address,teacher=None,student=None):
        self.age=age
        self.address=address
        self.teacher=teacher
        self.student=student
    def __repr__(self):
        return "{} {} {} {} {}".format(self.teacher.name,self.student.dept,self.age,self.address,self.teacher.cv)
if __name__=="__main__":
    obj=person(25,"cbe",teacher("archana"),student("kannan"))
    obj.teacher.fun()
    obj.student.fun1()
    print(obj)
           
'''class Learner:
    def __init__(self):  
        self.classes = []                              #list creation 
    def enrol(self, course):                      #__init__ method takes one argument(course)
        self.classes.append(course)           #appending course to list       

class Teacher:                                             #Creating  class Teacher 
    def __init__(self, name):                      #__init__ method takes one argument(name)
        self.name = name
        self.courses_taught = ["C", "C++", "Java"]      
    def assign_teaching(self, course):        # two parameter /can add new course in list 
        self.courses_taught.append(course)
        print( self.courses_taught )
class Person: 
    def __init__(self, name, surname, number, learner=None, teacher=None) :   #learner and teacher is object here
        self.name = name
        self.surname = surname
        self.number = number
                                                             # Here the Person class Has-A learner and teacher as attributes
        self.learner = learner                  # if i declare a object as attribute in another calss  its  strong association
        self.teacher = teacher
    def __str__(self):
          return "name:{},\nno:{},\nlearnername{}". format(self.name,self.number,self.learner.classes,self.teacher.name)

myobj = Person("Raj", "Kumar", "SMTJNX045", Learner(), Teacher("John"))   #person class strongly depends on learner   
print(myobj.learner.classes)
myobj.teacher.assign_teaching("Python")
print(myobj)'''
