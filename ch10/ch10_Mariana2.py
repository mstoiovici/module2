#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:02:31 2018

@author: maria
"""


print("-----17.12 further practice-------------------------------------------")
print("-----17.12 further practice-------------------------------------------")
metals_sPF={"gold":(19.3,272.1,4),"iron":(7.8,165.9,78),"zinc":(7.13,87.2,35.4),"lead":(11.4,485,27.8)}
print(metals_sPF)
print(sorted(metals_sPF.items(), key=lambda kv:kv[0]))
a=sorted(metals_sPF.items(), key=lambda kv:kv[1])
print(a[0:3])
print(a[0:])
print(sorted(metals_sPF.items(), key=lambda kv:kv[1][1],reverse=True)[2])
print()
#Practise with dict with function & subFun, variable, user inputs & if/else
#Write a function that can generate a phoneBook_dict which contains 4 classmates’ info as below:
#{Name: [‘last-3-digit of phoneNo.’, LuckyNo., PostCode, Town/city]}
#Tip, you can use user input, and append to append more items to the value_list
#Challenge -- A: the function also can:
#Sort the dictionary by Name -- alphabet
#Sort the dictionary by Town/city -- alphabet
#Sort dictionary by LuckyNo
#Challenge -- 2: add two more items in the value_list, and can be sorted as well:
#1. How many years differ from the Queen's age? (use QueenAge variable).
#2. Write the final dict to a file. 
"""
def get_info(phoneBook_dict={},values="",age=0,name="",last_3_digit_of_phoneNo="",luckyNo="",postCode="",town="",i=0):
    name=str(input("Please type the name:\n"))
    last_3_digit_of_phoneNo=input("Please type last_3_digit_of_phone\n")
    luckyNo=input("Please type luckyNo\n")
    postCode=input("Please type postCode\n")
    town=input("Please typetown \n")
    age=int(input("Please type age\n"))
    #values=last_3_digit_of_phoneNo,luckyNo,postCode,town,age
    phoneBook_dict[name]=last_3_digit_of_phoneNo,luckyNo,postCode,town,age
    print(phoneBook_dict)
    return phoneBook_dict
    
def generate_dict(phoneBook_dict,i=0):
    while i<1:
        phoneBook_dict =get_info(phoneBook_dict,i=0)
        i+=1  
    return phoneBook_dict
def sort_dictionary(phoneBook_dict):
    phoneBook_dict =generate_dict(phoneBook_dict)
    print(sorted(phoneBook_dict.items(), key=lambda kv:kv[0]))
    print(sorted(phoneBook_dict.items(), key=lambda kv:kv[1][3]))
    print(sorted(phoneBook_dict.items(), key=lambda kv:kv[1][1]))

def add_age (phoneBook_dict,queen_age=95,age_diff=0):
    generate_dict(phoneBook_dict)
    print(phoneBook_dict)  
    
  
    if age<queen_age:
    
        
        age_diff=queen_age-age
        print("you are younger than the queen by {} years.".format(age_diff))
        
    elif age==queen_age:
        print("you are the same age as the queen")
    else:
        age_diff=age-queen_age
        print("wow,you are older than the queen by {} years.".format(age_diff))
     
    return phoneBook_dict
    
add_age (phoneBook_dict,queen_age=95,age_diff=0)
#sort_dictionary(phoneBook_dict={})
"""
print()
print("-----my way-------------------------------------------")

def get_info(phoneBook_dict,name,last_3_digit_of_phoneNo="",luckyNo="",postCode="",town="",age=0):
    name=input("Please type the name:\n")
    last_3_digit_of_phoneNo=input("Please type last_3_digit_of_phone\n")
    luckyNo=int(input("Please type luckyNo\n"))
    postCode=input("Please type postCode\n")
    town=input("Please typetown \n")
    age=int(input("Please type age\n"))
    phoneBook_dict[name]=last_3_digit_of_phoneNo,luckyNo,postCode,town,age
    print(phoneBook_dict)
    return phoneBook_dict
    

def generate_dict(phoneBook_dict,i=0):
   
    while i<4:
        phoneBook_dict =get_info(phoneBook_dict,name)
        i+=1  
    print(phoneBook_dict)
    return phoneBook_dict
"""
def check_age (phoneBook_dict,queen_age=95,age_diff=0):
    
    print(phoneBook_dict)  
    
  
    if age<queen_age:
    
        
        age_diff=queen_age-age
        print("you are younger than the queen by {} years.".format(age_diff))
        
    elif age==queen_age:
        print("you are the same age as the queen")
    else:
        age_diff=age-queen_age
        print("wow,you are older than the queen by {} years.".format(age_diff))
     
    return phoneBook_dict
"""
name=""
phoneBook_dict = {}
generate_dict(phoneBook_dict)
print()
print("-----Kirsties's way-------------------------------------------")
def get_info(phoneBook_dict):
    name=str(input("Please type the name:\n"))
    last_3_digit_of_phoneNo=input("Please type last_3_digit_of_phone\n")
    luckyNo=int(input("Please type luckyNo\n"))
    postCode=input("Please type postCode\n")
    town=input("Please typetown \n")
    age=int(input("Please type age\n"))
    diff = get_difference_in_age(age)
    return generate_dict(name, last_3_digit_of_phoneNo,luckyNo,postCode,town,age,diff,phoneBook_dict)
     

def generate_dict( name, last_3_digit_of_phoneNo,luckyNo,postCode,town,age,diff,phoneBook_dict):
    
    phoneBook_dict[name]=last_3_digit_of_phoneNo,luckyNo,postCode,town,age
    again = input("would you like to add another student? type y or n:")
    if again == "y":
        return get_info(phoneBook_dict)
    else:
        print(phoneBook_dict)
    return phoneBook_dict

def get_difference_in_age(age):
    if age<92:
        diff=92-age
        print("you are younger than the queen by {} years.".format(diff))
        return diff
    elif age==92:
        diff = 0
        print("you are the same age as the queen")
        return diff
    elif age>92:
        diff=age-92
        #print("wow,you are older than the queen by {} years.".format(diff))        return diff
        return diff
    else:
        print("what")
        return diff
  
        
   
phoneBook_dict = {}
get_info(phoneBook_dict)
print()
print("-----improved way 1-------------------------------------------")
name = ""
last3digit = ""
luckyNo = ""
phoneBook_dict = {}

def readInput():
    global name
    name = input("Give the name of the user you want to add: ")
    global last3digit 
    last3digit = input("Give the last3digit: ")
    global luckyNo 
    luckyNo = input("Give the luckyNo: ")
    

def generate(phoneBook_dict):
    cont = 'Y'
    while (cont == 'Y'):
        readInput()
        #print(name + " " + last3digit + " " + luckyNo)
        phoneBook_dict.update({
            name: [last3digit, luckyNo]
        })
        
        cont = input("Want to add another? (Y/N)")
        if cont == "N":
            return phoneBook_dict
    
result = generate(phoneBook_dict)
print(result)
print()
print("-----improved way 2-------------------------------------------")
name = ""
last3digit = ""
luckyNo = ""
phoneBook_dict = {}

def readInput():
    global name
    name = input("Give the name of the user you want to add: ")
    global last3digit 
    last3digit = input("Give the last3digit: ")
    global luckyNo 
    luckyNo = input("Give the luckyNo: ")
    

def generate():
    cont = 'Y'
    while (cont == 'Y'):
        readInput()
        #print(name + " " + last3digit + " " + luckyNo)
        phoneBook_dict.update({
            name: [last3digit, luckyNo]
        })
        
        cont = input("Want to add another? (Y/N)")
        if cont == "N":
            break;
        #return phoneBook_dict

#phoneBook_dictMama = generate()  
generate()
print(phoneBook_dict)