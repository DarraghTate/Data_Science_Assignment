# Dublin Airport Weather Data Science Assignment by A00288436

from Mathematical_Functions import *
from Plotting import * 
from Get_Seasonal_Data import get_wind_data, get_humidity_data, get_sunshine_data, get_extremes
from Printing import print_data

def user_seasonal_interactivity(user_season, all_season_rain, total_season_rain, all_season_temperatures, mean_season_temperature, years, seasons, days, wind_direction, mean_wind_speed, individual_years, individual_seasons, wind_data_zip, humidity_data_zip, sunshine_data_zip):
    '''
    Asks the user what type of data they would like to see, collects it if it has not yet been collected, and then calls the print_formatted_output() on that data.
    Parameters:
    -------------
    user_season             - string - the season the user has selected to perfom analysis on
    all_season_rain         - list   - a list of every collected record of rainfall from the csv
    total_season_rain       - dict   - dictionary with each key a year, and each value the mean representation of mean rain for that year
    all_season_temperatures - list   - a list of every collected record of temperature from the csv
    mean_season_temperature - dict   - dictionary with each key a year, and each value the mean representation of mean temperature for that year
    years                   - list   - list of every entry in the csv's 'year' column
    seasons                 - list   - list of every entry in the csv's 'year' column
    days                    - list   - list of every entry in the csv's 'year' column
    wind_direction          - list   - list of every entry in the csv's 'year' column
    mean_wind_speed         - list   - list of every entry in the csv's 'year' column
    individual_years        - list   - list of every entry in the csv's 'year' column
    individual_seasons      - list   - list of every entry in the csv's 'year' column
    wind_data_zip           - list   - a zip containing every year, season, day, wind_speed and wind_direction record
    humidity_data_zip       - list   - a zip containing every year, season, day, and humidity record
    sunshine_data_zip       - list   - a zip containing every year, season, day, and sunshine record

    Returns:
    -------------
    Nothing. return keyword used to break out of function if user opts to not plot anything
    '''
    while(True):
        print('\n')
        try:
            user_request = int(input("What type of weather would you like to see data on?\n1: Rain\n2: Temperature\n3: Wind Speed\n4: Wind Direction\n5: Humidity\n6: Sunshine\n99: Select Different Season, or Exit\n>: "))
        except ValueError:
            print("That is not a valid input.")
            continue

        if (user_request == 99):
            break
        
        if (user_request not in (list(range(1, 7)))):
            print ("\nPlease enter a valid input (1-6 or 99)")
            continue

        user_season = user_season.title()
        if user_request == 1:
            print_formatted_output(user_season, all_season_rain, total_season_rain, "rainfall", "mm", "wettest", "driest")

        elif user_request == 2 :
            print_formatted_output(user_season, all_season_temperatures, mean_season_temperature, "temperature", "degrees", "hottest", "coolest" )

        elif user_request == 3 or user_request == 4:
            all_season_wind_speeds, mean_season_wind_speeds, all_season_wind_directions, mean_season_wind_directions = get_wind_data(user_season, years, seasons, days, wind_direction, mean_wind_speed, individual_years, individual_seasons, wind_data_zip)
            if user_request == 3: 
                print_formatted_output(user_season, all_season_wind_speeds, mean_season_wind_speeds, "wind speed", "kph", "most windy", "least windy")
            else:
                print_formatted_output(user_season, all_season_wind_directions, mean_season_wind_directions, "wind direction", "degrees", "highest degree wind direction", "lowest degree wind direction")
        
        elif user_request == 5:
            all_season_humidity, mean_season_humidity = get_humidity_data(user_season, years, seasons, days, individual_years, individual_seasons, humidity_data_zip)
            print_formatted_output(user_season, all_season_humidity, mean_season_humidity, "humidity", "%", "most humid", "least humid")
        elif user_request == 6:
            all_season_sunshine, mean_season_sunshine = get_sunshine_data(user_season, years, seasons, days, individual_years, individual_seasons, sunshine_data_zip)
            print_formatted_output(user_season, all_season_sunshine, mean_season_sunshine, "sunshine", "hours", "sunniest", "least sunny")


def print_formatted_output(user_season, all_season_data, mean_season_data, type_in, units, max_descriptor, min_descriptor):
    '''
    Prints the collected data. The data is formated in such a way as to make sense in English.

    Parameters:
    -------------
    user_season      - string - the season the user has selected to perfom analysis on
    all_season_data  - list   - a list of every collected record of the chosen data from the csv
    mean_season_data - dict   - dictionary with each key a year, and each value the mean representation of the chosen data for that year
    type_in          - string - the category of information in data (eg 'temperature', 'rainfall')
    units            - string - the unit of measurement used by type_in (eg 'degrees', 'mm')
    max_descriptor   - string - The way to describe the largest record, eg "temperature" would be "hottest", "rainfall" would be "wettest"
    min_descriptor   - string - The way to describe the smallest record, eg "temperature" would be "colest", "rainfall" would be "driest"

    Returns:
    -------------
    Nothing. return keyword used to break out of function if user opts to not plot anything
    '''
    print(f'\n{user_season} {type_in} mean: {get_mean(all_season_data):.2f} {units}.')
    print(f'{user_season} {type_in} mode: {get_mode(mean_season_data):.2f} {units}.')
    season_variable_median = get_median(mean_season_data)
    print(f'{user_season} {type_in} median: {season_variable_median[1]:.2f} {units}, which occured in {season_variable_median[0]}')
    print(f'{user_season} {type_in} standard deviation: {get_standard_deviation(all_season_data):.2f} %')
    season_extreme_values = get_extremes(mean_season_data)
    print(f'The {max_descriptor} {user_season} was in {season_extreme_values[1][0]}, when the average {type_in} was {season_extreme_values[1][1]:.2f} {units}.')
    print(f'The {min_descriptor} {user_season} was in {season_extreme_values[0][0]}, when the average {type_in} was {season_extreme_values[0][1]:.2f} {units}.')
    plot_data(user_season, all_season_data, mean_season_data, type_in, units)


def plot_data(user_season, all_metrics, mean_metrics, type_in, units):
    '''
    Asks user if they want to plot the data collected, and if so which type of plot. Asks until valid answers are selected.
    If they wish to plot something, then that plot function is called passing in the required parameters

    Parameters:
    -------------
    user_season -  string - the season the user has selected to perfom analysis on
    all_metrics -  list   - a list of every collected record of the chosen data from the csv
    mean_metrics - dict   - dictionary with each key a year, and each value the mean representation of the chosen data for that year
    type_in -      string - the category of information in data (eg 'temperature', 'rainfall')
    units -        string - the unit of measurement used by type_in (eg 'degrees', 'mm')

    Returns:
    -------------
    Nothing. return keyword used to break out of function if user opts to not plot anything
    '''
    while True:
        print_seasonal_data(mean_metrics, type_in, units)
        req_plot = input("would you like to plot the means? y/n : ")
        if req_plot == 'y':
            while True:
                req_plot_style = int(input("What type of plot would you like?\n1: bar chart\n2: pie chart\n3: line chart\n4: scatter plot\n>: "))
                if req_plot_style == 1:
                    print_bar_chart(mean_metrics, user_season, type_in, units)
                    while True:
                        req_continue = input("Would you like to see this on a different type of graph? y/n: ").lower()
                        if req_continue == 'y':
                            break
                        elif req_continue == 'n':
                            return
                        else:
                            print("Not a valid input")
                            continue
                elif req_plot_style == 2:
                    print_pie_chart(mean_metrics, user_season, type_in, units)
                    while True:
                        req_continue = input("Would you like to see this on a different type of graph? y/n: ").lower()
                        if req_continue == 'y':
                            break
                        elif req_continue == 'n':
                            return
                        else:
                            print("Not a valid input")
                            continue
                elif req_plot_style == 3:
                    print_line_chart(mean_metrics, user_season, type_in, units)
                    while True:
                        req_continue = input("Would you like to see this on a different type of graph? y/n: ").lower()
                        if req_continue == 'y':
                            break
                        elif req_continue == 'n':
                            return
                        else:
                            print("Not a valid input")
                            continue
                elif req_plot_style == 4:
                    print_scatter_plot(mean_metrics, user_season, type_in, units)
                    while True:
                        req_continue = input("Would you like to see this on a different type of graph? y/n: ").lower()
                        if req_continue == 'y':
                            break
                        elif req_continue == 'n':
                            return
                        else:
                            print("Not a valid input")
                            continue
        elif req_plot =='n':
            return
        else:
            print("Not valid input.")
            req_plot = ""
            continue
        return

def print_seasonal_data(data, type_in, units):
    '''
    Calls the print_data() function passing in the parameters recieved. Asks if user wants to print data until they answer 'y' or 'n'.

    Parameters:
    -------------
    data -    list/dict -  the list or dictionary to be printed
    type_in - string - the category of information in data (eg 'temperature', 'rainfall')
    units -   string - the unit of measurement used by type_in (eg 'degrees', 'mm')

    Returns:
    -------------
    Nothing
    '''
    while True:
        req_print = input("would you like to print the annual means? y/n : ").lower()
        #print("req plot: " + str(req_print))
        if req_print == 'y':
            print_data(data, type_in, units)
            break
        elif req_print == 'n':
            return
        else:
            print("\nNot a valid input. Please enter \'y\' for yes or \'n\' for no.")
            continue