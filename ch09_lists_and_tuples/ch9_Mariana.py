# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:24:19 2018

@author: maria
"""

print("------------------------Compound Data Types----------------")
print("---------Lists and Tuples------------------------------")
print("---------Lists------------------------------")

print()
print("---------task1 Write a list and access it's elements------------------------------")
my_favourite_fruits=["apple","orange","banana"]
x=["this",55,"that",my_favourite_fruits]
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[3][0]) ###### so you can access an element inside another element


print()
print("---------task2 Accessing elements out of range------------------------------")
#print(x[4]) # error: list index out of range
print("error: list index out of range")

print()
print("---------task3 Accessing elements------------------------------")
print(x[-1])
print(x[-2])  #### so you can access the first element of a list with 0, and so on from there. And you can access the last item of the list starting with -1 and then the previous last with -2 and so on.
########## x=[a,b,c,d]
########## x[0]=a
########## x[0]=a
########## x[1]=b
########## x[2]=c
########## x[3]=d
########## x[-1]=d
########## x[-2]=c
########## x[-3]=b
########## x[-4]=a


print()
print(x[-1][-2])
print(x[-2][-2]) # you can access a string as well and retrieve a part of it 
print(x[-1][-2][-2][0]) #???????????????????????????????


print()
print("---------task4 Remove an element from a list------------------------------")
x.remove(my_favourite_fruits) # removes the element from x
print(x)

print()
print("---------task5 Modify an element from a list------------------------------")
x[1]="and" # changes the element at position 1 with a new element:"and"
print(x)


print()
print("---------task6 Append an element to a list------------------------------")
x.append("again") # appends an element to a list
print(x)


print()
print("---------task7 Operations on lists------------------------------")
x=["the","cat","sat"]
y=["on","the","mat"]
z=x+y
print(z)
set(x+z)
print(set(x+z))## does something # set returns something but doesn't change the value of z. The return result of set is a dictionary.
#w=(z-y) #this doesn't work. Minus is not suported for lists
#print(w)


print()
print("---------task8 Slicing a list------------------------------")
x=["this","and","that","once","again"]
print(x[1:4])
print(x[1:3])
print(x[3:5])
print(x[-3:-1])


print()
print("---------task9 Sorting a list using sorted------------------------------")
x=[7,11,3,9,2]
print(x)
print(sorted(x))
print(x)
sorted(x,reverse=True)

####################from here is from pythontutor


print()
print("-----------------task 10 Variable holding strings versus variable holding lists--------------")
print("--------------Variables")
x="Mari"
y=x
y="Mariana"
print(y)
print(x)


print()
x="Mari"
y=x
y="Mari"
print(y)
print(x)



print()
print("----------------Lists")
x=["Mari","Ana"]
y=x
y=["Mari","Ana","Maria"]
print(y)
print(x)

print()
print("-----------------Task 11 Operations on lists--------------")
x=["the","cat","sat"]
y=["on","the","mat"]
z=x+y
print(z)
set(x+z)
print(set(x+z))
#w=(z-y)
#print(w)


print()
print("-----------------Task 12 Sort versus sorted on lists--------------")
print("----------------Sorted")
x=[7,11,3,9,2]
y=sorted(x)
print(y)

print("----------------Sort")
x.sort()
print(x)

print("----------------Sorted")
x=["this","that","again","and","if"]
y=sorted(x)
print(y)

print("----------------Sort")
x.sort()
print(x)
print(x.sort())

print()
print("-----------------Task 13 Using reverse with sort and sorted--------------")
print("----------------Sorted")
x=[7,11,3,9,2]
print(sorted(x))
print(x)
print(sorted(x,reverse=True))
print(x)


print()
print("----------------Sort")
x=[7,11,3,9,2]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

print()
print("----------------Sorted")
x=["ab","cs","yw","zs","hd"]
y= sorted(x,reverse=True)
print("now x is: ",x)
print("now y is: ",y)


print()
print("----------------Sort")
x.sort(reverse=True)
y=x.sort(reverse=True)
print("now x is: ",x)
print("now y is: ",y)


print()
print("----------------------------Tuples------------------------------------------")
print("------------Task1 Lists versus tuples with del function--------------")
print("----list--")
a=[0,1,2,3,4,5,6,7,8,9]
#del a[-1]
del a[-4]

print("----tuple--")
b=(0,1,2,3,4,5,6,7,8,9)
#del b[-1] # doesn't work cause tuple doesn't support the del function, or other changes to the tuple changes


print("------------Task2 lists versus tuple with new assigning-----------")
print("----list--")
a=[0,1,2,3,4,5,6,7,8,9]
a[0]=50
print(a)

print("----tuple--")
b=(0,1,2,3,4,5,6,7,8,9)
#b[0]=50 # tuples doesn't support new assignements to their elements, tuples are immutable

print("------------Task3 Lists versus tuple with append-----------")
print("----list--")
a=[0,1,2,3,4,5,6,7,8,9]
a.append("z")
print(a)

print("----tuple--")
b=(0,1,2,3,4,5,6,7,8,9)
#b.append("z") # tuple doesn't support append attribute/methos, is imumtable
print(b)

print("------------Task4 Changing tuples into lists-----------")
b=(0,1,2,3,4,5,6,7,8,9)
list(b) # to change the tuple in a list
y=list(b) #to assign the value to a new variable cause b didn't change, it's still a tuple
print(type(b))
print(type(y))



