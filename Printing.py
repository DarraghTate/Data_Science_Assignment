# Dublin Airport Weather Data Science Assignment by A00288436

def print_data(data, data_type, units):
    '''
    Prints out the contents of a given data set.
    If a list, it prints out each item in the list.
    If a dict, prints out the data and keys in the format "Average {data type} in {dict key}: {dict value} {units}
    Parameters:
    -------------
    data        - list/dict - the data of which the function has to find the min or max
    data_type   - string - Represents the type of data being analysed (eg "temperature", "wind speed")
    units       - string - Represents the measurement unit for data_type (eg "temperature" is "degrees)
    Returns:
    -------------
    Nothing
    '''
    if isinstance(data, dict):
        for key, value in data.items():
            print (f"Average {data_type.title()} in {key}: {value:.2f} {units}")
    else:
        for value in data:
            print(value)