#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:35:31 2018

@author: maria
"""

print("---------------------------task1-------------------------")
print(5-6)
print("\n")
print(8*9)
print(6/2)
print(5/2)
print(5.0 / 2)
print(5 % 2)
print(2 * (10 + 3))
print(2 ** 4)

print()
print("---------------------------task2-------------------------")
age = 5
age = "almost three"
age = 29.5
age = "I really don’t know!"
print(age)

print()
print("---------------------------task3-------------------------")
print ("hello" + "world")
print ("Joke " * 3)
print ("Chen" + "3")


print()
print("---------------------------task4-------------------------")
a="Chen" + "3"
print(a)
type(a)
type("Chen" + "3")

print()
print("---------------------------task5-------------------------")
print ("hello".upper())


print()
print("---------------------------task6-------------------------")
S1 = "hello" + "world"
S2 = "Joke " * 3
S3 = "5"
print((S1 + S2)*10)
print(S1+S2+S3)

print()
print("---------------------------task7-------------------------")
print("Bob \n" *10)
print("bob" + "\n")
print("\n")
print("bob")
print("john")
print("john"+"\n")
print("bob")


print()
print("---------------------------task8-------------------------")
s1="4"
s2="5"
s3=4
result=int(s1)+int(s2)+s3
#print(result)
print(result)


print()
print("---------------------------task9-------------------------")
strExample="a,b,c,d,happy"
splitExample=strExample.split("-")
print(splitExample)


print()
print("---------------------------task10-------------------------")
age = 5
like = "painting"
age_description = "My age is {} and I like {}.".format(age, like)
age_description = "My age is {1} and I like {0}.".format(age, like)


print()
print("---------------------------task11-------------------------")
name = input("What’s your name? ")
city = input("What’s your city? ")
print ("Hello {}! from {}".format(name,city))
print("Hello "+name+"! from "+city)


print()
print("---------------------------task12-------------------------")
s1="4"
s2="5"
s3=4
result=int(s1)+int(s2)+s3
print(result)


print()
print("---------------------------task13-------------------------")
strExample="Mariana are mere"
splitExample=strExample.split(" ")

print()
print("---------------------------task14-------------------------")
print("What is your name?")
name=input().upper()
name=name.upper()
print("hello {}".format(name.upper()))

print()
print("---------------------------task15:ex11 - LPTHW-------------------------")
"""
print("How old are you?"),
age=input()
print("How tall are you?"),
height=input()
print("How much do you weigh?"),
weight=input()
print (("So, you're %r tall and %r heavy.")%(age, height,weight))
"""

age=input("How old are you?")

height=input("How tall are you?")

weight=input("How much do you weigh?")
print (("So, you're %r tall and %r heavy.")%(age, height,weight))    
 
