#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:59:18 2018

@author: maria
"""



print("-----------------------------task1-------------------------------")
def hello_world():
    print("Hello World!")
    print_name()
    
print()    
print("-----------------------------task2-------------------------------")
def print_name():
    print("Type your name")
    name=input()
    sum=2+2
    print("Nice to meet you "+name+"\n"+str(sum))    
hello_world()


print()    
print("-----------------------------task3-------------------------------")
def add_two_numbers():
    number1=1
    number2=2
    result=number1+number2
    #print(result)
    print(str(number1)+" plus "+str(number2)+" is " +str(result))
    print("{} plus {} is {}.".format(number1,number2,result))
add_two_numbers()


print()    
print("-----------------------------task4-------------------------------")
def add_two_numbers_from_args(number1,number2):
    result=number1+number2
    #print(result)
    print(str(number1)+" plus "+str(number2)+" is " +str(result))
    print("{} plus {} is {}.".format(number1,number2,result))
add_two_numbers_from_args(1,2)


print()    
print("-----------------------------task5-------------------------------")  
def hello_world_2args(a,b):
    print("{} {}".format(a,b))
    
a="hello"
b="world"
hello_world_2args(a,b)

print()
a="love"
b="coding"
hello_world_2args(a,b)


print()    
print("-----------------------------task6-------------------------------")
def hello_world_2args(a,b,c,d):
    print("{} {} {} {}".format(a,b,c,d))

a1="I"
b1="love"
c1="coding"
d1="so much"

hello_world_2args(a,b,c,d)
#hello_world_2args("I", "love","coding","so much")


print()    
print("-----------------------------task7-------------------------------")
def convert_distance(miles):
    kilometers=(miles*8.0)/5.0
    print("Converting distance in miles to kilometers:")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)
    
convert_distance(44)
convert_distance(122.5)


print()    
print("-----------------------------task8 -------------------------------")
def get_size(width,height,depth):
    area=width*height
    volume=width*height*depth
    sizes=(area,volume)
    return(sizes)
    
area_one=get_size(3,2,3)[0]
volume_one=get_size(3,2,3)[1]
sizes_one=get_size(3,2,3)
print(area_one)
print(volume_one)


print()    
print("-----------------------------task9-------------------------------")
def temp_converter(celsius):
    fahrenheit=celsius*9.0/5.0+32
    kelvin=celsius+273.15
    print("that's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit,kelvin))

celsius=float(input("what's the temperature in your city today?"))
temp_converter(celsius)


print()    
print("-----------------------------task10-------------------------------")
def temp_converter(celsius):
    fahrenheit=celsius*9.0/5.0+32
    kelvin=celsius+273.15
    temperature=(fahrenheit,kelvin)
    return(temperature)
    
celsius=float(input("what's the temperature in your city today?"))
fahrenheit_one=temp_converter(celsius)[0]
kelvin_one=temp_converter(celsius)[1]
print("that's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit_one,kelvin_one))


print()    
print("-----------------------------task11-------------------------------")
def convert_temperature_kelvin(centigrade):
    kelvin=centigrade+273.15
    return kelvin
def convert_temperature_fahrenheit(centigrade):
    fahrenheit=(centigrade*9)/5.0+32
    return fahrenheit
def convert_temperature_kelvin_to_fahrenheit(centigrade):
    kelvin=convert_temperature_kelvin(centigrade)
    fahrenheit=convert_temperature_fahrenheit(centigrade)#((kelvin*9)/5)-459.67
    print("converting temperature in kelvin to fahrenheit.")
    print("temperature in kelvin:", kelvin)
    print("temperature in fahrenheit:", fahrenheit)
   
    return (kelvin,fahrenheit)
centigrade=float(input("what's the temperature in centigrade in your city today?"))
convert_temperature_kelvin_to_fahrenheit(centigrade)


print()    
print("-----------------------------task12-------------------------------")
def add_two_numbers():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))

add_two_numbers()


print()    
print("-----------------------------task13-------------------------------")
def add_two_numbers_from_args(number1, number2): 
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))

add_two_numbers_from_args(5,10)

print()    
print("-----------------------------task14-------------------------------")
def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 
    return answer 

returned_value = add_two_numbers_and_return_value()
print (returned_value)
print(returned_value-5)



print()    
print("-----------------------------task15-------------------------------")
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print ("Get a blanket.\n")

#print("We can just give the function numbers directly:")
#cheese_and_crackers(20,30)
#print("Or, we can use the variables from our script:")
amount_of_cheese=10
amount_of_crackers=50
#cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#print("We can even do math inside too:")
#cheese_and_crackers(10+20,5+6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


print()    
print("-----------------------------task16-------------------------------")
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

print ("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print ("That becomes: ", what, "Can you do it by hand?")

