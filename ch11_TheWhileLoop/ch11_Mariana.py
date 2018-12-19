#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:53:45 2018

@author: maria
"""

print("----Chapter 11, The While Loop-----------")
print("----Task1------------------------------------------")
x=33
while x>=1:
    print(x,":",end="")
    x=x/2
print(x)




print()
print("-Task2- return the sum of values from n down to 1,(n+(n-1)+(n-2)+...+2+1)---------")

def get_sum(mySum,n):
    while n>0: 
        mySum += n
        n -= 1    
    print (mySum)
    return mySum
mySum = 0 
n = 3     
get_sum(mySum,n)




print()
print("----Task3- return the values of multiplying from n down to 1,(n*(n-1)*(n-2)*...*2*1)------------")
def get_multiplyed_value(myValue,n):
    while n>0: 
        myValue *= n
        n -= 1    
    print (myValue)
    return myValue
myValue = 1
n = 4    
get_multiplyed_value(myValue,n)


print()
print("-----------------------Task4------------------------------------")
   
def decide_pass(student_number):
    while student_number>0: 
        print("You have ",student_number," to evaluate: ",end="")
        mark = int(input("what is the mark?\n"))
        if mark>=70:
            print("You pass first!")
        elif mark>=40:
            print("You pass!")
        else:
            print("You did not pass!")
        student_number-=1

student_number =5
decide_pass(student_number)


print()
print("---------------------Task5-------------------------------------")
print("--- ex1-----------------")

i=55
while i>10:
    print(i)
    i=i*0.8
    if i==35.2:
        break



print()
print("------- ex2--------------")
def give_greetings(greeting_no):
    while greeting_no>0:
        name=input("Whats your name?\n")
        if name=="done":
            break
        print("hello",name)
        greeting_no-=1
       

greeting_no=int(input("How many greeting would you like to give?"))
give_greetings(greeting_no)



