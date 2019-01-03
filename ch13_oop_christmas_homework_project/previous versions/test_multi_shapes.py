#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:33:22 2018

@author: maria
"""
# tests both Square and Circles
from MovingShapes2 import *
frame=Frame()
numshapes=4
shapes=[]
size=60

for i in range(numshapes):
    shapes.append(Square(frame,100))
    shapes.append(Circle(frame,100))
for i in range(200):
    for shape in shapes:
        shape.moveTick()
frame.close()
