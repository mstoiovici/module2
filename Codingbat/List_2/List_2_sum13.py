# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:52:50 2019

@author: maria
"""

"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""

def sum13(nums):
    sum=0
    #print(len(nums))
    if len(nums) != 0:
        for index in range(len(nums)):
            
            print("index is:",index)
            if nums[index] != 13:
                sum+=nums[index]
                #print("sum is: ",sum)
            
                
            else:
                #print("this is 13. we stop here")
                index+=2
                sum+=nums[index]
                
    return sum

#sum13([1, 2, 13, 2, 1, 13]) 
def sum3(nums):
    sum=0
    #print(len(nums))
    if len(nums) != 0:
        for index in range(len(nums)):
            
            print("index is:",index)
            if nums[index] == 13:
                index+=2
                #print("sum is: ",sum)
            sum+=nums[index]
                
            
               
                
    return sum

def sum31(nums):
    sum=0
    for index in range(len(nums)):
        if nums[index] != 13:
            
            sum+=nums[index]
            
    print(sum)                    
    return sum
sum31([1, 2, 13, 2, 1, 13]) 