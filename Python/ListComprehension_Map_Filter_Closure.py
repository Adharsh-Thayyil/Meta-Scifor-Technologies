# List Comprehension
str = "hello world"
uppercase_letters = [char.upper() for char in str if char.isalpha()]
print("List Comprehension - Uppercase letters:", uppercase_letters)

# Map
number = [1,2,3,4,5]
doubled_numbers = list(map(lambda x: x*2, number))
print("Map - Doubled Numbers:", doubled_numbers)

# Filter
wrds = ["adharsh","abhay","shikha"]
wrds_with_d = list(filter(lambda x: "d" in x, wrds))
print("Filter - Words with 'd':", wrds_with_d)

# Closure
def nth_power(n):
  def power(x):
    return x ** n
  return power

sqr = nth_power(2)
cbe = nth_power(3)

print("Closure - Square:", sqr(5))
print("Closure - Cube:", cbe(5))