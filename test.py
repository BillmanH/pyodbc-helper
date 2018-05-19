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