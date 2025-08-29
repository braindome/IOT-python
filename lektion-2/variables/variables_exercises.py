# ==========================
# Variables in Python - Exercises
# ==========================

# 1. Simple variable
# Create a variable 'city' and assign it the name of your hometown. Print the value.

city = 'Stockholm'
print(city)

# 2. Naming rules
# The following variable names are invalid. Explain why and rewrite them so they work.
# 1variable = 100 # Can't start with a number
# my-variable = "hello" # Not snake_case
# print = "hej" # Reserved word




# 3. Case sensitivity
# What will be the output of the code below, and why?
# Age = 25
# age = 30
# print(Age)
# print(age)

# Two lines: 25 and 30, they are different variables



# 4. Dynamic typing
# Create a variable x and assign it an integer value.
# Then change x to a string value. Print both values.
x = 2
print(x)
x = "Lololol"
print(x)


# 5. Multiple assignments
# Create three variables (a, b, c) in one line
# and assign them the values 10, 20, and "Thirty". Print them.
a, b, c = 10, 20, "Thirty"
print(a, b, c)


# 6. Type casting
# Create a variable num_str = "123".
# Convert it to int and float.
# Print both values and their types.
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(num_int, type(num_int))
print(num_float, type(num_float))

# 7. Object references
# Run the following code and explain the result.
x = 5
y = x
x = 10
print("x:", x)
print("y:", y)

# y is assigned x former value, while x gets assigned a new value. So y prints the first value of x and x prints the newest value.


# 8. Swapping values
# Swap the values of two variables a and b without using a third variable.
a, b = 2, 10
a, b = b, a


# 9. String length
# Create a variable word with any word.
# Use len() to calculate the number of characters in the word and print the result.
word = "Dunkelheit"
print(len(word))


# 10. Scope
# Study the code and explain why the output is what it is.
# x = "global"
#
# def my_func():
#     x = "local"
#     print("In function:", x)
#
# my_func() # Prints the value of variable named x inside the function
# print("Outside function:", x) # Prints the value of variable named x in the outer scope

