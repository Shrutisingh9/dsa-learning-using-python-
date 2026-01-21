# arrays
arr = [10, 20, 30, 40]

# can store mixed data types
data = [10, "hi", 3.5, True]


# accessing elements
arr = [5,10,15,20]

print(arr[0])
print(arr[-1])

# traversing an array
# using for 
for i in arr:
    print(i)
    
# using index
for i in range(len(arr)):
    print(arr[i])
    
# inserting elements
arr.append(50)
arr.insert(1, 100)

# deleting elements
arr.pop()
arr.pop(1)
arr.remove(10)

# updating elements
arr[2] = 999

# length of array
len(arr)

# searching in array
if 20 in arr:
    print("Found")
    
# basic array programs
# find sum
def array_sum(arr):
    return sum (arr)

# find max
def find_max(arr):
    return max(arr)

# reverse array
arr.reverse()

# PRACTICE QUESTIONS
# Find largest element
n = int(input("enter number of elements: "))
arr= []
for i in range(n):
    num = int(input(f"enter elements{i+1}: "))
    arr.append(num)
largest = arr[0]
for i in range(1, n):
    if arr[i]>largest:
        largest = arr[i]
print("largest element is ", largest)
    
# Find smallest element
n = int(input("enter number of elements: "))
arr= []
for i in range(n):
    num = int(input(f"enter elements{i+1}: "))
    arr.append(num)
smallest = arr[0]
for i in range(1, n):
    if arr[i]<smallest:
        smallest = arr[i]
print("smallest element is ", smallest)
# Reverse array
n = int(input("enter numbers of elements: "))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    arr.append(num)
reversed_arr = []
for i in range(n-1, -1, -1):
    reversed_arr.append(arr[i])
print("reversed array is ", reversed_arr)

# Find sum of elements
n = int(input("enter number of elements: " ))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    arr.append(num)
sum_elements = sum(arr)
print("sum of elements is ", sum_elements)

# Linear search
n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    arr.append(num)
key = int(input("enter element to search: "))
found = False
for i in range(n):
    if arr[i] ==key:
        print(f"elemtnets found at position {i+1}")
        found = True
        break
if not found:
    print("element not found")
        
# Count even & odd numbers
n = int(input("enter number of elements: "))
arr =[]
for i in range(n):
    num = int(input(f"enter elements {i+1}"))
    arr.append(num)
even_count = 0
odd_count = 0
for i in range(n):
    if arr[i]%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even count is ", even_count)
print("odd count is ", odd_count)

# Remove duplicates
n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"enter numbers {i+1}: "))
    arr.append(num)
unique_arr = []
for i in range(n):
    if arr[i] not in unique_arr:
        unique_arr.append(arr[i])
print("array after removing duplicqates is ", unique_arr)

# Second largest element
n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    arr.append(num)
first = second = float('-inf')
for i in range(n):
    if arr[i]>first:
        second = first
        first = arr[i]
    elif first > arr[i] > second:
        second = arr[i]
if second == float('-inf'):
    print("there is no second largest element")
else:
    print("second largest element is ", second)

# Rotate array by 1

# Check if array is sorted