#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:42:48 2018

@author: maria
"""

from MovingShapes import *
frame=Frame()
shape1=Square(frame,100)
for i in range(100):
    shape1.moveTick()