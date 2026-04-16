# Basic python (Variables and Input)
# print("Hello , World!")

# name =input("Enter your name: ")
# print("Hello "+ name+ " nice meeting you ")

# a=int(input("Enter a number: "))
# b=int(input("Enter second nubmer: "))
# print(a+b)

# len=float(input("Enter Length: "))
# bth=float(input("Enter Breadth: "))
# print("Area of the rectangle is ",len*bth)

# celsius to fahrenheit
# (0°C × 9/5) + 32 = 32°F

# cel= float(input("Enter the Temperature in Celsius: "))
# frh= (cel * 9/5 ) + 32
# print("Temperature in fahrenheit: ",frh,"°F" )

# fahrenheit to celsiuc 
# °C = (°F - 32) × 5/9

# Operators & conditions

# n=int(input("Enter a nubmer: "))
# if(n%2 ==0 or n==0 ):
#    print("The number is even")

# else:
#    print("The number is odd")
print("This is end of Question serirs")


# Start again for revision 

print("Hello, World!")


# n=int(input("Enter a value: "))
# print("The number is",n)


# n = int(input("Enter number: "))
# print("Even" * (n % 2 == 0) + "Odd" * (n % 2 != 0))

# find the sum of two numbers 
# n1= int(input("Enter first number: "))
# n2=int(input("Enter second number: "))

# sum=n1+n2
# print("The sum of two number is :",sum)


# #swap number wihtout third variable 
# a=12
# b=23
# print(f"a= {a} and b= {b}")
# a,b=b,a
# print("The swap number is :")
# print("a= ",a)
# print("b= ",b)

# # Swap numbers with third variable
# a=12
# b=23
# print(f"a= {a} and b= {b}")
# temp = a 
# a=b
# b=temp
# print("The swap number is :")
# print("a= ",a)
# print("b= ",b)

# Conditional statements
# # check a number positive , negative or zero 
# n=int(input("Enter a number: "))
# if(n>0):
#     print("The nubmer is positive")
# elif(n<0):
#     print("The number is negative")
# elif(n==0):
#     print("The number is zero ")
# else:
#     print("Wrong Input")        


# #Find the largest of three numbers

# n1=int(input("Enter First nubmer: "))
# n2=int(input("Enter second nubmer: "))
# n3=int(input("Enter Third nubmer: "))

# if(n1>n2 and n1>n3):
#     print(f"{n1} is greatest number")
# elif(n2>n1 and n2>n3):
#     print(f"{n2} is greatest number")
# elif(n3>n1 and n3>n2):
#     print(f"{n3} is greatset number")
# else:
#     print("You enter wrong input")  

# # find year is a leap year or not 
# year=int(input("Enter a year: "))              

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print("Leap year")    
# else:
#     print(" Not a Leap Year")

# Number is divisible by 5 and 11
# n= int(input("Enter  a nubmer: "))
# if(n%5 == 0 and n%11==0):
#     print("The number is divisible is 5 and 11 ")
# elif(n%5 ==0 and n%11 != 0):
#     print("The nubmer is only divisible by 5")   
# elif(n%11==0 and n%5 != 0):
#     print("The number is only divisible by 11")
# else:
#     print("The number is not divisible by 5 and 11")


# #check whether a character is a vowel or consontant
# c= input("Enter a character :") 

# if(c =="a" or c =="e" or c =="i" or c =="o" or c =="u"):
#     print(f"{c} is  a vowel")
# else:
#     print(f"{c} is a consonant")    


# -----Loops 

for i in range (1,11):
    print(i)
print("  ")
# While loop 


i = 1
while i <= 10:
    print(i)
    i += 1 