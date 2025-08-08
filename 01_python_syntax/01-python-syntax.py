"""
Operators
"""
# Arithmetic Operators
print(5 + 3)  # Addition
print(10 - 2)  # Subtraction
print(4 * 2)  # Multiplication
print(8 / 2)  # Division
print(5 % 2)  # Modulus
print(2 ** 3)  # Exponentiation
print(10 // 3)  # Floor Division = 3 instead of 3.3333


# Comparison Operators
print(5 == 5)  # Equal to
print(5 != 3)  # Not equal to
print(5 > 3)  # Greater than
print(5 < 3)  # Less than   
print(5 >= 5)  # Greater than or equal to
print(5 <= 3)  # Less than or equal to

# Logical Operators
print(True and False)  # Logical AND = False
print(True or False)   # Logical OR = True
print(not True)  # Logical NOT = False

# Logical NOT
print(not False)  # Logical NOT

# Identity Operators
print(5 is 5)  # Identity = True
print(5 is not 3)  # Identity = True

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Membership = True
print(6 not in my_list)  # Membership = True

"""
Concatenation and Replication
"""
print("Hello " + "World")  # String Concatenation = Hello World
print("Hello " * 3)  # String Replication = Hello Hello Hello

"""
Type Conversion
"""
print(int(3.14))  # Convert float to int = 3
print(float(5))  # Convert int to float = 5.0
print(str(100))  # Convert int to string = '100'

# Type Conversion with Lists
my_list = [1, 2, 3]
print(list("123"))  # Convert string to list = ['1', '2', '3']

# Type Conversion with Tuples
my_tuple = (1, 2, 3)
print(tuple([1, 2, 3]))  # Convert list to tuple = (1, 2, 3)

# Type Conversion with Sets
my_set = {1, 2, 3}
print(set([1, 2, 3]))  # Convert list to set = {1, 2, 3}

# Type Conversion with Dictionaries
my_dict = {'a': 1, 'b': 2}
print(dict([(1, 'one'), (2, 'two')]))  # Convert list of tuples to dict = {1: 'one', 2: 'two'}

# Type Conversion with Booleans
print(bool(1))  # Convert int to bool = True
print(bool(0))  # Convert int to bool = False

# Type Conversion with None
print(bool(None))  # Convert None to bool = False

# Type Conversion with Strings
print(bool(""))  # Convert empty string to bool = False
print(bool("Hello"))  # Convert non-empty string to bool = True

# Type Conversion with Floats
print(bool(3.14))  # Convert float to bool = True
print(bool(0.0))  # Convert float 0.0 to bool = False