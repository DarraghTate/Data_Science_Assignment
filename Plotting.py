# Dublin Airport Weather Data Science Assignment by A00288436

from matplotlib import pyplot as plt

def print_line_plot(data): 
    '''
    Plots the data parameter to a line plot.
    If a dictionary, plots the values against the keys.
    If a list, plots the list items
    Allows user to save plot as a .png file
    Parameters:
    -------------
    data        - list/dict - the data of which the function has to plot
    Returns:
    -------------
    Nothing
    '''
    fig, ax = plt.subplots 
    if isinstance(data, dict):
        data_values = data.values()
        ax.plot(data_values)
        plt.show()
        return    
    ax.plot(data)
    plt.show()
    while True:
        req_save = input("Would you like to save this file? y/n").lower()
        if req_save == 'y':
            file_name = input("Input the file name")
            extension_name = file_name + ".png"
            fig.savefig(extension_name, bbox_inches="tight")
            print('file ' + extension_name + " saved!" )
            break
        elif req_save =='n':
            return
        else:
            print("Not a valid input")
            continue

def print_line_chart(data, title, type_in, units):
    '''
    Plots the data parameter to a line plot.
    If a dictionary, plots the values against the keys.
    If a list, plots the list items
    Allows user to save plot as a .png file
    Parameters:
    -------------
    data        - list/dict - the data of which the function has to plot
    title       - string    - the month being analysed
    type_in     - string    - the parameter being analysed (eg 'temperature')
    units       - string    - the units type_in is measured in (eg temperature would be "degrees")
    Returns:
    -------------
    Nothing
    '''
    fig, ax = plt.subplots()
    years = list(data.keys())
    ax.set_title("Annual " + title.title() + " " +  type_in)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total " + type_in + " in " + units)
    plt.xticks(range(0, 31), years, rotation=90)
    ax.plot(list(data.values()))
    plt.show()
    while True:
        req_save = input("Would you like to save this file? y/n : ").lower()
        if req_save == 'y':
            file_name = input("Input the file name (no file type extension)\n>: ")
            extension_name = file_name + ".png"
            fig.savefig(extension_name, bbox_inches="tight")
            print('file ' + extension_name + " saved!" )
            break
        elif req_save =='n':
            return
        else:
            print("Not a valid input")
            continue

    

def print_pie_chart(data, title,type_in, units):
    '''
    Plots the data parameter to a pie chart.
    Plots the values against the keys.
    Allows user to save plot as a .png file
    Parameters:
    -------------
    data        - list/dict - the data of which the function has to plot
    title       - string    - the month being analysed
    type_in     - string    - the parameter being analysed (eg 'temperature')
    units       - string    - the units type_in is measured in (eg temperature would be "degrees")
    Returns:
    -------------
    Nothing
    '''
    fig, ax = plt.subplots()
    ax.set_title("Annual " + title.title() + " " +  type_in)
    ax.pie(data.values(), labels = data.keys())
    plt.show()
    while True:
        req_save = input("Would you like to save this file? y/n : ").lower()
        if req_save == 'y':
            file_name = input("Input the file name (no file type extension)\n>: ")
            extension_name = file_name + ".png"
            fig.savefig(extension_name, bbox_inches="tight")
            print('file ' + extension_name + " saved!" )
            break
        elif req_save =='n':
            return
        else:
            print("Not a valid input")
            continue

def print_bar_chart(data, title, type_in, units):
    '''
    Plots the data parameter to a bar chart.
    Plots the values against the keys.
    Allows user to save plot as a .png file
    Parameters:
    -------------
    data        - list/dict - the data of which the function has to plot
    title       - string    - the month being analysed
    type_in     - string    - the parameter being analysed (eg 'temperature')
    units       - string    - the units type_in is measured in (eg temperature would be "degrees")
    Returns:
    -------------
    Nothing
    '''
    fig, ax = plt.subplots()
    ax.set_title("Annual " + title.title() + " " +  type_in)
    y_pos = [i for i in range (len(data))]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.keys())
    ax.set_xlabel("Total " + type_in + " in " + units)
    ax.set_ylabel("Year")
    ax.barh(y_pos,data.values(), align="center")
    plt.show()
    while True:
        req_save = input("Would you like to save this file? y/n : ").lower()
        if req_save == 'y':
            file_name = input("Input the file name (no file type extension)\n>: ")
            extension_name = file_name + ".png"
            fig.savefig(extension_name, bbox_inches="tight")
            print('file ' + extension_name + " saved!" )
            break
        elif req_save =='n':
            return
        else:
            print("Not a valid input")
            continue

def print_scatter_plot(data, title, type_in, units):
    '''
    Plots the data parameter to a scatter plot.
    Plots the values against the keys.
    Allows user to save plot as a .png file
    Parameters:
    -------------
    data        - list/dict - the data of which the function has to plot
    title       - string    - the month being analysed
    type_in     - string    - the parameter being analysed (eg 'temperature')
    units       - string    - the units type_in is measured in (eg temperature would be "degrees")
    Returns:
    -------------
    Nothing
    '''
    fig, ax = plt.subplots()
    ax.set_title("Annual " + title.title() + " " +  type_in)
    y_pos = [i for i in range (len(data))]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.keys())
    ax.set_xlabel("Total "+ type_in + " in " + units )
    ax.set_ylabel("Year")
    ax.scatter(data.values(), y_pos)
    plt.show()
    while True:
        req_save = input("Would you like to save this file? y/n : ").lower()
        if req_save == 'y':
            file_name = input("Input the file name (no file type extension)\n>: ")
            extension_name = file_name + ".png"
            fig.savefig(extension_name, bbox_inches="tight")
            print('file ' + extension_name + " saved!" )
            break
        elif req_save =='n':
            return
        else:
            print("Not a valid input")
            continue