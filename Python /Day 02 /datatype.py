# Basic Data Types in Python

# Integer
integer_example = 42
print(f"Integer: {integer_example} Type: {type(integer_example)}")

# Float
float_example = 3.14
print(f"Float: {float_example} Type: {type(float_example)}")

# String
string_example = "Hello, Python!"
print(f"String: {string_example} Type: {type(string_example)}")

# List
list_example = [1, 2, 3, "four", 5.5]
print(f"List: {list_example} Type: {type(list_example)}")

# Tuple
tuple_example = (10, 20, "thirty", 40.5)
print(f"Tuple: {tuple_example} Type: {type(tuple_example)}")

# Dictionary
dictionary_example = {"name": "Diya", "age": 19, "grades": [85, 90, 95]}
print(f"Dictionary: {dictionary_example} Type: {type(dictionary_example)}")

# Set
set_example = {1, 2, 3, 4, 4, 5}  # Sets automatically remove duplicates
print(f"Set: {set_example} Type: {type(set_example)}")

# Boolean
boolean_example = True
print(f"Boolean: {boolean_example} Type: {type(boolean_example)}")

"""
OUTPUT:
        Integer: 42 Type: <class 'int'>
        Float: 3.14 Type: <class 'float'>
        String: Hello, Python! Type: <class 'str'>
        List: [1, 2, 3, 'four', 5.5] Type: <class 'list'>
        Tuple: (10, 20, 'thirty', 40.5) Type: <class 'tuple'>
        Dictionary: {'name': 'Diya', 'age': 19, 'grades': [85, 90, 95]} Type: <class 'dict'>
        Set: {1, 2, 3, 4, 5} Type: <class 'set'>
        Boolean: True Type: <class 'bool'>
"""
