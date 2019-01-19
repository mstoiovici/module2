# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:56:24 2019

@author: maria
"""

"""
Write the letters 'A' to 'Z' ( upper case) to the console, placing each letter on a new line.
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