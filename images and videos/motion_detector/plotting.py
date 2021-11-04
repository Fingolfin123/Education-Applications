from motion_detector import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M%:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M%:%S")
cds=ColumnDataSource(df)

f=figure(x_axis_type='datetime',height=100,width=500,sizing_mode="scale_both", title="Motion Graph")
f.yaxis.minor_tick_line_color=None
#f.yaxis.y_minor_ticks(1)
#f.yaxis.minor_tick_out=True

hover=HoverTool(tooltips=[("Start:","@Start_string"),("End:","@End_string")])
f.add_tools(hover)


q=f.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("Graph.html")
show(f)
