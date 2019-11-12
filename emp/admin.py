'''
Created on Jul 24, 2017

@author: Archana
'''
import cx_Oracle
class admin:
    global cur
    con=cx_Oracle.connect('root/root@127.0.0.1/Employee')
    cur=con.cursor()
    def adetails(self):
        username=input("Enter the name")
        password=input("enter the password")
        #con=cx_Oracle.connect('root/root@127.0.0.1/Employee')
        #cur=con.cursor()
        try:
            cur.execute("create table login(username varchar(40),password varchar(40))")
            cur.execute("insert into login values(%s,%s)" %(username,password))
        except:
            try:
                cur.execute("insert into login values(%s,%s)" %(username,password))
                print("you have successfully registered")
            except:
                print("failed in registration")
    def addEmployee(self):        
        Emp_id=input("Enter the employee id")
        Emp_name=input("Enter the employee name")  
        Emp_designation=input("Enter the designation")
        Emp_department=input("Enter the department")  
        Emp_contactno=int(input("Enter the contact number"))
        Emp_basicpay=eval(input("Enter the basic pay"))
        Emp_hra= eval(input("Enter the hra amount"))     
        Emp_da= eval(input("Enter the da amount")) 
        Emp_salary= eval(input("Enter the salary"))
        try:
            cur.execute("create table addEmployee(Emp_id varchar(20),Emp_name varchar(40),Emp_designation varchar(40),Emp_department varchar(40),Emp_contactno number(10),Emp_basicpay number(20),Emp_hra number(20),Emp_da number(20),Emp_salary number(20)")
            cur.execute("insert into login values(%s,%s,%s,%s,%d,%d,%d,%d,%d)" %(Emp_id,Emp_name,Emp_designation,Emp_department,Emp_contactno,Emp_basicpay,Emp_hra,Emp_da,Emp_salary))
        except:
            try:
                cur.execute("insert into login values(%s,%s,%s,%s,%d,%d,%d,%d,%d)" %(Emp_id,Emp_name,Emp_designation,Emp_department,Emp_contactno,Emp_basicpay,Emp_hra,Emp_da,Emp_salary))
                print("successfully added")
            except:
                print("sorry try again")
            
    def viewSalary(self):
            cur.execute("select Emp_id,Emp_salary from addEmployee")
     
        
        
        
        