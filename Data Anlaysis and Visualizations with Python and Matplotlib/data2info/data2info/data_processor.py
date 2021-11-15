#import modules

from data2info.utilities.db_get_copy import getCopy
from data2info.utilities.db_read import dbRead
from data2info.utilities.db_open import openDb
from data2info.utilities.calc_tb_stats import calcTBStats
from data2info.utilities.db_write import dbWrite
from data2info.utilities.csv_read import readCSV
from data2info.utilities.excel_read import readExcel
from data2info.utilities.get_col_types import getTypes
from data2info.utilities.build_figures import createBokeh

import os
import sqlite3
from pathlib import Path
from datetime import datetime
from pytz import utc    #required for translating/interepreting timezones

class DataProcessor:

    def __init__(self, db_path):
        """
        Open data file and generate dataframe for downstream use
        """

        #Set path of local copy of database
        self.path = getCopy(db_path,db_path.rsplit('.', 1)[1])

        print("\nLoading file: \ntype: " + self.path.rsplit('.', 1)[1])

        #Open a connection to local copy
        if self.path.rsplit('.', 1)[1] == "csv":
            print("\npath: " + self.path)
            self.df = readCSV(self.path,False)
        elif self.path.rsplit('.', 1)[1] == "xlsx":
            print("\npath: " + self.path)
            self.df = readExcel(self.path,False)
        elif self.path.rsplit('.', 1)[1] == "db":
            print("\npath: " + self.path)
            self.conn = openDb(self.path)
            self.df = dbRead(self.conn, "")

        #get column types
        self.dftypes = getTypes(self.df)

    def filter_data(self, df, filtParam, filtCol, returnCol):

        """
        Filter selected data into filtered dataframe for plotting and analysis
        ">" | "<" | "==" | ">=" | "<=" | "!=" | "is" ["not"] | ["not"] "in"
        """

        #key, value
        if df.empty:
            df = self.df

        print("\nFilter(s) applied:")
        for key,value in filtParam.items():
            print(f"{filtCol} {key} {value}")
            if key == ">":
                self.filt = df[df[filtCol] > value][returnCol]    #filter values that filtered column are greater than comparison value
            elif key == "<":
                self.filt = df[df[filtCol] < value][returnCol]    #filter values that filtered column are less than comparison value
            elif key == "==":
                self.filt = df[df[filtCol] == value][returnCol]   #filter values that filtered column are equal than comparison value
            elif key == ">=":
                self.filt = df[df[filtCol] >= value][returnCol]   #filter values that filtered column are greater or equal than comparison value
            elif key == "<=":
                self.filt = df[df[filtCol] <= value][returnCol]   #filter values that filtered column are less or equal than comparison value
            elif key == "!=":
                self.filt = df[df[filtCol] != value][returnCol]   #filter values that filtered column are not equal to comparison value

            return self.filt
        #print(self.filt)

    def __getitem__(self):
        return getattr(self)

    def help(self):
        """
        Show method descriptions
        """

        print('\nMethods for data2info include: ')
        print("show_df(df): shows preview of data frame and (row,col) count")
        print("select_data(self, df, selCols, selRowsLo, selRowsHi): returns selected subset datframe of source data")
        print("filter_data(self, df, filtParam, returnCol): returns filtered subset datframe of selected data\n")
        print("get_col_stats(self,df): returns statistical subet dataframe of all columns\n")

    def get_col_stats(self,df):
        """
        Get column types and determine range value for numerical and time data types, 
        and alphabetical range for string datatypes. Automatically converts time columns
        datetime[ns,UTC] format.
        """

        if df.empty:
            df = self.df   

        #get column stats
        self.stats = df.agg(['min', 'max'])
        print(self.stats)
        return self.stats

    def plot_data(self, df):
        """
        Plot input dataframe
        Requries user interaction to:
            figType = set plot library to use
            params = basic setting of title, x and y axis
        """

        if df.empty:
            df = self.df

        print("\nFigure library includes: ")
        def_FigTypes = ["matplotlib","bokeh","plotly","seaborn","ggplot"]
        print(def_FigTypes)

        print("\nOptions for data axis include: ")
        print(list(sorted(df)))
                
        print("\nOptions for plot type include: ")
        def_PlotTypes = ["line","histogram","scatter",]
        print(def_PlotTypes)

        figType = int(input("\nEnter the index for which python library you would like to use to create a figure:"))
        params = input("\nEnter basic figure parameters seperated by a column ('type','title','xaxis','yaxis')").split(",")
        params = {'plot_type':params[0],
                  'plot_title':params[1],
                  'plot_xaxis':params[2],
                  'plot_yaxis':params[3],
                  'plot_xaxis_type':False
                  }

        if figType == 0:
            print("\n Matplotlib plot:")
            print(def_PlotTypes)
            print("plotting under dev")
        elif figType == 1:
            print("\nBokeh plot:")
            self.plotFig = createBokeh(df, params, True)
        elif figType == 2:
            print("\n Plotly plot:")
            print(def_PlotTypes)
            print("plotting under dev")
        elif figType == 3:
            print("\n Seaborn plot:")
            print(def_PlotTypes)
            print("plotting under dev")
        elif figType == 4:
            print("\n ggplot plot:")
            print(def_PlotTypes)
            print("plotting under dev")

    def select_data(self, df, selCols, selRowsLo, selRowsHi, step):
        """
        Grab selection into new dataframe for specific filtering, this is simple row filter
        """
        if selRowsLo == "*":
            selRowsLo = 0

        if selRowsHi == "*":
            selRowsHi = df[df.columns[0]].count()

        if df.empty:
            df = self.df 
                   
        #recieves list of columns and rows and gets selected dataframe
        print ("\nSelected Subset Preview: ")
        self.sel = df[selCols].iloc[selRowsLo:selRowsHi:step,:]
        return self.sel
        print(self.sel.head())

    def show_df(self,df):
        """
        Show preview of source data
        """

        if df.empty:
            df = self.df

        print ("\nDataframe Preview: ")
        print(df.head()) #show first 5 rows only
        print ("\nCount of (row,col): ")
        print(df.shape) # show (row,col) count
          
    #def run_cse_exercise(self, optional_path=str(os.getcwd())+"/output"):
        """
        Create dataframes and generate plot and
        summary statistical table in copy of 
        database
        """

        #read data tables from SQLLite and convert to data frames for analysis
        tableNames = ['smaller_bin_consumption_data','larger_bin_consumption_data']
        
        df_1 = dbRead(self.conn, tableNames[0])
        df_2 = dbRead(self.conn, tableNames[1])

        #generate dataframe containing summary table
        df_out = calcTBStats(df_1, df_2)

        #write new table using summary dataframe into a copy of db file that also contains summary table
        path = dbWrite(self.path, 'load_summary', df_out, optional_path)
        self.conn.close()
        print("Summary output database and load duration plot can be found here: " + os.path.dirname(path).replace("/","\\"))

        #plot load duration curves
        plotTables(df_1, df_2, tableNames, optional_path)
        
    #def test(self):
        """
        Run Test on csv file
        """

        #Test csv file
        #Test excel file
        #Test db file
        #Test json file
        #Test tdms file

        #print("myself: " + self.df)
        #print("test: " + readCSV(self.path,True))
        
