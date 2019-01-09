#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("----Chapter 12, The For Loop-----------")
print()
print("---------------Task1 - Loop through a list-----------------------------------")
print("--exp1--")
my_shopping_cart=["cake","plates","plastic forks","juice","cups"]
print(my_shopping_cart)
for item in my_shopping_cart:
    print(item)
  
print()
print("--exp2--")
values=[875,23,451]
print(values)
for val in values:
    print("--> "+str(val))

print()    
print("------Task2 - Update list value------")   
print("-----exp1-------")
values=[875,23,451] 
for val in values:
    print("--> "+str(val))    # for every items do first step, then second step, then go to next item,
    print("--> "+str(val+50))

print()
print("-----exp2-------")  
values=[875,23,451] 
for val in values:
    print("--> "+str(val**2))

print()
print("--------Task3 - Create a list and use a for loop to print each item-----------")
names=["mari","cata","ana","andreea"] #list
for name in names:
    print("***",name)   

print()
print("--Task4 Loop through a string data type--")  

for char in "Yes":
    print(char)
    
for char in "I love codey codey!":
    print(char)
    

for char in "I love codey codey!".split("o"):
    print(char)   

for char in "I love codey codey!".split("-"): #this doesn't do anything
    print(char)   
    



print()
print("--------Task5 - Loop through a tuple data type----------")
names=("mari","cata","ana","andreea") #tuple
for name in names:
    print("***",name)

print()    
print("-------------Task6- loop through a dictionary data type---------------")    
print("--exp1-loop through the key-value pair")
metals={"gold":(19.3,272.1,4),"iron":(7.8,165.9,78),"zinc":(7.13,87.2,35.4),"lead":(11.4,485,27.8)}
print(metals)
metals_list=sorted(metals.items(),key=lambda kv:kv)
print(metals_list)
for metals in metals_list:
    print (metals)
    
    
print() 
print("--exp2 -loop through the keys and only print the keys")
metals={"gold":(19.3,272.1,4),"iron":(7.8,165.9,78),"zinc":(7.13,87.2,35.4),"lead":(11.4,485,27.8)}
print(metals)
key_list=list(metals.keys())
print(key_list)
key_list.sort(key=lambda k:metals[k])
print(key_list)
for key in key_list:
    print(key)


print() 
print("--exp3-loop through the values and only print the values")
metals={"gold":(19.3,272.1,4),"iron":(7.8,165.9,78),"zinc":(7.13,87.2,35.4),"lead":(11.4,485,27.8)}
print(metals)
key_list=list(metals.keys())
print(key_list)
key_list.sort(key=lambda k:metals[k])
print(key_list)
for metals_key in key_list:
    print(metals[metals_key])

print()
print("------------------------------to do- and use the reverse as well----------------------------")
print("loop through the key value pair after sorting the dict by the key ")
print("loop through the key value pair after sorting the dict by the value")



print()
print("----------Task7 from curriculum- loop through a dictionary----------------")
print("-------exp1-----------")
densities = {"iron":7.8, "gold":19.3, "zinc":7.13, "lead":11.4}
metals = list(densities.keys())
print( metals)
metals.sort(reverse=True,key=lambda m:densities[m])
print(metals)
for metal in metals:
    print("{0:>8}={1:5.1f}".format(metal,densities[metal]))

print()    
print("-----------------------to do  {0:>8}={1:5.1f}.format(metal,densities[metal]) -------")
    
print()
print("-------exp2-----------")
densities = {"iron":(7.8,5,1000), "gold":(19.3,20,2), "zinc":(7.13,10,50), "lead":(11.4,3,25)}
metals = list(densities.keys())
print( metals)
metals.sort(reverse=True,key=lambda k:densities[k])
print(metals)
for metal in metals:
    print("{0:>8}={1:5.1f}".format(metal,densities[metal][0]))
    



print()
print("----------Task8 Combine  loop and conditionals to filter out values---------------")
print("----------exp1-----------")
names=("mari","cata","ana","andreea") #tuple
for name in names:
    if len(name)>=4:
        print(name)
    
print()
print("----------exp2-----------")
densities = {"iron":(7.8,5,1000), "gold":(19.3,20,2), "zinc":(7.13,10,50), "lead":(11.4,3,25)}
print(densities)
metals = list(densities.keys())
print( metals)
metals.sort(reverse=True,key=lambda m:densities[m])
print(metals)
keyValue=sorted(densities.items(),key=lambda kv:kv[1][1],reverse=True)
for metal in metals:
    if densities[metal][0]>10:
        print(metal,densities[metal][0])
    else:
        print("The item doesn't meet the condition!")

print()
print("----------Task9 Design a sum function-----------")
"""
How about using ‘for’ loops to compute the sum of values in a list of numbers? Try
the code below in a file. Can you convert it into a SumValues function with a
returned sum value?
"""
print()
print("--step1--")
values = [3, 12, 9]
total = 0
for val in values:
    print("before adding: ",val,"total is: ", total)
    total += val
    print("after adding: ",val,"total is: ", total)
    print("TOTAL:"+ str(total)) 

print()    
print("--step2 VERSION 1--")
def get_sum(values,total=0):
    for val in values:
        total += val
    print("TOTAL:"+ str(total)) 
    return total

values = [3, 12, 9]
get_sum(values)

print()
print("--step2 VERSION 2--")
def get_sum(values=[],total=0):
    for val in values:
        total += val
    print("TOTAL:"+ str(total)) 
    return total

get_sum([3,12,9])




print()
print("------------------------task 10 and 11 Loop with index and range-------------------------------------")
print("--reminding len and range--")
values=[3,12,9]
print(len(values))
print(len("lalalal"))
print(len("lalalal    ")) # white space is being counted as well!!!!!!!
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,2)))


print()
print("---exp1---")
values=[3,12,9]
for i in range(len(values)):
    values[i]=values[i]*2
print(values)

print()
print("-----exp2--- where i is the index of the item in the list----")
values=[3,12,9]
for index in range(len(values)):
    values[index]=values[index]*2
print(values)

print()
print("-----exp3-------")
values=[3,12,9]
for i in range(len(values)):
    print("i is: ",i)
    values[i]=values[i]*2
    print("the new value for ",i," position is now ",values[i])
print(values)

print()
print("---- ex4 ---")
for i in range(3,10,2):
    print(i)
    
print()    
print("---- ex 5 ---")
values=[3,12,9,5,6]
for index in range(1,len(values),2):
    print("we are at index",index)
    print("the value for index",index,"is",values[index])
    values[index]=values[index]**2
    print("the updated value for index",index,"is now",values[index])
    print("we skip one position because we have a step of 2 in range")
print(values)

print()
print("---- ex 6 ---")
values=["milly","sarika","fabi","amina","joke","chen","loren"]
for index in range(0,len(values),3):
    print("we are at index",index)
    print("the value for index",index,"is",values[index])
    print(values[index])
    print("we skip two positions because we have a step of 3 in range")
print(values)

print()
print("---------------Task 12 -Using a break in a for loop---")
print("----ex1---")
values=["milly","sarika","fabi","amina","joke","chen","loren"]
for index in range(0,len(values),2):
    if values[index]=="fabi":
        print("find her",values[index])
        break
    print("we are at index",index)
    print("the value for index",index,"is",values[index])
    print(values[index])
    print("we skip two positions because we have a step of 3 in range")
print(values)

print()
print("----ex 2 ---")
values=["milly","sarika","fabi","amina","joke","chen","loren"]
for index in range(0,len(values),2):
    print("we are at index",index)
    print("the value for index",index,"is",values[index])
    if values[index]=="fabi":
        print("because the value is",values[index],"then the if condition is true,so we get out of the loop and stop")
        break
    print(values[index])
    print("we skip one position because we have a step of 2 in range")
print(values)

print()
print("---- ex 3 ---")
nums=[1,5,30,200,101,100,22]
for item in nums:
    if item>100:
        print("break:",item)
        break


print()
print("---- ex 3.1 ---")
nums=[1,5,30,200,101,100,22]
for index in range(len(nums)):
    print("we are at",index,"position which has the value:",nums[index])
    print("if the value of our item is >100 break the loop")
    if nums[index]>100:
        print("so ",index,"position has a value >100, which is",nums[index],"so we break the loop") 
        break

print()    
print("----how to loop trough a dictionary printing key value pair---")
masGiftDict={"jumper":5,"candy":2,"socks":3,"product":7}
for k,v in masGiftDict.items():
    print(k,v)

print()
print("----how to loop trough a dictionary printing every item from the dictionary as a tuple---")   
masGiftDict={"jumper":5,"candy":2,"socks":3,"product":7}    
for item in masGiftDict.items():
    print(item)

print()
print("----counter---")
colors=["red","green","red","green","blue","green","green"]
d={}
for item in colors:
    if item not in d:
        d[item]=1
        print(d,"first time")
    else:
        d[item]+=1
        print(d)

print()
print("---------------Task 13 -Creating nested loops in a for loop---")
print("----exp1 is not ok, cause we override the value from every key value pair, and it's not the result we want in dict---")
outer_vals_list=[1,2,3]
inner_vals_list=["A","B","C"]
dict={}
for outer_val in outer_vals_list:
    
    for inner_val in inner_vals_list:
        print(outer_val,inner_val)
        dict[outer_val]=inner_val
        print(dict)
        dict[outer_val]+=inner_val
        print(dict)

print()
print("----exp2 is not ok, cause we get dict={1:A,2:B,3:C}---")
outer_vals_list=[1,2,3]
inner_vals_list=["A","B","C"]
dict={}
for outer_val in outer_vals_list:
    index=0
    for inner_val in inner_vals_list:
        print(outer_val,inner_val)
        dict[outer_vals_list[index]]=inner_vals_list[index]
        print(dict)
        index+=1

print()
print("----exp3  how do you get dict={1:[A,B,C],2:[A,B,C],3:[A,B,C]}---")
outer_vals_list=[1,2,3]
inner_vals_list=["A","B","C"]
dict={}
for outer_val in outer_vals_list:
    index=0
    for inner_val in inner_vals_list:
        print(outer_val,inner_val)
        dict[outer_vals_list[index]]=inner_vals_list[index]
        print(dict)
        index+=1
        



print()
print("----bla bla---")# this seems to do the same thing as what I got with nested loops

from collections import defaultdict
d=defaultdict(list)

outer_vals_list=[1,2,3]
inner_vals_list=["A","B","C"]

for outer_val,inner_val in zip (outer_vals_list,inner_vals_list): 
    d[outer_val].append(inner_val)
print(d)


print()
print("----Task 14 Multiplication table with a for loop---")   
for i in range(1,11):
    for j in range(1,11):
        print("{0:>3})".format(i*j),end="")
    print("\n")











