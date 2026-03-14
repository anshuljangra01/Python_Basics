# ******** Wrtie a python program to display a user entered name followed by Good Afternoon using input() Function
# /////////////////////////////
# name= input(" Please Enter your name")
# print(" Good Afternoon",name)
# #    or 
# print(f"Good Afternoon {name}")

# ******  Write a program to filll in a letter template given below with name and date.
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# date= int(input("Enter today's date"))
# letter= ''' 
#         Dear ''',name, ''' You are Selected !''' ,date

# or /////////////////////////////////////////
# letter =(f" Dear {name} \n You are selected! \n  on Date: {date}")
# print(letter) 
#  or  with replace function in string  //////////////////////////////
letter =''' Dear <|Name|>,
            you are Selected!
            <|Date|>'''
print(letter.replace("<|Name|", "Anshul").replace("<|Date|>","09 feb 2027"))

# write a program to detect double space in a string.
# ////////////////////////////////////////
string=" This  is  string with  double  spaces" 
print(string.find("  ")) 

 #replace the double space from problem 3 with single spaces .
print(string.replace("  "," "))
# Write a program to format the following letter using escape sequence characerts. 
string1="Dear Harry, this pyton course is nice. Thanks!"
print(string1)
print("Dear Harry,\n This pyton course is nice.\n Thanks!")
# 
