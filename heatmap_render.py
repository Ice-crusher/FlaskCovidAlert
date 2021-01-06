import folium
from folium.plugins import HeatMap


def get_map_html(touches_data, infected_touches_data):
    location = ['52.2297', '21.0122']
    zoom = 6
    title = 'OpenStreetMap'
    mainMap = folium.Map(location=location,
                      zoom_start=zoom,
                      tiles=title)

    hmap = folium.plugins.HeatMap(touches_data,
                                min_opacity=0.2,
                                radius=17,
                                blur=15,
                                max_zoom=1)
    hmap.add_to(folium.FeatureGroup(name='Heat Map').add_to(mainMap))

    folium.LayerControl().add_to(mainMap)

    return mainMap._repr_html_()
