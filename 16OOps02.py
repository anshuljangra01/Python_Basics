# ------------------------Self parameter-----------------

class Employee:
    lang="Python" # This is class attribute
    salary = 1200000
    # ----------------Constructor 
    # --------- _ _init_ _ () method -------------
    def __init__(self,name,salary,lang): # Dunder method which is automatically called
        self.name =name
        self.salary= salary 
        self.lang =lang
        print("I am createing an object")


    def getinfo(self):
        print(f"The Language is {self.lang}. The salary is {self.salary}")

    @staticmethod  # It is a decorator in Python 
    def greet():
        print("Good Evening")    

# anshul =Employee()
anshul =Employee("Anshul",1300000,"Java")

# anshul.lang  ="Java" # This is Instance or Object attribute

# anshul.greet()
# anshul.getinfo() # it convert into
# " Employee.getinfo(anshul) " function call 
print(anshul.name,anshul.salary)
