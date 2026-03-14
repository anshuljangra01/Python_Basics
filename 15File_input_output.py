# # -------------read a file in python 
# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

# #--------------- Write a file in Pyhton  
# st ="This is a new string enter in the existing file" 
# f=open("file.txt","w")
# f.write(st)
# f.close


# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

#  -----------More File Functions in Python
# ---------f.readline() or f.readlines() 
# f=open("file.txt")
# lines=f.readlines()
# print(lines,type(lines))

# f.close()

# 

# f=open("file.txt")

# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))
# line4=f.readline()
# print(line4,type(line4))
# line5=f.readline()
# print(line5,type(line5))
# line6=f.readline()
# print(line6,type(line6))
# print(line6=="")
# line=f.readline()
# while(line !=""):
#     print(line)
#     line=f.readline()

# f.close()

#------------------- .append() function in files
st="Hey Harry you are amazing "
f=open("Myfile.txt","a")

f.write(st)
f.close()
# --------------------with statement --------------------
# It has dosen't need to close the tag 

with open ("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file 

