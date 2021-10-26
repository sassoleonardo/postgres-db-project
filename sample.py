import os
import psycopg2
from datetime import datetime
import shutil

#conecct

connection = psycopg2.connect(
    database = "northwind",
    user = "northwind_user",
    password = "thewindisblowing",
    host = "localhost",
    port = "5432"
)
print("connected")
cursor = connection.cursor()



#date time variable
date = datetime.now()
current_date = date.strftime("%m-%d-%Y")

#create folder path
def create(table_name,current_date,_csv):
    dir = os.path.join("C:\\","users","leosa","desktop","desafio_py",_csv,table_name,current_date)
    os.makedirs(dir)

#creatte csv path
def create_csv():
    _csv = "csv"
    table_name = ""
    create(table_name,current_date,_csv)
  

create_csv()
#copy csv to created path
src = r"C:\Users\leosa\desktop\desafio_py\code-challenge\data\order_details.csv"
dest = r"C:\Users\leosa\desktop\desafio_py/csv/"+current_date+"/file.csv"
shutil.copy(src, dest)


#select db tables
cursor.execute("""SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'public'""")

#for each db table is created a different path with de files saved 
for table in cursor.fetchall():
    _csv = "postgres"
    table_name = ''.join(table)
    create(table_name,current_date,_csv)
    print(table_name)
    sql = "COPY "+ table_name +" TO STDOUT WITH CSV DELIMITER ';' "
    with open(r"C:\Users\leosa\Desktop\desafio_py/"+_csv+"/"+table_name+"/"+current_date+"/"+table_name+".txt", "w") as file:
        cursor.copy_expert(sql, file) 


        
