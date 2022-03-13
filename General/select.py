#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
def select_general():
     print("""
1:To view basic details
2:To view parental details
                  """)
     k=int(input("What would you to like do:"))
     if(k==1):
          #a=mydb.cursor()
          #query="SELECT ROLLNO,NAME,CLASS,DOB,SEX,STREAM from STUDENT"
          #a.execute(query)
          for i in a:
               for c in i:
                    print(c,end="\t")
               print()     
     elif(k==2):
          #b=mydb.cursor()
          #query="SELECT ROLLNO,NAME,F_NAME,M_NAME,ADDRESS,CONTACT,EMAIL from STUDENT"
          #b.execute(query)
          for i in b:
               for a in i:
                    print(a,end="\t")
               print()
     else:
          print("Enter a valid option.")
