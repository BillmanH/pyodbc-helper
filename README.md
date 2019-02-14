# pyodbc-helper
some assistance for pyodbc to make working with SQL server much less painful.

# You will need a config_file that has the connection string values from azure.portal.net
### Example:
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

## while there is some room for ambiguity, you should stick to these naming conventions
It may be that you have a keyfile that is using annother connection parameter (e.g. node.js sql module uses `host` instead of `name`)
<br>`name = ["name","Name","Server","server","host","Host"]`
<br>`Database = ["Database","database","DB","db","Db"]`
<br>`Uid = ["Uid","uid","Login","login","username",'UserName','User']`
<br>`Pwd = ["pwd","Pwd","Password","password"]`

## Requirements
* pyodbc, obviously
* you also need the **ODBC driver for SQL server**. It doesn't come with the python module. If you don't have it you have to download and install it from Microsoft.
### Notes:
* If you are using an Azure SQL Server instance you will need to encrypt and distrust the serverCert. 
* I'm only building this for the tcp connection with ODBC. If you are using annother connection you will need to manage that yourself. 

# getting a table 
**get_table**
`df = get_table(cnxn,tableName,nrows=None,verbose=True)`
sometimes you just want to fetch a table from SQL server in the form of a dataframe. Pandas already has a great function fro this. I've just
embelished it a little to add a variable to specify the number of rows. 

# updating a table 
**upload_df**
`upload_df(df,conn,table,matchID='id',type='update')`
send a dataframe to SQL server database

if 'id' exists, it will update that record. If 'id' does not exist, add a new row.
df = typical pandas.DataFrame
conn = the db connection object
table = the name of the table in your database (without the dbo.)
[matchID] = When updating rows, the unique id of the records to update
[type] = 'update' default #only type I have right now
        'append'
        'replace'
# TODO
1) Speficy randomization in `get_table`

