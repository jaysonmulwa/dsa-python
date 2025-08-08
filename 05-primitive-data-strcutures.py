"""
Primitive Data Structures in Python
==================
- Primitive data structures are the basic building blocks of data manipulation in Python. They include:
- List, Tuple, Set, Dictionary, String, and Number types.
- Each of these structures has its own characteristics and use cases.

- Ordered: Lists, Tuples, Dictionaries
- Unordered: Sets, Dictionaries

- Mutable: Lists, Sets, Dictionaries
- Immutable: Tuples, Strings, Numbers
"""


"""
Lists
"""
### Lists are ordered collections that can hold a variety of data types.
my_list = [1, 2, 3, "four", 5.0]
print("List:", my_list)  # Output: List: [1, 2, 3, 'four', 5.0]

### Tuples are similar to lists but are immutable (cannot be changed).
my_tuple = (1, 2, 3, "four", 5.0)
print("Tuple:", my_tuple)  # Output: Tuple: (1, 2, 3, 'four', 5.0)

### Sets are unordered collections of unique elements.
my_set = {1, 2, 3, "four", 5.0}
print("Set:", my_set)  # Output: Set: {1, 2, 3, 'four', 5.0}

### Dictionaries are collections of key-value pairs, where keys are unique.
my_dict = {"one": 1, "two": 2, "three": 3}
print("Dictionary:", my_dict)  # Output: Dictionary: {'one': 1, 'two': 2, 'three': 3}

### Strings are sequences of characters, immutable in nature.
my_string = "Hello, World!"
print("String:", my_string)  # Output: String: Hello, World!

### Numbers in Python can be integers or floating-point numbers.
my_int = 42
my_float = 3.14
print("Integer:", my_int)  # Output: Integer: 42
print("Float:", my_float)  # Output: Float: 3.14

##### Python Lists ####
# Lists are mutable, ordered collections that can hold a variety of data types.
my_list = [1, 2, 3, "four", 5.0]
print("List:", my_list)  # Output: List: [1, 2, 3, 'four', 5.0]
print("First element:", my_list[0])  # Accessing first element: Output: 1
my_list.append(6)  # Adding an element to the list
print("Updated List:", my_list)  # Output: Updated List: [1, 2, 3, 'four', 5.0, 6]
print("List Length:", len(my_list))  # Output: List Length: 6
print("List Slice:", my_list[1:4])  # Slicing the list: Output: [2, 3, 'four']
# Removing an element from the list
my_list.remove("four")
print("List after removal:", my_list)  # Output: List after removal: [1, 2, 3, 5.0, 6]

print("List contains 3:", 3 in my_list)  # Checking membership: Output: True
print("List contains 4:", 4 in my_list)  # Checking membership: Output: False

print("List is empty:", not my_list)  # Checking if the list is empty: Output: False
print("List is not empty:", bool(my_list))  # Checking if the list is not empty: Output: True

print("List is equal to [1, 2, 3, 5.0, 6]:", my_list == [1, 2, 3, 5.0, 6])  # Checking equality: Output: True
print("List is not equal to [1, 2, 3]:", my_list != [1, 2, 3])  # Checking inequality: Output: True
print("List is greater than [1, 2]:", my_list > [1, 2])  # Checking greater than: Output: True
print("List is less than [1, 2, 3, 5.0, 6, 7]:", my_list < [1, 2, 3, 5.0, 6, 7])  # Checking less than: Output: True

print(my_list + [7, 8])  # Concatenation: Output: [1, 2, 3, 5.0, 6, 7, 8]
print(my_list * 2)  # Replication: Output: [1, 2, 3, 5.0, 6, 1, 2, 3, 5.0, 6]
print("List after clearing:", my_list.clear())  # Clearing the list: Output: None
print("List after clearing:", my_list)  # Output: List after clearing: []

print(my_list.count(2))  # Counting occurrences of an element: Output: 1
print(my_list.index(3))  # Finding the index of an element: Output: 2
my_list.reverse()  # Reversing the list
print("Reversed List:", my_list)  # Output: Reversed List: [6, 5.0, 3, 2, 1]
my_list.sort()  # Sorting the list
print("Sorted List:", my_list)  # Output: Sorted List: [1, 2, 3, 5.0, 6]
my_list.sort(reverse=True)  # Sorting the list in reverse order
print("Sorted List in reverse order:", my_list)  # Output: Sorted List in reverse order: [6, 5.0, 3, 2, 1]

print(my_list[-1]) # my_list[-1] accesses the last element of the list
print(my_list[-2]) # my_list[-2] accesses the second last element of the list

furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture[0:4]) # Output: ['table', 'chair', 'rack', 'shelf']
print(furniture[0:2]) # Output: ['table', 'chair']
print(furniture[1:])  # Output: ['chair', 'rack', 'shelf']
print(furniture[1:2])  #  Output: ['chair'] (slicing with start < end)
print(furniture[:2])  # Output: ['table', 'chair']
print(furniture[-1])  # Output: 'shelf' (last element)
print(furniture[-2])  # Output: 'rack' (second last element)
print(furniture[2:1])  # Output: ['rack'] (slicing with start > end)
print(furniture[1:3])  # Output: ['chair', 'rack'] -->"Print the items in the list furniture starting from index 1 up to but not including index 3."


"""
Tuples
"""
### Tuples are similar to lists but are immutable (cannot be changed).
my_tuple = (1, 2, 3, "four", 5.0)
print("Tuple:", my_tuple)  # Output: Tuple: (1, 2, 3, 'four', 5.0)
print("First element:", my_tuple[0])  # Accessing first element: Output: 1
print("Tuple Length:", len(my_tuple))  # Output: Tuple Length: 5    
print("Tuple Slice:", my_tuple[1:4])  # Slicing the tuple: Output: (2, 3, 'four')
print("Tuple contains 'four':", "four" in my_tuple)  # Checking membership
print("Tuple is empty:", not my_tuple)  # Checking if the tuple is empty: Output: False
print("Tuple is not empty:", bool(my_tuple))  # Checking if the tuple is not empty: Output: True
print("Tuple is equal to (1, 2, 3, 'four', 5.0):", my_tuple == (1, 2, 3, "four", 5.0))  # Checking equality: Output: True
print("Tuple is not equal to (1, 2, 3):", my_tuple != (1, 2, 3))  # Checking inequality: Output: True

#etc.



"""
Sets
"""
### Sets are unordered collections of unique elements.
my_set = {1, 2, 3, "four", 5.0}
print("Set:", my_set)  # Output: Set: {1, 2, 3, 'four', 5.0}
print("Set contains 3:", 3 in my_set)  # Checking membership: Output: True
print("Set contains 4:", 4 in my_set)  # Checking membership: Output: False
print("Set is empty:", not my_set)  # Checking if the set is empty:
print("Set is not empty:", bool(my_set))  # Checking if the set is not empty: Output: True

print(my_set.remove(3))  # Removing an element from the set
print("Set after removal:", my_set)  # Output: Set after removal: {1, 2, 'four', 5.0}
print("Set Length:", len(my_set))  # Output: Set Length: 4
print("Set is equal to {1, 2, 'four', 5.0}:", my_set == {1, 2, "four", 5.0})  # Checking equality: Output: True
print("Set is not equal to {1, 2, 3}:", my_set != {1, 2, 3})  # Checking inequality: Output: True

print(my_set.union({6, 7}))  # Union with another set: Output: {1, 2, 'four', 5.0, 6, 7}
print(my_set.intersection({2, 3, 4}))  # Intersection with another set: Output: {2}
print(my_set.difference({1, 2}))  # Difference with another set: Output: {5.0, 'four'}
print(my_set.symmetric_difference({2, 3, 4}))  # Symmetric difference with another set: Output: {1, 3, 'four', 5.0, 4}
print("Set is a subset of {1, 2, 'four', 5.0}:", my_set.issubset({1, 2, "four", 5.0}))  # Checking subset: Output: True
print("Set is a superset of {1, 2}:", my_set.issuperset({1, 2}))  # Checking superset: Output: True
print("Set is disjoint with {6, 7}:", my_set.isdisjoint({6, 7}))  # Checking disjoint: Output: True
print("Set after clearing:", my_set.clear())  # Clearing the set: Output: None
print("Set after clearing:", my_set)  # Output: Set after clearing: set()

"""
Dictionaries
"""
### Dictionaries are collections of key-value pairs, where keys are unique.
my_dict = {"one": 1, "two": 2, "three": 3}
print("Dictionary:", my_dict)  # Output: Dictionary: {'one': 1, 'two': 2, 'three': 3}
print("Value for key 'one':", my_dict["one"])  # Accessing value by key: Output: 1
print("Dictionary Length:", len(my_dict))  # Output: Dictionary Length: 3
print("Dictionary Keys:", my_dict.keys())  # Output: Dictionary Keys: dict_keys(['one', 'two', 'three'])
print("Dictionary Values:", my_dict.values())  # Output: Dictionary Values: dict_values([1, 2, 3])
print("Dictionary Items:", my_dict.items())  # Output: Dictionary Items: dict_items([('one', 1), ('two', 2), ('three', 3)])
print("Dictionary contains 'two':", "two" in my_dict)  # Checking membership: Output: True
print("Dictionary is empty:", not my_dict)  # Checking if the dictionary is empty: Output: False
print("Dictionary is not empty:", bool(my_dict))  # Checking if the dictionary is not empty: Output: True
print("Dictionary is equal to {'one': 1, 'two': 2, 'three': 3}:", my_dict == {"one": 1, "two": 2, "three": 3})  # Checking equality: Output: True
print("Dictionary is not equal to {'one': 1, 'two': 2}:", my_dict != {"one": 1, "two": 2})  # Checking inequality: Output: True

print("Value for key 'four':", my_dict.get("four", "Not Found"))  # Accessing value with default: Output: Not Found
my_dict["four"] = 4  # Adding a new key-value pair
print("Dictionary after adding 'four':", my_dict)  # Output: Dictionary after adding 'four': {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_dict["two"] = 22  # Updating an existing key-value pair
print("Dictionary after updating 'two':", my_dict)  # Output: Dictionary after updating 'two': {'one': 1, 'two': 22, 'three': 3, 'four': 4}
print("Keys in the dictionary:", my_dict.keys())  # Output: Keys in the dictionary dict_keys(['one', 'two', 'three', 'four'])
print("Values in the dictionary:", my_dict.values())  # Output: Values in the dictionary

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Iterating through key-value pairs
    # Output: Key: one, Value: 1
    # Output: Key: two, Value: 22
    # Output: Key: three, Value: 

print(my_dict.pop("three"))  # Removing a key-value pair: Output: 3
print("Dictionary after popping 'three':", my_dict)  # Output: Dictionary after popping 'three': {'one': 1, 'two': 22, 'four': 4}

print(my_dict.popitem())  # Removing the last inserted key-value pair: Output: ('four', 4)
print("Dictionary after popping last item:", my_dict)  # Output: Dictionary after popping last item: {'one': 1, 'two': 22}

del my_dict["two"]  # Deleting a key-value pair
print("Dictionary after deleting 'two':", my_dict)  # Output: Dictionary after deleting 'two': {'one': 1}

print(my_dict.get("one", "Not Found"))  # Accessing value with default: Output: 1
print(my_dict.get("two", "Not Found"))  # Accessing non-existing key with default: Output: Not Found



"""
Comprehensions
===========================
"""
# List comprehension
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_list = [name for name in names if len(name) > 3]
print("New List:", new_list)  # Output: New List: ['Alice', 'Charlie', 'David']


# Dictionary comprehension
new_dict = {name: len(name) for name in names if len(name) > 3}
print("New Dictionary:", new_dict)  # Output: New Dictionary: {'Alice': 5, 'Charlie': 7, 'David': 5}

# Set comprehension
new_set = {name[0] for name in names if len(name) > 3}
print("New Set:", new_set)  # Output: New Set: {'A', 'C', 'D'}
