# function
def greet():
    print("hello")
    
greet()

def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

# types of funtion 
# function withno arguments and no return
def hello():
    print("Hello World")

hello()

# function with arguments and no return
def print_sum(a, b):
    print(a + b)

print_sum(5, 6)

# function with arguments and return
def square(n):
    return n * n
result = square(4)
print("Square:", result)

# return statement
def test():
    return 5
    print("Hello")  # never executed

# types of arguments
# positional arguments
def sub(a, b):
    return a - b

sub(5, 3)

# keyword arguments
sub(b=3, a=5)

# default arguments
def greet(name="User"):
    print("Hello", name)

greet()
greet("Shruti")

# variable-length arguments
# *args
def total(*nums):
    return sum(nums)

total(1, 2, 3, 4)

# **kwargs
def info(**data):
    print(data)

info(name="A", age=20)

# local variables
def fun():
    x = 10
    print(x)

# global variables
x = 5

def fun():
    global x
    x = 10
    print(x)
    
# nested functions
def outer():
    def inner():
        print("Inner")
    inner()

# recursive function 
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# lambda function
square = lambda x: x * x
print(square(5))

# practice questions
# Function to add two numbers
def add(a,b):
    return a+b
a=int(input("enter first number to add: "))
b=int(input("enter second number to add: "))
print ("sum", add(a, b))

# Function to find square of a number
def square(n):
    return n*n
n=int(input("enter a number to find square: "))
print("square", square(n))

# Function to check even or odd
def odd_even(num):
    if num %2 == 0:
        return "even"
    else:
        return "odd"
num= int(input("enter a num to check odd or even: "))
print(odd_even(num))

# Function to find maximum of two numbers
def max(a, b):
    if a>b:
        return a
    else:
        return b
a= int(input("enter first number to find max: "))
b=int(input("enter second number to find max: "))
print("maximus is", max(a, b))

# Function to convert Celsius to Fahrenheit
def temp(celsius):
    return (celsius *9/5) +32
celsius= float(input("enter temperature in celsius: "))
print("temperature in fahrenheit is ", temp(celsius))

# Function to find factorial
def factorial(n):
    if n ==0:
        return 1
    return n * factorial(n-1)
n = int(input("enter number to find factorial: "))
print("factorial is ", factorial(n))

# Function to check prime
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n= int(input("enter number to check prime: "))
if prime(n):
    print("prime number")
else:
    print("not a prime number")
        
# Function to reverse a number
def reverse(n):
    rev = 0
    while n >0:
        digit = n %10
        rev = rev *10 + digit
        n = n //10
    return rev
n= int(input("enter number to reverse: "))
print("reversed number is ", reverse(n))        

# Function to check palindrome number
def palindrome(n):
    return n == reverse(n)
n= int(input("enter number to check palindrome: "))
if palindrome(n):       
    print("palindrome")
else:
    print("not a palindrome")   
# Function to find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
a= int(input("enter first number to find GCD: "))
b= int(input("enter second number to find GCD: "))
print("GCD is ", gcd(a, b)) 

# Function to find maximum in list
def max_in_list(lst):
    return max(lst)
lst = [int(x) for x in input("enter numbers separated by space: ").split()]
print("maximum in list is ", max_in_list(lst))  

# Function to count vowels in string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = input("enter a string to count vowels: ")
print("number of vowels is ", count_vowels(s))  

# Function to reverse a string  
def reverse_string(s):
    return s[::-1]
s = input("enter a string to reverse: ")
print("reversed string is ", reverse_string(s)) 

# Function to remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))
lst = [int(x) for x in input("enter numbers separated by space: ").split()]
print("list after removing duplicates is ", remove_duplicates(lst))

# Function to check anagram
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)
s1 = input("enter first string: ")
s2 = input("enter second string: ") 
if anagram(s1, s2):
    print("anagram")
else:
    print("not anagram")

# Recursive factorial
def factorial_recursive(n): 
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)   
n = int(input("enter number to find factorial recursively: "))
print("factorial is ", factorial_recursive(n))  

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("enter n to find nth Fibonacci number recursively: "))
print("nth Fibonacci number is ", fibonacci_recursive(n))   

# Recursive sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
n = int(input("enter number to find sum of digits recursively: "))
print("sum of digits is ", sum_of_digits(n))

# Recursive power (xⁿ)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
x = int(input("enter base: "))
n = int(input("enter exponent: "))
print("power is ", power(x, n))

# Recursive palindrome check
def palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome_recursive(s[1:-1])
s = input("enter a string to check palindrome recursively: ")
if palindrome_recursive(s):
    print("palindrome")
else:
    print("not a palindrome")

# Linear search using function
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
lst = [int(x) for x in input("enter numbers separated by space: ").split()]
target = int(input("enter number to search: "))
index = linear_search(lst, target)
if index != -1:
    print("found at index", index)
else:
    print("not found")

# Binary search using function
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Count frequency using function
def count_frequency(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count    
lst = [int(x) for x in input("enter numbers separated by space: ").split()]
target = int(input("enter number to count frequency: "))
frequency = count_frequency(lst, target)
print("frequency is ", frequency)

# Check if list is sorted
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
lst = [int(x) for x in input("enter numbers separated by space: ").split()]
if is_sorted(lst):  
    print("list is sorted")
else:
    print("list is not sorted") 

# Second largest element
def second_largest(lst):
    first = second = float('-inf')
    for number in lst:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None  
lst = [int(x) for x in input("enter numbers separated by space: ").split()]
result = second_largest(lst)
if result is not None:
    print("second largest element is ", result)
else:
    print("no second largest element")
