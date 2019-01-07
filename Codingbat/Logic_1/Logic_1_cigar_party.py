#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:12:51 2019

@author: maria
"""
"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
def cigar_party(cigars, is_weekend):
    if is_weekend:
        if cigars>=40:
            #print("True")
            return True
        else:
            #print("False")
            return False
    else:
        if cigars>=40 and cigars<=60:
            #print("True")
            return True
        else:
            #print("False")
            return False

cigar_party(70, True)