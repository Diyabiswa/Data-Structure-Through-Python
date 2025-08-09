# --- Creating tuples ---
fruits = ("apple", "banana", "cherry", "banana")
coordinates = (4, 7)

print("Fruits tuple:", fruits)
print("Coordinates tuple:", coordinates)

# --- Accessing elements ---
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# --- Slicing ---
print("First two fruits:", fruits[:2])
print("Middle fruits:", fruits[1:3])

# --- Tuple immutability demonstration ---
try:
    fruits[0] = "mango"  # ❌ This will raise an error
except TypeError:
    print("Error: Tuples are immutable!")

# --- Swapping values using tuples ---
a = 5
b = 10
print("\nBefore swapping: a =", a, ", b =", b)
a, b = b, a  # Swap using tuple unpacking
print("After swapping: a =", a, ", b =", b)

# --- Handling coordinate pairs ---
point1 = (2, 3)
point2 = (5, 7)

# Calculate distance between two coordinates
distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
print("\nDistance between points:", distance)

# --- Tuple methods ---
print("\nCount of 'banana':", fruits.count("banana"))
print("Index of 'cherry':", fruits.index("cherry"))

# --- Tuple packing and unpacking ---
person = ("Alice", 25, "Engineer")  # Packing
name, age, profession = person      # Unpacking
print(f"\nName: {name}, Age: {age}, Profession: {profession}")
"""
OUTPUT
  Fruits tuple: ('apple', 'banana', 'cherry', 'banana')
  Coordinates tuple: (4, 7)
  First fruit: apple
  Last fruit: banana
  First two fruits: ('apple', 'banana')
  Middle fruits: ('banana', 'cherry')
  Error: Tuples are immutable!

  Before swapping: a = 5 , b = 10
  After swapping: a = 10 , b = 5

  Distance between points: 5.0

  Count of 'banana': 2
  Index of 'cherry': 2

  Name: Alice, Age: 25, Profession: Engineer
"""
