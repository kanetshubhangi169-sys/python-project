#Create a dictionary of student names and marks
student = {"name":"rahul","marks":70}
print(student)

#Add, update, and delete elements from dictionary
#add
dict = {"name":"rahul","sub":"python"}

dict["role"] = "ai-ml"
print(dict)

#update
dict = {"name":"rahul","sub":"python"}

dict.update({"role":"ai-ml"})

#delete
dict = {"name":"rahul","sub":"python"}
del dict ["sub"]
print(dict)



#Access dictionary keys, values, and items
student = {"name": "Rahul","marks": 90,"course": "Python"}

print(student.keys())
print(student.values())
print(student.items())

#Find key with maximum value in dictionary
marks = {"Rahul": 85,"Sneha": 95,"Aman": 78}

maximum = max(marks, key=marks.get)
print(maximum)

#Count frequency of characters using dictionary
text = "apple"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

#Merge two dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict3 = dict1 | dict2

print(dict3)


#Sort dictionary by values.
data = {"Rahul": 85,"Aman": 95,"Priya": 78}

sorted_values = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_values)


#Check whether a key exists in dictionary
students = {"Rahul": 85,"Aman": 90}

if "Rahul" in students:
    print("Key exists")
else:
    print("Key not found")

#Convert two lists into dictionary
names = ["Rahul", "Aman", "Priya"]
marks = [85, 90, 78]

result = dict(zip(names , marks))

print(result)


#Create nested dictionary and access inner values
students = {"Rahul": {"age": 20,"marks": 85},"Aman": {"age": 21,"marks": 90 }}

print(students["Rahul"]["marks"])


#Build a simple inventory management system using dictionary
inventory = {"Laptop": 10,"Mouse": 25,"Keyboard": 15}

# Add new product
inventory["Monitor"] = 8

# Update stock
inventory["Mouse"] = 30

# Delete product
del inventory["Keyboard"]

# Display inventory
for product, quantity in inventory.items():
    print(product, ":", quantity)