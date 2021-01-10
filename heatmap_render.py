import folium
from folium.plugins import HeatMap


def get_map_html(touches_data, infected_touches_data):
    location = ['52.2297', '21.0122']  # center of warsaw
    zoom = 14
    title = 'OpenStreetMap'
    mainMap = folium.Map(location=location,
                         zoom_start=zoom,
                         tiles=title)

    gradient_hmap = {.25: '#92E01C', .50: '#FEF921', .90: '#F3733F', 1: '#EE3D3D'}
    # gradient_hmap1 = {.25: '#FDB7C8', .50: '#FE6B8F', .90: '#D34468', 1: '#8E2D46'}
    hmap = folium.plugins.HeatMap(touches_data,
                                  gradient=gradient_hmap,
                                  max_val=1,
                                  min_opacity=0.3,
                                  radius=17,
                                  blur=15,
                                  max_zoom=1)

    gradient = {.25: '#A6F2E5', .50: '#6ED4BF', .75: '#4DAA98', 1: '#337A6C'}
    infected_hmap = folium.plugins.HeatMap(infected_touches_data,
                                           max_val=1,
                                           gradient=gradient,
                                           min_opacity=0.3,
                                           radius=17,
                                           blur=15,
                                           max_zoom=1)
    hmap.add_to(folium.FeatureGroup(name='People contacts').add_to(mainMap))
    infected_hmap.add_to(folium.FeatureGroup(name='Infected people contacts').add_to(mainMap))

    folium.LayerControl().add_to(mainMap)

    return mainMap._repr_html_()
