#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:59:41 2019

@author: maria
"""

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
            #print (True)
            return True
        else:
            pass
    #print (False)
    return False
has22([1, 2, 2])
has22([1, 2, 1, 2])
has22([2, 1, 2])