# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:28:54 2018

@author: maria
"""

from shape import *

frame=Frame()
s1=Shape("square",100)
s1.goto(400,500)
for i in range(100):
    s1.goto(x,y)
    x=x+5
    y=y+5
s2=Shape("circle",75)
s2.goto(275,55)
