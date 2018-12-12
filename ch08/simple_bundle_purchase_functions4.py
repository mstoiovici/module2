#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:21:16 2018

@author: maria
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        askForTransaction(balance)
           
    else:
        return "If you forgot your password please see instructions on how to recover it."
    
    

def passwordCheck(truePasscode):
    attempt1=input("Please enter your password: ")

    if attempt1==truePasscode:
        return True
    elif attempt1!=truePasscode:
        attempt2=input("Please enter your password for the second time: ")
        if attempt2==truePasscode:
            return True
        elif attempt2!=truePasscode:
            attempt3=input("Please enter your password for the third time: ")
            if attempt3==truePasscode:
                return True
            else:
                return False
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
        showBalance(balance)
    elif transactionType=="2":
       purchaseDataBundle(balance)
    else:
        print("You did not choose a transaction type. Have a good day.")
    
def purchaseDataBundle(balance):
    if checkBalance(balance):
        print ("Your balance is {}, but the service is unavailable".format(balance))
        return (balance)
    else:
        print ("Your balance is not sufficient.You have: {}.".format(balance))
        return (balance)
 
