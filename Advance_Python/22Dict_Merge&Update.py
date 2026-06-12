dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged = dict1 | dict2
print(merged)

with(
    open('file.txt')as f1,
    open('Hi_score.txt')as f2,
    open('Myfile.txt')as f3 ):
     print(f1.read())
     print(f2.read())
     print(f3.read())
