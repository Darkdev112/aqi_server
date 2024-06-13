import os
import numpy as np
import pandas as pd
from prophet import Prophet
from load_data import get_conc
from load_index import calc_index
from preprocessing import preprocess_data

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

        df = pd.DataFrame({'pm_conc' : pm_conc, 'co_conc' : co_conc,'o3_conc' : o3_conc})
        df.to_csv(f'{folder_path}/ref.csv')


    except OSError as error:
        print(f"Error creating folder : {error}")
    


# start_lat, start_lon = calc_index(8.0,68.0)
# end_lat, end_lon = calc_index(38.0,98.0)

# end_lat = end_lat + 1
# end_lon = end_lon + 1

# for lat_index in range(start_lat,end_lat):
#     for lon_index in range(start_lon,end_lon):
#         train_model(lat_index,lon_index)

start_lat, start_lon = calc_index(-20.7832,-85.5085)
train_model(start_lat,start_lon)