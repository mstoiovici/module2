#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:32 2018

@author: maria
"""
################################## task1 ###########################
def add_two_numbers():
    number1=1
    number2=2
    result=number1+number2
    #print(result)
    print(str(number1)+" plus "+str(number2)+" is " +str(result))
    print("{} plus {} is {}.".format(number1,number2,result))

################################## task2 ###########################   
def hello_world_2args(a,b):
    print("{} {}".format(a,b))

################################## task3 ###########################    
def convert_distance(miles):
    kilometers=(miles*8.0)/5.0
    print("Converting distance in miles to kilometers:")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)

################################## task4 ###########################   
def get_size(width,height,depth):
    area=width*height
    volume=width*height*depth
    sizes=(area,volume)
    return(sizes)
    
################################## task5 ###########################    
def get_size(width,height,depth):
    area=width*height
    volume=width*height*depth
    sizes=(area,volume)
    return(sizes)

################################## task6 ###########################
def temp_converter(celsius):
    fahrenheit=celsius*9.0/5.0+32
    kelvin=celsius+273.15
    print("that's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit,kelvin))

################################## task7 ###########################
def temp_converter(celsius):
    fahrenheit=celsius*9.0/5.0+32
    kelvin=celsius+273.15
    temperature=(fahrenheit,kelvin)
    return(temperature)

################################## task8 ###########################
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print ("Get a blanket.\n")
    
################################## task9 ###########################    
def add(a,b):
    print("adding %d+%d" % (a,b))
    return a+b
def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a-b
def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b
def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b
    