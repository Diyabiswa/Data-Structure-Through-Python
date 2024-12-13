#Variables and comments
name = "Diya"
age = 19
height = 5.2
print("Name:", name)
print("Age:", age)
print("Height:", height) 

# Input/output
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height: "))
print(f"Hello {user_name}, you are {user_age} years old and {user_height} feet tall.")

# Indentation example
if user_age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Simple programs
# Pattern
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
for i in range(rows, 0, -1):
    print("* " * i)

# Area calculations
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14 * radius ** 2
print("Area of the circle:", area_circle)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print("Area of the rectangle:", area_rectangle)

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print("Area of the triangle:", area_triangle)

# Function example with comments
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"The number {num} is {result}.")
"""
OUTPUT:
      Name: Diya  
      Age: 19
      Height: 5.2
      Enter your name: Zhao lusi
      Enter your age: 25
      Enter your height: 5.5
      Hello Zhao lusi, you are 25 years old and 5.5 feet tall.
      You are an adult.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
      Enter the radius of the circle: 2
      Area of the circle: 12.56
      Enter the length of the rectangle: 4
      Enter the width of the rectangle: 2
      Area of the rectangle: 8.0
      Enter the base of the triangle: 4
      Enter the height of the triangle: 4
      Area of the triangle: 8.0
      Enter a number: 4
      The number 4 is Even.

"""
