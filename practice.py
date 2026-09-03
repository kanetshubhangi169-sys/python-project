# for i in range(1,5):
#     for j in range(4):
#         if j<i-1:
#           print("*",end="")
#         elif j==i-1:
#           print(i,end="")    
#         else:
#           print("#",end="")

# print()

# for i in range(1,5):
#   for j in range(1,5):
#     print(("*"), end= " ")

# print()

# print("1###")
# print("*2##")
# print("**3#")
# print("***4")

# print ("prime number")
# num = int(input("enter number: "))

# for i in range(2, num):
#     if num % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# import re
# email="shubhangi169@gmail.com"
# result =re.findall(r"\w+",email)
# print(result)

# def add(a,b):
#     return a+b

# result=add(5,6)
# print(result)


# for i in range(1,6):
#     print(i)

# num=int(input("enter number: "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


# numbers = [1, 2, 3, 4, 5, 6]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# try:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter second number:"))

#     result=num1/num2
#     print(result)

# except ZeroDivisionError:
#     print("cannot divide by zero")

# except ValueError:
#     print("enter valid number")

# rows = 4

# for i in range(1, rows + 1):
#     stars = "*" * (i - 1)
#     number = str(i)
#     hashes = "#" * (rows - i)

#     print(stars + number + hashes)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)


# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# n=int(input("enter number: "))
# a=0
# b=1

# for i in range(n):
#         print(a,end="")
#         c=a+b 
#         a=b 
#         b=c

# n=int(input("enter number:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# marks = 75
# if marks>=35:
#     print("Pass")
# else:
#     print("fail")

# while True:
    
#     a=int(input("Enter number: "))
#     b=int(input("Enter number: "))

#     print(f"Even number between {a} and {b} :")
    
#     print("\neven number")
#     for i in range(a,b):
#         if i % 2==0:
#             print(i, end=" ")

#     print("\nodd number")
#     for i in range(a,b):
#         if i % 2 != 0:
#             print(i,end=" ")

#     print()
            
#     choice=input("if you want to continoue (yes/no):")
    
#     if choice == "no":
#         print("thank you")
#         break

# text = input("Enter sentence: ")

# words = text.split()

# longest = max(words, key=len)

# print("Longest word =", longest)



# for i in range(3):
#     for j in range(2):
#         print(i, j)

# num = int(input("enter number: "))
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print(reverse)

# a=[1,2,4,3,1,2,3]
# num=int(input("enter number:"))
# count=0

# for i in a:
#     if i==num:
#         count+=1
# print(count)



# num = int(input("enter number: "))

# for i in range(2, num):
#     if num % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")


# def add(a,b):
#     return a+b

# print(add(5,6))


# name =input("Enter your Name:")
# age =input("Enter your Age:")
# city =input("Enter your city:")

# print("My name is",name)
# print("My age is",age)
# print("I live in",city)

# a = int(input("Enter first number:"))
# b  = int(input("Enter second number:"))

# print("add",a+b)
# print("sub",a-b)
# print("divi",a/b)
# print("multipl",a*b)

# num=int(input("Enter number:"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number") 

# num = 0
# if num > 5:
#     print("positive number")
# elif num < 5:
#     print("negative number")
# else:
#     print("zero")


# a= int(input("enter first number:"))
# b= int(input("enter second number:"))

# if a > b:
#     print(a,"is larger")
# elif a < b:
#     print(b,"is smaller")
# else:
#     print("both are equal")


# a= int(input("Enter first number:"))
# b= int(input("Enter second number:"))
# c= int(input("Enter third number:"))

# if a > b and a > c:
#     print(a,"is larger")
# elif b > a and b > c:
#     print(b, "is larger")
# else:
#     print(c,"is larger")



# num =int(input("enter number:"))
# if num > 0 and num % 2 == 0:
#     print("positive even")
# elif num > 0 and num % 2 != 0:
#     print("positive odd")
# elif num < 0 and num % 2 == 0:
#     print("negetive even")
# elif num < 0 and num % 2 != 0:
#     print("negetive odd")
# else:
#     print("zero")

# for i in range(2,21):
#     if i % 2 == 0:
#         print(i)


# total = 0

# for i in range(1,11): 
#     total = total+i
# print(total)

# num = int(input("enter number:"))

# for i in range(1,11):
#     print(num, "x" ,i ,"=",num*i)

# even_count=0
# odd_count=0

# for i in range(1,21):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
        
# print(even_count)
# print(odd_count)

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
# num4 = int(input("enter fourth number:"))
# num5 = int(input("enter fifth number:"))
# numbers = [num1, num2, num3, num4, num5]
# largest = 0

# for num in numbers:
#     if num > largest:
#         largest = num

# print(largest)


# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
# num4 = int(input("enter fourth number:"))
# num5 = int(input("enter fifth number:"))
# numbers = [num1, num2, num3, num4, num5]

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num
        
# print(smallest)


# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

# i = 2
# while i <= 20:
#     if i % 2==0:
#         print(i)
#     i = i+ 1

# i= 1
# total = 0

# while i <= 10:
#     total = total + i
#     i = i +1

# print(total)

# def greet():
#     print("hello,wlcome to python!")
# greet()

# def greet(name):
#     print("hello",name)
# greet("shubhangi")

# def add(a,b):
#     return a+b
# result = add(10,20)
# print(result)

# def check_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(check_even(10))
# print(check_even(7))
    
# def largest(a,b):
#     if a > b:
#         return a 
#     else:
#         return b 

# print(largest(10,40))
# print(largest(40,20))

# def factorial(n):
#     result = 1

#     for i in range(1, n + 1):
#         result = result * i

#     return result
# print(factorial(5))

# try:
#     num = int(input("enter number:"))
# except:
#     print("invalid input")
# else:
#     print("complete")

# try:
#     num1 = int(input("enter first number"))
#     num2 = int(input("enter second number"))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("not divided by zero")
# except ValueError:
#     print("invalid input")
# else:
#     print("complete")

# numbers = [15, 8, 25, 3, 42, 10]
# largest = 0
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)

# numbers = [15, 8, 25, 3, 42, 10]
# smallest = numbers[0]
# for number in numbers:
#     if number < smallest:
#         smallest = number
# print(smallest)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# even_count = 0
# odd_count = 0
# for  number in numbers:
#     if number % 2 == 0:
#         even_count += 1 
#     else:
#         odd_count +=1
# print(even_count)
# print(odd_count)

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for number in numbers:
#     total = total + number
# print(total)

# numbers = (10, 20, 30, 40, 50)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:-1])

# numbers = (10, 20, 10, 30, 10, 40)
# print(numbers.count(10))
# print(numbers.index(30))

# import numpy as np

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print(arr[1, 2])
# print(arr[2, 0])
# print(arr[:, 1])

# import numpy as np

# arr = np.array([10, 20, 30])

# print(arr + 5)
# print(arr * 2)

