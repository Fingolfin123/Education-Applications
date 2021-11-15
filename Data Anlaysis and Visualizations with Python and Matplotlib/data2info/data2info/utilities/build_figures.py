import numpy as np
from bokeh.layouts import gridplot
from bokeh.models import BoxSelectTool, LassoSelectTool
from bokeh.plotting import curdoc
from bokeh.plotting import figure, output_file, show
import pandas

from .build_plots_bokeh import bokehLine, bokehScatter, bokehHistogram


def createBokeh(df, params, showPrev):
	
	"""
	Create bokeh plot and return figure for downstream formatting and reporting
	
	params = ['plot_type(0)','plot_title(1)','plot_xaxis(2)','plot_yaxis(3)', 'plot_xaxis_type(4)']
	"""

	#Set x and y for plot building
	x = df[params['plot_xaxis']]
	y = df[params['plot_yaxis']]
	
	#Check if column is in time format to set xaxis appropriately
	if type(x[0])== pandas._libs.tslibs.timestamps.Timestamp:
		params['plot_xaxis_type'] = True
	else:
		print(False)

	#Launch plot type specific figure build
	if params['plot_type'] == "line":
		print("Creating Line Plot")
		f = bokehLine(x,y,params)

	elif params['plot_type'] == "histogram":
		print("Creating Histogram")
		print("sorry...code under construction")
		#f.histogram()
		f = bokehHistogram(x,y,params,50)
		
	elif params['plot_type'] == "scatter":
		print("Creating Scatter Plot")
		f = bokehScatter(x,y,params)
		#bokeh serve --show bokeh_scatter.py

	#Create bokeh server and launch interface
	#Combine selected plots into tabs or grid
	
	#curdoc().theme = 'dark_minimal'
	show(f)
	

	
