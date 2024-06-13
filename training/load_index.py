import numpy as np

def calc_index(given_lat,given_lon):
    lon_index = int(((np.floor(given_lon/0.625) * 0.625) - (-180))/0.625)
    lon_index = 0 if lon_index == 576 else lon_index
    lat_index = int(((np.floor(given_lat/0.5) * 0.5) - (-90))/0.5)
    return lat_index,lon_index