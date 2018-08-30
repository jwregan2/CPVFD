
import pandas as pd
import plotly
from plotly.graph_objs import *
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


geolocator = GoogleV3(user_agent="unit_plotter")
mapbox_access_token='pk.eyJ1IjoiandyZWdhbjIiLCJhIjoiY2psODQwdW1lMGJuMDNrbWswMnY3aWpvbSJ9.EX8PvswZCvOAKiqKviw3TA'



# ##CHOOSE DATES####
# ##THIS AREA IS FOR SPECIFIC PEIRODS IN WHICH STATS ARE DESIRED. 
manual_dates = True
if manual_dates ==True:
	#Enter Year in XXXX Format
	year=2018

	#Enter Month in XX 
	past_mo=8

	# Period_St=''
	# Period_End=''
else:
	date = time.strftime('%m/%Y')
	current_mo = int(date[:2])
	past_mo = int(current_mo - 1)
	year = (date[-4:])
  
conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/39912/Documents/GitHub/CPFD/CPVFD/Stats/2013_IRS.accdb;')
cur = conn.cursor()

fire_responses = pd.read_sql_query("select * from  Responses_Fire;", conn)
ambo_responses = pd.read_sql_query("select * from  Responses_Ambo;", conn)
member_names = pd.read_sql_query("select * from  CPVFD_members;", conn)
member_names = member_names.set_index('ID')
output_location='../Monthly_Stats/'

units_ls = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5']

#Loop through fire dataframe and assign stats to each person on a call

print(geolocator.geocode("8115 Baltimore Ave College Park MD"))
unit_dict ={}
unit_groups = ['TK12','E121','E122','HMSU12','F12']
colors = cycle(['g','r','r','b','y'])
for unit in unit_groups:

	df = pd.DataFrame(data={'Incident Index':fire_responses.index.values,'Latitude':np.zeros(len(fire_responses.index.values)),'Longitude':np.zeros(len(fire_responses.index.values))})
	
	df = df.set_index('Incident Index')
	unit_dict[unit]=df
# exit()
# for group in unit_groups
for i in fire_responses.index.values:
	df_month = str(fire_responses['Date'][i]).split('-')[1]
	df_year = str(fire_responses['Date'][i]).split('-')[0]

	if str(df_year) == str(year):
		print(fire_responses['Date'][i])
		for unit in units_ls:
			if pd.isnull(fire_responses[unit][i]):
				continue
			elif fire_responses[unit][i] not in unit_groups:
				continue
			unit_df = unit_dict[fire_responses[unit][i]]
			try:

				# geolocator = Nominatim(user_agent="specify_your_app_name_here")
				location = geolocator.geocode(str(fire_responses['Location'][i])+" Prince George's County MD")
				# print(fire_responses['Location'][i])
				unit_df['Latitude'][i] = location.latitude
				unit_df['Longitude'][i] = location.longitude
				# print(location.latitude,location.longitude)
				unit_dict[fire_responses[unit][i]]=unit_df
				# print('worked')
			except:
				print(fire_responses['Location'][i])
				continue

pickle.dump(unit_dict, open ('unit_locs.dict','wb'))
fig=plt.figure()
ax1 = plt.gca()
for unit in unit_dict:
	unit_df = unit_dict[unit]
	if unit == 'E121' or unit =='E122':
		color='r'
	elif unit =='TK12':
		color='g'
	elif unit =='HMSU12':
		color='y'
	elif unit =='F12':-
		color='g'
	ax1.scatter(unit_df['Longitude'],unit_df['Latitude'], marker='s',label=unit,color=color)
ax1.scatter(geolocator.geocode("8115 Baltimore Ave College Park MD").longitude,geolocator.geocode("8115 Baltimore Ave College Park MD").latitude,color='k')# ax2.plot(data_df['Total Energy (kJ)'].index.values,data_df['Total Energy (kJ)'].rolling(window=5, center=True).mean(),ls='-', marker='o',markevery = 50,markersize=8,mew=1.5,mec='none',ms=7,label='Total Energy (kJ)',color='b')
plt.grid(True)
# plt.xlabel('Time (s)', fontsize = 16)
# ax1.set_ylabel('Layer Height ft',fontsize = 16)
# # ax2.set_ylabel('Total Energy (kJ)',fontsize = 16)
# fig.set_size_inches(fig_width, fig_ht)
plt.xlim([-77.028611,-76.757386])				
plt.ylim([38.892317,39.099375])
# # plt.title('Experiment '+str(experiment)+' '+chart, y=1.08)
plt.tight_layout()	
handles1, labels1 = ax1.get_legend_handles_labels()	
plt.legend(handles1, labels1,   fontsize=12, handlelength=1)	
plt.savefig('../runs_map.pdf')
plt.close('all')

