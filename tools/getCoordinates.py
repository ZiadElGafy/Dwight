import geocoder
from geopy.geocoders import Nominatim

def get_current_country_and_city():
    loc = geocoder.ip('me')
    country = loc.country
    city = loc.city
    return country, city

def driver():
    location = {}
    geolocator = Nominatim(user_agent="MyApp")

    current_country, current_city = get_current_country_and_city()
    location["country"] = current_country
    location["city"] = current_city

    loc = geolocator.geocode(current_city)
    location["latitude"] = loc.latitude
    location["longitude"] = loc.longitude
    
    return location