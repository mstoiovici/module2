#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:46:01 2018

@author: maria
"""

"""
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""
def make_out_word(out, word):
  a=out[0:2]
  b=out[2:4]
  print(a+word+b)
  return a+word+b

make_out_word("lala", "wow")