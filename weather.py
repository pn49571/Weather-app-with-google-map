
import os
import forecastio
from geopy.geocoders import Nominatim
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons


# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# reload(sys)
# sys.setdefaultencoding('utf8')


def get_forecast(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    lat1 = location.latitude
    lng1 = location.longitude
    forecast = forecastio.load_forecast('ba96530a9d10cfa774a8747c7e03e6ed', lat1, lng1)
    current_forecast = forecast.currently()
    current_condition = current_forecast.icon
    current_temperature = current_forecast.temperature
    current_wind = current_forecast.windSpeed
    current_bearing = current_forecast.windBearing
    current_visibility = current_forecast.visibility
    forecast = "Currently {} and {}°F, with winds {}mph {}NNE, visibility {} miles at {}".format(
        current_condition.lower(),
        current_temperature,
        current_wind,
        current_bearing,
        current_visibility,
        address
    )

    mymap = Map(
        identifier="view-side",  # for DOM element
        varname="mymap",  # for JS object name
        lat=lat1,
        lng=lng1,
        markers=[(lat1, lng1)]
        )
    return forecast
