#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""
import sqlite3
conn=sqlite3.connect("phoneBookProject.db")
c=conn.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS businesses(business_type TEXT , business_name TEXT, adress TEXT,city TEXT, postcode TEXT, telephoneNo TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS people(surname TEXT , name TEXT, adress TEXT,city TEXT, postcode TEXT, telephoneNo TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS postcodes(postcode TEXT , latitude TEXT, longitude TEXT)")
def data_entry():
    c.execute("INSERT INTO businesses VALUES('restaurant','Jamie' ,'15 Tarves Way','London','SE109JP','07569655766')")
    conn.commit()
    c.close()
    conn.close()


#create_table()
data_entry()