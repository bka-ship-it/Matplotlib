import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data=pd.read_csv('covid_data.csv')
data.set_index('OBJECTID')

data=data[['Province_State','Country_Region','Last_Update','Lat','Long','Confirmed','Recovered','Deaths','Active']]
data.colums=('State','Country','Last Update','Lat','Long','Confirmed','Recovered','Deaths','Active')

data['State'].fillna(value='',inplace=True)

import datetime as dt

def ConvertTime(t):
    t=int(t)
    return dt.datetime().fronttimestamp(t)

data=data.dropna(subset=['Last Update'])
data['Last Update']=data['Last Update']/1000
data['Last Update']=data['Last Update'].apply(ConvertTime)
print(data.head)