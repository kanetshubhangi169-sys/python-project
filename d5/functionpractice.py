#create a function to add a two numbers 
def num(a , b):
    return a + b
result = num(2 , 5)

print(result)

#Create a function to check whether a number is even or odd
def my_function(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
result = my_function(5)
print(result)

#Create a function to find factorial of a number
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact
result = factorial(5)
print("factorial = " , result)

#Create a function to check whether a number is prime
def prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")


#Create a function to reverse a string
def reverse(text):
    return text[::-1]

word = "Welcome"

result = reverse(word)
print(result)

#Create a function to calculate Fibonacci series up to N terms
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

number = int(input("Enter number of terms: "))

result = fibonacci(number)



#Create a function to find largest element in a list
def largest(numbers):

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

my_list = [12, 45, 7, 89, 23]

result = largest(my_list)
print(result) 

# Create a recursive function for factorial calculation
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = 7

result = factorial(num)

print(result)

#Create a recursive function for Fibonacci series
def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = 6

for i in range(number):
    print(fibonacci(i), end=" ")


#Create a lambda function to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers are:", even_numbers)


#Create a function that accepts variable-length arguments (*args)
def add_numbers(*args):
    total = 0

    for num in args:
        total += num

    return total


result = add_numbers(10, 20, 30, 40)

print(result)

#Create a function that accepts keyword arguments (**kwargs)
def student_info(**kwargs):

    for key, value in kwargs.items():
        print(key, ":" ,value)

result = student_info(name="rahul", age = 21)

    
