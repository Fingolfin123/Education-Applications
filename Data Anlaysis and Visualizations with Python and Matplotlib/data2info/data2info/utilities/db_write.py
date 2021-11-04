import pandas as pd
import sqlite3
import os
from shutil import copyfile
from pathlib import Path



def dbWrite(dbPath, dbTable, df, optional_path):
    '''
    Writes dataframe to summary database file. 

    Parameters:
        dbPath:
            Path of summary database
            this database is saved to local test directory

        dbTable:
            Name of resulting summary table

    Returns:
        df:
            Dataframe representing selected table

    '''
    if not os.path.exists(optional_path):
        os.mkdir(optional_path)
            
    dbPath_out = optional_path + "/" + Path(dbPath).stem + "_summary.db"
    
    #clean up old file if exists
    if os.path.exists(dbPath_out):
        print("summary file exists. removing and replacing")
        os.remove(dbPath_out)

    #Copies output file to desired path
    copyfile(dbPath, dbPath_out)
      
    try:
        conn = sqlite3.connect(dbPath_out)    
    except Error as e:
        print(e)

    df.to_sql(dbTable, conn, if_exists='fail')
    
    conn.close()

    return dbPath_out
