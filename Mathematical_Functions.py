# Dublin Airport Weather Data Science Assignment by A00288436

from math import sqrt

def get_mean(input_list):
    '''
    Calculates the mean of a given list
    Parameters:
    -------------
    input_list - list - the list of numbers to find the mean of

    Returns:
    -------------
    Unnamed variable  - float/integer - the mean of the list
    '''
    return sum (input_list) / len (input_list)

def get_mode(input_list):
    '''
    Calculates the mode of a given list or dictionary
    If list, returns the mode
    If dict, returns an object containing the mode of the list values, and it's associated key
    Parameters:
    -------------
    input_list - list/dict - the list of numbers to find the mean of

    Returns:
    -------------
    Unnamed variable  - None - returned if input_list is empty
    mode    - if input_list is list:
                float/integer - the mode of the list
            - if input_list is dict:
                object, containing (key, value), value being the mode
    '''
    if len(input_list) == 0:
            return None

    if isinstance (input_list, dict):
        input_list = input_list.values()
    position_dictionary=  {}
    for x in input_list:
        if x not in position_dictionary:
            position_dictionary[x] = 1
        else:
            position_dictionary[x] +=1
    mode = max(position_dictionary, key = position_dictionary.get)
    return mode

def get_median(input_list):
    '''
    Calculates the median of a given list or dictionary
    If list, returns the median
    If dict, returns an object containing the median of the list values, and it's associated key
    Parameters:
    -------------
    input_list - list/dict - the list of numbers to find the mean of

    Returns:
    -------------
    if input_list is dict:
        return_value - object -  containing (key, value), value being the median
    if input_list is list:
        median_value -float/integer - median value of input_list
    '''
    if isinstance (input_list, dict):   
        return_value = ()
        dict_values = list(input_list.values())
        dict_values = sorted(dict_values)
        if len(dict_values) % 2 != 0:
            midpoint = int((len(dict_values)/2))
            median_value = dict_values[midpoint]
        else:
            midpoint_1 = int((len(dict_values)/2 )- 1)
            midpoint_2 = int((len(dict_values)/2 ))
            median_value = (dict_values[midpoint_1] + dict_values[midpoint_2]) / 2
        for x, y in input_list.items():
            if y == median_value:
                dict_key_value = x
                return_value = (x, median_value)
                return return_value 
    else:
        input_list = sorted(input_list)
        if len(input_list) % 2 != 0:
            midpoint = int((len(input_list)/2))
            median_value = input_list[midpoint]
        else:
            midpoint_1 = int((len(input_list)/2 )- 1)
            midpoint_2 = int((len(input_list)/2 ))
            median_value = (input_list[midpoint_1] + input_list[midpoint_2]) / 2
        return median_value

def get_standard_deviation(input_list):
    '''
    Calculates the standard deviation of a given list or dictionary
    Parameters:
    -------------
    input_list - list/dict - the list of numbers to find the standard deviation of

    Returns:
    -------------
    standard_deviation - float/integer - the standard deviation of the input_list, or of the dictionary values 
    '''

    if isinstance(input_list, dict):
        input_list = input_list.values()
    list_mean = get_mean(input_list)
    deviations = [(x - list_mean) ** 2 for x in input_list]
    standard_deviation = sqrt(sum(deviations)/(len(input_list)-1))
    return standard_deviation