"""
This module defines the functions to collect data from the Historical Weather API in NB01.
"""

# Imports
import requests
import json
import pandas as pd

load_dotenv()  # take environment variables from .env file


def get_lat_long(country_code, city_name, world_cities):
    """
    Retrieves the latitude and longitude of a given city in a specific country.

    Parameters:
        country_code (str): The country code of the city.
        city_name (str): The name of the city.
        world_cities (dict): A dictionary containing city data for different countries.

    Returns:
        Float: returns two floats representing latitude and longitude.
    """
    
    valid_rows = (world_cities['country']==country_code) & (world_cities['name']==city_name)
    city_data = world_cities[valid_rows]
    return city_data['lat'].iloc[0], city_data['lng'].iloc[0]


def get_rain_sum(country_code, city_name, start_date, end_date, world_cities):
    """
    A function which retrieves the rain sum for a given country code and city name.

    Parameters:
        country_code (str): The country code of the location.
        city_name (str): The name of the city.
        start_date (str): The start date of the historical data in the format 'YYYY-MM-DD'.
        end_date (str): The end date of the historical data in the format 'YYYY-MM-DD'.
        world_cities (dict): A dictionary containing city data for different countries.

    Returns:
        list: a list of the daily rain_sum (in mm) for the given data range. 
    """

    latitude, longitude = get_lat_long(country_code, city_name, world_cities)

    base_url = "https://archive-api.open-meteo.com/v1/archive?"
    params_lat_long     = "latitude=" + str(latitude) + "&longitude="  + str(longitude)
    params_date         = "&start_date=" + str(start_date) + "&end_date=" + str(end_date)
    params_others       = "&daily=rain_sum"

    final_url = base_url + params_lat_long + params_date + params_others

    response = requests.get(final_url)
    rain_data = response.json()
    rain_sum = rain_data['daily']['rain_sum']
   
    return rain_sum


def num_days_rain(country_code, city_name, start_date, end_date, world_cities):
    """
    A function which retrieves the number of days it rained in a given country code and city name.
    
    Parameters:
        country_code (str): The country code of the location.
        city_name (str): The name of the city.
        start_date (str): The start date of the historical data in the format 'YYYY-MM-DD'.
        end_date (str): The end date of the historical data in the format 'YYYY-MM-DD'.
        world_cities (dict): A dictionary containing city data for different countries.

    Returns:
        int: the number of days it rained in the given city in a given time period.
    """
        
    days_of_rain = 0
    for rain_sum in get_rain_sum(country_code, city_name, start_date, end_date, world_cities):
        if rain_sum > 0:
            days_of_rain += 1

    return days_of_rain


def total_precipitation(country_code, city_name, start_date, end_date, world_cities):
    """
    A function which retrieves the total precipitation in a given country code and city name.
    
    Parameters:
        country_code (str): The country code of the location.
        city_name (str): The name of the city.
        start_date (str): The start date of the historical data in the format 'YYYY-MM-DD'.
        end_date (str): The end date of the historical data in the format 'YYYY-MM-DD'.
        world_cities (dict): A dictionary containing city data for different countries.

    Returns:
        int: the total precipitation in mm in the given city in a given time period.
    """

    precipitation = 0
    for rain_sum in get_rain_sum(country_code, city_name, start_date, end_date, world_cities):
        precipitation += rain_sum

    return precipitation