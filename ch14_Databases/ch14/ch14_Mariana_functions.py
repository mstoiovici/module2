#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:18:07 2019

@author: maria
"""
import sqlite3
conn=sqlite3.connect("task1.db")
c=conn.cursor()

######## Task1 Insert table and insert data
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT,value REAL)")
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01','python',5)")
    conn.commit()
    c.close()
    conn.close()


######### Task2 Insert data automatically with variables

import time
import datetime
import random
def dynamic_data_entry():
    unix=time.time()
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)
    c.execute("INSERT INTO stuffToBuild(unix,datestamp,keyword,value) VALUES(?,?,?,?)", (unix,date,keyword,value))
    conn.commit()



######### Task3 Read and select data from a database
def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value=8')
    for row in c.fetchall():
        print(row)

def read_from_db2():
    c.execute('SELECT*FROM stuffToBuild WHERE value=8 and unix>1534855733 and unix<1547033137')
    for row in c.fetchall():
        print(row[0])
