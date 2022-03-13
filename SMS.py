from tkinter import *
from tkinter import ttk
#from General.general import general as gen
#from academic.academic import academic as acd
import time
import datetime

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


m=IntVar()
def con():
    a=m.get()
    if a==1:
          root.destroy()
          gen()
    elif a==2:
          root.destroy()
          acd()
    else:
          i=messagebox.askquestion("Exit","Would you like to exit ?")
          if i=="yes":
              root.destroy()
r_g=Radiobutton(root,font=('arial',12,'bold'),text="To view general details.",variable=m,value=1)
r_a=Radiobutton(root,font=('arial',12,'bold'),text="To view academic details.",variable=m,value=2)
r_e=Radiobutton(root,font=('arial',12,'bold'),text="Exit.",variable=m,value=3)
btn=Button(root,text='Continue',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=con)
r_g.place(x=1,y=90)
r_a.place(x=1,y=130)
r_e.place(x=1,y=160)
btn.place(x=100,y=190)
root.mainloop()
