import h5py
import numpy as np
import os

def get_conc(list_name,lat_index,lon_index):
    conc_column = np.empty((0,),dtype='float32')

    with h5py.File('./data/model_data/aqi.h5','r') as f:
        data = f[list_name][:]
    
    for monthly_data in data:
        conc_val = monthly_data[lat_index][lon_index]
        conc_column = np.append(conc_column,conc_val)
    
    return conc_column