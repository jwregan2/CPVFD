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

# ##CHOOSE DATES####
# ##THIS AREA IS FOR SPECIFIC PEIRODS IN WHICH STATS ARE DESIRED. 
manual_dates = True
if manual_dates ==True:
	#Enter Year in XXXX Format
	year=2016

	#Enter Month in XX 
	past_mo=7

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
fire_mo_s = pd.Series(fire_mo_ls,index=number_mo_ls)
fire_mo = fire_mo_s[past_mo]
fire_yr = str(year)[-2:]

##DATA LOCATIONS##

output_location='../Monthly_Stats/'

member_names=pd.read_csv('../csv_files/CPVFD_Members.csv')
member_names=member_names.set_index('ID')

fire_responses=pd.read_csv('../csv_files/Responses_Fire.csv')


ambo_responses=pd.read_csv('../csv_files/Responses_Ambo.csv')
##ASSEMBLE STAT ARRAY##

## BUILD DATAFRAME THAT HAS COLUMNS FOR EACH STAT CATEGORY AND HAS ROWS FOR EACH MEMBER IN MEMBER NAMES
column_headers=['ID', 'LAST NAME', 'FIRST NAME', 'TKD', 'TKO', 'TKB', 'END', 'ENO', 'ENB', 'FMD', 'FMO', 'FMB', 'HMD', 'HMO', 'CTD', 'CTO', 'CTB', 'AMD', 'AMO', 'AMB', 'PAD', 'PAO', 'PAB', 'STAT', 'CFO','MON', 'YR', 'M RANK', 'Y RANK']

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
for i in fire_responses.index.values:
	df_month = fire_responses['Date'][i].split('-')[-2]
	df_year = fire_responses['Date'][i].split('-')[-1]

	if str(df_year) == str(fire_yr):
		for unit in units_ls:
			for seat in seats_ls:
				if pd.isnull(fire_responses[unit+seat][i]):
					continue
				member = int(fire_responses[unit+seat][i])
				if member not in stats_array.index.values:
					continue
				stats_array.loc[(member),'YR'] = int(stats_array.loc[(member),'YR'] +1)
		if str(df_month) == str(fire_mo):
			for unit in units_ls:
				for seat in seats_ls:
					if pd.isnull(fire_responses[unit+seat][i]):
						continue
					member = int(fire_responses[unit+seat][i])
					if member not in stats_array.index.values:
						continue
					unit_id =fire_responses[unit][i]

					if unit_id =='TK12':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'TKD'] = int(stats_array.loc[member,'TKD'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'TKO'] = int(stats_array.loc[member,'TKO'] +1)
						else:
							stats_array.loc[member,'TKB'] = int(stats_array.loc[member,'TKB'] +1)
					elif unit_id =='HMSU12':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'HMD'] = int(stats_array.loc[member,'HMD'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'HMO'] = int(stats_array.loc[member,'HMO'] +1)
					elif unit_id =='E121':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'END'] = int(stats_array.loc[member,'END'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'ENO'] = int(stats_array.loc[member,'ENO'] +1)
						else:
							stats_array.loc[member,'ENB'] = int(stats_array.loc[member,'ENB'] +1)
					elif unit_id =='E122':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'END'] = int(stats_array.loc[member,'END'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'ENO'] = int(stats_array.loc[member,'ENO'] +1)
						else:
							stats_array.loc[member,'ENB'] = int(stats_array.loc[member,'ENB'] +1)
					elif unit_id =='F12':
						if 'Dr' in unit+seat:
							stats_array.loc[member,'FMD'] = int(stats_array.loc[member,'FMD'] +1)
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
						if 'Dr' in unit+seat:
							stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)
						elif 'Off' in unit+seat:
							stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)
						else:
							stats_array.loc[member,'STAT'] = int(stats_array.loc[member,'STAT'] +1)						
ambo_ls =['Unit 1 Dr ID','Unit 1 Off ID','Unit 1 FF1 ID','Unit 1 FF2 ID']
for i in ambo_responses.index.values:
	if pd.isnull(ambo_responses['Date'][i]):
		continue
	df_month = str(ambo_responses['Date'][i]).split('/')[0]
	df_year = ambo_responses['Date'][i].split('/')[-1]
	if str(df_year) == str(year):
		for seat in ambo_ls:
			if pd.isnull(ambo_responses[seat][i]):
				continue
			member = int(ambo_responses[seat][i])
			if member not in stats_array.index.values:
				continue
			stats_array.loc[(member),'YR'] = stats_array.loc[(member),'YR'] +1
		if str(df_month) == str(past_mo):
			for seat in ambo_ls:
				if pd.isnull(ambo_responses[seat][i]):
					continue
				if member not in stats_array.index.values:
					continue
				member = int(ambo_responses[seat][i])
				if 'Dr' in seat:
					stats_array.loc[member,'AMD'] = int(stats_array.loc[member,'AMD'] +1)
				elif 'Off' in seat:
					stats_array.loc[member,'AMO'] = int(stats_array.loc[member,'AMO'] +1)
				else:
					stats_array.loc[member,'AMB'] = int(stats_array.loc[member,'AMB'] +1)		

for i in stats_array.index.values:
	month_stats=pd.to_numeric(stats_array.loc[i,:],errors='coerce')
	month_stats=month_stats.drop(['MON','YR','M RANK','Y RANK'])
	month_stats= month_stats.dropna()
	stats_array.loc[i,'MON']=month_stats.sum()
	# print()
	if int(month_stats.sum())==0:
		print(i)
		stats_array = stats_array.drop(i,axis=0)
stats_array['M RANK'] = stats_array['MON'].rank(ascending = False)
stats_array['Y RANK'] = stats_array['YR'].rank(ascending = False)
print(stats_array)
if not os.path.exists(output_location):
	os.makedirs(output_location)
stats_array.to_csv(output_location+str(fire_mo)+'_'+str(year)+'.csv')

