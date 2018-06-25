"""
use os.urandom(size) to generate secret key
size is length of secretKey
"""
SECRET_KEY = 'p9Bv<3Eid9%$i01'
""" 
It is equivalent to connection string in MVC.
The syntax for pyodbc is 'mssql+pyodbc://scott:tiger@mydsn' where
mydsn is DSN(Data Source Name)
To set DSN visit https://support.microsoft.com/en-us/help/965049/how-to-set-up-a-microsoft-sql-server-odbc-data-source
"""
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:sa123##@pytest'



