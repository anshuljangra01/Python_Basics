from typing import List,Tuple,Dict,Union

  # Type Defination in python 

#Variable Type hint
age:int =23

# #Function Type hints
# def greeting (name : str) -> str:
#     return f"hello",{name}

# print (greeting("Alice"))

# Type Definition
n:int =5

Name:str ="Jai"

def sum(a: int,b:int)->int:
    return a+b 

sum(34,4)

# from typing import List,Tuple,Dict,Union
# list of Integers
Number: List[int]= [1,2,3,4,5]

# Tuple of a string and an Integer 
Person: Tuple[str, int] =("Alice",30)

# Dictionary With string keys and integer values
score : Dict[str,int]= {"Alice":90, "Bob":85}

#Union type for variable that can hold multiple types
identifier: Union[int,str]="ID123"
identifier=12345 # Also valid
