'''
OOPS:
    
What is Object-Oriented Programming in Python?

    In Python object-oriented Programming (OOPs) is a programming paradigm
that uses objects and classes in programming. It aims to implement real-world
entities like inheritance, polymorphisms, encapsulation, etc.

OOPs Concepts in Python:
    Class and Objects
    Polymorphism
    Encapsulation
    Inheritance
    Abstraction 

Polymorphism in Python:
        We can use the concept of polymorphism while creating class methods as Python
    allows different classes to have methods with the same name.
'''

'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()
    '''

'''
Encapsulation in python:
    Encapsulation is demonstrated by a class which encapsulates all data,
such as member functions, variables, and so forth.
'''

'''

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)
'''

'''
https://www.programiz.com/java-programming/inheritance#:~:text=Inheritance%20is%20an%20important%20concept%20of%20OOP%20that
Inheritance in python:
        Inheritance in python is a mechanism where one class is allowed
    to inherit the variables and methods of another class.

Types of inheritance:
    Single inheritance.
    Multiple Inheritance
    Multi-level Inheritance.
    Hierarchical Inheritance.
    Hybrid Inheritance.
'''

'''
#Single-level inheritance
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
 
# Driver's code
object = Child()
object.func1()
object.func2()

'''

'''
#Multiple Inheritance
class parent1:  
    def add(self,a,b):  
        return a+b;
    
class parent2:  
    def mul(self,a,b):  
        return a*b;
    
class child(parent1,parent2):  
    def Divide(self,a,b):  
        return a/b;  

d = child()  
print(d.add(10,20))  
print(d.mul(10,20))  
print(d.Divide(10,20))
'''

'''
#Multi-level Inheritance

class Base:
    # Constructor to set Data
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role
 
# Intermediate Class: Inherits the Base Class
class Intermediate(Base):
    # Constructor to set age
    def __init__(self, age, name, roll, role):
        super().__init__(name, roll, role)
        self.age = age
 
# Derived Class: Inherits the Intermediate Class
class Derived(Intermediate):
    # Method to Print Data
    def __init__(self, age, name, roll, role):
        super().__init__(age, name, roll, role)
 
    def Print_Data(self):
        print(f"The Name is : {self.name}")
        print(f"The Age is : {self.age}")
        print(f"The role is : {self.role}")
        print(f"The Roll is : {self.roll}")
 
# Creating Object of Base Class
obj = Derived(21, "Lokesh Singh", 25, "Software Trainer")
 
# Printing the data with the help of derived class
obj.Print_Data()
'''

'''
# Hierarchical inheritance

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")

class Child3(Parent):
	def func4(self):
		print("This function is in child 3.")


# Driver's code
object1 = Child1()
object2 = Child2()
object3 = Child3()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
object3.func4()
'''

'''
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()

'''

'''

Abstraction:
    Data abstraction in Python is a programming concept that hides complex
implementation details while exposing only essential information and functionalities to users.

'''


'''
from abc import ABC

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = False  # Initially the engine should be off

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.model}'s engine.")
            self.engine_started = True
        else:
            print("Engine is already running.")

# Instantiate the Car class
c = Car('Toyota', '9600', 2013)

# Start the engine
c.startEngine()
'''