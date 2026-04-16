# class number:
#     def __init__(self,n):
#         self.n=n

#     def __add__(self,num):
#         return self.n+num.n  

      
# n=number(1)
# m =number(2)
# print(n + m)

#  p1+p2  #p1.__add__(p2)
#  p1-p2  #p1.__sub_(p2)
#  p1*p2  #p1.__mul__(p2)
#  p1/p2  #p1.__truediv__(p2)
#  p1//p2  #p1.__floordiv__(p2)

# n+m #p1.__add__(p2)
# n-m #p1.__sub_(p2)
# n*m #p1.__mul__(p2)
# n/m #p1.__truediv__(p2)
# n/m  #p1.__floordiv__(p2)


class Number:
    def __init__(self, value):
        self.value = value

    # + operator
    def __add__(self, other):
        return self.value + other.value

    # - operator
    def __sub__(self, other):
        return self.value - other.value

    # * operator
    def __mul__(self, other):
        return self.value * other.value


# Create objects
n1 = Number(10)
n2 = Number(5)

print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)
print("Multiplication:", n1 * n2)