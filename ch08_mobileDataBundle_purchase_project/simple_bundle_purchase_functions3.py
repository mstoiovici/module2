#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:21:16 2018

@author: maria
"""

def DataBundlePurchase(truePasscode, balance):
    
    if passwordCheck(truePasscode):
        if askForTransaction(balance):
            showBalance(balance)
        else:
            purchaseDataBundle(balance)
      
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

def showBalance(balance):
    print("Your balance is: {}.".format(balance))
    return balance
        
    
def askForTransaction(balance):
    transactionType=input("What do you want to do? \n1.Check your balance \n2.Purchase data bundle \nPlease type 1 or 2: ")
    if transactionType=="1":
        return True
    else:
        return False
    
def purchaseDataBundle(balance):
    if checkBalance(balance):
        print ("Your balance is {}, but the service is unavailable".format(balance))
        return (balance)
    else:
        print ("Your balance is not sufficient.You have: {}.".format(balance))
        return (balance)
 
