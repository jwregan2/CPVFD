import pandas as pd 
import os as os
import numpy as np 
import matplotlib.pyplot as plt
from pylab import * 
import datetime
import shutil
from dateutil.relativedelta import relativedelta
from scipy.signal import butter, filtfilt
from itertools import cycle
import time
# for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
# ##CHOOSE DATES####
# ##THIS AREA IS FOR SPECIFIC PEIRODS IN WHICH STATS ARE DESIRED. 
years_ls = [2018,2017,2016,2015,2014,2013 ]



##DATA LOCATIONS##

output_location='../NFRIS_stats/'

member_names=pd.read_csv('../csv_files/CPVFD_Members.csv', encoding = "ISO-8859-1")
member_names=member_names.set_index('ID')

fire_responses=pd.read_csv('../csv_files/Responses_Fire.csv', encoding = "ISO-8859-1")


ambo_responses=pd.read_csv('../csv_files/Responses_Ambo.csv')
##ASSEMBLE STAT ARRAY##

## BUILD DATAFRAME THAT HAS COLUMNS FOR EACH STAT CATEGORY AND HAS ROWS FOR EACH MEMBER IN MEMBER NAMES
column_headers=['Year', 'Vehicle Fire','Brush Fire','Structure Fire','Working Fire','Fire-Good Intent','False Alarm','Fire Rescue','Hazmat','Service','EMS Assist','Severe Weather','Mutual Aid','Auto Aid','Auto Aid Fire','EMS Rescue','BLS Calls', 'ALS Calls','Transport','Fire Standby-EMS','Other EMS','EMS-Good Intent']

N_rows=len(years_ls)
N_cols=len(column_headers)


stats_array=pd.DataFrame(np.zeros((N_rows,N_cols)))

stats_array.columns=column_headers
stats_array['Year'] = years_ls
stats_array=stats_array.set_index('Year')
for year in years_ls:
	text_yr = str(year)[-2:]
	for i in fire_responses.index.values:
		# print(fire_responses['Date'][i])
		if '/' in str(fire_responses['Date'][i]):
			df_year = fire_responses['Date'][i].replace('-','/').split('/')[-1]
			year = year

		elif '-' in str(fire_responses['Date'][i]):
			fire_year = text_yr
			df_year = fire_responses['Date'][i].split('-')[-1]
			df_year='20'+str(df_year)
		if str(df_year) == str(year):
			
			if fire_responses['Working Fire'][i]==True:
				stats_array['Working Fire'][year]=stats_array['Working Fire'][year]+1
			
			if fire_responses['Call Type'][i]=='EMS Assists':
				stats_array['EMS Assist'][year]=stats_array['EMS Assist'][year]+1
			elif fire_responses['Call Type'][i]=='Hazmat / Hazardous Condition':
				stats_array['Hazmat'][year]=stats_array['Hazmat'][year]+1
			elif fire_responses['Call Type'][i]=='Non-Emergency Incidents':
				stats_array['Service'][year]=stats_array['Service'][year]+1
			elif fire_responses['Call Type'][i]=='Rescues':
				stats_array['Fire Rescue'][year]=stats_array['Fire Rescue'][year]+1
			elif fire_responses['Call Type'][i]=='Structure Fire':
				if fire_responses['Unit 1 Disposition'][i]=='Emergency Operations Performed':
					stats_array['Structure Fire'][year]=stats_array['Structure Fire'][year]+1
				else:
					stats_array['Fire-Good Intent'][year]=stats_array['Fire-Good Intent'][year]+1

			elif fire_responses['Call Type'][i]=='Vegetation Fire':
				stats_array['Brush Fire'][year]=stats_array['Brush Fire'][year]+1
			elif fire_responses['Call Type'][i]=='Vehicle Fire':
				stats_array['Vehicle Fire'][year]=stats_array['Vehicle Fire'][year]+1
			elif fire_responses['Call Type'][i]=='Water Incidents':
				stats_array['Severe Weather'][year]=stats_array['Severe Weather'][year]+1
			elif fire_responses['Call Type'][i]=='Other Emergency':
				stats_array['Service'][year]=stats_array['Service'][year]+1
			elif fire_responses['Call Type'][i]=='Automatic Alarms':
				stats_array['Fire-Good Intent'][year]=stats_array['Fire-Good Intent'][year]+1
			if fire_responses['Unit 1 Disposition'][i]== 'Investigation - Malfunctioning Alarm':
				stats_array['False Alarm'][year]=stats_array['False Alarm'][year]+1
			if str(fire_responses['Box Area'][i]) != '12':
				stats_array['Auto Aid'][year]=stats_array['Auto Aid'][year]+1
				if fire_responses['Call Type'][i]=='Structure Fire':
					stats_array['Auto Aid Fire'][year]=stats_array['Auto Aid Fire'][year]+1
			if fire_responses['Box Area'][i]=='Montgomery County':
				stats_array['Mutual Aid'][year]=stats_array['Mutual Aid'][year]+1

	for i in ambo_responses.index.values:
		if pd.isnull(ambo_responses['Date'][i]):
			continue
		if '/' in str(ambo_responses['Date'][i]):
			df_year = ambo_responses['Date'][i].replace('-','/').split('/')[-1]
			amb_year = year

		elif '-' in str(ambo_responses['Date'][i]):
			amb_year =text_yr
			df_year = ambo_responses['Date'][i].split('-')[-1]
			df_year='20'+str(df_year)

		if str(df_year) == str(year):
			if ambo_responses['Disposition'][i]=='Assist Medics':
				stats_array['ALS Calls'][year]=stats_array['ALS Calls'][year]+1
			elif ambo_responses['Unit 1'][i]=='PA812':
				stats_array['ALS Calls'][year]=stats_array['ALS Calls'][year]+1
			else:
				stats_array['BLS Calls'][year]=stats_array['BLS Calls'][year]+1

			if ambo_responses['Disposition'][i]=='Transport':
				stats_array['Transport'][year]=stats_array['Transport'][yeardf]+1
			elif ambo_responses['Disposition'][i]=='Fire Standby':
				stats_array['Fire Standby-EMS'][year]=stats_array['Fire Standby-EMS'][year]+1				
			else:#if ambo_responses['Disposition'][i]=='No Patient':
				stats_array['EMS-Good Intent'][year]=stats_array['EMS-Good Intent'][year]+1			

if not os.path.exists(output_location):
	os.makedirs(output_location)
stats_array.to_csv('../NFIRS.csv')
