def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        raise ValueError("Error:Division by zero is not allowed")
    return x/y
def calculator():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        print("Select Operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter your choice(1/2/3/4):")
        if choice == '1':
            print(f"{num1}+{num2}={add(num1,num2)}")
        elif choice == '2':
            print(f"{num1}-{num2}={subtract(num1,num2)}")
        elif choice == '3':
            print(f"{num1}*{num2}={multiply(num1,num2)}")
        elif choice == '4':
            print(f"{num1}/{num2}={divide(num1,num2)}")
        else:
            print("Invalid Input")
    except ValueError as e:
        print(f"Error:{e}")
    except Exception as e:
        print(f"An unexpected error occured:{e}")

if __name__ == "__main__":
    calculator()