import sqlite3
import os
from shutil import copyfile
from pathlib import Path

def openDb(dbPath):
    """
    Open a database connection for downstream use

    Parameters:
        dbPath:
            path to source database that is copied
            for local use

    Returns:
        conn:
            connection to database
    """  
    try:
        conn = sqlite3.connect(dbPath)    
    except Error as e:
        print(e)

    return conn
