from ipyleaflet import Map, basemaps, basemap_to_tiles, Rectangle
from ipyleaflet import ZoomControl



def display_map(bbox):
    esri = basemap_to_tiles(basemaps.Esri.WorldImagery)
    center = ((bbox[1] + bbox[3]) / 2,
        ((bbox[0] + bbox[2]) / 2))
    m = Map(layers=(esri, ), center=center, zoom=6, zoom_control=False)
    m.add_control(ZoomControl(position='topright'))
    rectangle = Rectangle(bounds=((bbox[1], bbox[0]), (bbox[3], bbox[2])), 
        weight=2,
        color="#FF0000")
    m.add_layer(rectangle)

    return m