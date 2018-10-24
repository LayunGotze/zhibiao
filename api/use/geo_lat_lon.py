from geopy.geocoders import Nominatim
geolocater=Nominatim(user_agent="my-application")
def geo2lat(address):
    try:
        location=geolocater.geocode(address)
        if location is not None:
            return location.latitude,location.longitude
        return 0,0
    except:
        return 0,0
