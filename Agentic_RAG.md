1. Number‑Based Coding Questions
Common beginner‑level tasks:

========================================================
Reverse an integer.


========================================================
## Check Armstrong number.
========================================================

num = int(input("Enter a number: "))

power = len(str(num))

if sum(int(d) ** power for d in str(num)) == num:
  ptrint("Armstrong")
else:
  print("not armstrong")

========================================================
# Check if a number is prime.
========================================================

n = int(input("Enter a number: "))

def is_prime(n):
  if n <= 0:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

print(is_prime(n))

========================================================
## Generate Fibonacci series (iterative & recursive).
========================================================

n = int(input("Enter number of terms: "))

a , b = 0, 1

for i in range(n):
  print(a, end = " ")
  a, b = b, a + b

========================================================
## Check palindrome number (iterative & recursive).
========================================================

num = input("Enter number of terms: ")

if num == num[::-1]:
  print("is Palindrome")
else:
  print("Is not Palindrome")
========================================================
## Find greatest among three numbers.
========================================================

a = int(input("Enter number of terms: "))
b = int(input("Enter number of terms: "))
c = int(input("Enter number of terms: "))

if a >= b and a >= c:
  print ("Greatest number is:", a)
elif b >= a and b >= c:
  print ("Greatest number is:", b)
else:
  print ("Greatest number is:", c)

============OR==============================================
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Greatest number is:", max(a, b, c))

========================================================
## Sum of digits using recursion.
========================================================

num = input("Enter number of terms: ")

print(sum(int(digit) for digit in num))

## Recursive method:

def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))

========================================================
Swap numbers (with/without third variable).
========================================================
##Swap with a Third Variable

a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

##Swap Without a Third Variable

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

========================================================
## Find prime factors.
========================================================

num = int(input("Enter a number: "))

i = 2

while num > 1:
  if num % i == 0:
    print(i, end = " ")
    num //= i
  else:
    i += 1


========================================================
Compute factorial (loop & recursion).
========================================================

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
  fact *= i

print(fact)


========================================================
Check if a string is a palindrome.
========================================================

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


========================================================
Find first non‑repeating character.
========================================================

s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")


========================================================
Reverse words in a sentence.
========================================================

sentence = input("Enter a sentence: ")

result = []

for word in sentence.split():
    result.append(word[::-1])

print(" ".join(result))


========================================================
Generate all permutations of a string.
========================================================
##Method 1"

from itertools import permutations

s = input("Enter a string: ")

for i in premutations(s):
  print(" ".join(i))
 

## Method 2

def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # swap
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]  # backtrack

string = "ABC"
permute(list(string), 0, len(string) - 1)

========================================================
Validate email using regex.
========================================================
import re

email = input("Enter email: ")
mobile = input("Enter mobile number: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^[6-9]\d{9}$'

print("Valid Email" if re.match(email_pattern, email) else "Invalid Email")
print("Valid Mobile" if re.match(mobile_pattern, mobile) else "Invalid Mobile")

========================================================
## Find mobile number & email id from given sentences
========================================================

import re

text = """
Contact me at kriti@gmail.com or support@yahoo.com.
My mobile numbers are 9876543210 and 9123456789.
"""

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
mobiles = re.findall(r'[6-9]\d{9}', text)

print("Emails:", emails)
print("Mobile Numbers:", mobiles)

========================================================
Reverse a linked list.
========================================================
def reverse(head):
    prev = None

    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    return prev

## Note: "I use three pointers: current node, previous node, and next node. For each node, I reverse its link,
move the pointers forward, and finally return the last processed node as the new head."

========================================================
Implement stack and queue using lists.
========================================================

Stack Using List (LIFO - Last In First Out)

stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop
print("Popped:", stack.pop())

print("Stack after pop:", stack)


========================================================
## Word frequency using dictionaries.
========================================================

sentence = input("Enter a sentence: ")

words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

========================================================
Merge two sorted lists.
========================================================

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged = sorted(list1 + list2)

print(merged)

========================================================

list1 = [1, 3, 5]
list2 = [2, 4, 6]

list1.extend(list2)
list1.sort()

print(list1)

========================================================
## Two‑sum problem.
Binary search implementation.
========================================================

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)


## Optimized method : HashMap

nums = [2, 7, 11, 15]
target = 9

lookup = {}

for i, num in enumerate(nums):
    diff = target - num

    if diff in lookup:
        print(lookup[diff], i)

    lookup[num] = i

========================================================
## Rotate a matrix (90 degrees).
========================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose
for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Reverse each row
for row in matrix:
    row.reverse()

for row in matrix:
    print(row)

========================================================
## Longest substring without repeating characters.
========================================================

s = "abcabcbb"

seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)


========================================================
Class vs instance variables.
========================================================


========================================================
## Implement inheritance & multiple inheritance.
========================================================

1. Single Inheritance

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()


2.  Multiple Inheritance

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skills()
c.talent()

========================================================
## Encapsulation examples.
Implement a simple class (e.g., BankAccount).
========================================================
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)

print("Balance:", acc.get_balance())

========================================================
## Implement decorators.
========================================================

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()


========================================================
## Context managers (with statement).
========================================================

with open("data.txt", "r") as file:
    content = file.read()
    print(content)




Explain and work around the GIL.
Design an LRU Cache.
