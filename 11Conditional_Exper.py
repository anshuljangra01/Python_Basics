a=int(input("Enter your age: "))
if(a>18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0): 
     print("You are enterrig an invalid age")
elif(a==0):
    print("You are enterring 0 which is not a valid age")     
else :
    print("You are below the age of consent")

print("End of program")

# Quick quiz: Write a program to print "yes" when teh age entered by the user is greater than or equal to 18.

age=int(input("Enter your age"))
if(age>=18):
    print("Yes")


