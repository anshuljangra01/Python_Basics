
try:
    a=int(input("Enter a nubmer: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("Finally block is running... ")

    # But the main use of finally is when we made function  example


def main():
    
    try:
        a=int(input("Enter a nubmer: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("Finally block is running... ")

main()        

