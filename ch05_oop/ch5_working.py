#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:26:10 2018

@author: maria
"""

#import sys

class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):             #superclass method
        print('yum')

class Dog(Animal):          
     def bark(self):          #subclass method
         print('Woof!')

class Cat(Dog):               # the Cat class inherites directly from Dog class, so you can call the Bark()method, but than again, Dog class inherites from Animal  so Cat becomes grandchild of Animal class, and so can call the Eat()method
    def meow(self):         #subclass method
         print('Meow')

#Snoopy=Dog(name,age)            # creating an object Snoopy with the subclass Dog and class Animal
#Snoopy.bark()              #subclass method
#Snoopy.eat()               #superclass method

#Pissy=Cat(name,age)             # creating an object Pissy with the subclass Cat and class Animal
#Pissy.meow()           #subclass method
#Pissy.eat()             #superclass method



class Robot():
    def __init__(self,name,time=0):
        self.name=name
        self.time=time
    def move(self):
        print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuumed all the dust today')
    def clean_bathroom(self):
        print("I cleaned the toilet today....yuuuuk lady!!!")
        if time>11:
            print("I emptied the  bathroom trash bin as well")
        elif time>6:
            print ("I didn't empty the bathroom trash bin yet, it's too early. I don't want to do that task twice this evening lady!!!")
        else:
            print("And I was too lazy to check the bathroom trash bin.")
class CookRobot(CleanRobot):
    
    def cook(self):
        if time>11:
            print("It's too late to have dinner, I made you only a desert. I know you can't go to sleep without dessert!!!")
            self.clean()
        elif time>6:
            print ('I made rice.I hope that"s enough for you')
        else:
            print("I didn't cook. I'm not your robot woman!!!!!")
            print("and..")
        self.clean_bathroom()
        
        
        
        
class SuperRobot():
    def __init__(self,name,age,time=0):
        self.name=name
        self.time=time
        self.age=age
        self.first=Robot(name)
        self.second=Dog(name,age)
        self.third=CleanRobot(name)
        self.forth=CookRobot(name)
       
    def playGame(self):
        print("alphago game")
    def move(self):
        return self.first.move() #using robot class method
    def bark(self):
        return self.second.bark() #using dog class method
    def clean(self):
        return self.third.clean() #using cleanrobot class method
    def move_cook(self):
        self.move() 
        return self.forth.cook()

time=int(input("At what hour did you arrive home?"))
#name=sys.argv[1]
#age=sys.argv[2]
machineDog=SuperRobot("Robotica",3)

#machineDog.move()
#machineDog.bark()
#machineDog.playGame()
print(machineDog.name)

machineDog.move_cook()