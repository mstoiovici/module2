#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:46:21 2018

@author: maria
"""


from ch3_file1_Mariana_functions import *


print("------------------------------task1-------------------------------")
add_two_numbers()


print()
print("------------------------------task2-------------------------------")
a="hello"
b="world"
hello_world_2args(a,b)



print()
print("------------------------------task2.1-------------------------------")
a="love"
b="coding"
hello_world_2args(a,b)


print()
print("------------------------------task3-------------------------------")
convert_distance(44)

print()
print("------------------------------task4,5-------------------------------")
area_one=get_size(3,2,3)[0]
volume_one=get_size(3,2,3)[1]
sizes_one=get_size(3,2,3)
print(area_one)
print(volume_one)


print()
print("------------------------------task6,7-------------------------------")
celsius=float(input("what's the temperature in your city today?"))
fahrenheit_one=temp_converter(celsius)[0]
kelvin_one=temp_converter(celsius)[1]
print("that's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit_one,kelvin_one))


print()
print("------------------------------task8 ex19 from LPTHW-------------------------------")
print ("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print()
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print()
print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print()
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




print()
print("------------------------------task9  ex21 from LPTHW -------------------------------")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print (("Age: %d, Height: %d, Weight: %d, IQ: %d") % (age, height, weight, iq))
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print ("That becomes: ", what, "Can you do it by hand?")

"""
print("------------------------------task1-------------------------------")
import ch3_file1_Mariana_functions
print(ch3_file1_Mariana_functions.add_two_numbers())


print()
print("------------------------------task2-------------------------------")
a="hello"
b="world"
print(ch3_file1_Mariana_functions.hello_world_2args(a,b))

print()
print("------------------------------task3-------------------------------")
a="love"
b="coding"
print(ch3_file1_Mariana_functions.hello_world_2args(a,b))

print()
print("------------------------------task4-------------------------------")
print(ch3_file1_Mariana_functions.convert_distance(44))
"""
