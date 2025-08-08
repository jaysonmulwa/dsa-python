"""
Functions in Python (python 3.10+)
==================
- args and kwargs
- decorators
- lambda functions
"""

#### args and kwargs allow you to pass a variable number of arguments to a function.
def example_function(*args, **kwargs):
    print("Positional arguments:", args) #
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, a=4, b=5)  # Positional and keyword arguments
# Positional arguments: (1, 2, 3) # 
# Keyword arguments: {'a': 4, 'b': 5} # 


#### Decorators are a way to modify the behavior of a function or method.
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@decorator_function
def decorated_function(x):
    print(f"Function called with argument: {x}")
    return x * 2

decorated_function(10)  # Calls the decorated function

### Lambda functions are small anonymous functions defined with the lambda keyword.
lambda_function = lambda x: x * 2
print(lambda_function(5))  # Output: 10

