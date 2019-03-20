
import pandas as pd
import plotly
from plotly.graph_objs import *
import pickle
import geopy
# import geocoder
from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
from geopy.geocoders import Yandex
from geopy.geocoders import Bing
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


# geolocator = GoogleV3(user_agent="unit_plotter")
# geolocator = Yandex(user_agent="unit_plotter")
geolocator = Nominatim(user_agent="unit_plotter")
# geolocator = Bing(user_agent="unit_plotter")

dict_name = 'unit_locs_preavl.dict'

# ##CHOOSE DATES####
# ##THIS AREA IS FOR SPECIFIC PEIRODS IN WHICH STATS ARE DESIRED. 
manual_dates = True
if manual_dates ==True:
	#Enter Year in XXXX Format
	years=[2014]#,2017,2018]

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

# for i in fire_responses.index.values:
# 	print(fire_responses['Incident Number'][i])
# print(len(fire_responses))
for i in fire_responses.index.values:
	if isnan(fire_responses['Incident Number'][i]):
		fire_responses=fire_responses.drop(i)
	# else:
	# 	fire_responses['Incident Number'][i] = str(int((fire_responses['Incident Number'][i])))
	# 	print(i)

fire_responses['Incident Number']= fire_responses['Incident Number'].astype(int)
# print(len(fire_responses))
fire_responses =fire_responses.set_index('Incident Number')
# fire_responses = fire_responses.index.astype(str)
print(fire_responses.index.values)
# exit()
# unit_dict = pickle.load(open('unit_locs.dict', 'rb'))

unit_groups = ['TK12','E121','E122','HMSU12','F12']

if os.path.isfile('./'+dict_name):
	unit_dict = pickle.load(open(dict_name, 'rb'))
	for unit in unit_groups:
		unit_df = unit_dict[unit]
		new_df = pd.DataFrame(index = fire_responses.index.values,data={'Latitude':np.zeros(len(fire_responses.index.values)),'Longitude':np.zeros(len(fire_responses.index.values)),'Address':np.zeros(len(fire_responses.index.values)),'Box Area':np.zeros(len(fire_responses.index.values)),'Call Type':np.zeros(len(fire_responses.index.values))})
		unit_df = unit_df.combine_first(new_df)
		unit_dict[i] = unit_df
	# print(unit_dict)
	# exit()
else:
	unit_dict ={}
	for unit in unit_groups:
		unit_df = pd.DataFrame(index = fire_responses.index.values,data={'Latitude':np.zeros(len(fire_responses.index.values)),'Longitude':np.zeros(len(fire_responses.index.values)),'Address':np.zeros(len(fire_responses.index.values)),'Box Area':np.zeros(len(fire_responses.index.values)),'Call Type':np.zeros(len(fire_responses.index.values))})
		unit_dict[unit] = unit_df
		# print(unit_df)
		# exit()
# print(fire_responses)

for i in fire_responses.index.values:
	df_month = str(fire_responses['Date'][i]).split('-')[1]
	df_year = str(fire_responses['Date'][i]).split('-')[0]

	if int(df_year) in years:
		print(fire_responses['Date'][i])
		for unit in units_ls:
			if pd.isnull(fire_responses[unit][i]):
				continue
			elif fire_responses[unit][i] not in unit_groups:
				continue
			unit_df = unit_dict[fire_responses[unit][i]]
			try:

				# geolocator = Nominatim(user_agent="specify_your_app_name_here")
				if unit_df['Latitude'][i]==0.0:
					# print(fire_responses['Box Area'][i],type(fire_responses['Box Area'][i]))
					if int(fire_responses['Box Area'][i]) == 12 or int(fire_responses['Box Area'][i]) == 11 or int(fire_responses['Box Area'][i]) == 14:
						city = ' College Park MD'
					elif int(fire_responses['Box Area'][i]) == 34 or int(fire_responses['Box Area'][i]) == 44 or int(fire_responses['Box Area'][i]) == 33 or int(fire_responses['Box Area'][i]) == 30 or int(fire_responses['Box Area'][i]) == 1:
						city =' Hyattsville MD'
					elif int(fire_responses['Box Area'][i]) == 7 or int(fire_responses['Box Area'][i]) == 13:
						city = ' Riverdale MD'
					elif int(fire_responses['Box Area'][i]) == 31 or int(fire_responses['Box Area'][i]) == 41:
						city = ' Beltsville MD'
					elif int(fire_responses['Box Area'][i]) == 35:
						city = ' Greenbelt MD'
					elif int(fire_responses['Box Area'][i]) == 28 or int(fire_responses['Box Area'][i]) == 48:
						city = ' Lanham MD'
					elif int(fire_responses['Box Area'][i]) == 9:
						city =' Bladensburg, MD'
					elif int(fire_responses['Box Area'][i]) ==  55:
						city = ' Brentwood, MD'
					elif fire_responses['Box Area'][i] == 'Montgomery County':
						city = ' Montogomery County MD'
					else:
						city =  " Prince George's County MD"
					
					location = geolocator.geocode(str(fire_responses['Location'][i])+city)

					unit_df['Latitude'][i] = location.latitude
					unit_df['Longitude'][i] = location.longitude
					# unit_df['Latitude'][i],unit_df['Longitude'][i] = geocoder.goodgle(str(fire_responses['Location'][i])+" Prince George's County MD")
					# unit_df['Longitude'][i
					unit_df['Address'][i] = str(fire_responses['Location'][i])
					unit_df['Box Area'][i] = str(fire_responses['Box Area'][i])	
					unit_df['Call Type'][i] = str(fire_responses['Call Type'][i])	
					unit_dict[fire_responses[unit][i]]=unit_df
					print(fire_responses['Location'][i]+city)
					print()

			except:
				print('fail ' + str(fire_responses['Location'][i]))
				continue
print(unit_dict['E122'])
pickle.dump(unit_dict, open (dict_name,'wb'))
