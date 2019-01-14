#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""
from  people_items import *
import sqlite3
conn=sqlite3.connect("phoneBookProject.db")
c=conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS businesses(business_category TEXT , business_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS people(first_name TEXT , last_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS postcodes(postcode TEXT , latitude TEXT, longitude TEXT)")


def people_data_entry():
    
   
    for item in people_items:
        #print("first item: ",item)
        #print(type(item))
        #print("-------------------------------")
        #key_list=list(item.keys())
        values_list=list(item.values())
        #print(key_list)
        #print(values_list)
        c.execute("INSERT INTO people(first_name,last_name,adress_line_1,adress_line_2,adress_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()
    

def business_data_entry():   
    for item in business_items:
        values_list=list(item.values())
        c.execute("INSERT INTO businesses(business_name, adress_line_1,adress_line_2, adress_line_3,postcode, country,telephone_number,business_category) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()

def change_postcodes_in_businesses():
    for item in business_items:
        values_list=list(item.values())
        #print(values_list)
        #print(type(values_list))
        postcodes_list=list(values_list[4])
        #print(values_list[4])
        print(postcodes_list)
        #for item in values_list:
            #c.execute(("INSERT INTO businesses(postcode) VALUES(?,?,?,?,?,?,?,?)", (values_list))
     

def postcodes_data_entry():
    for item in postcodes_items:
        values_list=list(item.values())
        c.execute("INSERT INTO postcodes(latitude,longitude) VALUES(?,?)", (values_list))
        conn.commit()


#create_table()
#people_data_entry()
#business_data_entry()
change_postcodes_in_businesses()