# Dublin Airport Weather Data Science Assignment by A00288436

from Mathematical_Functions import *
from Read_CSV import read_csv, get_individual_times
from Get_Seasonal_Data import get_seasonal_data
from Plotting import *
from User_Interface_Seasonal_Data import *


if __name__ == "__main__":
    dates, rain, temp, wet_bulb_temperature, dew_point_temperature, vapour, humidity, mean_sea_level_pressure, mean_wind_speed, wind_direction, sunshine, visibility, cloud_height, cloud_amount, locations = read_csv("DublinAirportHourlyWeather.csv")
    days, months, seasons, years, individual_days, individual_months, individual_seasons, individual_years = get_individual_times(dates)
    rain_and_temp_data_zip = list(zip(years, seasons, days, rain, temp))
    wind_data_zip = list(zip(years, seasons, days, mean_wind_speed, wind_direction))
    humidity_data_zip = list(zip(years, seasons, days, humidity))
    sunshine_data_zip = list(zip(years, seasons, days, sunshine))

    all_spring_temperatures, mean_spring_temperatures, all_spring_rain, total_spring_rain = get_seasonal_data("spring", years, seasons, days, rain, temp, individual_years, individual_seasons, rain_and_temp_data_zip )
    all_summer_temperatures, mean_summer_temperatures, all_summer_rain, total_summer_rain = get_seasonal_data("summer", years, seasons, days, rain, temp, individual_years, individual_seasons, rain_and_temp_data_zip )
    all_autumn_temperatures, mean_autumn_temperatures, all_autumn_rain, total_autumn_rain = get_seasonal_data("autumn", years, seasons, days, rain, temp, individual_years, individual_seasons, rain_and_temp_data_zip )
    all_winter_temperatures, mean_winter_temperatures, all_winter_rain, total_winter_rain = get_seasonal_data("winter", years, seasons, days, rain, temp, individual_years, individual_seasons, rain_and_temp_data_zip )
                
    while (True):
        user_season = input("Please enter a season, or enter 99 to exit: ").lower()
        if user_season == '99':
            print("Goodbye!")
            break

        if user_season in individual_seasons:
            if user_season == 'spring':
                all_season_rain, total_season_rain, all_season_temperatures, mean_season_temperature = all_spring_rain, total_spring_rain, all_spring_temperatures, mean_spring_temperatures
            elif user_season == 'summer':
                all_season_rain, total_season_rain, all_season_temperatures, mean_season_temperature = all_summer_rain, total_summer_rain, all_summer_temperatures, mean_summer_temperatures
            elif user_season == 'autumn':
                all_season_rain, total_season_rain, all_season_temperatures, mean_season_temperature = all_autumn_rain, total_autumn_rain, all_autumn_temperatures, mean_autumn_temperatures
            elif user_season == 'winter':
                all_season_rain, total_season_rain, all_season_temperatures, mean_season_temperature = all_winter_rain, total_winter_rain, all_winter_temperatures, mean_winter_temperatures
            
            user_seasonal_interactivity(user_season, all_season_rain, total_season_rain, all_season_temperatures, mean_season_temperature, years, seasons, days, wind_direction, mean_wind_speed, individual_years, individual_seasons, wind_data_zip, humidity_data_zip, sunshine_data_zip)
        else:
            print("Not a valid season.")
            continue 