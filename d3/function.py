mndef my_function():
    print("Hello, from a function")

my_function() 



#return statements
def add(a, b):
    return a + b

result = add(10, 5)

print(result)

#multiple parameters
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Rahul", 20)

#function with one argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#keyword argument
def my_function(animal,name):
  print("i have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "bunny",animal = "dog")

#positional argument
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


#passing a different data type
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#returning different data type
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])






