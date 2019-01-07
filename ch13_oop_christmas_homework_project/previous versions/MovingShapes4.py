#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:16:57 2018

@author: maria
"""
#07/7 at start the shapes take different random directions
from shape import *
import random
import math
class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape=shape
        self.frame=frame
        self.diameter=diameter
        self.figure=Shape(shape,diameter)
        self.minxy=self.diameter/2                       #minimum value of x and y
        self.maxx=self.frame.width-self.minxy           #maximum value of x
        self.maxy=self.frame.height-self.minxy          #maximum value of y
        self.x=random.randrange(self.minxy,self.maxx+1)  #starting position x
        self.y=random.randrange(self.minxy,self.maxy+1)  #starting position y
        self.dx=1+10*random.random()                     #rate of movement for x (how much distance it covers in 1 step and which direction)
        self.dy=1+10*random.random()                     #rate of movement for y (how much distance it covers in 1 step and which direction)
        self.goto(self.x,self.y)                         #starting position 

    def goto(self,x,y):
        self.figure.goto(x,y)

    def moveTick(self):
        if self.x>self.maxx:                     #if hitting the right wall of the frame(maximum value of x change direction)
            self.dx=1+(-10)*random.random()
        elif self.x<self.minxy:                  #if hitting theleft wall of the frame(minimum value of x change direcion)
            self.dx=1+10*random.random()
        else:
            pass
        self.x+=self.dx                         #updates x with the value of dx

        if self.y>self.maxy:                    #if hitting the top wall of the frame(maximum value of y change direction)
            self.dy=1+(-10)*random.random()
        elif self.y<self.minxy:                 #if hitting the bottom wall of the frame(minimum value of y change direction)
            self.dy=1+10*random.random()
        else:
            pass
        self.y+=self.dy                         #updates y with the value of dy

        self.figure.goto(self.x,self.y)         #calls goto() in order to move the figure using the updated values of x and y

class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"square",diameter)

class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"diamond",diameter)
        self.minxy=self.diameter*math.sqrt(2)/2  # override MovingShape for minimum value of x and y (for diamond)
        self.maxx=self.frame.width-self.minxy    # override MovingShape for maximum value of x
        self.maxy=self.frame.height-self.minxy   # override MovingShape for maximum value of y

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,"circle",diameter)
