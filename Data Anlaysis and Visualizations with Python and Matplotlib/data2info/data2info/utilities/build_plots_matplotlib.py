#load the required modules
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import os
from shutil import copyfile

def plotTables(df_1, df_2, tableNames, optional_path):
    '''
    Receives data frames containing load data for 
    plotting and saves resulting plot figure.

    Parameters:
        df_1:
            Dataframe representing first table

        df_2:
            Dataframe representing second table

        tableNames: tuple(str)
            Names of load data tables to be compared.
    
    Returns:
        none

    Outputs:
        plot image

    Future version may include this as a class and 
    allow for various plot output options and ability 
    to accomadate N plots

    '''
    plt = plotLoad(df_1, tableNames)
    plt = plotLoad(df_2, tableNames)

    if not os.path.exists(optional_path):
        os.mkdir(optional_path)
        
    savePath = optional_path
    
    if os.path.exists(savePath + '/load_duration.png'):
        print("image file exists. removing and replacing")
        os.remove(savePath + '/load_duration.png')
   
    plt.savefig(savePath + '/load_duration.png')
        
    plt.show()
    
def plotLoad(load_df, tableNames):
    '''
    Sets up plot for load duration curves

    Parameters:
        load_df:
            Dataframe to add to plot for load duration curve

        tableNames: tuple(str)
            Names of load data tables to be compared.

    Returns:
        plt:
            Plot containing load duration curve(s)
    '''

    # Plot the load profile
    sb.set(rc={"figure.figsize":(10, 7)})

    # Add a column for the time interval for which the loads were recorded
    load_df['interval'] = 1
    #print(load_df)

    # Sort the DataFrame by the loads, in descending order of magnitude
    load_df_sorted = load_df.sort_values(by=['total'], ascending = False)
    #print(load_df_sorted)

    # Use the cumsum() function to to add a column with the duration for which the system load is greater than or equal to each load
    load_df_sorted['duration'] = load_df_sorted['interval'].cumsum()
    #print(load_df_sorted)

    # Calculate the percentage of time for which the system load is greater than or equal to each load
    load_df_sorted['percentage'] = load_df_sorted['duration']*100/(24*365)
    #print(load_df_sorted)

    # Plot the load_duration curve (Load vs Percentage of time)

    p = sb.lineplot(x = "percentage", y = "total", data = load_df_sorted)
    plt.ylim(0, None)
    plt.xlim(0, None)
    p.set_title("Load-Duration Curve", fontsize = 30)
    p.set_xlabel("Time (%)", fontsize = 20)
    p.set_ylabel("Load (MW)", fontsize = 20)
    plt.autoscale()
    plt.legend(labels=tableNames)

    return plt
