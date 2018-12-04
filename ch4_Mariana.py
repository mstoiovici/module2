#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:05:55 2018

@author: maria
"""
"""
age=15
isaTeen=age>=13 and age<=19
print(isaTeen)

age=22
isaTeen=age>=13 and age<=19
print(isaTeen)
"""
"""
number=input("enter a number between 1 and 10: ")
number=int(number)
if number>10:
    print("Too high!")
elif number<=0:
    print("Too low!")
#else:
    #print("That's perfect. Your number is between 1 and 10!")
if 0<number<=10:
    print("That's perfect. Your number is between 1 and 10!")
"""
"""
age=int(input("please enter age number: "))
if age<13:
    print("child")
elif age<18:
    print("teen")
elif age<65:
    print("adult")
elif age<100:
    print("pensioner")
else:
    print("Are you sure you're still alive?!")
"""

######################ex11 LPTHW
"""
print("How old are you?"),
age=input()
print("How tall are you?"),
height=input()
print("How much do you weigh?"),
weight=input()
print (("So, you're %r tall and %r heavy.")%(age, height,weight))
"""

age=raw_input("How old are you?")

height=raw_input("How tall are you?")

weight=raw_input("How much do you weigh?")
print (("So, you're %r tall and %r heavy.")%(age, height,weight))
