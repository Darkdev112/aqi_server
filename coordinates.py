from geopy.geocoders import Nominatim

def get_coordinates(place):
    geolocator = Nominatim(user_agent="aqi_predictor")
    location = geolocator.geocode(place)
    given_lat = location.latitude if location else -1
    given_lon = location.longitude if location else -1
    return given_lat,given_lon