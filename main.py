# ref:https://github.com/Goncalo-Chambel/Dashboard-Example/blob/main/Files/main.py
# importing library
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import datetime as dt
from  dateutil.relativedelta import relativedelta
import matplotlib.dates as mdates
import numpy as np 

# returning mean dataframe
def relate_data(data, key_variable, value_variable):
    keys = data[key_variable]
    values = data[value_variable]

    info = {}
    aux = {} #to hold all the values to compute means
    for key, value in zip(key,value):
        if key in info:
            aux[key].append(value)
            info[key][0] = np.mean(aux[key])
        else:
            info[key] = [[]]
            aux[key] = []
    
    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.rename(columns={0:value_variable})

    return df 


def get_distribution(data, column_name):
    values = data[column_name].to_list()

    distribution = {}
    total = 0

    for value in values:
        total = total + 1
        if value not in distribution:
            distribution[value] = 1
        else:
            distribution[value] = distribution[value] + 1

    for key in distribution:
        distribution[key] = distribution[key] / total

    return distribution

def get_signups(data, start, end):
    dates = []
    delta = relativedelta(end, start)
    nr_months = delta.months + delta.years * 12
    current_date = start

    for i in range(nr_months):
        dates.append(current_date) 
        current_date = current_date + relativedelta(months=1)

    count  = np.zeros_like(dates, dtype=int)
    for date_str in data:
        date = dt.datetime.strptime(date_str, '%y-%m-%d')
        for i in range(len(dates)):
            if date.month == dates[i].month and date.year == dates[i].year:
                count[i] = count[i] + 1

    return dates, count


    data = pd.read_csv('data.csv')
    