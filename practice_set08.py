# # Write a program using function to find greatest of three numbers.
# def great():
#      n=int(input("Enter a number: "))
#      n1=int(input("Enter a number: "))
#      n2=int(input("Enter a number: "))
#      if(n>n1 and n>n2):
#           print(f"{n} is Greatest number of all three numbers")
#      elif(n1>n and n1>n2):
#           print(f"{n1} is Greatest number of all three numbers") 
#      else:
#          print(f"{n2} is Greatest number of all three numbers")       

# great()

# # Writes a python program using function to convert Celsius to Fahrenheit
# def f_to_c(f):
#      return 5*(f-32)/9
# f=int(input("Enter temperature in F:"))
# c=f_to_c(f)
# print(f"{round(c,2)} °C")
# # How do you prevent a python print() function to print a new line at the end .

# print("A")
# print("B")
# print("C",end="")
# print("D",end="")
# print("")

# # Write a recursive function to calculate teh sum of first n natureal numbers.

# def sum(n):
#     if(n==1):
#         return 1
#     else:
#         return sum(n-1)+n
    
# n=int(input("Enter a number: "))
# print(f"The Sum of firts n natural nubmers is: {sum(n)}")
# # Write a python function to print first n lines of the following pattern: 
# # ***
# # **      for n=3
# # *  
# n=int(input("Enter a nubmer: "))
# for i in range(1,n+1):
#     # print(" "* (n-i),end="")
#     print("*"* (i),end="")
#     print("")

# def pattern(n):
#     if(n==0):
#         return
#     print("*" *n)
#     pattern(n-1)

# pattern(5)

# write  a Python function which converts inches to cms.
# 1 Inch =2.54 cm   multiply the length value by 2.54
# 1 cms = 0.393701 divided the value by 2.54
# def cnvrt_cms():
#     n=int(input("Enter the number: "))
#     cm=n*2.54
#     print(f"{n} convert into Centimeters {cm} cm")

# def cnvrt_inchs():
#     n=int(input("Enter the number: "))
#     ins=n/2.54
#     print(f"{n} convert into Inches {ins} inches")

# cnvrt_cms()
# cnvrt_inchs()    
 
# # Write a python function to remove a given word from a list ad strip it at the same time.


# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l 

# l=["Anshul", "Jai","Rohan","Shubham","an"]

# print(rem(l,"an"))

# # TO strip words or letters in the list use .strip function 

# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n 

# l=["Anshul", "Jai","Rohan","Shubham","an"]

# print(rem(l,"an"))

# Write a python function to print multiplicatioin table of a given number.
def multiply(n):
    for i in range(1,11):
        print(f"{n} × {i}= {n*i} ")


multiply(5)
