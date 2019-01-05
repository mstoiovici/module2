# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:51:44 2019

@author: maria
"""
"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""
def first_two(str):
    lenght=len(str)
    if lenght==0:
        #print("")
        return ""
    elif lenght<=2:
        #print(str)
        return str
    elif lenght>2:
        #print(str[0:2])
        return str[0:2]
    else:
        pass

first_two("Mariana")