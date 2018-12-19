# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:13:55 2018

@author: maria
"""

print("---------Task1-----------")
age=int(input("What's your age? \n"))
print(type(age))
new_age=age+2
print(new_age)
#debugging using print
#always use print to show what you return from the script

print()
print("---------Task2-----------")

age=int(input("What's your age? \n"))

def doOperations(age):
    new_age=age+2
    print(new_age)
    return new_age

def callDoOperations(new_age):
    new_age1=doOperations(age)
    print(new_age1)
    new_age2=new_age1+20
    print(new_age2)
    return new_age2

new_age=doOperations(age)
new_age2=callDoOperations(new_age)
  
#debugging using breakpoints  
#1.double click on the line number of your code to put a breakpoint(red circle)

#2.you can now run your code in debug mode using debugging buttons on the toolbar
#  - first button starts running your code until the break point.
#  - second button allows you to run your code line-by-line until the breakpoint.
#  - third button is for stepping into the sections (class and functions) 
#  - fourth button takes you out when the error is not related to the current section
#  - fifth button is takes you to the next breakpoint
#  - last button exits debugging mode and go back to normal coding mode.
    


