def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error:Division by zero is not allowed"
    return x/y
def main():
    print("Simple Calculator")
    print("Select Operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
        choice = input("Enter your choice(1/2/3/4):")
        if choice in ['1','2','3','4']:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))

            if choice == '1':
                print(f"The result is:{add(num1,num2)}")

            elif choice == '2':
                print(f"The result is:{subtract(num1,num2)}")

            elif choice == '3':
                print(f"The result is:{multiply(num1,num2)}")

            elif choice == '4':
                print(f"The result is:{divide(num1,num2)}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation?(Y/N):")
        if next_calculation.lower() != 'y':
            break

if __name__ == "__main__":
    main()