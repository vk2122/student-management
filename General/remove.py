from tkinter import *
#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
import time
import datetime
def remove():
    root=Tk()
    root.geometry("500x400")
    root.title("Delete")

    localtime=time.asctime(time.localtime(time.time()))
    lblInfo=Label(root,font=('tohoma',30,'bold'),text="Delete Student Details ",fg="Black",bd=10,anchor='w')
    lblInfo.pack()

    lblInfo=Label(root,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
    lblInfo.pack()

    def dele():
        f=mydb.cursor()
        rn=r.get()
        query="DELETE FROM STUDENT WHERE ROLLNO={}".format(rn)
        f.execute(query)
        mydb.commit()

    label_r=Label(root,text='Enter Roll No of Student: ',font=('Arial',12,'bold'),bg='white')
    label_r.place(x=0,y=150)

    r=IntVar()
    input_r=Entry(root,width=5,bd=8,textvariable=r)
    input_r.place(x=220,y=150)

    btn=Button(root,text='Delete',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=dele)
    btn.place(x=100,y=250)
    root.mainloop()
