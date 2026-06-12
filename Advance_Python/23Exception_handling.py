# Excepiton Handling 
a=12
b=0
try:
    # Code might throw Exception
    result =a/b
    print(result)

except Exception as e:
    print(e)

try:
    a=int(input("Hey, Enter a number:"))  
    print(a)
except Exception as e:
    print(e)

print("Thank you")
# print(a)