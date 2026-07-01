# 1. Write a program to open three files 1.txt, 2.txt,3.txt of any these file are not present, a message without exiting the program msut be printed promoting the same. 
# try:
        
#     with open('1.txt','r')as f:
#         print(f.read())
# except Exception as fe:
#     print("File does not exist Pelase choose correct file ")
#     print(fe)


# try:
#     with open('2.txt','r')as f:
#         print(f.read())
# except Exception as fe:
#     print("File does not exist Pelase choose correct file ")
#     print(fe)


# try:
#     with open('3.txt','r')as f:
#         print(f.read())
# except Exception as fe:
#     print("File does not exist Pelase choose correct file ")
#     print(fe)
# print("Thank you")
                     



# Write a program to print third, fifth, and seventh element from a list using enumerate function.
# l=[1,2,3,4,5,6,7,8] 

# for i, item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)



# Write a list comprehension print a list which contains the multiplication table of a user entered nubmer.
# n=int(input("Enter a number: "))

# table=[n*i for i in range(1,11)]
# print(table)

# Write a program to display a/b where a and b are integes. if b=0, diplay infinite by handling the ZeroDivisionError.
# a= int(input("Enter a number: "))
# b= int(input("Enter a number: "))
# try:
#     result = a/b 
#     print(result)

# except Exception as e: 
#     print(e)

# print("Program Ended")
# # another solution 
# try :
#     a= int(input("Enter a number: "))
#     b= int(input("Enter a number: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("infinite") 
      
         

#store the multiplication table generator on problem 3 in a file named Tables.txt 

n=int(input("Enter a number: "))

table=[n*i for i in range(1,11)]
with open ("tables.txt",'a')as f:
    f.write(f"Table of {n}: {str(table)} \n")

