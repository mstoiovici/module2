#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:37:30 2019

@author: maria
"""
print("-----------Task1 -Counting words---------------")

def countWords(filename):
    """This function takes as an input a txt file and returns a results as a dictionary
    """
    result={}
    data=open(filename,'r')
        for row in data:
        words=row.split()
        #print(words)
        #print("------------------------------------")
        for word in words:
            #print("This word is: ",word)
            if word in result:
                result[word]+=1
                #print("wordCount is: ",result[word])
            else:
                result[word]=1
                #print("wordCount is: ",result[word])
    #print("Result is now",result)
    return result

 ####filename to camelcase;words to wordList

print("-----------Task2 -Sorting and ranking---------------")

def printTop20(dictionary):
    """This function takes as an input a dictionary in which the keys are words and the values are numbers and prints
     top 20 words from the input
    """

    keys=list(dictionary.keys())
    #print(keys)
    keys.sort(reverse=True,key=lambda value:dictionary[value])
    for index in range(20):
        key=keys[index]
        print(key," = ",dictionary[key])

######## keys to keyList

print("-----------Task3 -Stopwords---------------")

def readStopWords(filename):
    """This function takes a txt file as an input and returns a list of strings
    """
    stops=[]
    result=countWords(filename)
    #print(type(result))
    #print("--------------------------------------------------")
    stops=list(result.keys())
    print(stops)
    return stops


def countWordsNotInStopWords(filename,stopwords):
    """This function takes as an input a txt file and returns a results as a dictionary
    """
    result={}
    data=open(filename,'r')

    for row in data:
        words=row.split()
        #print(words)
        print("------------------------------------")
        for word in words:
            print("This word is: ",word)
            if word not in stopwords:
                print("This word is not in stopwords so it's being counted and added")
                if word in result:
                    result[word]+=1
                else:
                    result[word]=1

            else:
                print("This word is in stopwords")

    print("Result is now",result)
    return result







#countWords('textData/george01.txt')
#printTop20(countWords('textData/mobydick.txt'))
readStopWords('textData/stopwords.txt')
#countWordsNotInStopWords('textData/mobypara.txt',readStopWords('textData/stopwords.txt'))
