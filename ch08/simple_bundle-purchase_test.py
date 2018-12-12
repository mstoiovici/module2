#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:54 2018

@author: maria
"""

from simple_bundle_purchase_functions6 import DataBundlePurchase

# Test call to programme:
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = DataBundlePurchase('1234', 34.55,100)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')
"""
print ('TEST EXAMPLE 2')
result = DataBundlePurchase('2345', -1)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = DataBundlePurchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')
"""