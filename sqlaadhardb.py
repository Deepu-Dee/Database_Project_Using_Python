
# import module
import sqlite3

# connecting sqllite
conn = sqlite3.connect('aadhar.db')

# creating cursor object by using 'cursor()' method
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS AADHAR_DATA")

# creating table

table='''CREATE TABLE AADHAR_DATA
               (AADHAAR_NO INT PRIMARY KEY NOT NULL,
               NAME VARCHAR(255) NOT NULL,
               AGE INT NOT NULL,
               FATHER_NAME CHAR NOT NULL,
               GENDER TEXT NOT NULL, 
               CITY TEXT NOT NULL,
               MOBILE_NO INT NOT NULL)'''
cursor.execute(table)

# queries to insert table
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('252365892645','Deepu','27','Venkatesh','Female','Tumkur','9606643321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('586945632874','Roopa','25','Venkatesh','Female','Tumkur','9980369438')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('762365892285','Surya','25','Ravi','Male','Davanagere','6363859263')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('902365892645','Venu','26','Kumar','Male','Banglore','9608943321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('752365856645','Ravi','30','Basappa','Male','Mysore','8606643321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('802365892645','Guru','35','Ramayya','Male','Banglore','9606643521')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('952965892645','Darshan','40','Devaraj','Male','Kunigal','9906643321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('222320892645','Sudeep','45','Bharath','Male','Chitradurga','9666643321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('661265892645','Kumar','60','Jayaram','Male','Hiriyur','9906343321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('752365892645','Mahesh','55','Vinay','Male','Nelamangala','9606653321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('692365842645','Arun','39','Venkatesh','Male','Tumkur','9645643321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('372365892645','Arjun','20','Raghavendra','Male','Banglore','9646643321')''')
cursor.execute('''INSERT INTO AADHAR_DATA VALUES('852365895045','Kavitha','25','Gurusurya','Male','Mysore','9608943321')''')


# disply the data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM AADHAR_DATA''')
print(data)
for row in data:
    print(row)
    
# commit your changes in the database
conn.commit()

# closing the connection
conn.close()  
