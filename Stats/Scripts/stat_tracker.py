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
# for y in [2013,2014,2015,2016,2017,2018,2019]:
# 	for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
	# ##CHOOSE DATES####
	# ##THIS AREA IS FOR SPECIFIC PEIRODS IN WHICH STATS ARE DESIRED. 
manual_dates = True
# print(i)
if manual_dates ==True:
	#Enter Year in XXXX Format
	year=2019

	
	#Enter Month in XX 
	past_mo=3

	# Period_St=''
	# Period_End=''
else:
	date = time.strftime('%m/%Y')

	# print(type(date))
	current_mo = int(date[:2])
	past_mo = int(current_mo - 1)
	year = (date[-4:])

number_mo_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
fire_mo_ls = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fire_mo_ls = pd.Series(fire_mo_ls,index=number_mo_ls)
text_mo = fire_mo_ls[past_mo]
text_yr = str(year)[-2:]

##DATA LOCATIONS##

output_location='../Monthly_Stats/'

member_names=pd.read_csv('../csv_files/CPVFD_Members.csv', encoding = "ISO-8859-1")
member_names=member_names.set_index('ID')

fire_responses=pd.read_csv('../csv_files/Responses_Fire.csv', encoding = "ISO-8859-1")


ambo_responses=pd.read_csv('../csv_files/Responses_Ambo.csv', encoding = "ISO-8859-1")
##ASSEMBLE STAT ARRAY##

## BUILD DATAFRAME THAT HAS COLUMNS FOR EACH STAT CATEGORY AND HAS ROWS FOR EACH MEMBER IN MEMBER NAMES
column_headers=['ID', 'LAST NAME', 'FIRST NAME', 'TKD', 'TKO', 'TKB', 'END', 'ENO', 'ENB', 'FMD', 'FMO', 'FMB', 'HMD', 'HMO', 'CTD', 'CTO', 'CTB', 'AMD', 'AMO', 'AMB', 'PAD', 'PAO', 'PAB', 'STAT', 'CFO','MON', 'YR', 'M RANK', 'Y RANK','MO %']

N_rows=len(member_names)
N_cols=len(column_headers)


# exit()
stats_array=pd.DataFrame(np.zeros((N_rows,N_cols)))

stats_array.columns=column_headers
stats_array['ID'] = member_names.index.values
stats_array=stats_array.set_index('ID')
stats_array['LAST NAME']= member_names['LastName']
stats_array['FIRST NAME']= member_names['FirstName']

units_ls = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5']
seats_ls = [' Dr ID',' Off ID',' FF1 ID',' FF2 ID',' FF3 ID',' FF4 ID',' FF5 ID',' FF6 ID',' FF7 ID']
#Loop through fire dataframe and assign stats to each person on a call
wf=0
ems = 0
hazmat =0
service =0
rescue =0
s_b =0
brush =0
car =0
water =0
haz_cond=0
bells=0
other = 0
MA=0
yr_count = 0
eng_count = 0
trk_count = 0
ambo_count = 0
foam_count = 0
fire_count = 0
for i in fire_responses.index.values:
	# print(fire_responses['Date'][i])
	if '/' in str(fire_responses['Date'][i]):
		df_month = str(fire_responses['Date'][i]).replace('-','/').split('/')[0]
		df_year = fire_responses['Date'][i].replace('-','/').split('/')[-1]
		fire_mo = past_mo
		fire_year = year

	elif '-' in str(fire_responses['Date'][i]):
		fire_year = text_yr
		fire_mo = text_mo
		df_month = str(fire_responses['Date'][i]).split('-')[-2]
		df_year = fire_responses['Date'][i].split('-')[-1]
	# df_month = fire_responses['Date'][i].split('-')[-2]
	# df_year = fire_responses['Date'][i].split('-')[-1]
	# boolean = True
	# if boolean == True:
	if str(df_year) == str(fire_year):
		yr_count=yr_count+1
		# print(fire_responses['Working Fire'][i])
		if fire_responses['Working Fire'][i]==True:
			wf=wf+1
		
		if fire_responses['Call Type'][i]=='EMS Assists':
			ems = ems + 1
		elif fire_responses['Call Type'][i]=='Hazmat / Hazardous Condition':
			hazmat = hazmat + 1
		elif fire_responses['Call Type'][i]=='Non-Emergency Incidents':
			service = service + 1
		elif fire_responses['Call Type'][i]=='Rescues':
			rescue = rescue + 1
		elif fire_responses['Call Type'][i]=='Structure Fire':
			s_b = s_b + 1
		elif fire_responses['Call Type'][i]=='Vegetation Fire':
			brush = brush + 1
		elif fire_responses['Call Type'][i]=='Vehicle Fire':
			car = car + 1
		elif fire_responses['Call Type'][i]=='Water Incidents':
			water = water + 1
		elif fire_responses['Call Type'][i]=='Other Emergency':
			other = other + 1

		if fire_responses['Unit 1 Disposition'][i]== 'Investigation - Malfunctioning Alarm':
			bells=bells+1
		# elif fire_responses['Unit 1 Disposition'][i]== 'Investigation - Nothing Found':
		# 	bells=bells+1
		if fire_responses['Box Area'][i]=='Montgomery County':
			MA=MA+1





		for unit in units_ls:
			for seat in seats_ls:
				if pd.isnull(fire_responses[unit+seat][i]):
					continue
				member = int(fire_responses[unit+seat][i])
				if member not in stats_array.index.values:
					continue

				stats_array.loc[(member),'YR'] = int(stats_array.loc[(member),'YR'] +1)
				# if member == 23927:  
				# 	print(stats_array.loc[(member),'YR'] )

		# if boolean == True:
		if str(df_month) == str(fire_mo):
			fire_count=fire_count+1
			for unit in units_ls:
				for seat in seats_ls:
					if pd.isnull(fire_responses[unit+seat][i]):
						continue
					member = int(fire_responses[unit+seat][i])
					if member not in stats_array.index.values:
						continue
					unit_id =fire_responses[unit][i]
					

					if unit_id =='TK12' or unit_id == 'Reserve Truck':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'TKD'] = int(stats_array.loc[member,'TKD'] +1)
							trk_count=trk_count+1
						elif 'Off' in unit+seat:
							stats_array.loc[member,'TKO'] = int(stats_array.loc[member,'TKO'] +1)
						else:
							stats_array.loc[member,'TKB'] = int(stats_array.loc[member,'TKB'] +1)
					# elif unit_id =='HMSU12':
					# 	if 'Dr' in unit+seat:
					# 		stats_array.loc[member,'HMD'] = int(stats_array.loc[member,'HMD'] +1)
					# 	elif 'Off' in unit+seat:
					# 		stats_array.loc[member,'HMO'] = int(stats_array.loc[member,'HMO'] +1)
					elif unit_id =='E121':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'END'] = int(stats_array.loc[member,'END'] +1)
							eng_count = eng_count + 1
						elif 'Off' in unit+seat:
							stats_array.loc[member,'ENO'] = int(stats_array.loc[member,'ENO'] +1)
						else:
							stats_array.loc[member,'ENB'] = int(stats_array.loc[member,'ENB'] +1)
					elif unit_id =='E122':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'END'] = int(stats_array.loc[member,'END'] +1)
							eng_count = eng_count + 1
						elif 'Off' in unit+seat:
							stats_array.loc[member,'ENO'] = int(stats_array.loc[member,'ENO'] +1)
						else:
							stats_array.loc[member,'ENB'] = int(stats_array.loc[member,'ENB'] +1)
					elif unit_id =='F12':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'FMD'] = int(stats_array.loc[member,'FMD'] +1)
							foam_count = foam_count +1
						elif 'Off' in unit+seat:
							stats_array.loc[member,'FMO'] = int(stats_array.loc[member,'FMO'] +1)
						else:
							stats_array.loc[member,'FMB'] = int(stats_array.loc[member,'FMB'] +1)
					elif unit_id =='C12':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
						else:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
					elif unit_id =='C12A':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
						else:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
					elif unit_id =='C12B':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
						else:
							stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
					elif unit_id =='Stat':
						# print(member)
						# print(fire_responses[:][i])
						if 'Dr' in unit+seat:
							stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)
						else:
							stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)	
					elif unit_id =='Cart12':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'CTD'] = int(stats_array.loc[member,'CTD'] +1)								
							foam_count = foam_count + 1
						elif 'Off' in unit+seat:
							stats_array.loc[member,'CTO'] = int(stats_array.loc[member,'CTO'] +1)
						else:
							stats_array.loc[member,'CTB'] = int(stats_array.loc[member,'CTB'] +1)					
ambo_ls =['Unit 1 Dr ID','Unit 1 Off ID','Unit 1 FF1 ID','Unit 1 FF2 ID']
EMS_Counter=0
ALS_Counter=0
for i in ambo_responses.index.values:
	if pd.isnull(ambo_responses['Date'][i]):
		continue
	if '/' in str(ambo_responses['Date'][i]):
		df_month = str(ambo_responses['Date'][i]).replace('-','/').split('/')[0]
		df_year = ambo_responses['Date'][i].replace('-','/').split('/')[-1]
		amb_mo = past_mo
		amb_year = year

	elif '-' in str(ambo_responses['Date'][i]):
		amb_year =text_yr
		amb_mo = text_mo
		df_month = str(ambo_responses['Date'][i]).split('-')[-2]
		df_year = ambo_responses['Date'][i].split('-')[-1]

	if str(df_year) == str(amb_year):
		yr_count=yr_count+1
		if ambo_responses['Disposition'][i]=='Assist Medics':
			ALS_Counter=ALS_Counter+1
		if ambo_responses['Unit 1'][i]=='PA812':
			ALS_Counter=ALS_Counter+1
		EMS_Counter=EMS_Counter+1
		for seat in ambo_ls:
			if pd.isnull(ambo_responses[seat][i]):
				continue
			member = int(ambo_responses[seat][i])
			if member not in stats_array.index.values:
				continue
			stats_array.loc[(member),'YR'] = stats_array.loc[(member),'YR'] +1
		if str(df_month) == str(amb_mo):
			ambo_count = ambo_count + 1
			for seat in ambo_ls:
				if pd.isnull(ambo_responses[seat][i]):
					continue
				member = int(ambo_responses[seat][i])	
				if member not in stats_array.index.values:
					continue
				if ambo_responses['Unit 1'][i]=='PA812':
					if 'Dr' in seat:
						stats_array.loc[member,'PAD'] = int(stats_array.loc[member,'PAD'] +1)
					elif 'Off' in seat:
						stats_array.loc[member,'PAO'] = int(stats_array.loc[member,'PAO'] +1)
					else:
						stats_array.loc[member,'PAB'] = int(stats_array.loc[member,'PAB'] +1)
				else:
					if 'Dr' in seat:
						stats_array.loc[member,'AMD'] = int(stats_array.loc[member,'AMD'] +1)
					elif 'Off' in seat:
						stats_array.loc[member,'AMO'] = int(stats_array.loc[member,'AMO'] +1)
					else:
						stats_array.loc[member,'AMB'] = int(stats_array.loc[member,'AMB'] +1)						
call_total = ambo_count + fire_count

for i in stats_array.index.values:
	month_stats=pd.to_numeric(stats_array.loc[i,:],errors='coerce')
	month_stats=month_stats.drop(['MON','YR','M RANK','Y RANK'])
	month_stats= month_stats.dropna()
	stats_array.loc[i,'MON']=month_stats.sum()
	stats_array.loc[i,'MO %'] = 100*np.round((stats_array.loc[i,'MON']/call_total),2)
	# print()
	if int(month_stats.sum())==0:
		stats_array = stats_array.drop(i,axis=0)
stats_array['M RANK'] = stats_array['MON'].rank(ascending = False)
stats_array['Y RANK'] = stats_array['YR'].rank(ascending = False)
# print(stats_array)
print(wf)
output_loc_fin = output_location+str(year)+'/'
if not os.path.exists(output_loc_fin):
	os.makedirs(output_loc_fin)
stats_array.to_excel(output_loc_fin+str(fire_mo)+'_'+str(year)+'.xlsx')
# print(fire_mo)
print('ambo: '+str(ambo_count))
print('fire: '+str(fire_count))

# print('Engine: '+str(eng_count))
# print('Truck: '+str(trk_count))
# print('Foam: '+str(foam_count))
# print('Ambo: '+str(ambo_count))


# print('Working Fire: '+str(wf))
# print('EMS Assist: '+str(ems)) 
# print('Hazmat: '+str(hazmat)) 
# print('Service Call: '+str(service-bells-haz_cond))
# print('Hazardous Condition: '+str(haz_cond))
# print('Bells: '+str(bells)) 
# print('Rescue: '+str(rescue)) 
# print('Good Intent: '+str(s_b-wf)) 
# print('Wildland: '+str(brush)) 
# print('Vehicle Fire: '+str(car)) 
# print('Water Rescue: '+str(water)) 
# print(other)
# print(yr_count)
# print('MA '+str(MA))
# print(ALS_Counter)
# print(EMS_Counter)