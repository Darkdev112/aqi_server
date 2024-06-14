from fastapi import FastAPI
from datetime import date
from coordinates import get_coordinates
from training.load_index import calc_index
from model import model_predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"status" : "server running"}

@app.post("/predict")
def predict(location : str, exact_date : date):
    ref_date = date(2024,1,1)
    periods = (exact_date.year - ref_date.year) * 12 + exact_date.month + 1 - ref_date.month 

    given_lat,given_lon = get_coordinates(location)

    lat_index,lon_index = calc_index(given_lat,given_lon)

    if lat_index<196 or lat_index > 256 or lon_index<396 or lon_index>444:
        return {"result" : None, "error" : "Not a valid location"}
    
    aqi = model_predict(periods,lat_index,lon_index)

    return {"result" : aqi, "error" : None}
    



