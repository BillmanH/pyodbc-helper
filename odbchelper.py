import pyodbc

Driver = "{SQL Server}"

def connect_from_dict(filepath):
    """
    loads a json or dict structured file and makes the connection. Errors will tell you if values are missing from your dict.
    """

    f = open(os.path.join(filepath), "r")
    keys = yaml.load(f)

    #things that you need
    Name = keys['name']
    Cataloge = keys['Database']
    Uid = keys['Uid']
    Pwd = keys['Pwd']
    #things that have defaults
    Server = keys.get('Server','tcp')
    port = keys.get('port',1433)
    MultipleActiveResultSets = keys.get('MultipleActiveResultSets',False)
    persistSecure = keys.get('MultipleActiveResultSets',False)
    Timeout = keys.get('Timeout',30)
    Encrypt = keys.get('Encrypt',"yes")
    Trust = keys.get('TrustServerCertificate',"no")
    cxn_string = f'DRIVER={Driver};' \
                + f'SERVER={Server}:{Name},{Port};' \
                + f'Initial Catalog={Cataloge};' \
                + f'Persist Security Info={persistSecure};' \
                + f'UID={Uid};PWD={Pwd};'\
                + f'MultipleActiveResultSets={MultipleActiveResultSets};' \
                + f'Encrypt={Encrypt};' \
                + f'TrustServerCertificate={Trust};' \
                + f'Connection Timeout={Timeout};' \

    cnxn = pyodbc.connect(cxn_string,Trusted_connection="no")
    return cnxn

