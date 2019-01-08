#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:47:57 2018

@author: maria
"""

"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, eg 5%2 is 1.
count_evens([2,1,2,3,4]) -3
count_evens([2,2,0]) -3
count_evens([1,3,5]) -0
"""
def count_evens(nums):
    i=0
    for item in nums:
        if item%2==0:
            i+=1
    #print(i)    
    return i   
  
#count_evens([2,1,2,3,4])   
#count_evens([2,2,0]) 
#count_evens([1,3,5])   

"""
 
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
​
has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""
def has22(nums):
    for index in range(len(nums)-1):
        #print(nums[index],nums[index+1])
        if nums[index]==2 and nums[index+1]==2:
    
        
        #break
            print (True)
            return True
        else:
            pass
    print (False)
    return False
has22([1, 2, 2])
has22([1, 2, 1, 2])
has22([2, 1, 2])

"""
Return the sum of the numbers in the array, but ignore sections of numbers starting with a 6 until the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
#def sum67(nums):
#    total = 0
#    for index in range(len(nums)):
#        print(total,nums[index])
#        #startWithSix=[6,61,62,63,64...]
#        #for nums[index] in startWithSix:
#        #for nums[index]!=6:
#            total += nums[index]
#            
#            print (total)
#        elif nums[index]==7:
#            total+=nums[index+1]
#        else:
#            pass
#    return total       
       
 
#sum67([1, 2, 2,60,6,1,7,2])


"""
Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line.
"""   
import string
letters = list(string.ascii_uppercase)
print (letters)
for val in letters:
    print(val)

"""
For every third letter, write it to the console in lowercase instead.

For every fourth letter, write its numeric position in the alphabet to the console instead (e.g. instead of outputting 'D' output '4').

If a letter satisfies both rules 2 and 3, write out its numeric position followed by the letter in lowercase (e.g. 'L' should be output as '12l').
"""
letters = list(string.ascii_uppercase)
print (letters)
         
letters=string.ascii_lowercase
for i in range(0,len(letters)):
    if i%3==2:
        print(letters[i].lower())
   
    else:
        print(letters[i].upper())
            
letters = list(string.ascii_uppercase)
print (letters)