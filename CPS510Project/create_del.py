# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:21:36 2020

@author: danie
"""


import cx_Oracle
from tkinter import *
from tkinter import messagebox

#Reads the drop table statments from the txt file
f = open('DropTable.txt','r')
Drop = f.read().split(",")

#Reads the created table sql queries from a txt file
Y = open('CreateTable.txt','r')
Create = Y.read().split(";")

#Creates connection to oracle 64 server
dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca',1521, "orcl")
conn = cx_Oracle.connect(user="dsadig", password="03134225",dsn=dsn_tns)
global c
c = conn.cursor()

def DropTables():
    '''
    droping the table
    If they are droped or cant be droped and error is shown
    
    Return: Nothing

    '''
    #try:
    for Dstatment in Drop:
        c.execute(Dstatment)
    messagebox.showinfo("Dropped","Tables have been deleted")
    
    conn.close()


def CreateTables():
    '''
    Creates the tables for database
    If tables already exist then an error will display

    Returns
    -------
    None.

    '''
    try:
        for i in Create:
            c.execute(i)
        messagebox.showinfo("Created","Tables Have been Created")
    except:
        messagebox.showerror("Dropped","Failed to create table")
    conn.close()