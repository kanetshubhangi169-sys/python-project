#Create a text file and write data into it
file = open("s.txt", "w")

file.write("Hello, world\n")
file.write("Python file handling is easy to learn.")

file.close()

#Read data from a text file
file = open("s.txt", "r")

data = file.read()

print(data)
file.close()

#Append new content to an existing file
file = open("s.txt", "a")

file.write("\nThis line is added later.")

file.close()

#Count number of lines in a file
file = open("s.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()

#Count number of words in a file
file = open("s.txt", "r")

data = file.read()

words = data.split()

print("Number of words:", len(words))
file.close()

#Count number of characters in a file
file = open("s.txt", "r")

data = file.read()

print("Number of characters:", len(data))
file.close()

#Read file line by line
file = open("s.txt", "r")

for line in file:
    print(line)

file.close()

#Copy content from one file to another.
source = open("s.txt", "r")

data = source.read()

destination = open("a.txt", "w")

destination.write(data)

source.close()
destination.close()


#Merge multiple text files into a single file
file1 = open("s.txt", "r")
file2 = open("a.txt", "r")

data1 = file1.read()
data2 = file2.read()

merged = open("merged.txt", "w")

merged.write(data1)
merged.write("\n")
merged.write(data2)

file1.close()
file2.close()
merged.close()


#Find frequency of words in a text file
file = open("s.txt", "r")
words = file.read().lower().split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
file.close()

#Extract email addresses from a file
file = open("s.txt", "r")
text = file.read()

words = text.split()

for w in words:
    if "@" in w:
        print("Email:", w)

file.close()

#Read CSV file and display records
file = open("data.csv", "r")

for line in file:
    print(line.strip().split(","))

file.close()

#Write student records into CSV file
file = open("students.csv", "w")

file.write("Roll,Name,Marks\n")
file.write("1,Alice,85\n")
file.write("2,Bob,90\n")

file.close()

#Create a log file analyzer for errors and warnings
file = open("a.txt", "r")

errors = 0
warnings = 0

for line in file:
    if "ERROR" in line:
        errors += 1
    elif "WARNING" in line:
        warnings += 1

print("Errors:", errors)
print("Warnings:", warnings)

file.close()

#Build a simple student record management system using file handling
while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        file = open("students.txt", "a")

        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        marks = input("Enter marks: ")

        file.write(name + "," + roll + "," + marks + "\n")
        file.close()

        print("Student added successfully")


    elif choice == "2":
        try:
            file = open("students.txt", "r")
            print("\n--- Student List ---")

            for line in file:
                data = line.strip().split(",")

                print("Name:", data[0], "Roll:", data[1], "Marks:", data[2])

            file.close()

        except FileNotFoundError:
            print("No student records found")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


