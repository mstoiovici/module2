#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:52:31 2018

@author: maria
"""

"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'S
first_half('abcdef') → 'abc'
"""
def first_half(str):
    lenght= len(str)
    print(str[0:int(lenght/2)])
    return str[0:int(lenght/2)]

first_half("lilian")