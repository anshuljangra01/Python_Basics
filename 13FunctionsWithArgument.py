# single parameter
def greet(name):
    print("Good day, "+name)
greet("Anshul")    

# Double parameter as input 
def greet(name,ending):
    print("Good day, "+name)
    print(ending)
greet("Anshul", "Thank you")
greet("Jai" , "Thank you")
greet("Aman" , "Thanks")   

# Function using with return statement 
def greet(name,ending):
    print("Good day, "+name)
    print(ending)
    return 0
a=greet("Anshul", "Thank you")
print(a)

# Default paarmeter value 
def grt(name, ending="Thanks"):  #ending is a default argument in this statement 
    print(f"Good Day, {name}"); 
    print(ending) 

grt("Anshul")
grt("Aman","Thank you")