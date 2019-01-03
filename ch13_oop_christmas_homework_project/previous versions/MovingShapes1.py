#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:16:57 2018

@author: maria
"""
#07/7 chamging the self.dx or self.dy into a negative number
#07/8 done, but diffferent way than the book
from shape import *
import random 
class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape=shape
        self.frame=frame
        self.diameter=diameter
        self.figure=Shape(shape,diameter)
        self.minx=self.diameter/2
        self.miny=self.diameter/2
        self.maxx=self.frame.width-self.diameter/2+1
        self.maxy=self.frame.height-self.diameter/2+1
        self.x=random.randrange(self.minx,self.maxx)
        self.y=random.randrange(self.miny,self.maxy)
        self.dx=5+10*random.random()
        self.dy=5+10*random.random()
        self.goto(self.x,self.y)
        
    def goto(self,x,y):
        self.figure.goto(x,y)
    def moveTick(self):
        self.x+=self.dx
        self.y+=self.dy
        self.figure.goto(self.x,self.y)
        
        
    
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"square",diameter)
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"diamond",diameter)
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"circle",diameter)


