import joblib
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from prophet import Prophet

def store_model(folder_path,data_type,conc):
    scaler = MinMaxScaler()
    model = Prophet(interval_width=0.95)

    start_date = '2005-01-01'
    end_date = '2023-12-31'
    ds = pd.date_range(start=start_date, end=end_date, freq='MS')

    df = pd.DataFrame({'ds' : ds,'y' : conc})
    df['y'] = scaler.fit_transform(df[['y']])
    print(df)
    model.fit(df)

    with open(f'{folder_path}/{data_type}_prophet.pkl', 'wb') as f:
        pickle.dump(model, f)
    joblib.dump(scaler, f'{folder_path}/{data_type}_scaler.pkl')