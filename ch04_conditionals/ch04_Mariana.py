#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:05:55 2018

@author: maria
"""

print("--------------------------task1----------------------------")
age=15
isaTeen=age>=13 and age<=19
print(isaTeen)

print()
print("--------------------------task2----------------------------")
age=22
isaTeen=age>=13 and age<=19
print(isaTeen)

print()
print("--------------------------task3----------------------------")
number=input("enter a number between 1 and 10: ")
number=int(number)
if number>10:
    print("Too high!")
elif number<=0:
    print("Too low!")
else:
    print("That's perfect. Your number is between 1 and 10!")

print()
print("--------------------------task4----------------------------")
number=input("enter a number between 1 and 10: ")
number=int(number)
if 0<number<=10:
    print("That's perfect. Your number is between 1 and 10!")
else:
    print("Your number has to be between 1 and 10!")
    
    
print()
print("--------------------------task5----------------------------")
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



