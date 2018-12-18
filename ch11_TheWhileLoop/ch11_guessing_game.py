#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:30:52 2018

@author: maria
"""
print()
print("----Guessing game 1------------------------------------------")
from random import randint
def guess(attempts,range):
    number=randint(1,20)
    print("Welcome! Can you guess my secret number?\n")
    
    while attempts>0:
        answer=int(input("So, what's the number?\n"))
        if answer==number:
            print("You guessed!You won!")
            break
        else:
            if answer<number:
                print("No, that's too low!")
            else:
                print("No, that's too high!")
            
        attempts-=1
        print("You have",attempts,"attempts left")
    print("End-Of-Game: thanks for playing! ")

#guess(3,20)



print()
print("----Guessing game 2------------------------------------------")
from random import randint
def guess():
    game=input("Do you want to play? Choose yes or no:\n")
    while game=="yes":
        guess=input("Do you think it will be odd or even?\n")
        dice1=randint(1,6)
        dice2=randint(1,6)
        sum=dice1+dice2
        if sum%2==0 and guess=="even":
            print("You guessed!")
            game_update=input("Do you still want to play? Choose yes or no:\n")
            if game_update=="no":
                break
        elif sum%2==0 and guess!="even":
            print("You din not guess!")
            game_update=input("Do you still want to play? Choose yes or no:\n")
            if game_update=="no":
                break
        elif sum%2!=0 and guess!="odd":
            print("You guessed!")
            game_update=input("Do you still want to play? Choose yes or no:\n")
            if game_update=="no":
                break
        else:
            print("You din not guess!")
            game_update=input("Do you still want to play? Choose yes or no:\n")
            if game_update=="no":
                break
    
    
    
    print("Thanks for playing! See you later!")
    
guess()
