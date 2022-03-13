from tkinter import *
#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
import time
import datetime
def mod():
    root=Tk()
    root.geometry("500x400")
    root.title("Update")

    localtime=time.asctime(time.localtime(time.time()))
    lblInfo=Label(root,font=('tohoma',30,'bold'),text="Update Student Details ",fg="Black",bd=10,anchor='w')
    lblInfo.pack()

    lblInfo=Label(root,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
    lblInfo.pack()

    def mod():
        #d=mydb.cursor()
        k=c.get()
        z=m.get()
        n=r.get()
        #query="UPDATE STUDENT SET {}='{}'WHERE ROLLNO={}".format(k,z,n)
        #d.execute(query)
        #mydb.commit()

    label_c=Label(root,text='Column to be modified:',font=('Arial',12,'bold'))
    label_c.place(x=0,y=150)
    label_m=Label(root,text='What is the modification:',font=('Arial',12,'bold'))
    label_m.place(x=0,y=200)
    label_r=Label(root,text='Enter Roll No of Student:',font=('Arial',12,'bold'))
    label_r.place(x=0,y=250)

    c=StringVar()
    m=StringVar()
    r=IntVar()
    input_c=Entry(root,width=15,bd=8,textvariable=c)
    input_c.place(x=220,y=150)
    input_m=Entry(root,width=15,bd=8,textvariable=m)
    input_m.place(x=220,y=200)
    input_r=Entry(root,width=5,bd=8,textvariable=r)
    input_r.place(x=220,y=250)

    btn=Button(root,text='Update',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=mod)
    btn.place(x=100,y=300)
    root.mainloop()
