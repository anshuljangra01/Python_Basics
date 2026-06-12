from typing import List
# # using walrus operator 
# if (n := len([1,2,3,4,5]))>3:
#     print(f"List is too long ({n} elements , expected <=3)")
#  # Output: List is too long (5 Elements , expected<=3)  

# # Type Defination in python 

# #Variable Type hint
# age:int =23

# #Function Type hints
# def greeting (name : str) -> str:
#     return f"hello",{name}

# print (greeting("Alice"))

# Type Definition
n:int =5

Name:str ="Jai"

def sum(a: int,b:int)->int:
    return a+b
