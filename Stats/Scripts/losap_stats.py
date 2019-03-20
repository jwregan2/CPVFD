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

year_ar =[2018]
# year_ar = [2013,2014,2015,2016,2017,2018]
mo_ar = [1,2,3,4,5,6,7,8,9,10,11,12]


##DATA LOCATIONS##

output_location='../Monthly_Stats/'

member_names=pd.read_csv('../csv_files/CPVFD_Members.csv', encoding = "ISO-8859-1")
member_names=member_names.set_index('ID')

fire_responses=pd.read_csv('../csv_files/Responses_Fire.csv', encoding = "ISO-8859-1")


ambo_responses=pd.read_csv('../csv_files/Responses_Ambo.csv')
##ASSEMBLE STAT ARRAY##
drills = pd.read_csv('../csv_files/Drills.csv')

## BUILD DATAFRAME THAT HAS COLUMNS FOR EACH STAT CATEGORY AND HAS ROWS FOR EACH MEMBER IN MEMBER NAMES
column_headers=['ID', 'LAST NAME', 'FIRST NAME', 'FIRE','EMS','WF','TOTAL','Y RANK','Drill']

N_rows=len(member_names)
N_cols=len(column_headers)
stats_array=pd.DataFrame(np.zeros((N_rows,N_cols)))
stats_array.columns=column_headers
stats_array['ID'] = member_names.index.values
stats_array=stats_array.set_index('ID')
stats_array['LAST NAME']= member_names['LastName']
stats_array['FIRST NAME']= member_names['FirstName']
for year in year_ar:
	for past_mo in mo_ar:
		print(past_mo,year)
		# if year == 2018 and past_mo < 7:
		# 	continue
		# if year == 2019 and past_mo > 7:
		# 	continue


		number_mo_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
		fire_mo_ls = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		fire_mo_ls = pd.Series(fire_mo_ls,index=number_mo_ls)
		text_mo = fire_mo_ls[past_mo]
		text_yr = str(year)[-2:]



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
		# foam_count = 0
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
			if str(df_year) == str(fire_year):
				fire_count=fire_count+1
				yr_count=yr_count+1
				# print(fire_responses['Working Fire'][i])
				if fire_responses['Working Fire'][i]==True:
					wf=wf+1
				

				# if fire_responses['Call Type'][i]=='Structure Fire':
				# 	if fire_responses['Box or Street Assignment'][i]==True:
				# 		print(fire_responses['Location'][i])
				# 		print(fire_responses['Date'][i])
				# 		print(fire_responses['Time Out'][i])
				# 		for unit in units_ls:
				# 			seat_counter=0
				# 			if pd.isnull(fire_responses[unit][i]):
				# 				continue
				# 			for seat in seats_ls:
				# 				if pd.isnull(fire_responses[unit+seat][i]):
				# 					continue
				# 				seat_counter = seat_counter + 1
				# 			print(str(fire_responses[unit][i])+' '+str(seat_counter))
				# 		print()
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

				if fire_responses['Box Area'][i]=='Montgomery County':
					MA=MA+1

				if str(df_month) == str(fire_mo):
					
					for unit in units_ls:
						for seat in seats_ls:
							if pd.isnull(fire_responses[unit+seat][i]):
								continue
							member = int(fire_responses[unit+seat][i])
							if member not in stats_array.index.values:
								continue
							unit_id =fire_responses[unit][i]

							if unit_id =='Cart12':
								# if 'Dr' in unit+seat:
								# 	stats_array.loc[member,'CTD'] = int(stats_array.loc[member,'CTD'] +1)								
								# 	foam_count = foam_count + 1
								# elif 'Off' in unit+seat:
								# 	stats_array.loc[member,'CTO'] = int(stats_array.loc[member,'CTO'] +1)
								# else:
								stats_array.loc[member,'EMS'] = int(stats_array.loc[member,'EMS'] +1)	
							else: 
								stats_array.loc[member,'FIRE'] = int(stats_array.loc[member,'FIRE'] +1)
							if fire_responses['Working Fire'][i]==True:
								stats_array.loc[member,'WF'] = int(stats_array.loc[member,'WF'] +1)
							# stats_array.loc[member,'TOTAL'] = int(stats_array.loc[member,'TOTAL'] +1)

							# if unit_id =='TK12':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'TKD'] = int(stats_array.loc[member,'TKD'] +1)
							# 		trk_count=trk_count+1
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'TKO'] = int(stats_array.loc[member,'TKO'] +1)
							# 	else:
							# 		stats_array.loc[member,'TKB'] = int(stats_array.loc[member,'TKB'] +1)
							# elif unit_id =='HMSU12':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'HMD'] = int(stats_array.loc[member,'HMD'] +1)
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'HMO'] = int(stats_array.loc[member,'HMO'] +1)
							# elif unit_id =='E121':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'END'] = int(stats_array.loc[member,'END'] +1)
							# 		eng_count = eng_count + 1
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'ENO'] = int(stats_array.loc[member,'ENO'] +1)
							# 	else:
							# 		stats_array.loc[member,'ENB'] = int(stats_array.loc[member,'ENB'] +1)
							# elif unit_id =='E122':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'END'] = int(stats_array.loc[member,'END'] +1)
							# 		eng_count = eng_count + 1
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'ENO'] = int(stats_array.loc[member,'ENO'] +1)
							# 	else:
							# 		stats_array.loc[member,'ENB'] = int(stats_array.loc[member,'ENB'] +1)
							# elif unit_id =='F12':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'FMD'] = int(stats_array.loc[member,'FMD'] +1)
							# 		foam_count = foam_count +1
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'FMO'] = int(stats_array.loc[member,'FMO'] +1)
							# 	else:
							# 		stats_array.loc[member,'FMB'] = int(stats_array.loc[member,'FMB'] +1)
							# elif unit_id =='C12':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# 	else:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# elif unit_id =='C12A':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# 	else:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# elif unit_id =='C12B':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# 	else:
							# 		stats_array.loc[member,'CFO'] = int(stats_array.loc[member,'CFO'] +1)
							# elif unit_id =='Stat':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)
							# 	else:
							# 		stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)	
							# elif unit_id =='Cart12':
							# 	if 'Dr' in unit+seat:
							# 		stats_array.loc[member,'CTD'] = int(stats_array.loc[member,'CTD'] +1)								
							# 		foam_count = foam_count + 1
							# 	elif 'Off' in unit+seat:
							# 		stats_array.loc[member,'CTO'] = int(stats_array.loc[member,'CTO'] +1)
							# 	else:
							# 		stats_array.loc[member,'CTB'] = int(stats_array.loc[member,'CTB'] +1)
		# print(stats_array)
		# exit()					
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
				if ambo_responses['Disposition'][i]=='Assist Medics':
					ALS_Counter=ALS_Counter+1
				if ambo_responses['Unit 1'][i]=='PA812':
					ALS_Counter=ALS_Counter+1
				EMS_Counter=EMS_Counter+1
				# for seat in ambo_ls:
				# 	if pd.isnull(ambo_responses[seat][i]):
				# 		continue
				# 	member = int(ambo_responses[seat][i])
				# 	if member not in stats_array.index.values:
				# 		continue
				# 	stats_array.loc[(member),'YR'] = stats_array.loc[(member),'YR'] +1
				if str(df_month) == str(amb_mo):
					# ambo_count = ambo_count + 1
					for seat in ambo_ls:
						if pd.isnull(ambo_responses[seat][i]):
							continue
						member = int(ambo_responses[seat][i])	
						if member not in stats_array.index.values:
							continue
						stats_array.loc[member,'EMS'] = int(stats_array.loc[member,'EMS'] +1)
						# stats_array.loc[member,'TOTAL'] = int(stats_array.loc[member,'TOTAL'] +1)
						# if ambo_responses['Unit 1'][i]=='PA812':
						# 	if 'Dr' in seat:
						# 		stats_array.loc[member,'PAD'] = int(stats_array.loc[member,'PAD'] +1)
						# 	elif 'Off' in seat:
						# 		stats_array.loc[member,'PAO'] = int(stats_array.loc[member,'PAO'] +1)
						# 	else:
						# 		stats_array.loc[member,'PAB'] = int(stats_array.loc[member,'PAB'] +1)
						# else:
						# 	if 'Dr' in seat:
						# 		stats_array.loc[member,'AMD'] = int(stats_array.loc[member,'AMD'] +1)
						# 	elif 'Off' in seat:
						# 		stats_array.loc[member,'AMO'] = int(stats_array.loc[member,'AMO'] +1)
						# 	else:
						# 		stats_array.loc[member,'AMB'] = int(stats_array.loc[member,'AMB'] +1)	
		for i in drills.index.values:
			if pd.isnull(drills['DateConducted'][i]):
				continue
			if '/' in str(drills['DateConducted'][i]):
				df_month = str(drills['DateConducted'][i]).replace('-','/').split('/')[0]
				df_year = drills['DateConducted'][i].replace('-','/').split('/')[-1]
				drill_mo = past_mo
				drill_year = year

			elif '-' in str(drills['DateConducted'][i]):
				drill_year =text_yr
				drill_mo = text_mo
				df_month = str(drills['DateConducted'][i]).split('-')[-2]
				df_year = drills['DateConducted'][i].split('-')[-1]

			if str(df_year) == str(drill_year):
				if str(df_month) == str(drill_mo):
					for attendant in np.linspace(1,50,50):
						atten = 'Attendant'+str(int(attendant))
						if pd.isnull(drills[atten][i]):
							continue
						member = int(drills[atten][i])	
						if member not in stats_array.index.values:
							continue
						stats_array.loc[member,'Drill'] = int(stats_array.loc[member,'Drill'] +1)
	# print('Engine: '+str(eng_count))
	# print('Truck: '+str(trk_count))
	# print('Foam: '+str(foam_count))
	# print('Ambo: '+str(ambo_count))

	print(fire_count)
	print('Working Fire: '+str(wf))
	print('EMS Assist: '+str(ems)) 
	print('Hazmat: '+str(hazmat)) 
	print('Service Call: '+str(service-bells-haz_cond))
	print('Hazardous Condition: '+str(haz_cond))
	print('Bells: '+str(bells)) 
	print('Rescue: '+str(rescue)) 
	print('Good Intent: '+str(s_b-wf)) 
	print('Wildland: '+str(brush)) 
	print('Vehicle Fire: '+str(car)) 
	print('Water Rescue: '+str(water)) 
	print(other)
	print(yr_count)   
	print('MA '+str(MA))
	print(ALS_Counter)
	print(EMS_Counter)					

for i in stats_array.index.values:
	month_stats=pd.to_numeric(stats_array.loc[i,:],errors='coerce')
	month_stats=month_stats.drop(['Y RANK','WF'])
	month_stats= month_stats.dropna()
	stats_array.loc[i,'TOTAL']=month_stats.sum()
	# print()
	if int(month_stats.sum())==0:
		stats_array = stats_array.drop(i,axis=0)
stats_array['Y RANK'] = stats_array['TOTAL'].rank(ascending = False)

stats_array=stats_array.dropna()
if not os.path.exists(output_location):
	os.makedirs(output_location)
stats_array.to_csv(output_location+str(year)+'_stats.csv')
print(stats_array)
print(fire_mo)
# print(ambo_count)



