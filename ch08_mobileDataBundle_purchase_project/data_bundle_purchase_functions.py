# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:18:49 2019

@author: maria
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        option = chooseTransaction(balance)
        if option == 1:
            return checkBalance(balance)
        elif option == 2:
            if validateNumbers():
                return purchaseDataBundle(balance) 
        elif option == 3:
            return topUp(balance)
         
            ##--Checking user password--##
        
def passwordCheck(truePasscode):
    while True:
        try:
            passcode = input("Please enter your password: ")
            if passcode == truePasscode:
                return True
            else: 
                raise passcode_no_match
        except Exception as passcode_no_match:
            print("You have entered an incorrect password. Please try again.")
        else:
            break
        
##--Asking user what type of transaction they would like to do--##         
            
def chooseTransaction(balance):
    print("To check your balance, please type 1: \n")
    print("To purchase a data bundle, please type 2: \n")
    print("To top up your account, please type 3: \n")
    while True:
        try:
            option = int(input(""))
            if option == 1:
                return option
            elif option == 2:
                return option
            elif option ==3:
                return option
            else:
                raise Exception
        except Exception:
            print("Sorry, you haven't chosen a valid option, please try again.")
        else:
            break
    
 
        

    

        

 
    ##--Display balance to user their balance--##
     
def checkBalance(balance):
    if balance > 0:
        print("Your balance is {}".format(balance))
        return balance
    
    else:
        print("Your balance is not sufficient: {}".format(balance))
        return balance
    
##--Purchasing data function if balance insufficient you can topUp--##
        
def purchaseDataBundle(balance):
    print("Your current balance is {}".format(balance))
    while True:
        try:
            dataPurchase=int(input("How much money would you like to spend on purchasing data? "))
            if dataPurchase<=0:
                print("You cannot purchase 0 or a negative amount of data. ")
                raise Exception
            elif dataPurchase > 100:
                print("You can only purchase less than £100 worth of data.") 
                raise Exception
            elif dataPurchase%5!=0:
                print("Data purchased value can only be a multiple of 5.")
                raise Exception
            elif dataPurchase > balance:
                print("Your balance is insufficient for this purchase.")
                balance=optToTopUp(balance)
                return balance
           
        except Exception:
            print("")
            
        else:
            balance=round(balance-dataPurchase, 2)
            print("Your new balance is {}".format(balance))
            return balance
            
    
def optToTopUp(balance):
    while True:
        try:
            topUpOption=int(input("Please type 1 if you would like to topUp or type 2 to go back: "))
            if topUpOption == 1:
                balance=topUp(balance)
                goBack = purchaseDataBundle(balance)
                return goBack
                
            elif topUpOption ==2:
                goBack=purchaseDataBundle(balance)
                return goBack
                
            elif topUpOption != 1 or topUpOption != 2:
                raise Exception
            
        except Exception:
            print("Please choose a valid option.")

            
            
            
#--Validate user number twice function using loop--#
            
def validateNumbers():  
    while True:    
        try:
            numbers=checkDataTypeOfNumbers()      
            if numbers[0]==numbers[1]:
                return True
            else:
                raise no_match
                
        except Exception as no_match:
            print("You need to enter the correct phone number twice in order to proceed. Please try again ")
        else:
            break
        
def checkDataTypeOfNumbers():
    while True:
        try:
            phoneOne=input("Please enter your phone number for the first time: ")
            if len(phoneOne) != 11:
                if phoneOne.isdigit():
                    raise digit_error 
                else:
                    raise character_error
                    
               
            elif phoneOne.isalpha():
                raise character_error
                
        except ValueError:
            print("Please only type an 11 digit phone number! ")

        except Exception as digit_error:
            print ("Please enter 11 digits\n")
            
        except Exception as character_error:    
            print("Please type numbers only!")
            

            
        else:
            break
        
    while True:
        try:
            phoneTwo=input("Please enter your phone number for the second time: ")
            if len(phoneTwo) != 11:
                if phoneTwo.isdigit():
                    raise digit_error 
                else:
                    raise character_error
                    
               
            elif phoneTwo.isalpha():
                raise character_error
                
        except ValueError:
            print("Please only type an 11 digit phone number! ")

        except Exception as digit_error:
            print ("Please enter 11 digits\n")
            
        except Exception as character_error:    
            print("Please type numbers only!")
                      
        else:
            break
    return phoneOne, phoneTwo            

    
##--Topping up account function--##
    
def topUp(balance):
    print("Your balance is {}".format(balance))
    while True:
        try:
            topUpValue=float(input("How much would you like to to top up your balance by? "))
            if topUpValue<=0:
                raise Exception
        except Exception:
            print("Please enter a valid topUp amount.")
        else:
            newBalance = round(balance + topUpValue, 2)
            print("Your new balance is {}".format(newBalance))
            break
    return newBalance
  
    











#------------------------------------------------------------------#

#Validation alternative for password:  
      
#def passwordCheckAttempt1(truePasscode):
#   """
#   takes only one parameter:truePasscode
#   checks the password from the user to be the true password from the database- given here when calling the main function DataBundlePurchase
#   """
#   attempt1=input("Please enter your password: ")
#   if attempt1==truePasscode:
#       return True
#   else:
#       giveMoreAttemptsToCheckPassword(truePasscode)
#def giveMoreAttemptsToCheckPassword(truePasscode):
#   """
#   takes only one parameter:truePasscode
#   gives 2 other attempts to user to give the right passcode
#   """
#   attempt2=input("Please enter your password for the second time: ")
#   if attempt2==truePasscode:
#       return True
#   else:
#       attempt3=input("Please enter your password for the third time: ")
#       if attempt3==truePasscode:
#           return True
#       else:
#           return False

    