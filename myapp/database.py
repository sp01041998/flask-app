import pymysql
 
hostname = 'localhost'
user = 'root'
password = 'Qwerty123'
 
# Initializing connection
db = pymysql.connections.Connection(
    host=hostname,
    user=user,
    password=password
)
 
# Creating cursor object
cursor = db.cursor()
 
# Executing SQL query
cursor.execute("CREATE DATABASE IF NOT EXISTS football")
cursor.execute("SHOW DATABASES")
 
# Displaying databases
for databases in cursor:
    print(databases)
 
# Closing the cursor and connection to the database
cursor.close()
db.close()