# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:28:20 2018

@author: maria
"""
def DataBundlePurchase(truePasscode, balance,maxDataAmount):
    if passwordCheck(truePasscode):
        transactionType=input("What do you want to do? \n1.Check your balance \n2.Purchase data bundle \nPlease type 1 or 2: ")
        if transactionType=="1":
            showBalance(balance)
        elif transactionType=="2":
            purchaseDataBundle(balance,maxDataAmount)
        else:
            print ("You did'n choose a transaction. Good bye.")
    else:
        print( "If you forgot your password please see instructions on how to recover it.")
    #return balance  
    

def passwordCheck(truePasscode):
    attempt1=input("Please enter your password: ")
    if attempt1==truePasscode:
        return True
    else:
        giveMoreAttemptsToCheckPassword(truePasscode)
        
        
def giveMoreAttemptsToCheckPassword(truePasscode):
    attempt2=input("Please enter your password for the second time: ")
    if attempt2==truePasscode:
        return True
    else:
        attempt3=input("Please enter your password for the third time: ")
        if attempt3==truePasscode:
            return True
        else:
            return False
            
def showBalance(balance):
    print("Your balance is: {}.".format(balance))
    return balance
def purchaseDataBundle(balance,maxDataAmount):
    if checkPhoneNumber():
        dataAmount=int(input("The maximum amount of data is 100.How much data do you want to purchase? \n"))

        if checkData(dataAmount,maxDataAmount):
            checkBalance(balance,dataAmount)
            
        else:
            return "You can purchase a maximum of only 100."
    
    else:
        return "You need to enter your phone number correctly twice. Please try again later."
def checkPhoneNumber():
    phoneNr1=input("Enter phone number: ")
    phoneNr2=input("Enter phone number again: ")
    if phoneNr1==phoneNr2:
        return True
    else:
        return "You need to enter your phone number correctly twice. Please try again later."    
def checkData(dataAmount,maxDataAmount):
    if maxDataAmount>=dataAmount:
        return True
    else:
        return False
    
def checkBalance(balance,dataAmount):
    if balance>=dataAmount:
        print("You have enough balance for this purchase.")
        return checkMultipleOfFive(dataAmount,balance)
    else:
        print("You don't have enough balance for this purchase.")
        

def checkMultipleOfFive(dataAmount,balance):
    if multipleOfFive(dataAmount):
        print("Transaction authorised")
        print("Your new balance is ", balance-dataAmount, " GBP")
        return ("top-up-request ", dataAmount)
    else:
        print("But amount is not a multiple of 5")
        print("Request refused")
    
def multipleOfFive(dataAmount):
    if dataAmount%5==0:
        return True
    else:
        return False
        


result = DataBundlePurchase('1234', 34.55,100)
print ('-----\nRESULT:', result)

        
        
        
        
     