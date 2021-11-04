# Data_Science_Assignment
"Seasonal Analysis of Weather Patterns Recorded at Dublin Airport, 1990-2020"

A data science assignment for an Applied Scripting Languages class. Features analysis and visualisation of weather patterns as recorded at Dublin Airport.

To download the repo, enter the command:

    git clone https://github.com/DarraghTate/Data_Science_Assignment_Weather_Analysis.git
    
To execute the program, enter the command:

    python -u Data_Science_Assignment.py

This program requires matplotlib, pandas, and can be rudimentally tested with pytest.

This data, as collected by Met Éireann, contains the hourly observations of the weather station situated at Dublin Airport, collected between 1990 and 2020.  
The station is located at 53.428°N, 6.421°W, and is at an elevation of 71 metres. 
The measurements taken include air temperature, humidity, air pressure, wind speed, wind direction and precipitation.

This data was found on the Met Éireann website (met.ie/climate/available-data/historical-data), with the parameters of 
Data Resolution = Hourly, County = Dublin, Station = Dublin Airport (1939-), and all available parametres selected. 
This data was collected hourly over the course of 30 years, and as such contains 269,545 records. 

The collected data consists of 16 different variables and, as per Met Éireann’s key (which comes via a .TXT file bundled with any downloaded data sets from their website, and it categorised thusly: 
date - Date (format dd-mon-yyyy hh:mm , eg “01-jan-1990 01:00”)
rain - Rain amount in mm
temp -Temperature in Celsius
wetb - Wet Bulb Temperature in Celsius
dewpt -Dew Point Temperature in Celsius
rhum - Relative Humidity as a Percentage
vappr - Vapour Pressure in Heptopascals
msl -Mean Sea Level Pressure in Heptopascals
wdsp - Mean Wind Speed in Knots
wddir - Wind Direction in Degrees
ww - SYNOP code for Present Weather
w - SYNOP code for Past Weather
sun – Sunshine Duration in Hours
vis - Visibility in Metres
clht - Cloud Height (format feet * 100, or 999 if sky is clear, eg 12 means clouds at 1200 feet)
clamt - Cloud Amount (1-10 scale)

All the data is stored as numbers, with the exception of the date, which is a string (due to the date being written as a 3 letter abbreviation, and not in the formats dd/mm/yyyy or yyyy/mm/dd). 
This means that analysis with dates involves string manipulation.

Note that SYNOP codes (Surface Synoptic Observations) are encoded messages that describe the general weather of an area (for example, notes if it is snowing, or a thunderstorm). There are 99 of these codes, and I am opting not to use them as they are specific to a very brief window of time, and I am more interested in analysing the overall trends in temperature, rainfall and wind speed.
