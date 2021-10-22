import folium
import pandas
#import codecs

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def setmap(xCoord,yCoord,zoom_scale):
	data = pandas.read_csv("Volcanoes.txt")
	lat = list(data["LAT"])
	lon = list(data["LON"])
	elev = list(data["ELEV"])
	name = list(data["NAME"])

	
	map = folium.Map([xCoord,yCoord], zoom_start=zoom_scale, tiles="Stamen Terrain")
	#Add Map elements
	fgv = folium.FeatureGroup(name="Volcanoes")
	
	for lt, ln, el, name in zip(lat, lon, elev, name):
                
                #iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100) couldnt get this to work so passed html variable directly and used % to poulate string var's
		fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10,
                popup=folium.Popup(html % (name, name, el)),
                fill_color= elColor(el),color = 'darkblue', fill_opacity=0.7,
                icon = folium.Icon(color = elColor(el))))

	fgp = folium.FeatureGroup(name="Population")
	fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
                
	map.add_child(fgv)
	map.add_child(fgp)
	map.add_child(folium.LayerControl())
	map.save("Map1.html")
	#codecs.open("Map1.html")


def elColor(el):
        if el < 1000:
                return 'green'
        elif 1000<=el < 3000:
                return 'orange'
        elif el > 3000:
                return 'red'        

setmap(35.6,-99,5)
