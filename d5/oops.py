#creating a class
class Student:
    name = "shubhangi"

#create a object
s1 = Student()
print(s1.name)


#encapsulation
class Bank:
    
    def __init__(self):
        self.__balance = 1000   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def show_balance(self):
        print("Balance:", self.__balance)


obj = Bank()
obj.deposit(500)
obj.show_balance()


#Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()

#overridding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()


#abstraction
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


obj = Dog()

obj.sound()


#inheritance
class Animal:

    def eat(self):
        print("Animal eats food")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


obj = Dog()

obj.eat()
obj.bark()




