# # 1. Write a program to print multiple table of a given number using for loop.
# n=int(input("Enter a number: "))
# for i in range (1,11):
#     print(f"{n} × {i} = {n*i}")

# #2. write a program to greet all the person names stored in a list 'l' and which starts with S. 
# # l=["Harry","Soham","Sachin", "Aman"]
# l=["Harry","Sohan","Sachin", "Aman"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# #3. Attempt problem 1 using while loop.
# n=int(input("Enter a number: "))
# i=1
# while(i<11):
#     print(f"{n} × {i} = {n*i}")
#     i+=1

# #4. Write a program to find whether a given number is prime or not .
# n=int(input("Enter a nubmer: "))
# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not Prime")
#         break
# else:
#     print("Number is Prime")    

# #5. Write a program to find the sum of first n natural numbers using while loop.
# n=int(input("Enter a nubmer: "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=i
# print(sum)   

# #6. Write a program   to calculate the factorial of  a given number using for loop.
# n=int(input("Enter a nubmer: "))
# prd=1
# for i in range(1,n+1):
#     prd=prd*i
# print(f"The factorial of {n} is {prd}")

# #7. Write a program to print the following star pattern:
# #  *
# # ***
# #***** for n=3 
# n=int(input("Enter a nubmer: "))
# for i in range(1,n+1):
#     print(" "* (n-i),end="")
#     print("*"* (2*i-1), end="")
#     print("")

# # 8. Write a program to print the following star pattern:
# #*
# #**
# #*** for n=3
# n=int(input("Enter a nubmer: "))
# for i in range(1,n+1):
#     # print(" "* (n-i),end="")
#     print("*"* (i),end="")
#     print("")

#9. Write a program to print the following star pattern.
#***
#* *  for n=3
#*** 
n=int(input("Enter a nubmer: "))
for i in range(1,n+1):
    if(i == 1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="") 
        print(" "*(n-2),end="")
        print("*",end="")   
    print("") 

# Write a program to print multiplication table of n using loops in reversed order. 
n=int(input("Enter a nubmer: "))
for i in range (1,11):
    print(f"{n} × {11- i}= {n*(11-i)}")
 