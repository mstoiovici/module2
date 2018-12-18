#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:46:21 2018

@author: maria
"""

"""
print("------------------------------task1-------------------------------")
import ch3_learn_python_the_hard_way_functions
print(ch3_learn_python_the_hard_way_functions.add_two_numbers())


print()
print("------------------------------task2-------------------------------")
a="hello"
b="world"
print(ch3_learn_python_the_hard_way_functions.hello_world_2args(a,b))

print()
print("------------------------------task3-------------------------------")
a="love"
b="coding"
print(ch3_learn_python_the_hard_way_functions.hello_world_2args(a,b))

print()
print("------------------------------task4-------------------------------")
print(ch3_learn_python_the_hard_way_functions.convert_distance(44))
"""

from ch3_learn_python_the_hard_way_functions import *


print("------------------------------task1-------------------------------")
add_two_numbers()
print("\n")

print()
print("------------------------------task2-------------------------------")
print("This is another exercise: ")
a="hello"
b="world"
hello_world_2args(a,b)
print("\n")


print()
print("------------------------------task2.1-------------------------------")
print("This is another exercise: ")
a="love"
b="coding"
hello_world_2args(a,b)
print("\n")

print()
print("------------------------------task3-------------------------------")
print("This is another exercise: ")
convert_distance(44)
print("\n")

print()
print("------------------------------task4,5-------------------------------")
print("This is another exercise: ")
area_one=get_size(3,2,3)[0]
volume_one=get_size(3,2,3)[1]
sizes_one=get_size(3,2,3)
print(area_one)
print(volume_one)
print("\n")

print()
print("------------------------------task6,7-------------------------------")
print("This is another exercise: ")
celsius=float(input("what's the temperature in your city today?"))
fahrenheit_one=temp_converter(celsius)[0]
kelvin_one=temp_converter(celsius)[1]
print("that's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit_one,kelvin_one))
print("\n")

print()
print("------------------------------task8-------------------------------")
print("This is another exercise: ")
cheese_and_crackers(20,30)
print("\n")

print()
print("------------------------------task9-------------------------------")
print("This is another exercise: ")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print ("That becomes: ", what, "Can you do it by hand?")