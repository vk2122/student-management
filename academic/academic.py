#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
import academic.delete as dele
import academic.insert as ins 
import academic.modify as mod
import academic.per as per
import academic.select as sele
def academic():
  while True:
    print("""
1:To view student records
2:To add a new student record
3:To modify student record
4:To search student record
5:To remove a student record
                                                """)
    m=int(input("What would you like to do:"))
    if(m==1):
      sele.select()
    elif(m==2):
      ins.insert()
    elif(m==3):
      mod.mod()
    elif(m==4):
      per.per()
    elif(m==5):
      dele.remove()
    else:
      print("Enter a valid option.")
