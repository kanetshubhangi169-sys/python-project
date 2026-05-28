#read file
f = open("a.txt")
print(f.read())
f.close()

#read a letter in insert num
with open("a.txt") as f:
    print(f.read(5))

#read line of code
with open("a.txt") as f:
  print(f.readline())


#read 2 line 
with open("a.txt") as f:
  print(f.readline())
  print(f.readline())

#loop through file line by line read
with open("a.txt") as f:
  for x in f:
    print(x)

#append the file
with open("a.txt", "a") as f:
  f.write("Now the file has more content!")

with open("a.txt") as f:
  print(f.read())

#overwrite the file
with open("a.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

with open("a.txt") as f:
  print(f.read())

#remove a file
import os
os.remove("demofile.txt")
