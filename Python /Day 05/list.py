# 1. Creating a sample list
my_list = [10, 20, 30, 40, 50, 20, 30, 60, 70, 10]

# --- Indexing ---
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# --- Slicing ---
print("First 3 elements:", my_list[:3])
print("Last 3 elements:", my_list[-3:])
print("Middle elements:", my_list[2:7])

# --- Modifying list ---
my_list[1] = 25
print("List after modification:", my_list)

# --- Adding elements ---
my_list.append(80)
my_list.insert(2, 15)
print("List after adding elements:", my_list)

# --- Removing elements ---
my_list.remove(25)      # removes first occurrence of 25
popped_item = my_list.pop()  # removes last element
print("Removed item:", popped_item)
print("List after removals:", my_list)

# --- List comprehension ---
squares = [x**2 for x in range(1, 6)]
print("Squares using list comprehension:", squares)

# --- Reversing a list ---
reversed_list = my_list[::-1]
print("Reversed list (slicing):", reversed_list)

# Another method
my_list.reverse()
print("Reversed list (in-place):", my_list)

# --- Finding duplicates ---
duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print("Duplicate elements:", duplicates)

# --- Removing duplicates (keeping order) ---
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List without duplicates:", unique_list)
"""
OUTPUT
  First element: 10
  Last element: 10
  First 3 elements: [10, 20, 30]
  Last 3 elements: [60, 70, 10]
  Middle elements: [30, 40, 50, 20, 30]
  List after modification: [10, 25, 30, 40, 50, 20, 30, 60, 70, 10]
  List after adding elements: [10, 25, 15, 30, 40, 50, 20, 30, 60, 70, 10, 80]
  Removed item: 80
  List after removals: [10, 15, 30, 40, 50, 20, 30, 60, 70, 10]
  Squares using list comprehension: [1, 4, 9, 16, 25]
  Reversed list (slicing): [10, 70, 60, 30, 20, 50, 40, 30, 15, 10]
  Reversed list (in-place): [10, 70, 60, 30, 20, 50, 40, 30, 15, 10]
  Duplicate elements: [10, 30]
  List without duplicates: [10, 70, 60, 30, 20, 50, 40, 15]
"""
