#Quiz 1
class BankAccount:
    def __init__(self):
        self.__balance = 0      

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money!")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(400) 

#quiz2
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0       # private

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100!")

    def get_marks(self):
        return self.__marks

# Usage
s = Student("Alice")
s.set_marks(85)
print(f"{s.name}'s marks: {s.get_marks()}")
s.set_marks(150)    

#quiz3*
class Animal:
    def eat(self):
        print("This animal is eating.")

class Dog(Animal):    # Dog inherits from Animal
    def bark(self):
        print("Woof!")

class Cat(Animal):    # Cat inherits from Animal
    def meow(self):
        print("Meow!")

dog = Dog()
dog.eat()    # inherited 
dog.bark()

cat = Cat()
cat.eat()    # also inherited
cat.meow()

#quiz4*
class Vehicle:
    def move(self):
        print("This vehicle is moving.")

class Car(Vehicle):
    def move(self):    # overriding parent method
        print("The car is driving on the road.")

class Bike(Vehicle):
    def move(self):    # overriding parent method
        print("The bike is cycling on the path.")

v = Vehicle()
v.move()    # Vehicle's version

c = Car()
c.move()    # Car's version

b = Bike()
b.move()    # Bike's version

#quiz5
class Wallet:
    def __init__(self):
        self.__balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount}. Wallet: {self.__balance}")

    def spend_money(self, amount):
        if amount > self.__balance:
            print("Not enough money!")
        else:
            self.__balance -= amount
            print(f"Spent {amount}. Wallet: {self.__balance}")

    def get_balance(self):
        return self.__balance

w = Wallet()
w.add_money(100)
w.spend_money(40)
w.spend_money(80)   

#quiz6* add more methods
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name} | Price: ${self.price}")

# Creating 3 objects from the same blueprint
p1 = Product("Laptop", 999)
p2 = Product("Phone", 499)
p3 = Product("Headphones", 79)

p1.display()
p2.display()
p3.display()

#quiz7*add more methods to class library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("=== Library Books ===")
        for book in self.books:
            print(f"  {book.title} by {book.author}")

lib = Library()
lib.add_book(Book("Python 101", "John"))
lib.add_book(Book("Clean Code", "Martin"))
lib.add_book(Book("The Pragmatic Programmer", "Hunt"))
lib.display_books()

#quiz8*
class Employee:
    def __init__(self, name):
        self.name = name
        self.__salary = 0

    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            print("Salary cannot be negative!")

    def get_salary(self):
        return self.__salary

    def display(self):
        print(f"{self.name} earns ${self.__salary}")

e = Employee("James")
e.set_salary(50000)
e.display()
e.set_salary(-100) 

#quiz9*
class Shape:
    def describe(self):
        print("I am a shape.")

class Circle(Shape):
    def describe(self):
        print("I am a Circle — round with no corners!")

class Square(Shape):
    def describe(self):
        print("I am a Square — four equal sides!")

shapes = [Circle(), Square(), Shape()]
for s in shapes:
    s.describe()

#quiz10
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password    # private!

    def check_password(self, attempt):
        if attempt == self.__password:
            print("Login successful!")
            return True
        else:
            print("Wrong password!")
            return False

u = User("alice", "secret123")
u.check_password("wrongpass")      # Wrong
u.check_password("secret123")      # Correct
# print(u.__password)  -- this would cause an error