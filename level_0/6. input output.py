# input and output
# input
# python uses the input() function to take input from the user
# x = input()

# taking user input
name = input("enter your name: ")
print(name)

# taking multiple inputs
# method 1: using multiple input lines
# a = int(input())
# b = int(input())

# method 2: single line input
# a, b =  map(int, input().split())

# taking list (array) as input
# method 1: using loop
n = int(input("enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print("array is ", arr)

# method 2: using map
# arr = list(map(int, input().split()))
# print("array is ", arr)

# output
# python uses print()

print("hello")
# priniting multiple values
a = 10
b = 20
print(a, b)

# seprator(sep)
print(1, 2, 3, sep="-")

# end
print("hello", end=" ")
print("world")

# formatted output
# using f-string
name = "Shruti"
age = 20
print(f"My name is {name} and I am {age} years old.")

# using format()
print("Name: {} Age: {}".format(name, age))

# output of list and string
arr = [1, 2, 3]
print(arr)

s = "Python"
print(s)

# Practice Questions
# Take name and print greeting
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Take two numbers and print sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum is {a + b}")

# Take length and breadth and print area
length = float(input("enter length: "))
breadth = float(input("enter breadth: "))
area = length * breadth 
print(f"Area is {area}")

# Take temperature and convert to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is {fahrenheit}")

# Take radius and print circle area
import math
radius = float(input("Enter radius: "))
circle_area = math.pi * radius * radius
print(f"Area of circle is {circle_area}")

# Take N elements and print them
n = int(input("enter number of elements: "))
elements = list(map(int, input("Enter the elements: ").split()))
print("The elements are:", elements)

# Print sum of array
print("Sum of array is:", sum(elements))

# Print maximum element
print("Maximum element is:", max(elements))

# Count even numbers
even_count = sum(1 for x in elements if x % 2 == 0)
print("Count of even numbers is:", even_count)

# Reverse array
reversed_elements = elements[::-1]
print("Reversed array is:", reversed_elements)

# Take string and print length
s = input("enter a string: ")
print("Length of string is:", len(s))

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in s if char in vowels)
print("Count of vowels is:", vowel_count)

# Reverse string
reversed_string = s[::-1]
print("Reversed string is:", reversed_string)

# Check palindrome
is_palindrome = s == reversed_string
print("Is palindrome?", is_palindrome)

# Count words
word_count = len(s.split())
print("Count of words is:", word_count)

# Take name & marks, print formatted output
name = input("Enter name: ")
marks = float(input("Enter marks: "))
print(f"Student Name: {name}, Marks: {marks}")

# Take 3 numbers and print average
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
average = (n1 + n2 + n3) / 3
print(f"Average is: {average}")

# Take sentence and count characters
sentence = input("Enter a sentence: ")
char_count = len(sentence)
print(f"Number of characters: {char_count}")

# Take list of strings
strings = input("Enter strings separated by space: ").split()
print("You entered:", strings)

# Take input until user enters 0
numbers = []
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)
print("You entered:", numbers)