# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:39:02 2020

@author: danie
"""


from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont
from tkinter import messagebox
#from show import *
import cx_Oracle

R = open('Populate.txt','r')
Insert = R.read().split(";")

f = open('DropTable.txt','r')
Drop = f.read().split(",")

#Reads the created table sql queries from a txt file
Y = open('CreateTable.txt','r')
Create = Y.read().split(";")


#Creating connection to database 
dsn_tns = cx_Oracle.makedsn('oracle.scs.ryerson.ca',1521, "orcl")
conn = cx_Oracle.connect(user="Enter Username", password="Enter PSD",dsn=dsn_tns)
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



def CreateTables():
    '''
    Creates the tables for database
    If tables already exist then an error will display

    Returns
    -------
    None.

    '''
    #try:
    for i in Create:
        c.execute(i)
    messagebox.showinfo("Created","Tables Have been Created")
    #except:
     #   messagebox.showerror("Dropped","Failed to create table")





def show(clicked):
    '''
    Parameters
    ----------
    clicked : string

    Returns
    -------
    None.

    Displays the selected query
    Go to readme to see what the query's display : ) '
    '''
    # Creating the window for the display
    window2 = Tk()
    window2.geometry("400x200")
    print(clicked)
    global i
    i = 0;
    
    if(clicked == "Members in gym 1"):
        statement = "select * from Members_Gym where gym_address = 'AD1'"
        c.execute(statement)
        for row in c:
            i = i + 2
            label = Label(window2, text = (str(row[0]) + '-' + str(row[1])), font=("Helvetica", 11))
            label.grid(row=i, column=0)
            print()
    
    elif(clicked == "Members in gym 2"):
        statement = "select * from Members_Gym where gym_address = 'AD2'"
        c.execute(statement)
        for row in c:
            i = i + 2
            label = Label(window2, text = (str(row[0]) + '-' + str(row[1])), font=("Helvetica", 11))
            label.grid(row=i, column=0)
            print()
    
    elif(clicked == "Member Contact Info"):
        statement = "select m.membership_id, c.F_name, c.Mem_address, c.age, c.height from members m right join Contact_Info c on m.membership_id = c.membership_id"
        c.execute(statement)
        for row in c:
            i = i + 2
            label = Label(window2, text = (str(row[0]) + '-' + str(row[1])  + '-' + str(row[2]) + '-' + str(row[3])+ '-' + str(row[2])),font=("Helvetica", 11))
            label.grid(row=i, column=0)
            print()
    
    elif(clicked == "GYM Hours"):
        statement = "select O_hours from GYM"
        c.execute(statement)
        for row in c:
            i = i + 2
            label = Label(window2, text = (str(row[0])), font=("Helvetica", 11))
            label.grid(row=i, column=0)
            print()
    elif(clicked == "Id > 42"):
        statement = "select c.l_name, c.mem_address, m.membership_id, m.gym_address from contact_info c right join Members_Gym m on c.membership_id = m.membership_id where m.membership_id > 42" 
        c.execute(statement)
        for row in c:
            i = i + 2
            label = Label(window2, text = (str(row[0]) + '-' + str(row[1])+ '-' + str(row[2]) + '-' + str(row[3])),font=("Helvetica", 11))
            label.grid(row=i, column=0)
            print()
    
    #Place the return button on the screen
    button = Button(window2, text="Go Back",command= window2.destroy)
    button.grid(row=i+1, column=0)
    mainloop()



class option:
    def __init__(self,window):
        '''
        Parameters
        ----------
        window : Tkinter window

        Returns
        -------
        None.

        '''
        self.window = window
        self.window.geometry("670x446")
        #x = 46
        
        #Options for the drop down menu
        options = [
        	"Members in gym 1",
        	"Members in gym 2",
        	"Id > 42",
        	"GYM Hours",
        	"Member Contact Info"
        ]
        clicked = StringVar()
        clicked.set(options[0])
        head = Label(self.window,text = 'Select Query')
        head.grid(row = 0, column =0, columnspan =4)
        
        #Creating and placing the drop down widget
        self.drop = OptionMenu(self.window, clicked, *options)
        self.drop.grid(row=1,column=0,padx = 50, columnspan = 4)
        self.myButton = Button(self.window, text="   Show Selection   ", command=lambda:show(str(clicked.get())))
        self.myButton.grid(row=2,column=0,columnspan = 4)
        
        # Label widget for creating a new window
        Header2 = Label(self.window, text="Complete the following to add a new member: ")
        Header2.grid(row=3, column=0,columnspan=4)
        
        payinfo = Label(self.window, text="Payment Info:").place(relx = 0.1, rely = 0.44)
        ContactInfo = Label(self.window, text="Contact Info:").place(relx = 0.1, rely = 0.6)
        
        M_Level = Label(self.window, text="Member Level (G/S/B) : ").place(relx=0.01, rely = 0.24, anchor='w')
        Trainer_Lab = Label(self.window, text="Trainer (Y/N): ").place(relx=0.01, rely = 0.29, anchor='w')
        Class_Label = Label(self.window, text="Class (Y/N): ").place(relx=0.01, rely = 0.34, anchor='w')
        GAdress = Label(self.window, text="Gym Adress (1/2): ").place(relx=0.01, rely = 0.39, anchor='w')
        
        #Dialog boxes
        self.MemberLevel = Entry(self.window, width=30, borderwidth=2)
        self.MemberLevel.place(relx = 0.2, rely=0.22)
        self.Trainer = Entry(self.window, width=30, borderwidth=2)
        self.Trainer.place(relx = 0.2, rely=0.27)
        self.Class = Entry(self.window, width=30, borderwidth=2)
        self.Class.place(relx = 0.2, rely=0.32)
        self.GymAdress = Entry(self.window, width=30, borderwidth=2)
        self.GymAdress.place(relx = 0.2, rely=0.37)
        
        PayMethod_L = Label(self.window, text="Payment Method : ").place(relx=0.01, rely = 0.52, anchor='w')
        AccountNum_L = Label(self.window, text="Account Number : ").place(relx=0.01, rely = 0.57, anchor='w')
        
        #=========== label widget for paymethod ===========#
        self.PayMethod = Entry(self.window, width=30, borderwidth=2)
        self.PayMethod.place(relx = 0.2, rely=0.5)
        self.AccountNum = Entry(self.window, width=30, borderwidth=2)
        self.AccountNum.place(relx = 0.2, rely=0.55)
        
        
        #=========== Label Widgets for payment and contact info ===========#
        F_Name_L = Label(self.window, text="First Name: ").place(relx=0.01, rely = 0.68, anchor='w')
        L_Name_L = Label(self.window, text="Last Name : ").place(relx=0.01, rely = 0.73, anchor='w')
        Adress_L = Label(self.window, text="Home Address: ").place(relx=0.01, rely = 0.78, anchor='w')
        Height_L = Label(self.window, text="Height : ").place(relx=0.01, rely = 0.83, anchor='w')
        Age_L = Label(window, text="Age : ").place(relx=0.01, rely = 0.88, anchor='w')
        
        #=========== The entry boxes for payment and contact info ===========#
        self.F_Name = Entry(self.window, width=30, borderwidth=2)
        self.F_Name.place(relx = 0.2, rely=0.66)
        self.L_Name = Entry(self.window, width=30, borderwidth=2)
        self.L_Name.place(relx = 0.2, rely=0.71)
        self.Adress = Entry(self.window, width=30, borderwidth=2)
        self.Adress.place(relx = 0.2, rely=0.76)
        self.Height = Entry(self.window, width=30, borderwidth=2)
        self.Height.place(relx = 0.2, rely=0.81)
        self.Age = Entry(self.window, width=30, borderwidth=2)
        self.Age.place(relx = 0.2, rely=0.86)
        
        self.myButton = Button(window, text="   Submit   ", command=self.submit).place(relx=0.9, rely=0.9, anchor='e')
        
        #   For deleting a Member Based on membership id     #
        self.DeleteMember = Entry(self.window, width=30, borderwidth=2)
        self.DeleteMember.place(relx = 0.96, rely=0.25, anchor='e')
        M_Level = Label(self.window, text="Enter Membership ID to delete: ").place(relx=0.69, rely = 0.18)
        
        self.deletebutton = Button(window, text="   Delete   ", command=self.deletemember).place(relx=0.9, rely=0.70, anchor='e')
        
        
        
    def submit(self):
        if(self.MemberLevel.get() == 'G'):
            price = 121.50
        elif(self.MemberLevel.get() == 'S'):
            price = 65.0
        elif(self.MemberLevel.get() == 'B'):
            price = 60.5
         
        mem_id = 0
        c.execute("select * from Members")
        for row in c:
            mem_id = int(row[0])        
        mem_id = mem_id + 1

        try:
            Members = ("insert into Members values(" + str(mem_id) + "," + "'" + str(self.MemberLevel.get())+"'"+ "," + "'" + str(self.Trainer.get())+"'" 
                + "," + "'" +str(self.Class.get())+"'" + "," + str(price) + ")")
            c.execute(Members)

            Members_gym = ("insert into Members_Gym values(" + str(mem_id) + "," + "'AD" + str(self.GymAdress.get()) +"'" + ")")
            c.execute(Members_gym)
 
            Payment_Info = ("insert into Payment_Info values(" + str(mem_id) + ","  + str(price) +"," + str(self.AccountNum.get()) + ")")
            c.execute(Payment_Info)

            Payment_Method = ("insert into Payment_Method values(" + str(self.AccountNum.get()) + "," + "'" + str(self.PayMethod.get()) + "'" +")")
            c.execute(Payment_Method)
            
            Contact_info = ("insert into Contact_info values('" + str(self.L_Name.get()) + "'" + "," + "'" + str(self.F_Name.get())+"'"+ "," + "'" + str(self.Adress.get())+"'"
                            + "," +str(self.Age.get()) + "," +str(self.Height.get()) + "," + str(mem_id) + ")")
            c.execute(Contact_info)
        except:
            self.DeleteMember.insert(0,mem_id)
            messagebox.showerror("Dropped","Failed to insert user")
            self.deletemember()
            
        c.execute("select * from Contact_info")
        for row in c:
            print(str(row[0]) + '-' + str(row[1]))
    
    def deletemember(self):
        '''
        Returns
        -------
        None.
        Deletes a users based on the membership_id
        '''
        try:
            statement = "DELETE FROM Members WHERE membership_id = " + str(self.DeleteMember.get())
            c.execute(statement)
            
            delete_gymad = "DELETE FROM Members_Gym WHERE membership_id = " + str(self.DeleteMember.get())
            c.execute(delete_gymad)
            c.execute("select * from Members")
            messagebox.showinfo("delete","user has been deleted ")
            for row in c:
                print(str(row[0]) + '-' + str(row[1]))
        except:
            essagebox.showerror("Delete","No such user exist")
        
        
        

        

        
        
def Populate():
    #Inserting the information into the tables 
    for i in Insert:
        c.execute(i)
#Header = tkFont.Font(family="times new roman", size=25)
    window = Tk()
    obj = option(window)
    window.mainloop()

