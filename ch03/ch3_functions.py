#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:32 2018

@author: maria
"""

def add_two_numbers():
    number1=1
    number2=2
    result=number1+number2
    #print(result)
    print(str(number1)+" plus "+str(number2)+" is " +str(result))
    print("{} plus {} is {}.".format(number1,number2,result))
    
def hello_world_2args(a,b):
    print("{} {}".format(a,b))
    
def convert_distance(miles):
    kilometers=(miles*8.0)/5.0
    print("Converting distance in miles to kilometers:")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)
    
def get_size(width,height,depth):
    area=width*height
    volume=width*height*depth
    sizes=(area,volume)
    return(sizes)
    
def get_size(width,height,depth):
    area=width*height
    volume=width*height*depth
    sizes=(area,volume)
    return(sizes)

def temp_converter(celsius):
    fahrenheit=celsius*9.0/5.0+32
    kelvin=celsius+273.15
    print("that's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit,kelvin))

def temp_converter(celsius):
    fahrenheit=celsius*9.0/5.0+32
    kelvin=celsius+273.15
    temperature=(fahrenheit,kelvin)
    return(temperature)

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print ("Get a blanket.\n")
    
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
    