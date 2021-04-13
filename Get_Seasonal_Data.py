# Dublin Airport Weather Data Science Assignment by A00288436

from Mathematical_Functions import *
def get_seasonal_data(user_season, years, seasons, days, rain, temp, individual_years, individual_seasons, rain_and_temperatures_zip):
    '''
    Calculates the mean seasonal rainfall and temperature, and also a record of every rainfall and temperature amount in the given season
    Parameters:
    -------------
    user_season             - string - the season the user has selected to perfom analysis on
    all_season_rain         - list   - a list of every collected record of rainfall from the csv
    total_season_rain       - dict   - dictionary with each key a year, and each value the mean representation of mean rain for that year
    all_season_temperatures - list   - a list of every collected record of temperature from the csv
    mean_season_temperature - dict   - dictionary with each key a year, and each value the mean representation of mean temperature for that year
    years                   - list   - list of every individual day's year
    seasons                 - list   - list of every individual day's season
    days                    - list   - list of every day that has records
    rain                    - list   - list of every entry in the csv's 'rain' column
    temp                    - list   - list of every entry in the csv's 'temp' column
    individual_years        - list   - list of every year that occurs in the csv
    individual_seasons      - list   - list of every season
    rain_and_temperature_zip- list   - lists every day, season, year, rain and temp record
    wind_data_zip           - list   - a zip containing every year, season, day, wind_speed and wind_direction record

    Returns:
    -------------
    all_{season}_temperatures  - list - list containing every temperature measurement for the given season
    mean_{season}_temperatures - dict - dict containing each year(key) and the mean temperature(value)
    all_{season}_rainfall      - list - list containing every rainfall measurement for the given season
    total_{season}_rainfall    - dict - dict containing each year(key) and the mean rainfall(value)
    '''

    yearly_mean_temperatures = {}

    all_spring_temperatures = []
    mean_spring_temperatures = {}
    all_spring_rain = []
    total_spring_rain = {}

    all_summer_temperatures = []
    mean_summer_temperatures = {}
    all_summer_rain = []
    total_summer_rain = {}

    all_autumn_temperatures = []
    mean_autumn_temperatures = {}
    all_autumn_rain = []
    total_autumn_rain = {}

    all_winter_temperatures = []
    mean_winter_temperatures = {}
    all_winter_rain= []
    total_winter_rain = {}

    for year in individual_years:
        for season in individual_seasons:
            season_rain_total = []
            season_temperature_total = []
            for y,s,d,r,t in rain_and_temperatures_zip:
                if y == year and s == season and season == user_season:  
                    season_temperature = float(t)
                    season_rain = float(r)              
                    season_temperature_total.append(season_temperature)
                    season_rain_total.append(season_rain)
                    if season == 'spring':
                        all_spring_temperatures.append(season_temperature)
                        all_spring_rain.append(season_rain)
                    elif season =='summer':
                        all_summer_temperatures.append(season_temperature)
                        all_summer_rain.append(season_rain)
                    elif season == 'autumn':
                        all_autumn_temperatures.append(season_temperature)
                        all_autumn_rain.append(season_rain)
                    elif season == 'winter':
                        all_winter_temperatures.append(season_temperature)
                        all_winter_rain.append(season_rain)
                    
            if len(season_temperature_total) >1 :            
                season_mean_temperature = get_mean(season_temperature_total)
                if season == 'spring':
                    mean_spring_temperatures[int(year)] = season_mean_temperature
                elif season =='summer':
                    mean_summer_temperatures[int(year)] = season_mean_temperature
                elif season == 'autumn':
                    mean_autumn_temperatures[int(year)] = season_mean_temperature
                elif season == 'winter':
                    mean_winter_temperatures[int(year)] = season_mean_temperature

            if len(season_rain_total) >1 :
                season_mean_rain = get_mean(season_rain_total)
                if season == 'spring':
                    total_spring_rain[int(year)] = sum(season_rain_total)
                    #total_spring_rain.append((sum(season_rain_total), year))
                elif season =='summer':
                    total_summer_rain[int(year)] = sum(season_rain_total)
                elif season == 'autumn':
                    total_autumn_rain[int(year)] = sum(season_rain_total)
                elif season == 'winter':
                    total_winter_rain[int(year)] = sum(season_rain_total)

    if user_season == "spring":
        return all_spring_temperatures, mean_spring_temperatures, all_spring_rain, total_spring_rain 
    elif user_season == "summer":
        return all_summer_temperatures, mean_summer_temperatures, all_summer_rain, total_summer_rain 
    elif user_season == "autumn":
        return all_autumn_temperatures, mean_autumn_temperatures, all_autumn_rain, total_autumn_rain 
    elif user_season == "winter":
        return all_winter_temperatures, mean_winter_temperatures, all_winter_rain, total_winter_rain 

def get_wind_data(user_season, years, seasons, days, wind_direction, mean_wind_speed, individual_years, individual_seasons, wind_data_zip):
    '''
    Calculates the mean seasonal sunshine, and also a record of every sunshine amount in the given season
    Parameters:
    -------------
    user_season             - string - the season the user has selected to perfom analysis on
    years                   - list   - list of every individual day's year
    seasons                 - list   - list of every individual day's season
    days                    - list   - list of every day that has records
    wind_direction          - list   - list of every entry in the csv's 'year' column
    mean_wind_speed         - list   - list of every entry in the csv's 'mean)wind_speed' column
    individual_years        - list   - list of every year that occurs in the csv
    individual_seasons      - list   - list of every season
    wind_data_zip           - list   - a zip containing every year, season, day, wind_speed and wind_direction record

    Returns:
    -------------
    all_{season}_wind_speeds     - list - list containing every wind speed measurement for the given season
    mean_{season}_wind_speeds    - dict - dict containing each year(key) and the mean wind speed(value)
    all_{season}_wind_directions - list - list containing every wind direction measurement for the given season
    mean_{season}_wind_directions- dict - dict containing each year(key) and the mean wind direction(value)
    '''
    all_season_wind_speeds = []
    all_season_wind_directions = []
    mean_season_wind_speeds = {}
    mean_season_wind_directions = {}

    for year in individual_years:
        for season in individual_seasons:
            season = season.lower()
            season_wind_directions_total = []
            season_wind_speeds_total = []

            for y,s,d,mws,wd in wind_data_zip:
                if y == year and s == season and season == user_season.lower():  
                    season_wind_speed = float(mws)
                    season_wind_direction = float(wd)   

                    season_wind_directions_total.append(season_wind_direction)
                    season_wind_speeds_total.append(season_wind_speed)
                    all_season_wind_speeds.append(season_wind_speed)
                    all_season_wind_directions.append(season_wind_direction)

            if len(season_wind_directions_total) >1 :         
                season_mean_wind_direction = get_mean(season_wind_directions_total)
                mean_season_wind_directions[int(year)] = season_mean_wind_direction

            if len(season_wind_speeds_total) >1 :
                season_mean_wind_speed = get_mean(season_wind_speeds_total)
                mean_season_wind_speeds[int(year)] = season_mean_wind_speed
    return all_season_wind_speeds, mean_season_wind_speeds, all_season_wind_directions, mean_season_wind_directions

def get_humidity_data(user_season, years, seasons, days, individual_years, individual_seasons, humidity_data_zip):
    '''
    Calculates the mean seasonal humidity, and also a record of every humidity amount in the given season
    Parameters:
    -------------
    user_season             - string - the season the user has selected to perfom analysis on
    years                   - list   - list of every individual day's year
    seasons                 - list   - list of every individual day's season
    days                    - list   - list of every day that has records
    individual_years        - list   - list of every year that occurs in the csv
    individual_seasons      - list   - list of every season
    humidity_data_zip       - list   - a zip containing every year, season, day, and humidity record

    Returns:
    -------------
    all_season_humidity     - list   - list containing every humidity measurement for the given season
    mean_season_humidity    - dict   - dict containing each year(key) and the mean humidity(value)
    '''
    all_season_humidity = []
    mean_season_humidity = {}
    for year in individual_years:
        for season in individual_seasons:
            season = season.lower()
            season_humidity_total = []
            for y,s,d,h in humidity_data_zip:
                if y == year and s == season and season == user_season.lower():  
                    season_humidity = float(h)  
                    season_humidity_total.append(season_humidity)
                    all_season_humidity.append(season_humidity)

            if len(season_humidity_total) >1 :          
                season_mean_humidity = get_mean(season_humidity_total)
                mean_season_humidity[int(year)] = season_mean_humidity
    return all_season_humidity, mean_season_humidity

def get_sunshine_data (user_season, years, seasons, days, individual_years, individual_seasons, sunshine_data_zip):
    '''
    Calculates the mean seasonal sunshine, and also a record of every sunshine amount in the given season
    Parameters:
    -------------
    user_season             - string - the season the user has selected to perfom analysis on
    years                   - list   - list of every individual day's year
    seasons                 - list   - list of every individual day's season
    days                    - list   - list of every day that has records
    individual_years        - list   - list of every year that occurs in the csv
    individual_seasons      - list   - list of every season
    sunshine_data_zip       - list   - a zip containing every year, season, day, and sunshine record

    Returns:
    -------------
    all_season_sunshine     - list   - list containing every sunshine measurement for the given season
    mean_season_sunshine    - dict   - dict containing each year(key) and the mean hours of sunlight(value)
    '''
    all_season_sunshine = []
    mean_season_sunshine = {}
    for year in individual_years:
        for season in individual_seasons:
            season = season.lower()
            #print(year, season)
            season_sunshine_total = []
            for y,s,d,sunshine in sunshine_data_zip:
                if y == year and s == season and season == user_season.lower():  
                    season_sunshine = float(sunshine)  
                    season_sunshine_total.append(season_sunshine)
                    all_season_sunshine.append(season_sunshine)

            if len(season_sunshine_total) >1 :          
                season_mean_sunshine = get_mean(season_sunshine_total)
                mean_season_sunshine[int(year)] = season_mean_sunshine
    return all_season_sunshine, mean_season_sunshine

def get_extremes(data):
    '''
    Calculates and returns the min and max of the given data. 
    If the data is a list, it returns the min and max. 
    If it's a dictionary, it returns 2 objects, each containing (x, y), x being the key of the dictionary associated with the min or max, and y being the min or max.

    Parameters:
    -------------
    data - list/dict - the data of which the function has to find the min or max

    Returns:
    -------------
    2 Values

    if data is a list:
        2 numbers, the min and the max
    if data is a dict:
        2 objects, each containing the dictionary key at which the min or max is found, and the min or max
    '''
    if isinstance(data, list):
        data = sorted(data)
        return data[0], data[-1]

    elif isinstance(data, dict):
        values = data.values()
        values = sorted(values)
        least_extreme = values[0]
        most_extreme = values[-1]

        least_extreme_item = []
        most_extreme_item = []

        for x, y in data.items():
            if y == least_extreme:
                least_extreme_item = (x, least_extreme)
            elif y == most_extreme:
                most_extreme_item = (x, most_extreme)
        return least_extreme_item, most_extreme_item