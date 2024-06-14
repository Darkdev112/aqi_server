def calc_index(given_lat,given_lon):
    lat_list = []
    lon_list = []
    lat = -90.0
    lon = -180.0
    lat_index = -1
    lon_index = -1

    while(lat <= 90):
        lat_list.append(lat)
        lat += 0.5

    while(lon <= 180):
        lon_list.append(lon)
        lon += 0.625

    for i,val in enumerate(lat_list):
        diff = (given_lat-val)
        if  diff>=0 and  diff<0.5:
            lat_index = i
            break

    for i,val in enumerate(lon_list):
        diff = (given_lon-val)
        if  diff>=0 and  diff<0.625:
            lon_index = i
            break

    lon_index = 0 if lon_index == 576 else lon_index 

    return lat_index,lon_index