import math
from pyproj import Proj, transform
import numpy as np


from ipyleaflet import Map, basemaps, basemap_to_tiles, Rectangle
from ipyleaflet import ZoomControl

def _degree_to_zoom_level(l1, l2, margin=0.0):
    # Helper function to set zoom level for `display_map`
    degree = abs(l1 - l2) * (1 + margin)
    zoom_level_int = 0
    if degree != 0:
        zoom_level_float = math.log(360 / degree) / math.log(2)
        zoom_level_int = int(zoom_level_float)
    else:
        zoom_level_int = 18
    return zoom_level_int


def display_map(x, y, crs='EPSG:4326', margin=-0.5, zoom_bias=0):
    all_x = (x[0], x[1], x[0], x[1])
    all_y = (y[0], y[0], y[1], y[1])
    all_longitude, all_latitude = transform(Proj(crs),
                                            Proj('EPSG:4326'),
                                            all_x, all_y)

    # Calculate zoom level based on coordinates
    lat_zoom_level = _degree_to_zoom_level(min(all_latitude),
                                           max(all_latitude),
                                           margin=margin) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(min(all_longitude),
                                           max(all_longitude),
                                           margin=margin) + zoom_bias
    zoom_level = min(lat_zoom_level, lon_zoom_level)

    # Identify centre point for plotting
    center = [np.mean(all_latitude), np.mean(all_longitude)]


    esri = basemap_to_tiles(basemaps.Esri.WorldImagery)

    m = Map(layers=(esri, ), 
        center=center, 
        zoom=zoom_level, 
        zoom_control=False,
        scroll_wheel_zoom=True)
    m.add_control(ZoomControl(position='topright'))
    rectangle = Rectangle(bounds=((y[0], x[0]), (y[1], x[1])), 
        weight=2,
        color="#FF0000")
    m.add_layer(rectangle)

    return m
