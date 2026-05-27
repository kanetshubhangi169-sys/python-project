# fruits = ["apple", "banana", "cherry"]
# for fruite in fruits:
#     print(fruite)

 #loop through a string
word = "shubhangi"
for letter in word:
     print(letter)

for i in range(1,10,2):
     print(i)

 #nested loop
for i in range(1,4):
     for j in range(1,4):
        print(i, "*",j,"=",i*j)



#while loop
count = 1

while count <= 5:
    print(count)
    count += 3

#reverse counting
num = 5
while num >= 1:
    print(num)
    num -= 2

#while True:
#    print("hello")

#continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#else statement with loops
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Done")

#square pattern
for i in range(4):
    print("* * * *")

#triangle pattern
for i in range(1, 6):
    print("*" * i)

#example
numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total += num

print("Sum =", total)

