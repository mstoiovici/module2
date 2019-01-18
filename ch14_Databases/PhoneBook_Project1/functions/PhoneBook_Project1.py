#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""
import sqlite3
conn=sqlite3.connect("phoneBookProject1.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS businesses(business_category TEXT , business_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS people(first_name TEXT , last_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS location(postcode TEXT , latitude TEXT, longitude TEXT)")


def people_data_entry():
    for item in people_data:
        #print("first item: ",item)
        #print(type(item))
        #print("-------------------------------")
        #key_list=list(item.keys())
        values_list=list(item.values())
        #print(key_list)
        #print(values_list)
        c.execute("INSERT INTO people(first_name,last_name,adress_line_1,adress_line_2,adress_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()
        c.close()
        conn.close()
    

def business_data_entry():   
    for item in business_data:
        values_list=list(item.values())
        print(values_list)
        c.execute("INSERT INTO businesses(business_name, adress_line_1,adress_line_2, adress_line_3,postcode, country,telephone_number,business_category) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()
        c.close()
        conn.close()

     
def location_data_entry():
    for item in postcodes_items:
        values_list=list(item.values())
        c.execute("INSERT INTO postcodes(latitude,longitude) VALUES(?,?)", (values_list))
        conn.commit()
        c.close()
        conn.close()

import json
def store_data_in_variables():
    global business_data
    global people_data
    with open('../json/business.js') as business:
        business_data=json.load(business)
    with open('../json/people.js') as people:
        people_data=json.load(people)
    #print("business_data: ",business_data)
    #print("people_data: ",people_data)
    return business_data,people_data




