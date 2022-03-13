#import mysql.connector as sql
#mydb=sql.connect(host="localhost",user="root",passwd="admin123",database="SMS")
def select():
	g=mydb.cursor()
	query="SELECT * FROM RECORDS"
	g.execute(query)
	for i in g:
                for c in i :
                        print(c,end="\t")
                print()
