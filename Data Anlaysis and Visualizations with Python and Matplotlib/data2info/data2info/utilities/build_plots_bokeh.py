
''' Present a scatter plot with linked histograms on both axes.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve selection_histogram.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/selection_histogram
in your browser.
'''


import numpy as np

from bokeh.layouts import gridplot
from bokeh.models import BoxSelectTool, LassoSelectTool, LabelSet
from bokeh.plotting import curdoc, figure, output_file, show

TOOLS="pan,wheel_zoom,box_select,lasso_select,reset"

def bokehLine(x,y,params):

    if params['plot_xaxis_type'] == True:
        x_axis_type = "datetime"
    else:
        x_axis_type = "linear"

    f = figure(tools=TOOLS, width=1200, height=600,
               toolbar_location="above", x_axis_type=x_axis_type, x_axis_label=x.name, y_axis_label=y.name,
               title=params['plot_title'])
    f.background_fill_color = "#fafafa"
    print("\nHello " + x.name)
    #f.xaxis.axis_label = str(x.name)
    #f.yaxis.axis_label = y.name

    f.line(x,y,color="orange",alpha=0.5)

    return f

def bokehScatter(x,y,params):
    #output_file(params['plot_title']+".html")
    
    # create the scatter plot
    f = figure(tools=TOOLS, width=600, height=600,
               toolbar_location="above", x_axis_label='x', y_axis_label='y',title=params['plot_title'])
    #f.background_fill_color = "#fafafa"
    f.select(BoxSelectTool).select_every_mousemove = False
    f.select(LassoSelectTool).select_every_mousemove = False

    r = f.scatter(x, y, size=3, color="#3A5785", alpha=0.6)

    return f

def bokehHistogram(x,y,params, binCount):
    # create the horizontal histogram
    
    hist, edges = np.histogram(y, density=False, bins=binCount)

    x = np.linspace(y.min(), y.max(), binCount)
    #pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
    #cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2

    f = figure(tools=TOOLS,title=params['plot_title'], x_axis_label='x', y_axis_label='y', background_fill_color="#fafafa")
    f.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
          fill_color="navy", line_color="white", alpha=0.5)

    #f = make_plot("Normal Distribution (μ=0, σ=0.5)", hist, edges, x, pdf, cdf)

    return f
    """
    # create the vertical histogram
    vhist, vedges = np.histogram(y, bins=20)
    vzeros = np.zeros(len(vedges)-1)
    vmax = max(vhist)*1.1

    pv = figure(toolbar_location=None, width=200, height=f.height, x_range=(-vmax, vmax),
                y_range=f.y_range, min_border=10, y_axis_location="right")
    pv.ygrid.grid_line_color = None
    pv.xaxis.major_label_orientation = np.pi/4
    pv.background_fill_color = "#fafafa"

    pv.quad(left=0, bottom=vedges[:-1], top=vedges[1:], right=vhist, color="white", line_color="#3A5785")
    vh1 = pv.quad(left=0, bottom=vedges[:-1], top=vedges[1:], right=vzeros, alpha=0.5, **LINE_ARGS)
    vh2 = pv.quad(left=0, bottom=vedges[:-1], top=vedges[1:], right=vzeros, alpha=0.1, **LINE_ARGS)

    layout = gridplot([[p, pv], [ph, None]], merge_tools=False)

    curdoc().add_root(layout)
    curdoc().title = "Selection Histogram"
    r.data_source.selected.on_change('indices', update)
    #show(layout)
    """    

