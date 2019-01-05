#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:03:10 2019

@author: maria
"""

"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""
def left2(str):
    up_to2=str[0:2]
    from2=str[2:]
    #print(from2+up_to2)
    return(from2+up_to2)

left2("Mariana")