"""
Control Flow in Python
==================
"""

# Control flow statements allow you to control the execution of your code based on certain conditions.
# - `if`, `elif`, `else`: Conditional statements to execute code based on conditions.

x = 10
if x > 0:
    print("x is positive")  # Output if condition is true
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# - `for`: Looping through a sequence (like a list or string).
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# - `while`: Looping while a condition is true.
count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1

# - `break`: Exits the loop prematurely.
for i in range(5):
    if i == 3:
        break  # Exit loop when i is 3
    print(i)  # Output: 0, 1, 2

# - `continue`: Skips the current iteration and continues with the next.
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)  # Output: 0, 1, 3, 4

# - `pass`: A null statement that does nothing; used as a placeholder.
for i in range(5):
    if i == 2:
        pass  # Do nothing when i is 2
    print(i)  # Output: 0, 1, 2, 3, 4

# - `try`, `except`: Exception handling to catch and handle errors gracefully.
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
# - `finally`: A block that executes after try/except, regardless of whether an exception occurred.
finally:
    print("This will always execute.")

# - match-case: A way to match a value against multiple patterns (Python 3.10+).
def match_example(value):
    match value:
        case 1:
            print("Value is one")
        case 2:
            print("Value is two")
        case _:
            print("Value is something else")
