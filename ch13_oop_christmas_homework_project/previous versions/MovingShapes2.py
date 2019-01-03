#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:16:57 2018

@author: maria
"""
#07/9 solved when squares are hitting the walls
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
        self.dx=1+10*random.random()
        self.dy=1+10*random.random()
        self.goto(self.x,self.y)
        
    def goto(self,x,y):
        self.figure.goto(x,y)
    def moveTick(self):
        self.x+=self.dx
        self.y+=self.dy
        self.figure.goto(self.x,self.y)
        
        if self.x>self.maxx:
            self.dx=1+(-10)*random.random()
            self.x+=self.dx
            self.y+=self.dy
            self.figure.goto(self.x,self.y)
        if self.x<self.minx:
            self.dx=1+10*random.random()
            self.x+=self.dx
            self.y+=self.dy
            self.figure.goto(self.x,self.y)
            
        
        if self.y>self.maxy:
            self.dy=1+(-10)*random.random()
            self.x+=self.dx
            self.y+=self.dy
            self.figure.goto(self.x,self.y)
        if self.y<self.miny:
            self.dy=1+10*random.random()
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


