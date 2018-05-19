# pyodbc-helper
some assistance for pyodbc to make working with SQL server much less painful.

# You will need a config_file that has the connection string values from azure.portal.net

`{`
`  "name": "myDatabase.database.windows.net",`
`  "Uid": "me@myDatabase",`
`  "Server": "tcp",`
`  "Database": "DBname",`
`  "Pwd": "thanksBill",`
`  "Encrypt": "yes",`
`  "TrustServerCertificate": "no",`
`  "Timeout":30`
`}`

### Notes:
* If you are using an Azure SQL Server instance you will need to encrypt and distrust the serverCert. 
* I'm only building this for the tcp connection with ODBC. If you are using annother connection you will need to manage that yourself. 

#TODO:
1) Everything