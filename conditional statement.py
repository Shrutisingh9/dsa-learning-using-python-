# conditional statements examples
num = int(input("Enter number:"))

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