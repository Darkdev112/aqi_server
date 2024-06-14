import os
from load_data import get_conc
from load_index import calc_index
from preprocessing import preprocess_data
from store_model import store_model

def train_model(lat_index,lon_index):
    directory = os.getcwd()
    folder_name = f'model{lat_index}{lon_index}'

    folder_path = os.path.join(directory,'models',folder_name)

    try:
        os.makedirs(folder_path)

        aqi1_conc = get_conc('aqi1',lat_index,lon_index)
        aqi2_conc = get_conc('aqi2',lat_index,lon_index)
        aqi3_conc = get_conc('aqi3',lat_index,lon_index)

        pm_conc = preprocess_data(aqi1_conc,'aqi1')
        co_conc = preprocess_data(aqi2_conc,'aqi2')
        o3_conc = preprocess_data(aqi3_conc,'aqi3')

        store_model(folder_path,'pm',pm_conc)
        store_model(folder_path,'co',co_conc)
        store_model(folder_path,'o3',o3_conc)

    except OSError as error:
        print(f"Error creating folder : {error}")
    


start_lat, start_lon = calc_index(8.0,68.0)
end_lat, end_lon = calc_index(38.0,98.0)

end_lat = end_lat + 1
end_lon = end_lon + 1

for lat_index in range(start_lat,end_lat):
    for lon_index in range(start_lon,end_lon):
        train_model(lat_index,lon_index)