# Dublin Airport Weather Data Science Assignment by A00288436

def read_csv(csv_in):
    '''
    Reads the given CSV and returns a list for each column (excluding index columns, as they contain no valuable information)
    Parameters:
    -------------
    csv_in - string - the name of the CSV to be scanned in

    Returns:
    -------------
    dates                   - list - Every entry in the dates column of the input csv
    rain                    - list - Every entry in the rain column of the input csv
    temp                    - list - Every entry in the temp column of the input csv
    wet_bulb_temperature    - list - Every entry in the wet_bulb_temperature column of the input csv 
    dew_point_temperature   - list - Every entry in the dew_point_temperature column of the input csv
    vapour                  - list - Every entry in the vapour column of the input csv
    humidity                - list - Every entry in the humidity column of the input csv
    mean_sea_level_pressure - list - Every entry in the mean_sea_level_pressure column of the input csv
    mean_wind_speed         - list - Every entry in the mean_wind_speed column of the input csv
    wind_direction          - list - Every entry in the wind_direction column of the input csv
    sunshine                - list - Every entry in the sunshine column of the input csv
    visibility              - list - Every entry in the visibility column of the input csv
    cloud_height            - list - Every entry in the cloud_height column of the input csv
    cloud_amount            - list - Every entry in the cloud_amount column of the input csv
    locations               - list - Every entry in the locations column of the input csv
    '''
    with open(csv_in, 'r') as csv:
        csv = csv.read()
    rows = csv.split('\n')

    # Lists which will contain the values in every column of the CSV (asides from 'index' values, as they don't provide weather information)
    dates = []
    rain = []
    temp = []
    wet_bulb_temperature = []
    dew_point_temperature = []
    vapour = []
    humidity = []
    mean_sea_level_pressure = []
    mean_wind_speed = []
    wind_direction=[]
    sunshine = []
    visibility = []
    cloud_height = []
    cloud_amount = []
    locations = []
    #date 0,ind1, rain2, ind3, temp4, ind5, wetb6, dewpt7, vappr8,rhum9,msl10,ind11,wdsp12,ind13,wddir14,ww15,w16,sun17,vis18,clht19,clamt20
    # Start at 25, as there are 25 rows of documentation
    for i in range(25, len(rows)):
        row = rows[i]
        if len(row) > 0:        
            split_row = row.split(',')
            dates.append(split_row[0])
            # Note: '-' is used as placeholder for null value in CSV, so it doesn't add null values to the lists
            if not ('-' in split_row[2]):
                try:
                    rain.append(float(split_row[2]))
                # If ValueError is thrown, then that value isn't added and the next variable is checked
                except ValueError:
                    pass
            # Different conditional as temperatures below 0 degrees contains a '-'
            if len(split_row[4]) > 1:
                try:
                    temp.append(float(split_row[4]))
                except ValueError:
                    pass
            if not ('-' in split_row[6]):
                try:
                    wet_bulb_temperature.append(float(split_row[6]))
                except ValueError:
                    pass
            if not ('-' in split_row[7]):
                try:
                    dew_point_temperature.append(float(split_row[7]))
                except ValueError:
                    pass
            if not ('-' in split_row[8]):
                try:
                    vapour.append(float(split_row[8]))
                except ValueError:
                    pass
            if not ('-' in split_row[9]):
                try:
                    humidity.append(float(split_row[9]))
                except ValueError:
                    pass
            if not ('-' in split_row[10]):
                try:
                    mean_sea_level_pressure.append(float(split_row[10]))
                except ValueError:
                    pass
            if not (split_row[12]=='-'):
                try:
                    mean_wind_speed.append(float(split_row[12]))
                except ValueError:
                    pass
            if not ('-' in split_row[14]):
                try:
                    wind_direction.append(float(split_row[14]))
                except ValueError:
                    pass
            if not ('-' in split_row[17]):
                try:
                    sunshine.append(float(split_row[17]))
                except ValueError:
                    pass
            if not ('-' in split_row[18]):
                try:
                    visibility.append(float(split_row[18]))
                except ValueError:
                    pass
            if not ('-' in split_row[19]):
                try:
                    cloud_height.append(float(split_row[19]))
                except ValueError:
                    pass
            if not ('-' in split_row[20]):
                try:
                    cloud_amount.append(float(split_row[20]))
                except ValueError:
                    pass
    return dates, rain, temp, wet_bulb_temperature, dew_point_temperature, vapour,humidity, mean_sea_level_pressure, mean_wind_speed, wind_direction, sunshine, visibility, cloud_height, cloud_amount, locations

def get_individual_times(dates):
    '''
    Takes in every date recorded in the CSV and returns a list for each associated day, month, year and season.
    Also returns a list ontaining individual days, months, years and seasons (eg seasons contains 1 instance of 'spring', 1 of 'summer' etc)
    These lists are used for nested loops and cross referencing.
    Parameters:
    -------------
    dates - list - Every entry in the dates column of the input csv

    Returns:
    -------------
    days               - list - List of every day extracted from the dates list
    months             - list - List of every month extracted from the dates list
    years              - list - List of every year extracted from the dates list
    seasons            - list - List of every season from the dates list, calculated by checking the month
    individual_days    - list - Every individual day in the dates list (eg 0 - 31)
    individual_months  - list - Every individual month in the dates list (eg 'jan' - 'dec')
    individual_years   - list - Every individual year in the dates list (eg 1990 - 2020)
    individual_seasons - list - Every individual season in the dates list (eg 'spring' = 'winter')
    '''
    # Contains every instance of day (in format dd), month (as 3 letter abbreviations), years (format yyyy) and seasons (full spelling - 'spring', 'summer', 'autumn', 'winter')
    days = []
    months = []
    years = []
    seasons = []

    # Contains each unique variable, eg only one occurance of 'mon' in individual_months
    individual_days = []
    individual_months = []
    individual_years = []
    individual_seasons = []

    for date in dates:
        # Date written in format 'dd-mon-yyyy hh:mm', eg '01-jan-1990 00:00', so string indexes separate them into variables
        day, month, year = date[:2], date[3:6].lower(), date[7:11]

        # Categorises by season
        if month == 'dec' or month == 'jan' or month == 'feb':
            season = 'winter'
        elif month == 'mar' or month == 'apr' or month == 'may':
            season = 'spring'
        elif month == 'jun' or month == 'jul' or month == 'aug':
            season = 'summer'
        elif month == 'sep' or month == 'oct' or month == 'nov':
            season = 'autumn'

        days.append(day)
        months.append(month) 
        years.append(year)
        seasons.append(season)

        # Adds unique values only
        if day not in individual_days:
            individual_days.append(day)
        if month not in individual_months:
            individual_months.append(month)
        if year not in individual_years:
            individual_years.append(year)
        if season not in individual_seasons:
            individual_seasons.append(season)

    return days, months, seasons, years, individual_days, individual_months, individual_seasons, individual_years
