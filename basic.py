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

# conditional statements examples
num = int(input())

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q1 Check even/odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q2 Find largest of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest is:", a)
elif b > c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

# Q3Leap year check
year = int(input("Enter year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")