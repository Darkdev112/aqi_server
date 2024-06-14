import joblib
import pickle
import pandas as pd
from aqi import calc_aqi

def model_predict(periods,given_lat,given_lon):
    factors = ['pm','co','o3']
    conc = []

    for factor in factors:
        scaler = joblib.load(f'./models/model{given_lat}{given_lon}/{factor}_scaler.pkl')
        
        with open(f'./models/model{given_lat}{given_lon}/{factor}_prophet.pkl','rb') as f:
            model = pickle.load(f)
        
        future_date = model.make_future_dataframe(periods, freq='MS')
        forecast = model.predict(future_date)
        predicted_df = pd.DataFrame({'ds' : forecast.ds , 'conc' : forecast.yhat})
        predicted_df['conc'] = scaler.inverse_transform(predicted_df[['conc']])
        predicted_conc = predicted_df.iloc[-1]['conc']

        conc.append(predicted_conc)

    aqi = calc_aqi(conc)
    return aqi