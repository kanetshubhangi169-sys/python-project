numbers = [10, 20, 30, 40, 50]
print(numbers)


numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])
print(numbers[-1])



numbers = [10, 20, 30]
numbers.append(40)
print(numbers)




numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)


numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)


numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)




numbers = [10, 20, 30, 40]
print(len(numbers))



numbers = [10, 20, 30, 40]
if 30 in numbers:
    print("Found")
else:
    print("Not found")



numbers = [10, 50, 20, 80, 30]
print(max(numbers))
print(min(numbers))



numbers = [10, 20, 30, 40]
print(sum(numbers))



numbers = [10, 20, 30, 40]
for i in numbers:
    print(i)



numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i % 2 == 0:
        print(i)


    
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i % 2 != 0:
        print(i)

    

numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)


numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)



numbers = [1, 2, 3, 2, 4, 1, 5]
for i in numbers:
    if numbers.count(i) > 1:
        print(i)


    

numbers = [1, 2, 3, 2, 4, 1, 5]
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)




numbers = [10, 50, 20, 80, 30]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)



numbers = [10, 50, 20, 80, 30]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)




numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:", even)
print("Odd:", odd)



