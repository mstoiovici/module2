# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:48:50 2019

@author: maria
"""

print("------------------Codebar 16 of Jan----------------")
def sum_of(a,b):
    return a+b
    
def product_of(c,d):
    return c*d

def sum_then_square(egg,bacon):
    breakfast=sum_of(egg,bacon)
    big_breakfast=product_of(breakfast,breakfast)
    return big_breakfast
    
sum_then_square(5,7)