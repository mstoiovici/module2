#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:21:16 2018

@author: maria
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        if checkBalance(balance):
            return ("Your balance is {}.".format(balance))
        else:
            return ("Your balance is nop sufficient.You have: {}.".format(balance))
    else:
        return "Wrong password"
    
    

def passwordCheck(truePasscode):
    attempt=input("Please enter your password: ")
    
    if attempt==truePasscode:
        return True
    else:
        return False
    
def checkBalance(balance):
    if balance>0:
        return True
    else:
        return False