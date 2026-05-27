#print name,age,city
name = "shubhangi"
age = 20
city = "Mumbai"
print("Name:",name)
print("Age:",age)
print("City:",city)

#arithmetic operations
num1 = 20
num2 = 5
print("Addition:", num1 + num2)
print("subtraction:", num1 - num2)
print("multiplication:", num1 * num2)
print("division:", num1 / num2)
print("modulus:", num1 % num2)
print("exponentiation:", num1 ** num2)
print("floor division:", num1 // num2)

#check whether a number is even or odd
number = 15
if number % 2 == 0:
    print("even number")
else:
    print("odd number")

#check whether a number is positive, negative or zero
num = 10
if num > 5:
    print("positive number")
elif num < 5:
    print("negative number")
else:
    print("zero")

#find the largest among three numbers
num1 = 10
num2 = 20
num3 = 15
if num1 >= num2 and num1 >= num3:
    print("largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("largest number is:", num2)
else:
    print("largest number is:", num3)

#swap two variables with and without using a temporary variable
a = 10
b = 20
#using a temporary variable
temp = a
a = b
b = temp
print(a)
print(b)
#without using a temporary variable
a,b = b,a
print(a)
print(b)

#Convert Celsius to Fahrenheit and vice versa
celsius = float(input("Enter Celsius: "))

fahrenheit = (9/5 * celsius) + 32

print(fahrenheit)



#calculate simple interest
principal = 10000
rate = 5
time = 2

si = (principal * rate * time) / 100

print("print Interest =", si)

#Calculate area of circle, rectangle, and triangle.
#circle
radius = 5
area = 3.14 * radius * radius

print("Area of Circle =", area)

#rectangle
length = 10
breadth = 5
area = length * breadth

print("Area of Rectangle =", area)

#triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height

print("Area of Triangle =", area)

#Check whether a year is a leap year
year = 2026
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year,"is not leap year")

#Print multiplication table of a number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#Find the sum of first N natural numbers.
n = int(input("Enter a number: "))
sum = n*(n+1)//2
print("sum=" ,sum)

#Calculate factorial of a number
num = 3
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)

#Print Fibonacci series up to N terms
n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Check whether a number is prime.
num = int(input("enter number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

#Print all prime numbers in a given range
for num in range(1, 21):

    if num > 1:
        for i in range(2, num):

            if num % i == 0:
                break
        else:
            print(num)

#reverce a number
num = 123456789
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

#Check whether a number is palindrome
num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#Check whether a number is Armstrong number
num = 153

temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#Count digits in a number
num = int(input("Enter number: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print(count)

#Reverse a string
text =("Hello world")

reverse = text[::-1]

print("Reversed string =", reverse)

#Check whether a string is palindrome
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Count vowels in a string
name = ("Shubhangi Kanet")

count = 0

for ch in name:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Total vowels =", count)

#Count frequency of characters in a string
name = input("Enter string: ")

for ch in name:
    print(ch, "=", name.count(ch))

#Count words in a sentence
text = input("Enter sentence: ")

words = text.split()
print(len(words))

#Remove spaces from a string
text = input("Enter string: ") 

result = text.replace(" ",".")

print(result)


#Compress a string (example: aaabb → a3b2).
text = input("Enter string: ")

count = 1

for i in range(len(text)-1):

    if text[i] == text[i+1]:
        count += 1

    else:
        print(text[i] + str(count), end="")
        count = 1

print(text[-1] + str(count))

#Find the longest word in a sentence
text = input("Enter sentence: ")

words = text.split()

longest = max(words, key=len)

print("Longest word =", longest)


