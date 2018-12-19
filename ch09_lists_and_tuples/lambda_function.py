print# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:47:59 2018

@author: maria
"""
print("------------------------Lambda function----------------")
print("------Task1 Lists vs tuples----------------")
a=[50,1,2,3,4,5,6,7,8,9]
b=(10,1,2,3,4,5,6,7,8,9)
my_favourite_fruits=["apple","orange","banana"]
x=["yw","zs","cs","hd","ab"]
y=["ab","cs","hd","yw","zs"]
z=["zs","yw","hd","cs","ab"]
print(a)
print(b)
print(my_favourite_fruits)
print(x)
print(y)
print(z)

print()
print("-----Task2 Lists vs tuples when using simple sorted and sorted with lambda function-------")
print("------Simple sorted----------------")
a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["xa", "sb", "lf", "hw", "ed", "fy"]
y = sorted(x)

print()
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
x2=[("a",3,z),("c",1,y),("b",5,x)]
print(x2)
print()
print(sorted(x2))



print()
print("------And with lambda function----------------")
print(sorted(x2,key=lambda s:s[1]))
print()
print(sorted(x2,key=lambda s:s[2]))
print()
print(sorted(x2,key=lambda s:s[2][1]))


print()
print("------Task3----------------")
x=[1,2,3,4]
y=[3,4,10,3]
z=[20,10,30,40]
x2=[("a",3,z),("c",1,y),("b",5,x)]
print(sorted(x2,key=lambda s:s[2]))
print(sorted(x2,key=lambda s:s[2][0]))
#print(sorted(x2,key=lambda s:s[2][-1]))

print()
print("------Task4----------------")
a = [0,1,2,3]
b = (0,1,2,3)
myFavF = ["apple", "orange"]
x = ["xa", "sb", "lf"]
y = sorted(x)
z = ["fg", "uj", "sx"]
x2=[("a",3,z),("c",1,y),("b",5,x)]
print(x2)
print(sorted(x2))

print(sorted(x2,key=lambda s:s[1]))
print(sorted(x2,key=lambda s:s[2]))
print(sorted(x2,key=lambda s:s[2][1]))


print()
print("------Task5----------------")
a = [0,1,2,3]
b =(4,5,6)
myFavF = ["Joke", "Chen"]
x = ["Mari", "Fabiana", "Seraphine", "Hien"]
y = sorted(x)
z = ["Jennifer", "Katie", "Muna"]
x2=[("c",75,z),("a",23,y),("b",111,x)]
print(x2)
print(sorted(x2))
print()
print(sorted(x2,key=lambda s:s[1]))
print(sorted(x2,key=lambda s:s[1])[0])
print(sorted(x2,key=lambda s:s[2]))
print(sorted(x2,key=lambda s:s[2][1]))
print(sorted(x2,key=lambda s:s[2][-2][-2]))