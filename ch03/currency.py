#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:04:42 2018

@author: maria
"""
def condition(currency):
    if currency=="romanian":
        print("Those money converts into {} romanian lei ".format(romanian))
        
def change_currency(money):
    romanian= money * 5.15
    american=money*0.85
    euro=money*0.90
    values=(romanian,american,euro)
    #print("Those money converts into {} romanian lei ".format(romanian))
    print("Or you could get {} american dollars ".format(american))
    print("Or  {} euros, if you want to travel to Europe ".format(euro))
    return values

money=float(input("Hello,how many pounds would you like to convert? "))
currency=input("And what currency would you prefer? You can choose from romanian, american or euros " )

change_currency(money)
print("Now, tell me") # have to imprve this code with more statement, operations, or conditionals