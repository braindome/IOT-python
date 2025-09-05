def greeting():
  print("Hello World")

greeting()

# function arguments (with data types)
def even_odd(x: int) -> str:
  if x % 2 == 0:
    return 'Even'
  else:
    return 'Odd'
  
# default argument (in this case y = 10)
def default_args(x, y = 10):
  print("x: ", x)
  print("y: ", y)

# keyword args
def student(fname, lname):
  print(fname, lname)

student(fname="john", lname="doe")

# arbitrary keyword args - *args and **kwargs

def my_fun(*args):
  print(args)

my_fun(1, "a", True)

def my_fun2(**kwargs):
  print(kwargs)

my_fun2(name="jane", age=60)
my_fun2(city="Gothenburg", country="Sweden")

# docstring
def print_doc():
    """This text should describe the function
    """
    print(print_doc.__doc__)

print_doc()

# inner function / nested function
def outer_fun():
    s = 'Snakes'
    def inner_fun():
        print(s)
    inner_fun()

outer_fun()

# return - ends function and (opt) returns value 
# anonymous function
def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(7))


# reference value
# if you update a value, it will change outside the function
def ref_fun(x):
    x[0] = 20

li = [10, 11, 12, 13, 14, 15]
ref_fun(li)
print(li)


# if you assign a new value the link to the old object is broken
def ref_fun2(x):
    x = [20, 30, 40]

li = [10, 11, 12, 13, 14, 15]
ref_fun2(li)
print(li)