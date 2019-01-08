# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:36:03 2019

@author: maria
"""

"""

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(list1):
    i=0
    for item in list1:
        if item%2==0:
            i+=1
    #print(i)    
    return i   
  
count_evens([2,1,2,3,4])   
count_evens([2,2,0]) 
count_evens([1,3,5])   