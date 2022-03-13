from tkinter import *
from tkinter import ttk
import time
import datetime
#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
import General.insert as ins
import General.personal as per
import General.remove as rem
import General.select as sel
import General.update as upd


#______________________General data
def general():
      while True:
            #________________________________________________________________________________
            root=Tk()
            root.geometry("700x500")
            root.title("SMS")
            #================================================================================#
            #                                     TIME                                       #
            #================================================================================#
            localtime=time.asctime(time.localtime(time.time()))
                     
            lblInfo=Label(root,font=('helvetica',14,'bold'),text="Student Management System",fg="Black",bd=10,anchor='w')
            lblInfo.pack()

            lblInfo=Label(root,font=('arial',12,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
            lblInfo.pack()


            n=IntVar()
            def con():
                a=n.get()
                if(n==1):
                  sel.select_general()          
                elif(n==2):
                  ins.insert()   
                elif(n==3):
                  upd.mod()
                elif(n==4):
                    per.personal()
                elif(n==5):
                  rem.remove()
                else:
                  root.destroy()

            r_1=Radiobutton(root,font=('arial',12,'bold'),text="To view Student list",variable=n,value=1)
            r_2=Radiobutton(root,font=('arial',12,'bold'),text="To add a new student detail",variable=n,value=2)
            r_3=Radiobutton(root,font=('arial',12,'bold'),text="To modify student detail",variable=n,value=3)
            r_4=Radiobutton(root,font=('arial',12,'bold'),text="To search student detail",variable=n,value=4)
            r_5=Radiobutton(root,font=('arial',12,'bold'),text="To remove a student detail",variable=n,value=5)
            r_e=Radiobutton(root,font=('arial',12,'bold'),text="Exit.",variable=n,value=6)
            btn=Button(root,text='Continue',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=con)
            r_1.place(x=1,y=90)
            r_2.place(x=1,y=130)
            r_3.place(x=1,y=170)
            r_4.place(x=1,y=210)
            r_5.place(x=1,y=250)
            r_e.place(x=1,y=290)
            btn.place(x=100,y=330)
            root.mainloop()

general()
