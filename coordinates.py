from geopy.geocoders import Nominatim

def get_coordinates(place):
    geolocator = Nominatim(user_agent="aqi_predictor")
    location = geolocator.geocode(place)
    given_lat = location.latitude
    given_lon = location.longitude
    return given_lat,given_lon