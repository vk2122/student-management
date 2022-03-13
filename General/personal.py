#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
def personal():
    #e=mydb.cursor()
    #r=int(input("Enter rollno of student to be searched:"))
    #query="SELECT * FROM STUDENT WHERE ROLLNO={}".format(r)
    #e.execute(query)
    a=e.fetchall()
    for i in a:
        print("Roll No:",i[0])
        print("Name:",i[1])
        print("Class:",i[2])
        print("Father's Name:",i[3])
        print("Mother's Name: ",i[4])
        print("Address:",i[5])
        print("Date Of Birth:",i[6])
        print("Gender:",i[7])
        print("Contact:",i[8])
        print("Email id:",i[9])
        print("Stream:",i[10])    
        
