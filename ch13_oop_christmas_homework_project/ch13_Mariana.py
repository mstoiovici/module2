#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:22:59 2019

@author: maria
"""

######Task1 Initialise the person class
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        if gender=="m":
            self.isMale=True
        elif gender=="f":
            self.isMale=False
        else:
            print("Gender not recognised!")
    #define more functions/methods
    def greetingInformal(self):
        print("Hi",self.name)
    def greetingFormal(self):
        if self.isMale:
            print("Welcome,Mr ",self.name)
        else:
            print("Welcome, Ms ",self.name)
            
#exp of creating an instance
p1=Person("John",44,"m")
print(p1.name)
print(p1.isMale)

##########TAsk2 More functionalities for the Person class
p1=Person("Harry",12,"m")
p2=Person("Jean",12,"f")
p1.greetingFormal()
p2.greetingFormal()

#######Task3 A greeting filter
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        if gender=="m":
            self.isMale=True
        elif gender=="f":
            self.isMale=False
        else:
            print("Gender not recognised!")
    #define more functions/methods
    def greetingInformal(self):
        print("Hi",self.name)
    def greetingFormal(self):
        if self.isMale:
            print("Welcome,Mr ",self.name)
        else:
            print("Welcome, Ms ",self.name)
    #we add greetingAgeBased() in task3
    def greetingAgeBased(self):
        if self.age<18:
            print("Welcome, young ",self.name)
        elif self.age>60:
            print("Welcome, venerable ",self.name)
        else:
            self.greetingFormal()

p1=Person("Harry",12,"m")
p2=Person("Amali",88,"f")
p3=Person("Richard",50,"m")
p1.greetingAgeBased()
p2.greetingAgeBased()   
p3.greetingAgeBased() 

#####Task4 Create a subclass for the Person class
print("#####This is task 4####")
class Wizard(Person):
    def greetingFormal(self):
        print("Welcome, Mr ",self.name,end=" ")
        print("-you\'re a fine wizard!")
p1=Person("Harry",12,"m")
p1.greetingFormal()
p1=Wizard("Harry",12,"m")
p1.greetingFormal()
#######  Task 5 Redefine Init ----you can overwrite the __init__ function
####This is a way to do it, but you'll write some parts of code again, and this is bad code
class Wizard(Person):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.isMale=True
    def greetingInformal(self):
        print("Hi",self.name)
    def greetingFormal(self):
        print("Welcome, Mr ",self.name,end=" ")
        print("-you\'re a fine wizard!")
    def greetingAgeBased(self):
        if self.age<18:
            print("Welcome, young ",self.name)
        elif self.age>60:
            print("Welcome, venerable ",self.name)
        else:
            self.greetingFormal()

####Or you can do it like this, were you redefine the init method from the parent class
class Wizard(Person):
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,"m")
    def greetingInformal(self):
        print("Hi",self.name)
    def greetingFormal(self):
        print("Welcome, Mr ",self.name,end=" ")
        print("-you\'re a fine wizard!")
    def greetingAgeBased(self):
        if self.age<18:
            print("Welcome, young ",self.name)
        elif self.age>60:
            print("Welcome, venerable ",self.name)
        else:
            self.greetingFormal()
#####Task6 Add new methods to the Wizard class
class Wizard(Person):
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,"m")
    def greetingInformal(self):
        print("Hi",self.name)
    def greetingFormal(self):
        print("Welcome, Mr ",self.name,end=" ")
        print("-you\'re a fine wizard!")
    def greetingAgeBased(self):
        if self.age<18:
            print("Welcome, young ",self.name)
        elif self.age>60:
            print("Welcome, venerable ",self.name)
        else:
            self.greetingFormal()
    def spell(self):
        print("Expelliarmus!")