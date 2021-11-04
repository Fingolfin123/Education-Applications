import sqlite3
from sqlite3 import Error
import os
import pandas as pd
from ben_gislason_cse_exercise.utilities.db_read import dbRead
from ben_gislason_cse_exercise.utilities.db_open import openDb
from ben_gislason_cse_exercise.utilities.db_write import dbWrite

class TestRW:
    def __init__(self, db_path):
        """
        Open connection to database for downstream use
        """
        #Set path of local copy of database
        self.path = db_path
        #Open a connection to local copy
        
        try:
            self.conn = sqlite3.connect(self.path)    
        except Error as e:
            print(e)

        print(str(os.getcwd()).replace("\\","/")+"/tests/test.db")

    def run_test(self):
        """
        Create dataframes and generate plot and
        summary statistical table in copy of 
        database
        """

        #Set data frames to add to test_table
        columns = ['test1','test2']
        df_1 = pd.DataFrame({columns[0]:1
                             , columns[1]:1
                             },index = [0])
        df_2 = pd.DataFrame({columns[0]:2
                             , columns[1]:2
                             },index = [1])

        df_test = pd.DataFrame({columns[0]:3
                             , columns[1]:3
                             },index = [0])
        
        df_out = df_1.append(df_2)
        print("Columns to sum: ")
        print(df_out)

        #Set Summation results      
        sum1 = round(df_out[columns[0]].sum(),2)
        sum2 = round(df_out[columns[1]].sum(),2)        

        df_sum = pd.DataFrame({columns[0]:sum1
                             , columns[1]:sum2                          
                             }, index = [0])
        print(df_sum)
        df_out = df_out.append(df_sum)
        print(df_out)
        
        dbTable = "test_table"

        #Creating a cursor object using the cursor() method
        cursor = self.conn.cursor()

        #Dropping test table if already exists
        cursor.execute("DROP TABLE test_table")
        
        df_out.to_sql(dbTable, self.conn, if_exists='fail')

        df_in = dbRead(self.conn, dbTable)
        self.conn.close()
        
        #Print results
        print("Table with summation read from db file")
        print(df_in)

        print("Test Values: ")
        print(df_test)
        
        if df_in.iloc[2][1] == df_test.iloc[0][0] and df_in.iloc[2][2] == df_test.iloc[0][1]:
            print("TestRW status: Pass")
        else:
            print("TestRW status: Fail")
        
        


tO = TestRW(str(os.getcwd()).replace("\\","/")+"/test.db")
TestRW.run_test(tO)
