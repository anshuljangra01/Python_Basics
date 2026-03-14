# a= 12
# b=45
# c=56
# avg=(a+b+c)/3
# print(avg)

# ***************** Function Definition *****
def avg():
    a=int(input("Enter your number: "))
    b=int(input("Enter your number: "))
    c=int(input("Enter your number: "))
    average =(a+b+c)/3
    print("Average of these nubmers is: ",average)

# Function call
avg()

# Quick Quiz :
# Write a program ro greet a user with "Good day" using functions.

def greet():
    a=input("Enter your name: ")
    print(f"Good day {a}")

greet()