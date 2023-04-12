#bulk of code created by chatgpt
#with modifications, this should connect to an Oracle database and dump to a csv


import cx_Oracle
import csv
import os

A2000_PWD = os.environ.get('A2000_PWD')
A2000_USER = os.environ.get('A2000_PWD')
cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle_Instant_Client\instantclient_21_3")


# establish connection to the Oracle database
connection = cx_Oracle.connect(user=A2000_USER, password=A2000_PWD, dsn=" ")

# create a cursor object
cursor = connection.cursor()

# execute the query
cursor.execute(" ")

# fetch all the rows
rows = cursor.fetchall()

# define the output file name
output_file = "output.csv"

# open the output file in write mode
with open(output_file, mode='w', newline='') as file:

    # create a CSV writer object
    writer = csv.writer(file)

    # write the header row
    writer.writerow(['CUST_NO'])

    # write the data rows
    for row in rows:
        writer.writerow(row)

# close the output file
file.close()

# close the cursor and connection
cursor.close()
connection.close()

print(f"The query results have been saved to {output_file}.")
