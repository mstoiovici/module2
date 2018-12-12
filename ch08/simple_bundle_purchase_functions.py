#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:02 2018

@author: maria
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        return "Password ok"
    else:
        return "Wrong password"
    
    return "not yet created"

def passwordCheck(truePasscode):
    attempt=input("Please enter your password")
    
    if attempt==truePasscode:
        return True
    else:
        return False
    
