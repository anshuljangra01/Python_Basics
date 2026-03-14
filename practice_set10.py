import math
# import random
from random import randint
#1. Create a class "Programmer " for storing information of few programmers working at Microsoft.
class Programmer: 
    name ="Name"
    language ="Pyhton" or "Java"
    Company="Microsoft"
    salary= 2100000
    
obj=Programmer()
print(obj.name, obj.Company, obj.salary) 

#  or 
class Programmer:
     company = "Microsoft"
     def __init__(self,name,salary,pin):
          self.name=name
          self.salary =salary
          self.pin =pin
p=Programmer("Anshul",1200000,245001)
print(p.name,p.salary,p.pin,p.company)      
r=Programmer("Rohan",1200000,245001)
print(r.name,r.salary,r.pin,r.company)      

#2. Write a class "Calculator" capable of finding square, cube and square root of a number.
# class calculator :
#       # Finding Square 
#       n=float(input("Enter a number: "))
#       Square=n*n 
#       print(f"The Square of {n} is {Square}")

#       # Finding Cube 
#       cube =n*n*n
#       print(f"The Cube of {n} is {cube}")

#      # Finding Square Root 
#       sqroot= math.sqrt(n)
#       print(f"The Square root of {n} is {sqroot}")

# cal= calculator() 
# It not follows the proper approach of OOPs concepts 

#  or 
# It follows modularity and reusability
class calculator:
     def __init__(self,n):
          self.n = n
     def square(self):
          print(f"The Square is {self.n* self.n}")    
     def cube(self):
          print(f"The cube is {self.n*self.n*self.n}")
     def sqroot(self):
          print(f"The Square Root is {self.n**1/2}")     
a=calculator(4)
a.square()
a.cube()
a.sqroot()
# print(cal.result)   
#3. Create a class with a class attribute a: create an object  from it and set 'a' directly using object.a=o. Does this chanfe the class attribute?
class demo:
     a=4

o=demo()
print(o.a)
o.a=0
print(o.a)

#4. Add a static method in problem 2, to greet teh user with hello. 
class calculator:
     def __init__(self,n):
          self.n = n
     def square(self):
          print(f"The Square is {self.n* self.n}")    
     def cube(self):
          print(f"The cube is {self.n*self.n*self.n}")
     def sqroot(self):
          print(f"The Square Root is {self.n**1/2}") 
     @staticmethod    
     def greet():
      print("Hello ")          
a=calculator(4)
a.greet()
a.square()
a.cube()
a.sqroot()

#5. write a class Train which has methods to book a ticket, get status (No fo seats) and get fare information of train running under Indian Railways.
class train:
     def __init__(self,trainNo):
          self.trainNo=trainNo
     def book(self, fro,to):
          print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
     
     def getStatus(self):
          print(f"Train no: {self.trainNo} is running on time ")
     
     def getFare(self,fro,to):
          print(f"Ticket fare in Train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t= train(12399)
t.book("Rohtak","Kurukshetra")
t.getStatus()
t.getFare("Rohtak","Kurukshetra")
     

#6. can you change the self -parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects.
class train:
     def __init__(slf,trainNo):
          slf.trainNo=trainNo
     def book(slf, fro,to):
          print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
     
     def getStatus(slf):
          print(f"Train no: {slf.trainNo} is running on time ")
     
     def getFare(slf,fro,to):
          print(f"Ticket fare in Train no: {slf.trainNo} from {fro} to {to} is {randint(222,5555)}")

t= train(12399)
t.book("Rohtak","Kurukshetra")
t.getStatus()
t.getFare("Rohtak","Kurukshetra")
     