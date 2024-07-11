def get_input():
  while True:
    try:
      yield float(input("Enter a number: "))
    except ValueError:
      print("Invalid input. Please enter a number.")


def division(func):

  def wrapper(a, b):
    if b == 0:
      print("Cannot divide by zero.")
      return None
    return func(a, b)

  return wrapper


@division
def divide(a, b):
  return a / b


def add(a, b):
  return a + b


def sub(a, b):
  return a - b


def mul(a, b):
  return a * b


def Calculator():
  operation = input("Enter an operation (+, -, *, /): ")
  if operation not in ('+', '-', '*', '/'):
    print("Invalid operation.")
    return
  num1 = next(get_input())
  num2 = next(get_input())

  if operation == '+':
    result = add(num1, num2)
  elif operation == '-':
    result = sub(num1, num2)
  elif operation == '*':
    result = mul(num1, num2)
  else:
    result = divide(num1, num2)

  if result is not None:
    print(f"Result: {result}")


Calculator()
