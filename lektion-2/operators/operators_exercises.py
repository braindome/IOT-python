# ==========================
# Python Operators - Exercises
# ==========================

# 1. Arithmetic Operators
# Create two variables a = 8, b = 3
# Perform and print the result of:
# addition, subtraction, multiplication, division,
# floor division, modulus, exponentiation
a, b = 8, 3
print("Addiction: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Floor Division: ", a // b )
print("Modulus: ", a % b )
print("Exponentiation", a ** b)

# 2. Comparison Operators
# Create two variables a = 7, b = 10
# Print the result of:
a, b = 7, 10

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# 3. Logical Operators
# Create two boolean variables a = True, b = False
# Print the result of:
# a and b
# a or b
# not a

a, b = True, False
print(a and b)
print(a or b)
print(not a)


# 4. Assignment Operators
# Create a variable a = 5
# Use assignment operators to perform:
# - b = a
# - b += a
# - b -= a
# - b *= a
# Print the value of b after each operation
a = 5
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)

# 5. Identity Operators
# Create variables a = 10, b = 20, c = a
# Print the result of:
# a is b
# a is not b
# a is c
# a is not c
a = 10
b = 20
c = a
print(a is b)       # False
print(a is not b)   # True
print(a is c)       # True
print(a is not c)   # False

# 6. Membership Operators
# Create a list: my_list = [5, 10, 15, 20]
# Create two variables x = 25, y = 10
# Check and print whether x is in my_list
# Check and print whether y is in my_list

my_list = [5, 10, 15, 20]
x = 25, y = 10

print(x in my_list)
print(x not in my_list)

print(y in my_list)
print(y not in my_list)
