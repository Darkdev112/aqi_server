import h5py
import xarray as xr
import numpy as np
import os

dataset_list = ['aqi1','aqi2','aqi3']

for list_name in dataset_list:
    tdata = []
    monthly_data_folder = os.listdir(f'./giovanni_data/{list_name}')

    for monthly_data_file in monthly_data_folder:
        monthly_data = xr.open_dataset(f'./giovanni_data/{list_name}/{monthly_data_file}')
        
        if list_name == 'aqi1':
            code = 'DUSMASS'
        elif list_name == 'aqi2':
            code = 'COSC'
        elif list_name == 'aqi3':
            code = 'TO3'
        else:
            code = 'invalid'

        if code != 'invalid':
            monthly_conc_data = np.array(monthly_data[code].values)[0]

        tdata.append(monthly_conc_data)

    if list_name == 'aqi1':
        aqi1_data = np.array(tdata)
    elif list_name == 'aqi2':
        aqi2_data = np.array(tdata)
    elif list_name == 'aqi3':
        aqi3_data = np.array(tdata)
    else:
        print("Nothing to store")
    

with h5py.File('./model_data/aqi.h5', 'w') as f:
    f.create_dataset('aqi1', data=aqi1_data)
    f.create_dataset('aqi2', data=aqi2_data)
    f.create_dataset('aqi3', data=aqi3_data)
