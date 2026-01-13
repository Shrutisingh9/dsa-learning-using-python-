# loops
# for loops
# range function
for i in range(1, 6):
    print(i)

# traversing a list
arr = [10, 20, 30]

for x in arr:
    print(x)

# traversing a string
s = "python"
for ch in s:
    print(ch)
    
# while loops
n = 5
while n > 0:
    print(n)
    n -= 1

# nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# loops control statements
# break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# pass statement
for i in range(5):
    pass

# else with loops
for i in range(5):
    print(i)
else:
    print("Loop finished")
    
    
# Sum of digits
n = 123
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print(sum)

# Count vowels in string
s = "education"
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1
        
# Reverse a number
n = 123
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

# Q1 Print numbers from 1 to N
N = 10
for i in range(1, N + 1):
    print(i)

# Q2 Print even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i)
    
# Q3 Sum of first N natural numbers
natural_num = int(input("Enter a number for sum of N natural numbers: "))
sum = 0
for i in range(1, natural_num + 1):
    sum += i
print("Sum of first", natural_num, "natural numbers is:", sum)

# Q4 Print multiplication table of a number
num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
# Q5 Count digits in a number
n = int(input("Enter a number to count the digit of number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count)

# Reverse a number
n = int(input("Enter a number to reverse: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed number:", rev)

# Check palindrome number (palindrome reads same backward as forward)
n=int(input("Enter a number to check palindrome: "))
original=n

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not palindrome")

# Find factorial of a number
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# Check prime number
n=int(input("Enter a number to check prime: "))
is_prime = True 

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print("Prime")
else:
    print("Not prime")  

# Print all prime numbers from 1 to 100
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        
# *
# **
# ***
# ****
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
    
# 1
# 12
# 123
# 1234
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# ****
# ***
# **
# *
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Count vowels and consonants
n=input("Enter a string to count vowels and consonants: ")
vowels = 0
consonants = 0  
for ch in n.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)    

# Find sum of list elements
n=int(input("Enter number of elements in list to find sum: "))
sum = 0
for i in range(n):
    num = int(input("Enter element: "))
    sum += num
print("Sum of list elements:", sum) 

# Find maximum and minimum
n = int(input("Enter number of elements to find max and min: "))

numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Maximum element:", max_val)
print("Minimum element:", min_val)

# Remove duplicates from list
n= int(input("Enter number of elements to remove duplicates: " ))

numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)

# Count frequency of characters





# Linear search



# Check if list is sorted



# Find second largest element



# Count even and odd numbers




# Find GCD of two numbers






# Menu-driven calculator




# ATM simulation




# Guess the number game

