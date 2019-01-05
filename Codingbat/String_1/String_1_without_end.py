#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:01:52 2019

@author: maria
"""

"""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""
def without_end(str):
    #print(str[1:-1])
    return str[1:-1]
without_end("Mariana")