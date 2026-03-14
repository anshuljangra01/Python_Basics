# 1. Write a program to find the greatest of four numbers entered by the user.
# /////////////////
# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# n3=int(input("Enter third number: "))
# n4=int(input("Enter fourth number: "))

# if(n1>n2 and n1>n3 and n1>n4):
#     print("The greatest number is n1: ",n1)

# elif(n2>n1  and n2>n3 and n2>n4):
#     print("The greatest number is n2: ",n2)
# elif(n3>n1 and n3>n2 and n3>n4):
#     print("The greatest number is n3:",n3)
# else:
#     print("The greatest number is n4:",n4)


 
#2.  write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# ////////////////////////////////////////////
# sub1= int(input("Enter subject1 marks: "))
# sub2= int(input("Enter subject2 marks: "))
# sub3= int(input("Enter subject3 marks: "))
# total=(sub1+sub2+sub3)/3 

# if(sub1>=33 and sub2>=33 and sub3>=33 and total>=40):
#     print("Result- pass",total)
#     print(sub1 ,sub2 ,sub3)

# else:
#     print("Result- Fail",total)
#     print(sub1 ,sub2 ,sub3)
# //////////////////////////////////////////////////////////////////////////////////////
# 3. A spam comment is defined as a text containing following keywords: "Make a lot of money ", "Buy now", "subscribe this" , "click this". Write a program to detect these spams.
# p1 ="Make a lot of money " 
# p2 ="Buy now"
# p3 ="subscribe this"
# p4 ="click this"
# message=input("Enter your comment: ")

# if((p1 in message) or (p2 in message) or (p3 in message)  or  (p4 in message) ):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")  

# //////////////////////////////////////////////

#4.  Write a program to find  whether a given username contains less than 10 characters or not.
# username= input("Enter UserName  ")
# char=len(username)
# # print(char)
# if(char<10):
#     print("User name has less than 10 characters :",char)
# else:
#     print("User name has more than 10 characters : , ", char)    

#    //////////////////////////////////////////////////////////////////////////
#5. write a program which finds out whether a given name is present in a list or not. 

# l = ["Harry", "Anshul", "Aman", "Jai", "Sameer"]
# name= input("Enter your name: ")

# if(name in l):
#     print("your name is in the list")
# else:
#     print("Your name is not in the list")    
    
    # //////////////////////////////////////////////////////////////
# 6. Write a program to calculate the grade of a student from his marks from the following scheme: 
# 90-100 =>Ex 
# 80-90=> A
# 70-80=>B
# 60-70=>c
# 50-60=>d
# <50 =>f
# ///////////////////////////////////Ans
# marks = int(input("Enter your marks: "))

# if(marks<=100 and marks>=90):
#     Grade ="Ex"
# elif(marks<=90 and marks>=80 ):
#     Grade ="A"    
# elif(marks<80 and marks>=70 ):
#     Grade ="B"    
# elif(marks<70 and marks>=60 ):
#     Grade ="C"    
# elif(marks<60 and marks>=50 ):
#     Grade ="D"    
# elif(marks<=50 ):
#     Grade ="F"  

# print("your grade is: ",Grade)    

# ////////////////////////////////////////////////////////////////////////////////
#Write a program to find out whether a given post is talking about "Harry" or not.   
post =input("Enter the post: ")

if("harry" in post.lower()):
    print("This post is talking about harry ")
else:
    print("This post is not talking about harry")    