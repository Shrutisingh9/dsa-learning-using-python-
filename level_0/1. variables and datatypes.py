# variable and data type examples
a = 10          # int
b = 3.5         # float
c = "Hello"     # string
d = True        # boolean
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Q1 Take two numbers and print their sum, difference, product, division

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

# Q2 Convert kilometers to meters
kilometers = float(input("Enter distance in kilometers: "))
meters = kilometers * 1000
print("Distance in meters:", meters)

# Q3 Take name and age, print in one line
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:", name, "Age:", age)