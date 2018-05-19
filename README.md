# pyodbc-helper
some assistance for pyodbc to make working with SQL server much less painful.

# You will need a config_file that has the connection string values from azure.portal.net

`{` <br>
`  "name": "myDatabase.database.windows.net",`<br>
`  "Uid": "me@myDatabase",`<br>
`  "Server": "tcp",`<br>
`  "Database": "DBname",`<br>
`  "Pwd": "thanksBill",`<br>
`  "Encrypt": "yes",`<br>
`  "TrustServerCertificate": "no",`<br>
`  "Timeout":30`<br>
`}`<br>

## Requirements
* pyodbc, obviously
* you also need the **ODBC driver for SQL server**. It doesn't come with the python module. If you don't have it you have to download and install it from Microsoft.
### Notes:
* If you are using an Azure SQL Server instance you will need to encrypt and distrust the serverCert. 
* I'm only building this for the tcp connection with ODBC. If you are using annother connection you will need to manage that yourself. 

#TODO:
1) Everything