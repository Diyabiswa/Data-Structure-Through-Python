# --- Creating a dictionary ---
student = {
    "name": "Alice",
    "age": 21,
    "course": "BCA",
    "marks": [85, 90, 78]
}

print("Initial Dictionary:", student)

# --- Accessing values ---
print("\nStudent Name:", student["name"])
print("Student Age:", student.get("age"))  # safer method

# --- Adding & updating key-value pairs ---
student["grade"] = "A"        # adding new key
student["age"] = 22           # updating existing key
print("\nAfter adding/updating:", student)

# --- Deleting entries ---
removed_value = student.pop("course")   # removes and returns value
print("\nRemoved 'course':", removed_value)
del student["grade"]                    # deletes key-value pair
print("After deletion:", student)

# --- Iterating through dictionary ---
print("\nIterating through keys:")
for key in student:
    print(f"{key} : {student[key]}")

print("\nIterating through key-value pairs:")
for key, value in student.items():
    print(f"{key} : {value}")

# --- Dictionary methods ---
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# --- Problem 1: Count word frequency ---
text = "apple banana apple orange banana apple"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord Frequency:", word_count)

# --- Problem 2: Student marks lookup ---
students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

name = "Bob"
print(f"\nMarks of {name}:", students_marks.get(name, "Not Found"))
"""
OUTPUT
  Initial Dictionary: {'name': 'Alice', 'age': 21, 'course': 'BCA', 'marks': [85, 90, 78]}

  Student Name: Alice
  Student Age: 21

  After adding/updating: {'name': 'Alice', 'age': 22, 'course': 'BCA', 'marks': [85, 90, 78], 'grade': 'A'}

  Removed 'course': BCA
  After deletion: {'name': 'Alice', 'age': 22, 'marks': [85, 90, 78]}

  Iterating through keys:
  name : Alice
  age : 22
  marks : [85, 90, 78]

  Iterating through key-value pairs:
  name : Alice
  age : 22
  marks : [85, 90, 78]
  
  Keys: dict_keys(['name', 'age', 'marks'])
  Values: dict_values(['Alice', 22, [85, 90, 78]])
  Items: dict_items([('name', 'Alice'), ('age', 22), ('marks', [85, 90, 78])])

  Word Frequency: {'apple': 3, 'banana': 2, 'orange': 1}

  Marks of Bob: 92
"""
