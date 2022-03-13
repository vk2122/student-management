#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
def per():
        j=mydb.cursor()
        r=int(input("Enter rollno of student whose record to be searched:"))
        query="SELECT * FROM RECORDS WHERE ROLLNO={}".format(r)
        j.execute(query)
        b=j.fetchall()
        for i in b:
                print("Roll No:",i[0])
                print("Name:",i[1])
                print("Stream:",i[2])
                print("SUB1:",i[3])
                print("SUB2:",i[4])
                print("SUB3:",i[5])
                print("SUB4:",i[6])
                print("SUB5:",i[7])
                print("TOTAL:",i[8])
                print("AGGREGATE:",i[9])
                print("DIVISION:",i[10])
    
