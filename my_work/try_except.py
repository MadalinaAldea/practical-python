def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Divided by zero')
    finally:
        print("Finally block")

if __name__ == "__main__":
    division(1,0)
    print("Division was finished")


# f

## TRy-except for invalid user input

try:
    x=input("Enter your age: ")
    if not isinstance(x, int):
        raise ValueError("Wrong ")
except ValueError:
    print("Enter a valid input")
