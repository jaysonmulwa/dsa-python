"""
BUILTIN FUNCTIONS
==================
"""

# Built-in functions are always available in Python.
# They are not part of any module, so you can use them directly.
# Some common built-in functions include:

# - `print()`: Outputs data to the console.
print("Hello, World!")  # Output: Hello, World!
# - `len()`: Returns the length of an object.
print(len("Hello"))  # Output: 5
# - `type()`: Returns the type of an object.
print(type(42))  # Output: <class 'int'>

# - `int()`, `float()`, `str()`: Convert values to integer, float, or string types.
print(int(3.14))  # Convert float to int = 3
print(float(5))  # Convert int to float = 5.0
print(str(100))  # Convert int to string = '100'

# - `list()`, `tuple()`, `set()`, `dict()`: Convert values to list, tuple, set, or dictionary types.
print(list("123"))  # Convert string to list = ['1', '2', '3']
print(tuple([1, 2, 3]))  # Convert list to tuple = (1, 2, 3)
print(set([1, 2, 3]))  # Convert list to set = {1, 2, 3}
print(dict([(1, 'one'), (2, 'two')]))  # Convert list of tuples to dict = {1: 'one', 2: 'two'}

# - `abs()`: Returns the absolute value of a number.
print(abs(-5))  # Absolute value = 5

# - `round()`: Rounds a number to a specified number of decimal places.
print(round(3.14159, 2))  # Round to 2 decimal places = 3.14

# - `max()`, `min()`: Return the maximum or minimum value from an iterable.
print(max([1, 2, 3]))  # Maximum value = 3
print(min([1, 2, 3]))  # Minimum value = 1

# - `sum()`: Returns the sum of all items in an iterable.
print(sum([1, 2, 3]))  # Sum of list = 6

# - `sorted()`: Returns a sorted list from the items in an iterable.
print(sorted([3, 1, 2]))  # Sorted list = [1, 2, 3]

# - `range()`: Generates a sequence of numbers.
print(list(range(5)))  # Generates numbers from 0 to 4 = [0, 1, 2, 3, 4]

# - `enumerate()`: Adds a counter to an iterable and returns it as an enumerate object.
print(list(enumerate(['a', 'b', 'c'])))  # Enumerate list = [(0, 'a'), (1, 'b'), (2, 'c')]

# - `zip()`: Combines multiple iterables into a single iterable of tuples.
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # Zip lists = [(1, 'a'), (2, 'b'), (3, 'c')]

# - `any()`, `all()`: Check if any or all elements in an iterable are true.
print(any([False, True, False]))  # Any true = True
print(all([True, True, False]))  # All true = False

# - `map()`: Applies a function to all items in an iterable.
print(list(map(lambda x: x * 2, [1, 2, 3])))  # Map function = [2, 4, 6]

# - `filter()`: Filters items in an iterable based on a function.
print(list(filter(lambda x: x > 1, [1, 2, 3])))  # Filter items = [2, 3]

# - `reduce()`: Applies a rolling computation to sequential pairs of values in an iterable.
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # Reduce sum = 10

# - `id()`: Returns the identity of an object.
print(id(42))  # Identity of the integer 42

# - `help()`: Displays the documentation for an object.
# help(print)  # Uncomment to see the documentation for the print function

# - `dir()`: Returns a list of attributes and methods of an object.
print(dir([]))  # List of attributes and methods for a list object

# - `globals()`, `locals()`: Return the global and local symbol table, respectively.
print(globals())  # Global symbol table

print(locals())  # Local symbol table

# - `eval()`: Evaluates a string as a Python expression.
print(eval("2 + 3"))  # Evaluates the expression = 5

# - `exec()`: Executes a dynamically created Python code.
exec("print('Hello from exec!')")  # Output: Hello from exec!

# - `callable()`: Checks if an object appears callable (like a function).
print(callable(print))  # Check if print is callable = True

# - `isinstance()`: Checks if an object is an instance of a class or a tuple of classes.
print(isinstance(5, int))  # Check if 5 is an instance of int

# - `issubclass()`: Checks if a class is a subclass of another class.
print(issubclass(bool, int))  # Check if bool is a subclass of int = True

# - `memoryview()`: Returns a memory view object of the given object.
print(memoryview(bytes(5)))  # Memory view of a bytes object

# - `slice()`: Returns a slice object that can be used to slice sequences.
print(slice(1, 5))  # Slice object from index 1 to 5

# - `format()`: Formats a value according to a format specification.
print(format(255, 'x'))  # Format integer as hexadecimal = 'ff'

# - `repr()`: Returns a string representation of an object that can be used to recreate the object.
print(repr("Hello"))  # String representation = 'Hello'

# - `ascii()`: Returns a string containing a printable representation of an object, escaping non-ASCII characters.
print(ascii("Hello"))  # Printable representation = 'Hello'

# - `hash()`: Returns the hash value of an object.
print(hash("Hello"))  # Hash value of the string "Hello"

# - `next()`: Retrieves the next item from an iterator.
my_iter = iter([1, 2, 3])
print(next(my_iter))  # Next item from iterator = 1

# - `divmod()`: Returns the quotient and remainder of dividing two numbers.
print(divmod(10, 3))  # Quotient and remainder = (3, 1)

# - `pow()`: Returns the value of a number raised to the power of another number.
print(pow(2, 3))  # 2 raised to the power of 3

# - `chr()`, `ord()`: Convert between characters and their Unicode code points.
print(chr(65))  # Convert Unicode code point to character = 'A'
print(ord('A'))  # Convert character to Unicode code point = 65

# - `bin()`, `oct()`, `hex()`: Convert integers to binary, octal, or hexadecimal strings.
print(bin(10))  # Binary representation = '0b1010'
print(oct(10))  # Octal representation = '0o12'
print(hex(10))  # Hexadecimal representation = '0xa'

# - `breakpoint()`: Starts the debugger at the point where it is called.
# Uncomment the next line to start the debugger at this point
# breakpoint()  # Start the debugger

# - `complex()`: Creates a complex number from real and imaginary parts.
print(complex(1, 2))  # Create complex number = (1+2j)

# - `frozenset()`: Creates an immutable set.
print(frozenset([1, 2, 3]))  # Create frozenset = frozenset({1, 2, 3})

# - `bytearray()`, `bytes()`: Create mutable or immutable byte sequences.
print(bytearray([1, 2, 3]))  # Create mutable bytearray = bytearray(b'\x01\x02\x03')
print(bytes([1, 2, 3]))  # Create immutable bytes = b'\x01\x02\x03'