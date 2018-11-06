#%%
import os
import pyodbc
import yaml
import pandas as pd

#%%
class DB_PARAMS(object):

    def __init__(self, *args, **kwargs):

        self.Driver = "{SQL Server}"
        self.Encoding = "SQL_Latin1_General_CP1_CI_AS"
        return super().__init__(*args, **kwargs)


def connect_from_dict(filepath):
    """
    loads a json or dict structured file and makes the connection. Errors will tell you if values are missing from your dict.
    """

    f = open(os.path.join(filepath), "r")
    keys = yaml.load(f)

    #things that you need
    Name = keys['name']
    Database = keys['Database']
    Uid = keys['Uid']
    Pwd = keys['Pwd']
    #things that have defaults
    Driver = keys.get('driver','{ODBC Driver 13 for SQL Server}')
    Server = keys.get('Server','tcp')
    Port = keys.get('port',1433)
    MultipleActiveResultSets = keys.get('MultipleActiveResultSets',False)
    persistSecure = keys.get('MultipleActiveResultSets',False)
    Timeout = keys.get('Timeout',30)
    Encrypt = keys.get('Encrypt',"yes")
    Trust = keys.get('TrustServerCertificate',"no")
    cxn_string = f'DRIVER={Driver};' \
                + f'SERVER={Server}:{Name},{Port};' \
                + f'Database={Database};' \
                + f'Persist Security Info={persistSecure};' \
                + f'UID={Uid};PWD={Pwd};'\
                + f'MultipleActiveResultSets={MultipleActiveResultSets};' \
                + f'Encrypt={Encrypt};' \
                + f'TrustServerCertificate={Trust};' \
                + f'Connection Timeout={Timeout};' \

    cnxn = pyodbc.connect(cxn_string,Trusted_connection="no")
    cnxn.setencoding('utf-8')
    return cnxn

#%%
def get_table(cnxn,tableName,nrows=10,verbose=False):
    """
    get a full table (select *) and return it as a dataframe.
    
    df = get_table(cnxn,tableName,nrows=None,verbose=True)
    cnxn = connection object (TODO: replace with self)
    tableName (STR) = string table to retrieve from DB
    nrows (INT default:None) number of rows to return (used like 'select top n from table'
    """
    cursor = cnxn.cursor()
    topString = ""
    if nrows != None:
        topString = f"top {nrows}"
    sqlString = f"select {topString} * from {tableName}"
    if verbose:
        print(sqlString)
    DF = pd.read_sql_query(sqlString, cnxn)
    return DF



