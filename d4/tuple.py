#Create and print a tuple with different data types
data = (10, "Shubhangi", 95.5, True)
print(data)

#Find length of a tuple
fruits = ("apple","banana","cherry")

print(len(fruits))

#Access tuple elements using indexing and slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[-1])


#Count occurrences of an element in tuple
numbers = (10, 20, 30, 20, 40, 20)

count = numbers.count(20)
print(count)

#Find maximum and minimum values in tuple
numbers = (10, 5, 40, 25, 2)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)


#Convert tuple into list and vice versa
numbers = (10, 20, 30, 40)

my_list = list(numbers)
print(my_list)

#Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)

#Check whether an element exists in tuple
numbers = (10, 20, 30, 40)

if 20 in numbers:
    print("Element exists")
else:
    print("Element does not exist")

#Unpack tuple into variables
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Find repeated elements in tuple
numbers = (1, 2, 3, 2, 4, 5, 1, 6)

repeated = []

for i in numbers:
    if numbers.count(i) > 1 and i not in repeated:
        repeated.append(i)

print(repeated)

#Sort tuple elements
num = (4,7,9,6,1,2)
sorted_num = tuple(sorted(num))

print(sorted_num)

#Create nested tuples and access inner elements
data = ((1, 2), (3, 4), (5, 6))

print(data[0][1])      
print(data[1][0])   
print(data[2][1])   
