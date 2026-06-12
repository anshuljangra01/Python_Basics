# try:
#     a=int(input("Enter a nubmer: "))
#     print(a)

# except ValueError as v:
#     print("you enter wrong value or parameter")
#     print(v)

# except Exception as e:
#     print(e)



try:
    a=int(input("Enter a nubmer: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")

