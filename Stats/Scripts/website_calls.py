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

year_ar =[2017]
# year_ar = [2013,2014,2015,2016,2017,2018]
mo_ar = [1,2,3,4,5,6,7,8,9,10,11,12]


##DATA LOCATIONS##

output_location='../Monthly_Stats/'

member_names=pd.read_csv('../csv_files/CPVFD_Members.csv', encoding = "ISO-8859-1")
member_names=member_names.set_index('ID')

fire_responses=pd.read_csv('../csv_files/Responses_Fire.csv', encoding = "ISO-8859-1")


ambo_responses=pd.read_csv('../csv_files/Responses_Ambo.csv')
##ASSEMBLE STAT ARRAY##

## BUILD DATAFRAME THAT HAS COLUMNS FOR EACH STAT CATEGORY AND HAS ROWS FOR EACH MEMBER IN MEMBER NAMES
column_headers=['ID', 'LAST NAME', 'FIRST NAME', 'FIRE','EMS','WF','TOTAL','Y RANK']

N_rows=len(member_names)
N_cols=len(column_headers)
stats_array=pd.DataFrame(np.zeros((N_rows,N_cols)))
stats_array.columns=column_headers
stats_array['ID'] = member_names.index.values
stats_array=stats_array.set_index('ID')
stats_array['LAST NAME']= member_names['LastName']
stats_array['FIRST NAME']= member_names['FirstName']
for year in year_ar:
	hazmat_count =0
	yr_count = 0
	eng_count = 0
	trk_count = 0
	ambo_count = 0
	foam_count = 0
	fire_count = 0
	cart_count = 0
	ems_count = 0
	bls_count = 0
	als_count = 0
	# for past_mo in mo_ar:
	print(year)


	# number_mo_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
	# fire_mo_ls = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	# fire_mo_ls = pd.Series(fire_mo_ls,index=number_mo_ls)
	# text_mo = fire_mo_ls[past_mo]
	text_yr = str(year)[-2:]



	units_ls = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5']
	seats_ls = [' Dr ID',' Off ID',' FF1 ID',' FF2 ID',' FF3 ID',' FF4 ID',' FF5 ID',' FF6 ID',' FF7 ID']
	#Loop through fire dataframe and assign stats to each person on a call
	wf=0

	# hazmat_count =0
	# yr_count = 0
	# eng_count = 0
	# trk_count = 0
	# ambo_count = 0
	# foam_count = 0
	# fire_count = 0
	# cart_count = 0

	for i in fire_responses.index.values:
		# print(fire_responses['Date'][i])
		if '/' in str(fire_responses['Date'][i]):
			# df_month = str(fire_responses['Date'][i]).replace('-','/').split('/')[0]
			df_year = fire_responses['Date'][i].replace('-','/').split('/')[-1]
			# fire_mo = past_mo
			fire_year = year

		elif '-' in str(fire_responses['Date'][i]):
			fire_year = text_yr
			# fire_mo = text_mo
			# df_month = str(fire_responses['Date'][i]).split('-')[-2]
			df_year = fire_responses['Date'][i].split('-')[-1]
		# df_month = fire_responses['Date'][i].split('-')[-2]
		# df_year = fire_responses['Date'][i].split('-')[-1]
		if str(df_year) == str(fire_year):
			fire_count=fire_count+1
			yr_count=yr_count+1
			# print(fire_responses['Working Fire'][i])
			if fire_responses['Working Fire'][i]==True:
				wf=wf+1
			
			for unit in units_ls:
				# for seat in seats_ls:
					if pd.isnull(fire_responses[unit][i]):
						continue
					unit_id =fire_responses[unit][i]

					if unit_id =='Cart12':
						cart_count =cart_count + 1
					elif unit_id =='HMSU12':
						hazmat_count = hazmat_count + 1
					elif unit_id =='E121':
						eng_count = eng_count + 1
					elif unit_id =='E122':
						eng_count = eng_count + 1
					elif unit_id =='F12':
						foam_count = foam_count + 1
					elif unit_id =='TK12':
						trk_count = trk_count +1
					elif unit_id =='Cart12':
						cart_count = cart_count + 1
	ems_count = 0
	bls_count = 0
	als_count = 0
	for i in ambo_responses.index.values:

		if pd.isnull(ambo_responses['Date'][i]):
			continue
		if '/' in str(ambo_responses['Date'][i]):
			# df_month = str(ambo_responses['Date'][i]).replace('-','/').split('/')[0]
			df_year = ambo_responses['Date'][i].replace('-','/').split('/')[-1]
			# amb_mo = past_mo
			amb_year = year

		elif '-' in str(ambo_responses['Date'][i]):
			amb_year =text_yr
			# amb_mo = text_mo
			# df_month = str(ambo_responses['Date'][i]).split('-')[-2]
			df_year = ambo_responses['Date'][i].split('-')[-1]

		if str(df_year) == str(amb_year):
			ems_count = ems_count +1
			yr_count = yr_count+1
			if ambo_responses['Unit 1'][i]=='PA812':
				als_count = als_count + 1
			else:
				bls_count = bls_count + 1
	print('wf')
	print(wf)
	print()

	print('hazmat')
	print(hazmat_count)
	print()

	print('year')
	print(yr_count)
	print()

	print('engine')
	print(eng_count)
	print()

	print('truck')
	print(trk_count)
	print()

	print('ambo')
	print(bls_count)
	print()

	print('foam')
	print(foam_count)
	print()

	print('suppression')
	print(fire_count)
	print()

	print('cart')
	print(cart_count)
	print()
	
	print('ems')
	print(ems_count)
	print()
	print('BLS')
	print(bls_count)
	print()
	print('als')
	print(als_count)
	print()

# elif unit_id =='C12':
# elif unit_id =='C12A':
# elif unit_id =='C12B':
# elif unit_id =='Stat':
