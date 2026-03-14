# 1. create a class (2-D vector) and use it to create another representing a 3-D vector. 
# Create a 2D vector
class vector:
    v2 = Vector2D(3, 4)
    v2.display()
    print("Magnitude:", v2.magnitude())

# Create a 3D vector
v3 = Vector3D (3, 4, 5)
v3.display()
print("Magnitude:", v3.magnitude())

#2. Create a class 'pets' from a class 'Animals' and further create a class 'Dog' from 'pets'. Add a method 'bark' to class 'Dog'. 
 
#3. Create a class 'Employee' and add salary and increment properties to it. 
#3.1  Write a mehtod ' salaryAfterincrement ' method with a @property decorator with  a setter which changes the value of increment absed on the salary 

#4. Write a class 'Complex' to represent complex numbers, along with overloaded 
# operator '+' and '*' which adds and multiplies them.

#5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them. 

#6. Write __str__() method to print the vector as follows:
#     7i+8j+10k 
# Assume vector of dimension 3 for this problem.

#7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.