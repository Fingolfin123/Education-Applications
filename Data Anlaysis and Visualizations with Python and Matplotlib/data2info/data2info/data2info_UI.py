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
def ui_getStats():
	print("\nShow original data frame")
	myData.get_col_stats(myData.df)

#filter data
def ui_filter():
	filters = {">":datetime(2020,7,15,tzinfo=utc),"<":datetime(2020,8,1,tzinfo=utc)}
	myData.filter_data(myData.df,filters,"Timestamp",["Course Name","Timestamp","Rating"])
	dataOut = myData.filt
	filters = {">":2.5,"<":4}
	myData.filter_data(dataOut,filters,"Rating",["Course Name","Timestamp","Rating"])
	dataOut = myData.filt

	#Show results of filtered sections
	print("\nShow filter results: \n")
	myData.get_col_stats(dataOut)

#plot data
def ui_plot():
	print("\nPlotting Options: \n")
	myData.plot_data(myData.df)


#Choose which modules to interact with
ui_getStats()
#ui_filter()
#ui_plot()