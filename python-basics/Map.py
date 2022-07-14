import folium

map = folium.Map(location = [20,-110], zoom_start = 6, tiles="Stamen Terrain")

fg= folium.FeatureGroup(name = "My Map")

for coordinates in [[51.50473488683945, 0.28056483866931325],[52, 0.2]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Pin", icon=folium.Icon(color='blue')))


map.add_child(fg)

map.save("Map2.html")
