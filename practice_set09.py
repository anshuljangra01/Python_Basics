import random
import shutil
# 1. Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'Twinkle'. 

# with open ("file.txt") as f:
#     # print(f.read())
#     line=f.readline()
#     if(line == "twinkle"):
#         print("The word is present in the content")
#         print(line)
#     else:
#         print("The word Twinkle is not present in the content")

# 2. The game() function in a program lets a user play a game and returns the scores as an integer. you need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
# def game():
#     print("you are Playing the game....")
#     score =random.randint(1,101)
#     with open("Hi_score.txt") as f :
#         hiscore =f.read()
#         if(hiscore!=""):
#             hiscore =int(hiscore)
#         else:
#             hiscore=0
#     print(f"Your score: {score}")
#     if(score>hiscore):
#         # Write this hiscore to the file
#         with open("Hi_score.txt", "w") as f:
#             f.write(str(score))


#     return score

# game()

# re-attempt


# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files . Place these files in a folder for a 13- year old.
# def generateTable(n):
#     table= ""
#     for i in range(1,11):
#         table += f"{n} × {i}= {n*1}\n"

#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)


# for i in range(2,21):
#     generateTable(i)        
 

# 4. A file contains a word "Donkey" Multiple times. you need to write a program which replace this word with ###### by updating the same file.

# with open("Myfile.txt" ,"r") as f :
#     line =f.read()

#     if "Donkey" in line:
#        line= line.replace("Donkey","######")
#     else:
#         print("This type of word dosn't exist in this content")
# with open("Myfile.txt","w") as f:
#     f.write(line)

# print("All occurrences of 'Donkey' replaced with '######'")   


# # open the file in read mode
# with open("text.txt", "r") as f:
#     content = f.read()

# # replace the word
# content = content.replace("Donkey", "######")

# # open the same file in write mode and update it
# with open("text.txt", "w") as f:
#     f.write(content)

# print("All occurrences of 'Donkey' replaced with '######'")            

# ------------------------
#5. Repeat program 4 for a list of such words to be censored.
# words=["Monkey", "Donkey","Dog","Snake"]
# with open ("Myfile.txt","r") as f:
#     content=f.read()
#     for word in words:
#         content =content.replace(word,"#####")
# with open("Myfile.txt","w")as f:
#     f.write(content)

# print("All censored words have been replaced with ")


#6. Write a program to mine a log file and find out whether it contains 'Python'.
# with open("python.txt" ,"r") as f:
#     content=f.read()
# if("python" in content  ):
#         print("Yes Pyhon word is present in this content")
# else:
#         print("Pyhton word is not present in this content")     

#7. Write a program to find out the line number where python is present from ques 6.
# with open("python.txt" ,"r") as f:
#     lines=f.readlines()
# lineno=1
# for line in lines:
#     if("python" in line):
#         print(f"Yes Pyhon word is present in this content and Line no: {lineno}")
#         break
#     lineno +=1
# else:
#         print("Pyhton word is not present in this content")

#8. Write a program to make a copy of a text file "this.txt"
# with open("Myfile.txt","r") as f:
#       content= f.read()
# with open("text.txt","a")as f:
#       f.write(content)

# print("File copies successfully.")  


# shutil.copy("text.txt","copy.txt")
# print("File copies successfully.")  


#9. Write a program to find out whether a file is identical & matches the content of another file

with open("copy.txt","r")as f1 ,open("text.txt","r")as f2:
    content1= f1.read()
    content2=f2.read()
    if(content1==content2):
        print("Both file are same.")
    else:
        print("Both files have different content.")   


#10. Write a program to wipe out the content of a file using python .
# with open("file.txt","w")as f:
#     f.write("")

#11. write a python program to rename a file to "renamed_by_Python.txt".   
with open("file.txt", "r")as f:
    content =f.read()
with open("renamed_by_python.txt" ,"w") as f:
    f.write(content)    