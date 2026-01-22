# string
s = "Hello"

# accessing characters
print(s[0])
print(s[-1])

# traversing string
for ch in s:
    print(ch)
    
# string immutability
# s[0] = 'h'  # This will raise an error
s = 'h' + s[1:]  # creating a new string

# string slicing
s = "python"
print(s[0:3])  # 'pyt'
print(s[2:])   # 'thon'
print(s[:4])   # 'pyth'

# string reverse
s = "hello"
print(s[::-1]) # 'olleh'

# count vowels
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
print(count_vowels("Hello World"))

# palindrome check
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# preactice questions
# Reverse a string
s = input("Enter a string to reverse: ")
reversed_s = ""
for i in range(len(s)-1, -1, -1):
    reversed_s += s[i]
print("Reversed string is:", reversed_s)

# Count vowels & consonants
s = input("Enter a string to count vowels and consonants: ")
vowel_count = 0
consonant_count = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# Check palindrome  
s = input("Enter a string to check palindrome: ")       
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Count frequency of characters
s = input("Enter a string to count frequency of characters: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character frequencies:", freq)

# Check anagram
s1 = input("Enter first string for anagram check: ")
s2 = input("Enter second string for anagram check: ")
if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Remove spaces
s = input("Enter a string to remove spaces: ")
s_no_spaces = ""
for ch in s:
    if ch != ' ':
        s_no_spaces += ch   
print("String without spaces:", s_no_spaces)    

# Find first non-repeating character
s = input("Enter a string to find first non-repeating character: ")
char_count = {}
for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
first_non_repeating = None
for ch in s:
    if char_count[ch] == 1:
        first_non_repeating = ch
        break
if first_non_repeating:
    print("First non-repeating character is:", first_non_repeating)
else:
    print("All characters are repeating.")

# Count words
s = input("Enter a string to count words: ")
words = s.split()
print("Number of words:", len(words))   

# Convert string to title case
s = input("Enter a string to convert to title case: ")
print("Title case:", s.title())

# Replace vowels with *
s = input("Enter a string to replace vowels with *: ")
vowels = "aeiouAEIOU"
for vowel in vowels:
    s = s.replace(vowel, "*")
print("String with vowels replaced:", s)