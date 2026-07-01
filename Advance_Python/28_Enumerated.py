l=[1,342,33,345,56]

# index=0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index +=1


# This can be simplified using enumerated function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

