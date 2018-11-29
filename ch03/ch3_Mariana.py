#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:59:18 2018

@author: maria
"""
#print("What is your name?")
#name=input().upper()
#name=name.upper()
#print("hello {}".format(name.upper()))




""" 
def hello_world():
    print("Hello World!")
    print_name()
def print_name():
    print("Type your name")
    name=input()
    sum=2+2
    print("Nice to meet you "+name+"\n"+str(sum))    
hello_world()
"""  
def add_two_numbers():
    number1=1
    number2=2
    result=number1+number2
    #print(result)
    print(str(number1)+" plus "+str(number2)+" is " +str(result))
    print("{} plus {} is {}.".format(number1,number2,result))
add_two_numbers()

def add_two_numbers_from_args(number1,number2):
    result=number1+number2
    #print(result)
    print(str(number1)+" plus "+str(number2)+" is " +str(result))
    print("{} plus {} is {}.".format(number1,number2,result))
add_two_numbers_from_args(1,2)