# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:52:47 2020

@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd

# Database to keep track of health/fitness related records on a daily basis

# Empty dataframe to be updated with health/fitness data
dictionary = {'Date': [] , 'Weight AM': [],'Weight PM': [],'Exercise': [],'Exercise Duration': [],'Exercise Activity': [], '# Alchoholic Drinks': []}
global dataframe
dataframe = pd.DataFrame(data = dictionary, columns = ['Date','Weight AM','Weight PM','Exercise','Exercise Duration','Exercise Activity','# Alchoholic Drinks'] )  


def initialize_health_tracker():
    finished_entering_data = False
    while finished_entering_data == False:
        if finished_entering_data == False:
            date = input('Enter date in the form dd/mm/yyyy: ')
            weight_am = input('Enter morning weight: ')
            weight_pm = input('Enter evening weight: ')
            exercise = input('Enter Y if exercised N otherwise: ')
            exercise_duration = input('Enter amount of time while exercising: ')
            exercise_activity = input('Enter exercise activity: ')
            alchoholic_bevs = input('Enter number of alchoholic beverages consumed: ')
            data = updated_health_data(date,weight_am,weight_pm,exercise,exercise_duration,exercise_activity,alchoholic_bevs)
            return data
        else:
            return True
    

def updated_health_data(date,weight_am,weight_pm,exercise,exercise_duration,exercise_activity,alchoholic_bevs):
    global dataframe
    dataframe = dataframe.append({'Date': date,'Weight AM': weight_am,'Weight PM': weight_pm,'Exercise': exercise,
                                  'Exercise Duration': exercise_duration, 'Exercise Activity':exercise_activity, '# Alchoholic Drinks': alchoholic_bevs},
                                 ignore_index = True)
    return dataframe


initialize_health_tracker()



