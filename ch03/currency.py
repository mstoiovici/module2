#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:04:42 2018

@author: maria
"""

def change_currency(money):
    romanian_value= money * 5.15
    american_value=money*0.85
    euro_value=money*0.90
    values=(romanian_value,american_value,euro_value)
    print("Those money converts into {} romanian lei ".format(romanian_value))
    print("Or you could get {} american dollars ".format(american_value))
    print("Or  {} euros, if you want to travel to Europe ".format(euro_value))
    return values

money=float(input("Hello,how many pounds would you like to convert?"))
change_currency(money)
print("Now, tell me") # have to imprve this code with more statement, operations, or conditionals