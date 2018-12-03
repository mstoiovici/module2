# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:04:42 2018

@author: maria
"""

def change_romanian_currency(money):
    value= money * 5.15
    print("Those money converts into {} romanian lei ".format(value))
    return value
money=int(input("how many pounds would you like to convert?"))
change_romanian_currency(money)
