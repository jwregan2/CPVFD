
import pandas as pd
import plotly
plotly.tools.set_credentials_file(username='jwregan2', api_key='ZoUzJtQ49CTCXc5wae0q')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import pickle
import geopy
from geopy.geocoders import GoogleV3
import pyodbc
import pandas_access as mdb
import os as os
import numpy as np 
from pylab import * 
import datetime
import shutil
from dateutil.relativedelta import relativedelta
from scipy.signal import butter, filtfilt
from itertools import cycle
import time

mapbox_access_token='pk.eyJ1IjoiandyZWdhbjIiLCJhIjoiY2psODQwdW1lMGJuMDNrbWswMnY3aWpvbSJ9.EX8PvswZCvOAKiqKviw3TA'
unit_dict = pickle.load(open('unit_locs_preavl.dict', 'rb'))
colors = ['g','r','r','b','y']
geolocator = GoogleV3(user_agent="unit_plotter")

for i in unit_dict:
	print([i])
	unit_df = unit_dict[i]
	for j in unit_df.index.values:
		if int(str(j)[:2]) not in [13,14,15]:
			unit_df =  unit_df.drop(j)
	unit_dict[i] = unit_df
data_split = []
for i in unit_dict:
	if i == 9080:
		continue
	df_sub = unit_dict[i]
	# print(len())
	df_sub['Text'] = 'Unit: ' + i+'<br>Address: '+(df_sub['Address'].astype(str))  + '<br>Call Type: ' + df_sub['Call Type'].astype(str) + '<br>Box Area: ' + df_sub['Box Area'].astype(str)#+ '"></a>'
	print(i)
	df_sub = df_sub[df_sub.Latitude != 0]
	
	if i == 'E121' or i =='E122':
		c ="rgb(242, 23, 23)"
	elif i =='TK12':
		c ="rgb(31, 104, 23)"
	elif i =='HMSU12':
		c ="rgb(224, 242, 66)"
	elif i =='F12':
		c ="rgb(66, 230, 242)"



	data = go.Scattermapbox(
	        lat=list(df_sub['Latitude']),
	        lon=list(df_sub['Longitude']),
	        mode='markers',
	        text = df_sub['Text'],
	        marker=dict(
	            symbol='circle',
	            size=8,
	            color = c ,
	        ),
	        name = i
	    )
	
	data_split.append(data)


layout = Layout(
    title = '2018 Fire Responses',
    autosize=True,
    showlegend = True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38.9904301,
            lon=-76.9337422
        ),
        pitch=0,
        zoom=11
    ),
)
fig = dict(data=data_split, layout=layout )
plotly.offline.plot( fig,  filename='preavl_fire_responses_all.html' )
# plotly.offline.plot( fig, validate=False, filename='2018_fire_responses.html' )

# fig=plt.figure()
# ax1 = plt.gca()
# for unit in unit_dict:
# 	unit_df = unit_dict[unit]
# 	if unit == 'E121' or unit =='E122':
# 		color='r'
# 	elif unit =='TK12':
# 		color='g'
# 	elif unit =='HMSU12':
# 		color='y'
# 	elif unit =='F12':
# 		color='g'
# 	ax1.scatter(unit_df['Longitude'],unit_df['Latitude'], marker='s',label=unit,color=color)
# ax1.scatter(geolocator.geocode("8115 Baltimore Ave College Park MD").longitude,geolocator.geocode("8115 Baltimore Ave College Park MD").latitude,color='k')# ax2.plot(data_df['Total Energy (kJ)'].index.values,data_df['Total Energy (kJ)'].rolling(window=5, center=True).mean(),ls='-', marker='o',markevery = 50,markersize=8,mew=1.5,mec='none',ms=7,label='Total Energy (kJ)',color='b')
# plt.grid(True)
# # plt.xlabel('Time (s)', fontsize = 16)
# # ax1.set_ylabel('Layer Height ft',fontsize = 16)
# # # ax2.set_ylabel('Total Energy (kJ)',fontsize = 16)
# # fig.set_size_inches(fig_width, fig_ht)
# plt.xlim([-77.028611,-76.757386])				
# plt.ylim([38.892317,39.099375])
# # # plt.title('Experiment '+str(experiment)+' '+chart, y=1.08)
# plt.tight_layout()	
# handles1, labels1 = ax1.get_legend_handles_labels()	
# plt.legend(handles1, labels1,   fontsize=12, handlelength=1)	
# plt.savefig('../runs_map.pdf')
# plt.close('all')

