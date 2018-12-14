# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:50:09 2018

@author: maria
"""
print("----Chapter 10, Dictionaries-----------")
# dictionaries syntax: {key1:value1,key2:value2,key3:value3}
print("----Empty dictionaries-----------")
salary={}
print(salary)
print()
print("----Adding a new value to a key-----------")
salary["al"]=20000
print(salary)
salary["name"]="Mari Stoiovici"
print(salary)
salary["date of employment"]="12.03.2018"
print(salary)
salary["date of birth"]="15.06.1985"
print(salary)
print()
print("----Getting dictionariy values through a key-----------")
print(salary["al"])
print()
print("----Doing operations with those values----------")
salary["al"]+=2000
print(salary)
print(salary["al"])
print()
print("----you can create dictionaries with keys &values included-----")
tel={"alf":111,"bobby":222,"calvin":333}
print(tel)
print()
print("----team work-----")
print("--create a dictionary with key:your colleagues names and value: last three digits of their phoneNr---")
team={"Mari":885,"Seraphine":385,"Millie":862}
print(team)
print()
print("----add another collegue-----")
team["Chen"]=111
print(team)
print()
print("----update the values with one more digit-----")
team["Mari"]=1885
team["Seraphine"]=1385
team["Millie"]=1862
team["Chen"]=2111
print(team)
print(team)
print()
print("----deleting dictionary items-----")
del team["Chen"]
print(team)
print()
print("----get all keys from a dictionary-----")
print(team.keys())
print(type(team.keys()))
list1=list(team.keys())
print(list1)
print(list1[0])
print(type(list1))
print()
print("----get all values from a dictionary-----")
print(team.values())
print(type(team.values()))
print()
print("----avoid look-ups key errors-----")
print(team)
if "chen" in team:
    print("chen",":",team["chen"])
else:
    print("chen","not found!")
if "Mari" in team:
    print("Mari",":",team["Mari"])
else:
    print("Mari","not found!")
print()
print("----usong variables to avoid look-ups key errors-----")    
k="Seraphine"
if k in team:
    print(k,":",team[k])
else:
    print(k,"not found!")
print()
print("----using lambda function to sort a dictionary-----")
print()
print("----simple example-----")
counts={"a":3,"c":1,"b":5}
print(counts)
labels=list(counts.keys())
print(labels)
labels.sort(key=lambda k:counts[k])
print(labels)
print()
print("----now with multiple values for a key using sort-----")
team={"Mari":(885,12),"Seraphine":(385,3),"Millie":(862,9)}
print(team)
key_list=list(team.keys())
print(key_list)
key_list.sort(key=lambda k:team[k][1])
print(key_list)
print()
print("----now with multiple values for a key using sorted-----")
team={"Mari":(885,12),"Seraphine":(385,3),"Millie":(862,9)}
print(team)
key_list=list(team.keys())
print(key_list)
print(sorted(key_list,key=lambda k:team[k][1]))
# this next line comes with the same result as when you make a list(key_list) of the keys previously but Chen says it's not correct ?! 
#print(sorted(team,key=lambda k:team[k][1]))

print()
print("--now with multiple values for a key using sort to sort ")
team={"Mari":(885,"january",12),"Seraphine":(385,"october",3),"Millie":(862,"november",9)}
print(team)
# this comes with the same result as when you make a list of the keys previously but Chen says it's not correct ?! 
#print(sorted(team,key=lambda k:team[k][1]))

key_list=list(team.keys())
print(key_list)
key_list.sort(key=lambda k:team[k][1][-1])
print()
print("-- using sorted to sort the dictionary-")

team={"Mari":("Barbu",885,"january",12),"Seraphine":("Ana",385,"october",3),"Millie":("Costel",862,"november",9)}
print(team)
print()
print("-- using sorted to sort the dictionary-- 2 ways, the same result")
print(sorted(team,key=lambda k:team[k]))
print(sorted(team,key=lambda k:team[k][0]))
print()
print("-- using sorted to sort the dictionary-- 2 ways, the same result")
print(sorted(team.items(),key=lambda kv:kv))
print(sorted(team.items(),key=lambda kv:kv[0]))
print()
print("-- using sorted to sort the dictionary-- 2 ways, the same result")
print(sorted(team.items(),key=lambda kv:kv[1]))
print(sorted(team.items(),key=lambda kv:kv[1][0]))
print()
print("-- ------------------------inclass miniproject with reverse sorting-------------")

print("-- sorting with sort(sort changes the list)----------------")
metals={"gold":(19.3,272.1,4),"iron":(7.8,165.9,78),"zinc":(7.13,87.2,35.4),"lead":(11.4,485,27.8)}
print(metals)
list_metals=list(metals.keys())
print(list_metals)
list_metals.sort(reverse=True,key=lambda k:metals[k])
print(list_metals)
#and again the same result by targetting specific the first element of the value of the pair
list_metals.sort(reverse=True,key=lambda k:metals[k][0])
print(list_metals)
print()


print("-- sorting with sorted(doesn't make changes)----------------")
metals={"gold":(19.3,272.1,4),"iron":(7.8,165.9,78),"zinc":(7.13,87.2,35.4),"lead":(11.4,485,27.8)}
print(metals)
print(sorted(metals, key=lambda k:metals[k],reverse=True))
#and again the same result by targetting specific the first element of the value of the pair
print(sorted(metals, key=lambda k:metals[k][0],reverse=True))
print()
print("-----and now printing the key value pairs--------")
print()
print(sorted(metals.items(), key=lambda kv:kv,reverse=True))
print(sorted(metals.items(), key=lambda kv:kv[0],reverse=True))
print()
print(sorted(metals.items(), key=lambda kv:kv[1],reverse=True))
print(sorted(metals.items(), key=lambda kv:kv[1][0],reverse=True))
print()
print(sorted(metals.items(), key=lambda kv:kv[1][1],reverse=True))


    