import sqlite3

Sql_Conn = sqlite3.connect("My_Database.db")
print("Database Connected")

cursor = Sql_Conn.cursor()
print("Database Initialized")

sql_create_table = """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY,
        name varchar(100),
        gender char(1)
        );
"""

# Sql_Conn.execute(sql_create_table)
# print("Table Created")
#
#
# sql_command = """
# INSERT INTO user VALUES(2,"Ram","M");
# """
# cursor.execute(sql_command)
#
# sql_command = """
# INSERT INTO user VALUES(1,"Shyam","M");
# """
# cursor.execute(sql_command)
#
# Sql_Conn.commit()

# Reading Data From DataBase
read_query = """
    SELECT * from user WHERE name like "S%" and gender ="M";
"""

# Updating Data from Database
sql_command = """"
    UPDATE user SET name = "Hari" WHERE name like "S%"
    ;
"""
cursor.execute(sql_command)
Sql_Conn.commit()
print("Updated")

cursor.execute(read_query)
Data = cursor.fetchall()
print(Data)

