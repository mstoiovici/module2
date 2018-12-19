#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:21:16 2018

@author: maria
"""

def DataBundlePurchase(truePasscode, balance,maxDataAmount):
    """
    DataBundlePurchase uses 3 parameters: truePasscode,balance,maxDataAmount which will be given when calling the main function DataBundlePurchase
    if password from user will be the true password, the user will have tha option to choose from 2 transactions: see his balance or make a purchase
    """
    if passwordCheck(truePasscode):
        transactionType=input("What do you want to do? \n1.Check your balance \n2.Purchase data bundle \nPlease type 1 or 2: ")
        if transactionType=="1":
            showBalance(balance)
        elif transactionType=="2":
            purchaseDataBundle(balance,maxDataAmount)
        else:
            return "You did'n choose a transaction. Good bye."
    else:
        return "If you forgot your password please see instructions on how to recover it."
    
    
def passwordCheck(truePasscode):
    """
    takes only one parameter:truePasscode
    checks the password from the user to be the true password from the database- given here when calling the main function DataBundlePurchase
    """
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
    else:
        return False

def showBalance(balance):
    """
    takes only one parameter: balance
    shows the current balance if this function is called
    """
    print("Your balance is: {}.".format(balance))
    return balance

def purchaseDataBundle(balance,maxDataAmount):
    """
    uses 2 parameters: the given balance and the maximum data amount which will be given when calling the main function DataBundlePurchase
    calls checkPhoneNumber function
    calls checkData function
    calls checkBalance function
    calls the multipleOfFive function
    after all the checks it authorises the purchase and takes it from the balance
    """
    if checkPhoneNumber():
        dataAmount=int(input("The maximum amount of data is 100.How much data do you want to purchase? \n"))

        if checkData(dataAmount,maxDataAmount):
            if checkBalance(balance,dataAmount):
                if multipleOfFive(dataAmount):
                    print("Transaction authorised")
                    print("Your new balance is ", balance-dataAmount, " GBP")
                    return ("top-up-request ", dataAmount)
                else:
                    print("But amount is not a multiple of 5")
                    print("Request refused")
        else:
            return "You can purchase a maximum of only 100."
    
    else:
        return "You need to enter your phone number correctly twice. Please try again later."
def checkPhoneNumber():
    """
    checks if the phone number entered twice is the same
    """
    phoneNr1=input("Enter phone number: ")
    phoneNr2=input("Enter phone number again: ")
    if phoneNr1==phoneNr2:
        return True
    else:
        return "You need to enter your phone number correctly twice. Please try again later."
    
def checkData(dataAmount,maxDataAmount):
    """
    checks if the amount from the user is within the given maximum data
    """
    if maxDataAmount>=dataAmount:
        return True
    else:
        return False
    
def checkBalance(balance,dataAmount):
    """
    checks if the amount from the user is affordable within his balance 
    """
    if balance>=dataAmount:
        print("You have enough balance for this purchase.")
        return True
    else:
        print("You don't have enough balance for this purchase.")
        return False

def multipleOfFive(dataAmount):
    """
    checks if the amount from user is a multiple of 5
    """
    if dataAmount%5==0:
        return True
    else:
        return False
    
"""  
# this could be an improved version of checkPhoneNumber() but too complicated for the moment
#it checks that the input from the user with the phone nr has 11 digits
def checkPhoneNumber():
    while True:
        phoneNr1= input("Enter phone number: ")

        try:
            if len(phoneNr1) != 11:
                #print ("Enter 10 digits\n")#
                continue

        except ValueError:
            print ("Enter only numbers\n")
            continue

        else: 
            break
    while True:
        phoneNr2 = input("Enter number: ")

        try:
            if len(phoneNr2) != 11:
                print ("Enter 10 digits\n")
                continue

        except ValueError:
            print ("Enter only numbers\n")
            continue

        else: 
            break
    if phoneNr1==phoneNr2:
        return True
    else:
        return "You need to enter your phone number correctly twice. Please try again later."
"""