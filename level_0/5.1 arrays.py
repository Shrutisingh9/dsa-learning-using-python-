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
n = int(input("enter number of elements to find largest element: "))
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
n = int(input("enter number of elements to find smallest element: "))
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
n = int(input("enter numbers of elements to reverse array: "))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    arr.append(num)
reversed_arr = []
for i in range(n-1, -1, -1):
    reversed_arr.append(arr[i])
print("reversed array is ", reversed_arr)

# Find sum of elements
n = int(input("enter number of elements to find sum of array: " ))
arr = []
for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    arr.append(num)
sum_elements = sum(arr)
print("sum of elements is ", sum_elements)

# Linear search
n = int(input("enter number of elements for linear search: "))
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
n = int(input("enter number of elements to count odd even: "))
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
n = int(input("enter number of elements to remove duplicates: "))
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
n = int(input("enter number of elements to find second largest element: "))
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
n = int(input("enter number of elements to rotate element: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter element {i+1}: ")))
temp = arr[0]
for i in range(n-1):
    arr[i] = arr[i+1]
arr[n-1] = temp
print("array after left rotation is ", arr)

temp = arr[n-1]
for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = temp
print("array after right rotation is ", arr)

# Check if array is sorted
n = int(input("enter number of elements to check if array is sorted: "))
arr = []
for i in range(n):
    arr.append(int(input("enter elements")))
sorted = True
for i in range(n-1):
    if arr[i]>arr[i+1]:
        sorted = False
        break
if sorted:
    print("array is sorted")
else: 
    print("array is not sorted")
