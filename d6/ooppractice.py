#Create a class Student with attributes name, roll number, and marks
class Student:

    def __init__(self, name, roll_number, marks):

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

student1 = Student("Rahul", 101, 85)

print("Name:", student1.name)
print("Roll Number:", student1.roll_number)
print("Marks:", student1.marks)

#Create a class BankAccount with deposit, withdraw, and balance check methods
class Account:
    def __init__(self , bal , acc):
        self.balance = bal
        self.account_no= acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance =",self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance =",self.get_balance())
    
    def get_balance(self):
        return self.balance

    
acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
print(acc1.balance)
print(acc1.account_no)

#Create a class Rectangle to calculate area and perimeter
class Rectangle:
    def __init__(self, length, width):

        self.length = length
        self.width = width

    
    def area(self):
        return self.length * self.width

    def perimeter(self):

        return 2 * (self.length + self.width)


rect1 = Rectangle(10, 5)

print("Area =", rect1.area())
print("Perimeter =", rect1.perimeter())

#Create a class Employee with salary calculation functionality

class Employee:
    def __init__(self, name, basic_salary, bonus):

        self.name = name
        self.basic_salary = basic_salary
        self.bonus = bonus


    def calculate_salary(self):

        total_salary = self.basic_salary + self.bonus

        return total_salary


emp1 = Employee("Rahul", 25000, 5000)

print("Employee Name:", emp1.name)

print("Total Salary =", emp1.calculate_salary())

#Implement single inheritance using Person and Student classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        Person.__init__(self, name, age)

        self.course = course

    def show_student(self):
        print("Course:", self.course)



s1 = Student("Rahul", 20, "Python")
s1.show_person()
s1.show_student()

#Implement multilevel inheritance using Animal, Mammal, and Dog classes
class Animal:
    def eat(self):
        print("Animal can eat")


class Mammal(Animal):
    def walk(self):
        print("Mammal can walk")

class Dog(Mammal):
    def bark(self):
        print("Dog can bark")


d1 = Dog()
d1.eat()
d1.walk()
d1.bark()

#Implement hierarchical inheritance using a common parent class
class Person:
    def show(self):
        print("This is a Person class")


class Student(Person):
    def study(self):
        print("Student is studying")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


s1 = Student()
t1 = Teacher()


s1.show()
t1.show()
s1.study()
t1.teach()


#Demonstrate method overriding using inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a1 = Animal()
d1 = Dog()


a1.sound()
d1.sound()

#Implement polymorphism using multiple classes with same method name
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")

class Cow:
    def sound(self):
        print("Cow moos")


def make_sound(animal):
    animal.sound()



d1 = Dog()
c1 = Cat()
c2 = Cow()

make_sound(d1)
make_sound(c1)
make_sound(c2)


#Create a class with constructor and destructor methods
class Student:


    def __init__(self, name):
        self.name = name
        print("Constructor called")
        print("Student Name:", self.name)

    def __del__(self):
        print("Destructor called")
        print("Object destroyed")



s1 = Student("Rahul")
del s1

#Implement encapsulation using private variables and getter/setter methods
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   

   
    def get_marks(self):
        return self.__marks


    def set_marks(self, marks):
        self.__marks = marks



s1 = Student("Rahul", 85)
print("Marks:", s1.get_marks())


s1.set_marks(95)
print("Updated Marks:", s1.get_marks())


#Create a mini Library Management System using OOP concepts
class book:
    def __init__(self,book_name,auther):
        self.book_name = book_name
        self.auther = auther
        self.is_issued = False

    def display_book(self):
        print("book:",self.book_name)
        print("auther:",self.auther)
        print("issued:",self.is_issued)

class library:
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        print(book.book_name,"added successfully")

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            book.display_book()
            print()

    def issue_book(self, book_name):
        for book in self.books:
            if book.book_name == book_name:
                if not book.is_issued:
                    book.is_issued = True
                    print(book_name, "has been issued")
                else:
                    print(book_name, "is already issued")
                return

        print("Book not found")

    def return_book(self, book_name):
        for book in self.books:
            if book.book_name == book_name:
                book.is_issued = False
                print(book_name, "has been returned")
                return

        print("Book not found")

lib = library()
b1 = book("Python Basics", "Rahul")
b2 = book("AI Introduction", "Amit")

lib.add_book(b1)
lib.add_book(b2)

lib.show_books()

lib.issue_book("Python Basics")

lib.return_book("Python Basics")

lib.show_books()



    


    






