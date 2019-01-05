#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:05:20 2019

@author: maria
"""

"""
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""
def combo_string(a, b):
    lenght_a=len(a)
    lenght_b=len(b)
    if lenght_a<lenght_b:
        #print(a+b+a)
        return a+b+a
    elif lenght_b<lenght_a:
        #print(b+a+b)
        return b+a+b
    else:
        pass
    
combo_string("Mariana", "Chen")