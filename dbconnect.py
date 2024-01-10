import pyodbc as odbc

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'DESKTOP-61OT9AG\\SQLEXPRESS1'
DATABASE_NAME = 'pydbpractice'

#uid = <username>;
#pwd = <password>;
connection_string = f"""
    DRIVER = {{{DRIVER_NAME}}};
    SERVER = {SERVER_NAME};
    DATABASE = {DATABASE_NAME};
    Trust_Connection = yes;
"""


conn = odbc.connect(connection_string)
print(conn)
