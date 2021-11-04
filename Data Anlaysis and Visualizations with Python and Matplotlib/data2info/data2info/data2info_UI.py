from datetime import datetime
from pytz import utc
from data2info.data_processor import DataProcessor

"""
Load data and access filtering, statistics, plotting from DataProcessor class.
"""

#'C:/Users/bgislas/Documents/GitHub/Education-Applications/Data Anlaysis and Visualizations with Python and Matplotlib/data2info/data2info/tests/reviews.csv'
print("\n")
file = input("Enter full file path for data file: ")

#Set data object
myData = DataProcessor(file)

#Show preview of dataframe
print("Show orginal data frame")
myData.get_col_stats(myData.df)

#filter data
#datetime(2020,7,1,tzinfo=utc)

#filters = {">":datetime(2020,7,15,tzinfo=utc),"<":datetime(2020,8,1,tzinfo=utc)}
#myData.filter_data(myData.df,filters,"Timestamp",["Course Name","Timestamp","Rating"])
#dataOut = myData.filt
filters = {">":2.5,"<":4}
myData.filter_data(myData.df,filters,"Rating",["Course Name","Timestamp","Rating"])
dataOut = myData.filt

#Show results of filtered sections
print("\nShow results: \n")
myData.get_col_stats(dataOut)

