from tkinter import *
from tkinter import ttk
#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
def insert():              
     Msheet = Tk()
     Msheet.title("Student Details")
     Msheet.geometry('600x460')
     Msheet.configure(background = "grey")
     heading1 = Label(Msheet, text="Marksheet", bg="grey",font="50")
     rn1=Label(Msheet ,text = "Roll No.:", bg="grey",font="25")
     ename1=Label(Msheet ,text = "Name", bg="grey",font="25")
     stream1=Label(Msheet ,text = "Stream", bg="grey",font="25")
     sub1=Label(Msheet ,text = "Sub1", bg="grey",font="25")
     sub2=Label(Msheet ,text = "Sub2", bg="grey",font="25")
     sub3=Label(Msheet ,text = "Sub3", bg="grey",font="25")
     sub4=Label(Msheet ,text = "Sub4", bg="grey",font="25")
     sub5=Label(Msheet ,text = "Sub5", bg="grey",font="25")
     heading1.pack()
     rn1.place(x=1,y=20)
     ename1.place(x=1,y=60)
     stream1.place(x=1,y=100)
     sub1.place(x=1,y=140)
     sub2.place(x=1,y=180)
     sub3.place(x=1,y=220)
     sub4.place(x=1,y=260)
     sub5.place(x=1,y=300)
     
     #__________________________________________________________________________________
     r1=IntVar()
     n1=StringVar()
     s1=StringVar()
     s_1=IntVar()
     s_2=IntVar()
     s_3=IntVar()
     s_4=IntVar()
     s_5=IntVar()
     #___________
     def rec():
          h=mydb.cursor()
          r_1=r1.get()
          n_1=n1.get()
          st2=s1.get()
          su1=int(s_1.get())
          su2=int(s_2.get())
          su3=int(s_3.get())
          su4=int(s_4.get())
          su5=int(s_5.get())
          tmks=su1+su2+su3+su4+su5
          ag=tmks/5
          div2=""
          if ag >=90:
              div2='A'
          elif ag >=75:
              div2='B'
          elif ag >=60:
              div2='C'
          elif  ag >=40:
              div2='D'
          else:
              div2='F'

          r1.set("")
          n1.set("")
          s1.set("")
          s_1.set("")
          s_2.set("")
          s_3.set("")
          s_4.set("")
          s_5.set("")
          query="INSERT INTO RECORDS values({},'{}','{}',{},{},{},{},{},{},{},'{}')".format(r_1,n_1,st2,su1,su2,su3,su4,su5,tmks,ag,div2)
          h.execute(query)
          mydb.commit()
     def clear():
          r1.set("")
          n1.set("")
          s1.set("")
          s_1.set("")
          s_2.set("")
          s_3.set("")
          s_4.set("")
          s_5.set("")
     #___________________________________________
     R1=Entry(Msheet,width=5,bd=8,textvariable=r1)
     N1=Entry(Msheet,width=20,bd=8,textvariable=n1)
     S1=Entry(Msheet,width=20,bd=8,textvariable=s1)
     S_1=Entry(Msheet,width=20,bd=8,textvariable=s_1)
     S_2=Entry(Msheet,width=20,bd=8,textvariable=s_2)
     S_3=Entry(Msheet,width=20,bd=8,textvariable=s_3)
     S_4=Entry(Msheet,width=20,bd=8,textvariable=s_4)
     S_5=Entry(Msheet,width=20,bd=8,textvariable=s_5)
     R1.place(x=100,y=20)
     N1.place(x=100,y=60)
     S1.place(x=100,y=100)
     S_1.place(x=100,y=140)
     S_2.place(x=100,y=180)
     S_3.place(x=100,y=220)
     S_4.place(x=100,y=260)
     S_5.place(x=100,y=300)
     btn=Button(Msheet,text='Save',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=rec)
     btn.place(x=100,y=380)
     btn1=Button(Msheet,text='clear',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=clear)
     btn1.place(x=300,y=380)          
     Msheet.mainloop()

