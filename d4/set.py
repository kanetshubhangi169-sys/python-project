#Create a set and add elements dynamically
fruits = set()

fruits.add("orange")
fruits.add("mango")
print(fruits)

#Remove elements from a set
numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers)

#Find union of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)

#Find intersection of two sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1.intersection(set2)

print(result)

#Find difference between two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#Find symmetric difference between sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#Check subset and superset relationships
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))
print(set2.issuperset(set1))

#Remove duplicate values from list using set
numbers = [1, 2, 2, 3, 4, 4]

unique = list(set(numbers))

print(unique)

#Find common elements between multiple sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

result = set1 & set2 & set3

print(result)

#Check whether two sets are disjoint
set1 = {1, 2}
set2 = {3, 4}

print(set1.isdisjoint(set2))

#Find maximum and minimum values in set
numbers = {10, 5, 40, 2}

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

#Perform all set operations on user input data
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)