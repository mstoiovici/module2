#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:32:26 2019

@author: maria
"""

print("---------Lists and Tuples------------------------------")

print("-----task1 Sorting a list using sorted- doesn't change the list--------------------------")
x=[7,11,3,9,2]
print(x)
print(sorted(x))
print(x)
sorted(x,reverse=True)
print(sorted(x,reverse=True))

print()
print("-----------------Task 2 Sort versus sorted on lists--------------")
print("----------------Sorted -desn't change the list")
x=[7,11,3,9,2]
print(x)
y=sorted(x)
print(y)
print(x)
print("----------------Sort - changes the list")
x.sort()
print(x)

print()
print("-----------------Task 3 Using reverse with sort and sorted--------------")
print("----------------Sorted")
x=[7,11,3,9,2]
print(x)
print(sorted(x))
print(x)
print(sorted(x,reverse=True))
print(x)
print("----------------Sort")
x.sort()
print(x)
x.sort(reverse=True)
print(x)


print()
print("---------task4 Operations on lists------------------------------")
x=["the","cat","sat","what","Mari"]
y=["on","the","mat","Cata","what"]
z=x+y
print(z)
set(x+y) ###_this is not clear yet
print(set(x+y))

print()
print("---------------Tuples----------------")
print("------------Task5 Changing tuples into lists-----------")
b=(0,1,2,3,4,5,6,7,8,9)
list(b) 
y=list(b) 
print(y)
print(type(b))
print(type(y))

print()
print("---------------Dictionaries----------------")
print("----Task6 Using lambda function to sort a dictionary-----")
print()
print("----simple example- sorts the dictionary by it's keys(but it look at the values of the keys)-----")
counts={"a":3,"c":1,"b":5}
print(counts)
key_list=counts.keys()
print(key_list)
key_list=list(counts.keys())
print(key_list)
key_list.sort(key=lambda k:counts[k])
print(key_list)

print()
print("----Task16 now with multiple values for a key using sort--"
       "sorts the dictionary by it s keys but it looks at the values of the keys, so it there are several values, it sorts using the first value---")
team={"Mari":(885,12),"Seraphine":(385,3),"Millie":(862,9)}
print(team)
key_list=team.keys()
print(key_list)
key_list=list(team.keys())
print(key_list)
key_list.sort(key=lambda k:team[k])
print(key_list)
print(team)


print()
print("----Task17 now with multiple values for a key using sorted-----")
team={"Mari":(885,12),"Seraphine":(385,3),"Millie":(862,9)}
print(team)
key_list=list(team.keys())
print(key_list)
sorted_key_list=sorted(key_list)
print(sorted_key_list)
print(sorted(key_list,key=lambda k:team[k]))
print(team)
print(key_list)
team_sorted=sorted(key_list,key=lambda k:team[k])
print(team_sorted)



