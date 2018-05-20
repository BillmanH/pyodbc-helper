import os
import sys
import yaml
import pyodbc

UNAME = os.getlogin()
myPath = os.path.join("C:\\","Users","willi","source","repos","pyodbc-helper2")

sys.path.append(
        os.path.join(myPath)
        )


cnxn = connect_from_dict(os.path.join(myPath,"config_file.json"))
cursor = cnxn.cursor()


mytable = "[taxi]"
cursor.execute(f"select * from {mytable}")

test_string ="select * from [dbo].[Transaction2]"
cursor.execute(test_string)

cursor.execute(f"select * from {mytable}")
rows = cursor.fetchall()
for row in rows:
    print(row.user_id, row.user_name)