student={
    "Name":"Anshul",
    "age":21,
    "course": "Python",
    "roll-no": 12
}
print(type(student))
print(student.items())
print(student["Name"])
print(student.keys())
print(student.values())
student.update({"age":22,"marks":98})
print(student)
print(student.get("marks"))
print(student.get("mark")) # Prints None
# print(student("mark")) # Returns an error 
# "Pop and pop.item" methods of dictionary in python self check out 

 # write a python program to using numPy  to create a three * three matrix 
 # display its taranspos find the sum of all elements and find the maximum element in each row 

#  write a py program ot create a data frame ofour student detais name roll no marks 
# display only students who score more than 80 marks 
# find the average marks 

# /////////////////  Sets in Python //////////////

s={1,5,32}
e=set(s)

s.add(2)
s.add(3)
print(len(s))
print(type(s))
print(s)

