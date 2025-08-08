"""
Strings
=================
"""

# String Creation
print("Hello, World!")  # String literal
print('Single quotes are also valid')  # Single-quoted string
print("""Triple quotes allow for multi-line strings.""")  # Triple-quoted string for multi-line text
print('''You can also use triple single quotes.''')  # Triple single quotes for multi-line text
print(str(123))  # Convert integer to string = '123'
print(str(3.14))  # Convert float to string = '3.14'
print(str(True))  # Convert boolean to string = 'True'
print(str(None))  # Convert None to string = 'None'
print(str([1, 2, 3]))  # Convert list to string = "[1, 2, 3]"
print(str({'a': 1, 'b': 2}))  # Convert dictionary to string = "{'a': 1, 'b': 2}"

# formatting strings
a = 1000000000
b = 3.14159

print(f"Formatted number: {a:,}")  # Output: Formatted number: 1,000,000,000
print(f"Formatted float: {b:.2f}")  # Output: Formatted float: 3.14

# String Concatenation
print("Hello, " + "World!")  # Concatenation using +
print("Hello, " + str(123))  # Concatenation with type conversion

# String Replication
print("Hello! " * 3)  # Replication using * operator= Hello! Hello! Hello!
print("Repeat " * 2 + "this!")  # Replication with concatenation = Repeat Repeat this!

# String Length
print(len("Hello, World!"))  # Length of string = 13

# String Indexing and Slicing
my_string = "Hello, World!"
print(my_string[0])  # First character = 'H'
print(my_string[-1])  # Last character = '!'
print(my_string[7:12])  # Slicing = 'World'
print(my_string[:5])  # Slicing from start = 'Hello'
print(my_string[7:])  # Slicing to end = 'World!'
print(my_string[-6:])  # Slicing from the end = 'World!'

# String Methods
print(my_string.lower())  # Convert to lowercase = 'hello, world!'
print(my_string.upper())  # Convert to uppercase = 'HELLO, WORLD!'
print(my_string.title())  # Convert to title case = 'Hello, World!'
print(my_string.strip())  # Remove leading and trailing whitespace = 'Hello, World!'
print(my_string.replace("World", "Python"))  # Replace substring = 'Hello, Python!'
print(my_string.split(", "))  # Split string into list = ['Hello', 'World!']
print(my_string.find("World"))  # Find substring index = 7

print(my_string.startswith("Hello"))  # Check if starts with substring = True
print(my_string.endswith("!"))  # Check if ends with substring = True
print(my_string.count("o"))  # Count occurrences of substring = 2
print(my_string.isalpha())  # Check if all characters are alphabetic = False
print(my_string.isdigit())  # Check if all characters are digits = False
print(my_string.isalnum())  # Check if all characters are alphanumeric = False
print(my_string.islower())  # Check if all characters are lowercase = False
print(my_string.isupper())  # Check if all characters are uppercase = False

# String Iteration
for char in my_string:
    print(char, end=' ')  # Print each character in the string
    print()  # New line after iteration 

# String Comparison
print("abc" < "def")  # Compare strings lexicographically = True
print("abc" == "abc")  # Check if strings are equal = True
print("abc" != "def")  # Check if strings are not equal = True

# String Escape Characters
print("Line 1\nLine 2")  # New line character = Line 1
print("Tab\tSpace")  # Tab character = Tab    Space
print("Backslash: \\")  # Backslash escape = Backslash: \
print("Single quote: \'")  # Single quote escape = Single quote: '
print("Double quote: \"")  # Double quote escape = Double quote: "