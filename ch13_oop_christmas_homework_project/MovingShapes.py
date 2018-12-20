#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:24:29 2018

@author: maria
"""
from shapes import *
from pylab import random as r
class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape=shape
        self.diameter=diameter
        self.figure=Shape(shape,diameter)
        self.current_location=(0,0)
        self.speed="fastest"
    def goto(self,x,y):
        self.figure.goto(x,y)
    def moveTick(self):
        pass
    
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"square",diameter)
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"diamond",diameter)
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"circle",diameter)

