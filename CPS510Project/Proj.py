# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:42:18 2020

@author: danie
"""
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont
from tkinter import messagebox
import cx_Oracle
from populate import *
#from create_del import *


root = Tk()
root.title("Gym Login")
root.geometry("400x200")
Header = tkFont.Font(family="times new roman", size=25)

global f

def open():
    '''
    Widow 2, destroy previous window
    3 options:
        delete table, create table, populate table
        
    populate table will send you to a new window
    '''
    root.destroy()
    root2 = Tk()
    root2.title("Main Page")
    root2.geometry("670x446")
    
    #setting the back ground
    filename = PhotoImage(file = "Images\Gym.png")
    background_label = Label(root2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #Creating and placing labels to the screen
    label = Label(root2, text="Main Menu",font=Header)
    label.place(relx=0.5, rely=0.25, anchor = 'center')
    
    #Creating buttons and defining there functionality
    DropT = Button(root2, text="   Drop Table   ", command = DropTables)
    CreateT = Button(root2, text = "  Create Table  ", command = CreateTables)
    populate = Button(root2, text = "  Populate Data  ", command = Populate)
    
    #Placing button on the screen
    DropT.place(relx=0.0, rely=0.5, anchor = 'w')
    CreateT.place(relx=0.5, rely=0.5, anchor = 'center')
    populate.place(relx=1.0, rely=0.5, anchor = 'e')

    mainloop()
    #This closes the window


def confirm():
    """
    Verifies the users Id and Pasword
    """
    if(PsdEntry.get() == "Psd" and UserEntry.get() == "User"):
        open()
    else:
        messagebox.showerror("Error","Invalid Username")


def button_hover(e):
	Submit["bg"] = "white"

def button_hover_leave(e):    
	Submit["bg"] = "SystemButtonFace"


#Setting the back ground on screen 1
filename = PhotoImage(file = "Images\Dumbell.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Test Labels on screen 1
label = Label(root, text="Login Page", font=Header)
User = Label(root, text="Username  : ")
Psd = Label(root, text="Password   : ")

#Dialog boxes 
UserEntry = Entry(root, width=30, text = 'User', borderwidth=2)
PsdEntry = Entry(root, width=30, borderwidth=2)

#Placing labels on screen
label.grid(row=0, column=0, columnspan=3, padx=50, pady=10)
User.grid(row=1, column=0)
Psd.grid(row=2, column=0)

#Placing dialog boxes on screen
UserEntry.grid(row=1, column=1,columnspan = 2)
PsdEntry.grid(row=2, column=1, columnspan = 2)

# placing the button on the screen
Submit = Button(root, text="LOGIN", font=("Helvetica", 10), command=confirm)
Submit.grid(row=3,column=0)
Submit.bind("<Enter>", button_hover)
Submit.bind("<Leave>", button_hover_leave)

mainloop()
#c.close()
