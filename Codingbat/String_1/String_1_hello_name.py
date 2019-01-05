#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:50:37 2018

@author: maria
"""

"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

"""

def hello_name(name):
    print("Hello "+name+"!")
    return "Hello "+name+"!"

hello_name("Mimi")