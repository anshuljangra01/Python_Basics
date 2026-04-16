OSI=["Application Layer","Presentaion Layer" ,"Session Layer" ,"Transport Layer ", "Network layer" ,"Data Link Layer" ,"Physical Layer" ]
TCP=["Application Layer","Application Layer" ,"Application Layer" ,"Transport Layer ", "Internet layer" ,"Network Access" ,"Network Access" ]
func=[" "]
for i in range(len(OSI)):
    print(f"{OSI[i]}  -->  {TCP[i]}")  

#  Fibonacci series
# Program to print Fibonacci series

def fibonacci_series(n):
    """
    Generate and print the Fibonacci series up to n terms.
    
    Args:
        n (int): Number of terms to generate
    """
    if n <= 0:
        print("Please enter a positive integer")
        return
    elif n == 1:
        print("Fibonacci series up to", n, "term:")
        print(0)
        return
    elif n == 2:
        print("Fibonacci series up to", n, "terms:")
        print(0, 1)
        return
    
    # Initialize first two terms
    a, b = 0, 1
    print("Fibonacci series up to", n, "terms:")
    print(a, b, end=" ")
    
    # Generate remaining terms
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()

# Example usage
if __name__ == "__main__":
    # You can change this value to print more terms
    num_terms = 10
    fibonacci_series(num_terms)
