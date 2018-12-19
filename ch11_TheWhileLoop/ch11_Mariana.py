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

print("----Task6 Guessing game 1------------------------------------------")
from random import randint
def guess(attempts,end_range):
    
    number=randint(1,end_range)
    print("Welcome! Can you guess my secret number?\n")
    
    while attempts>0:
        answer=int(input("So, what's the number?\n"))
        if answer==number:
            print("You guessed! You won!")
            break
        else:
            if answer<number:
                print("No, that's too low!")
            else:
                print("No, that's too high!")
            
        attempts-=1
        print("You have",attempts,"attempts left")
    print("End-Of-Game: thanks for playing! ")

guess(3,20)



print()
print("----Task7 Guessing dicing game - improved version------------------------------")

#from random import randint
def guess():
    game=input("Do you want to play? Choose yes or no:\n")
    while game=="yes":
        guess=input("Do you think it will be odd or even?\n")
        dice1=randint(1,6)
        dice2=randint(1,6)
        sum=dice1+dice2
        print("First dice was: ",dice1,"and second dice was: ",dice2)
        if (sum%2==0 and guess=="even")or(sum%2!=0 and guess=="odd"):
            print("You guessed!")
        else:
            print("You din not guess!")
        game_update=input("Do you still want to play? Choose yes or no:\n")
        if game_update=="no":
            break
    print("Thanks for playing! See you later!")
    
guess()


print()
print("----Task7 Guessing dicing game - first version------------------------------------------")
#from random import randint
def guess():
    game=input("Do you want to play? Choose yes or no:\n")
    while game=="yes":
        guess=input("Do you think it will be odd or even?\n")
        dice1=randint(1,6)
        dice2=randint(1,6)
        sum=dice1+dice2
        if sum%2==0 and guess=="even":
            print("You guessed!")
            print("First dice was: ",dice1,"and second dice was: ",dice2,"so the sum is even")
        elif sum%2==0 and guess!="even":
            print("You din not guess!")
            print("First dice was: ",dice1,"and second dice was: ",dice2,"so the sum is even")

        elif sum%2!=0 and guess=="odd":
            print("You guessed!")
            print("First dice was: ",dice1,"and second dice was: ",dice2,"so the sum is odd")

        else:
            print("You din not guess!")
            print("First dice was: ",dice1,"and second dice was: ",dice2,"so the sum is odd")

        game_update=input("Do you still want to play? Choose yes or no:\n")
        if game_update=="no":
            break
    print("Thanks for playing! See you later!")
    
guess()



