# Simple or single level Inheritance
# ----------------------- Inheritance ----------------
class Employee:
    company ="Google"
    def show(self):
        print(f" The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company="Apple"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()

print(a.company ,b.company)

# ---------------- Multiple Inheritance -----------------
# class Employee:
#     company ="Google"
#     name ="default Name"

#     def show(self):
#         print(f" The name of the Employee is {self.name} and the company is {self.company}")

# class coder:
#     language="Python"
#     def printLanguages(self):
#         print(f"Out of all the languages here is your language: {self.language}")

# class Programmer(Employee,coder):
#     company="Apple"
#     def showLanguage(self):
#         print(f"The name is {self.company} and he is good with {self.language} language")

# a=Employee()
# b=Programmer()
# b.show()
# b.printLanguages()
# b.showLanguage()


#---------------- Multilevel Inheritance ------------
class Employee:
    a=1

class Programmer (Employee):
    b=2

class Manager(Programmer):
    c=3

o=Employee()
print(o.a)

o=Programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)
b=Manager()
print(b.a)
print(o.a) 


# Supper Key Word in Inheritance 
# -------------- super() keyWord -------------------
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1
class Programmer (Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):

    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

# o=Employee() 
# print(o.a)

# o= Programmer()
# print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)


## ------------  @classmethod  Decorator ----------------
# class Employee:
#     a=1
     
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")

# e=Employee()
# e.a=45

# e.show()
# -------------- @property Decorators ------------------
class Employee:
    a=1
     
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]    
        self.lname = value.split(" ")[1]    

e=Employee()
e.a=45

e.name ="Aman Bhardwaj"
print(e.fname ,e.lname)

e.show()
