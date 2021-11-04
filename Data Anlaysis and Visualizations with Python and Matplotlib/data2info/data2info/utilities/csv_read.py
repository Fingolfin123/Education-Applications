import pandas, os.path
from os import path
from datetime import datetime
from pytz import utc

def readCSV(data, showSample):
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
    if path.exists(data):
        try:
            df=pandas.read_csv(data, parse_dates=["Timestamp"])
        except Error as e:
            print(e)

        return df
    
    if showSample == True and df.empty == False:
        print(df.head()) #show first 5 rows only
        print ("Count of (row,col): " + df.shape) # show (row,col) count
        print(df.columns) # show names of columns

    return df
