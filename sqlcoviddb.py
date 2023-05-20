# import module
import sqlite3

# connecting sqllite to aadhar data base to fetch data to covid database
conn = sqlite3.connect('aadhar.db')

# creating cursor object by using 'cursor()' method
cursor = conn.cursor()

# executing data
aadhar_num = int (input("Enter 12-digit valid Aadhar Number: "))
rows=cursor.execute("SELECT * FROM AADHAR_DATA")
flag=False
for row in rows:
    if aadhar_num == row[0]:
        name = row[1]
        age = row[2]
        dose = int(input('Vaccination dose(s) taken (0 or 1 or 2):')) 
        flag=True  
        cursor.execute("DROP TABLE IF EXISTS Covid_Data")
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Covid_Data
               (AADHAR_NUM INT PRIMARY KEY NOT NULL,
               NAME VARCHAR(25) NOT NULL,
               AGE INT NOT NULL,DOSES INT);''')
        cursor.execute('''INSERT INTO Covid_Data (AADHAR_NUM, NAME, AGE, DOSES)
                  VALUES (?, ?, ?, ?)''', (aadhar_num, name, age, dose))

        data = cursor.execute('''Select * From Covid_Data ''')
        for row in data :
            print(row)
            
if flag == False:  
    print("invalid aadhar_numbers")  
         
