#%%

import os
import sys
import yaml
import pyodbc
import pandas as pd
import numpy as np


UNAME = os.getlogin()
myPath = os.path.join("C:\\","Users","williamh","source","repos","pyodbc-helper")

sys.path.append(
        os.path.join(myPath)
        )

import odbchelper as sql


#%%


cnxn = sql.connect_from_dict(os.path.join(myPath,"config_file.json"))
cursor = cnxn.cursor()

#%%
mytable = "[taxi]"
cursor.execute(f"select top 10 * from {mytable}")

#%%
test_string ="select top 10 * from [dbo].[Transaction2]"
cursor.execute(test_string)

#%%
cursor.execute(f"select * from {mytable}")
rows = cursor.fetchall()
for row in rows:
    print(row.user_id, row.user_name)


#%%
#Pulling data directly from SQL via Pandas.
DF = pd.read_sql_query("select top 10 * from [dbo].[Transaction2]", cnxn)


#%%
#Upload Testing
###  I'm adding a df that has some GUIDS and Dates to test some uploading features. 
df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))
df['Date Modified'] = '2-24-2019'
df['index'] = df.index.tolist()


#%%
replace_df(df,cnxn,table="DB_helper")


