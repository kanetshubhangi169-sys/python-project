#largest element in a list
num = [10,5,20,15,30,25]

largest = num[0]

for num in num:
    if num > largest:
        largest = num

print("Largest element:", largest)


#second largest element in a list
numbers = [10, 45, 2, 99, 23]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)

#Remove duplicates from a list
my_list = [1,1,2,3,4,4,5]

unique = []

for num in my_list:
    if num not in unique:
        unique.append(num)

print(unique)

#Reverse a list without using reverse()
numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)


#Sort a list without using sort()
numbers = [5, 2, 8, 1, 9]

for i in range(len(numbers)):
    for j in range(len(numbers)-1-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)


#Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)


#Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)

#Find frequency of each element in a list
numbers = [1, 2, 2, 3, 4, 4]

for i in set(numbers):
    print(i, "=", numbers.count(i))


#Rotate a list by N positions
numbers = [1, 2, 3, 4, 5]
n = 2

rotated = numbers[n:] + numbers[:n]

print(rotated)

#Find missing number in a list of consecutive numbers
numbers = [1, 2, 3, 5]

n = 5

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing number:", missing)

#Separate even and odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)


#Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]

flat = []

for i in nested:
    flat += i

print(flat)
