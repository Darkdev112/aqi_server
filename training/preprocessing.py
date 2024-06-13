import numpy as np

def preprocess_data(conc_data,data_type):
    if data_type == 'aqi1':
        conc_data *= 1e9
    elif data_type == 'aqi2':
        conc_data *= 1.15 * 1e-3
    else:
        conc_data *= 0.1

    nan_mask = np.isnan(conc_data)
    conc_data[nan_mask] = np.nan  

    extreme_neg_mask = conc_data < 0

    valid_mask = ~extreme_neg_mask & ~nan_mask
    if np.any(valid_mask):
        mean_value = conc_data[valid_mask].mean()
    else:
        mean_value = 0

    conc_data[nan_mask | extreme_neg_mask] = mean_value
    
    return conc_data