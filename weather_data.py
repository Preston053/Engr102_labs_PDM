# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Preston Montgomery
# Section:      522
# Assignment:   Lab 11-3
# Date:         11 9 2023

from statistics import*

# Open CSV file for reading
with open('WeatherDataCLL.csv','r+') as w_data:
    sort_list_data = []
    line_data = w_data.read()
    # splits the csv by each line
    list_data = line_data.split('\n')
    # sorts the list into a list of lists with each list containing a day
    for i in list_data:
        sort_list_data.append(i.split(','))
    
    ############
    # MAX TEMP #
    ############

    # list of all the max temperature values aka value [5] in each data
    max_temp_list = []
    # d for date
    for d in sort_list_data:
        # to avoid grabbing the title
        if len(d[5]) > 4:
            continue
        # for empty values
        if d[5] == '':
            continue
        # adds each maximum temp of each date to the max temp list
        else:
            max_temp_list.append(int(d[5]))
    # find the maximum temperature seen over the 10-year period
    print(f'10-year maximum temperature: {max(max_temp_list)} F')

    ############
    # MIN TEMP #
    ############

    # list of all the min temperature values aka value [6] in each data
    min_temp_list = []
    # d for date
    for d in sort_list_data:
        # to avoid grabbing the title
        if len(d[6]) > 4:
            continue
        # for empty values
        if d[6] == '':
            continue
        # adds each min temp of each date to the min temp list
        else:
            min_temp_list.append(int(d[6]))
    # find the minimum temperature seen over the 10-year period
    print(f'10-year minimum temperature: {min(min_temp_list)} F')

    #################
    # DATA ANALYSIS #
    #################

    # Take as input from the user a month and year
    print()
    month_user = str(input('Please enter a month: '))
    year_user = str(input('Please enter a year: '))
    print()
    print(f'For {month_user} {year_user}:')
    # dictionary of all the months and associated values
    month_dict = {"January": "1/", "February": "2/", "March": "3/", "April": "4/", "May": "5/", "June": "6/", "July": "7/", "August": "8/", "September": "9/", "October": "10/", "November": "11/", "December": "12/"}
    values_list = []
    # creates a list of all the data points of the users chosen month and year
    for dp in sort_list_data:
        if (month_dict[month_user] == '10/') or (month_dict[month_user] == '11/') or (month_dict[month_user] == '12/'):
            if month_dict[month_user] in dp[0][:3] and year_user in dp[0][4:]:
                values_list.append(dp)
        else:
            if month_dict[month_user] in dp[0][0:2] and year_user in dp[0][4:]:
                values_list.append(dp)
    
    #################
    # MEAN AVG TEMP #
    #################

    #Calculate mean of the average temperatures (1 decimal place)
    avg_temp_list = []
    a = 0
    for d in values_list:
        # to avoid grabbing the title
        if len(d[4]) > 6:
            continue
        # for empty values
        if d[4] == '':
            avg_temp_list.append(0)
        else:
            avg_temp_list.append(float(d[4]))
    print(f'Mean average daily temperature: {mean(avg_temp_list):.1f} F')

    #####################
    # MEAN REL HUMIDITY #
    #####################

    #Calculate mean relative humidity (1 decimal place)
    rel_humidity_list = []
    for d in values_list:
        # to avoid grabbing the title
        if len(d[3]) > 6:
            continue
        # for empty values
        if d[3] == '':
            continue
        else:
            rel_humidity_list.append(float(d[3]))
    print(f'Mean relative humidity: {mean(rel_humidity_list):.1f} %')

    #########################
    # MEAN DAILY WIND SPEED #
    #########################

    # Calculate mean daily wind speed (2 decimal places)
    wind_speed_list = []
    for d in values_list:
        # to avoid grabbing the title
        if len(d[1]) > 6:
            continue
        # for empty values
        if d[1] == '':
            continue
        else:
            wind_speed_list.append(float(d[1]))
    print(f'Mean daily wind speed: {mean(wind_speed_list):.2f} mph')

    ####################################
    # DAYS WITH NON-ZERO PRECIPITATION #
    ####################################

    # Calculate percentage of days with non-zero precipitation (1 decimal place)
    # days with precip / days total
    days_total = 0
    days_p = 0
    for d in values_list:
        # to avoid grabbing the title
        if len(d[2]) > 6:
            continue
        # for empty values
        if d[2] == '':
            days_total+=1
            continue
        if d[2] == '0':
            days_total+=1
            continue
        else:
            days_total+=1
            days_p+=1
    print(f'Percentage of days with precipitation: {((days_p/days_total)*100):.1f} %')