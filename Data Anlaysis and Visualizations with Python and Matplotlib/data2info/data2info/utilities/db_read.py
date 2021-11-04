import pandas as pd
import sqlite3
import os
from shutil import copyfile
from pathlib import Path

def dbRead(dbConn, dbTable):
    '''
    Reads in SQLite database and converts table 
    to pandas dataframe for downstream analysis

    Parameters:
        dbConn:
            connection to database to be used for comparison table

        dbTable:
            Name of table to convert to dataframe

    Returns:
        df:
            Dataframe representing selected table

    Future versions of this will be used in class to 
    read mutliple file types

    '''

    tableNames = pd.read_sql_query('SELECT name from sqlite_master where type= "table";', dbConn)
       
    print("\nAvailable tables:")
    print(tableNames["name"])

    dbTable = int(input("\nSelect the index of table you would like to load: "))

    if not dbTable:
        if tableNames["name"].count() == 0:
            print("Not tables found in data file.")
        else:
            #set default table to read from if none selected
            dbTable = tableNames["name"][0]
    
    print("Selected Table: " + dbTable)
    df = pd.read_sql_query('SELECT * FROM ' + dbTable, dbConn)
    
    return df


