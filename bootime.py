import os
import subprocess
import signal
import time
from datetime import datetime
import sqlite3
import pandas as pd
import sys
from tabulate import tabulate
	
#methods
def storeValues(tableName, ATTEMPTS, XTREAM_PAGE, ANDROID_PAGE, ONBOARDING_PAGE, HOME_PAGE):
	con = sqlite3.connect("bootimelog.db")
	con = sqlite3.connect(":memory:")
	cur = con.cursor()
	cur.execute("create table ",tableName,"(XTREAM_PAGE, ANDROID_PAGE, ONBOARDING_PAGE, HOME_PAGE)")
	cur.execute("insert into ",tableName," values (?, ?, ?, ?)", "(",ATTEMPTS, XTREAM_PAGE,ANDROID_PAGE,ONBOARDING_PAGE,HOME_PAGE,")")
	for row in cur.execute("select * from ",tableName):
		print(row)
	con.commit()
	con.close()

def currentTime():
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S.%m", t)
	print(current_time)
	return current_time
	
def currentYear():
	return str(datetime.datetime.now().year)

def getRealTIME(epoch_time):
	date_time = datetime.datetime.fromtimestamp(epoch_time)
	print(date_time)
	return date_time
		
def getEPOCH(date_time):
	pattern = '%Y-%m-%d %H:%M:%S.%f'
	epoch = int(time.mktime(time.strptime(date_time, pattern)))
	print(epoch)
	return epoch
		
def timeDifference(start_time,end_time):
	initial = datetime.strptime(str(start_time), "%H:%M:%S.%f")
	end = datetime.strptime(str(end_time), "%H:%M:%S.%f")
	
	# get difference
	delta = end - initial

	sec = delta.total_seconds()
	# print(sec,' seconds')
	return sec
	
WARM_BOOT = {'ATTEMPTS':[],'XSTREAM_PAGE':[],'ANDROID_PAGE':[],'ONBOARDING_PAGE':[],'HOME_PAGE':[], 'ONBOARDING_TO_HOME_PAGE':[]}

total_iterations = sys.argv[1]
print('running for ',total_iterations,' time(s)')
for i in range(1,int(total_iterations)+1):
	print('')
	print('#################### Iteration ',i, '#######################')
	initial_recorded_time = currentTime()
	print('reboot started')
	os.system('adb reboot')
	print('reboot completed')
	logcat = subprocess.Popen('adb logcat -v threadtime > temp.txt',stdout=subprocess.PIPE,
                   shell=True, start_new_session=True)
	# time.sleep(55)
	for retry in range(1,15):
		# print('retry....',retry)
		time.sleep(4)
		temp_str = os.popen("grep -i 'type=device_boot_complete' temp.txt").readlines()
		# print('ppppppppppp',temp_str)
		# print('*8888888888*',len(temp_str))
		# print(len(temp_str) == 1 and 'type=device_boot_complete' in temp_str[0])
		if len(temp_str) == 1 and 'type=device_boot_complete' in temp_str[0]:
			break
	print("Process ID:", logcat.pid)
	os.killpg(os.getpgid(logcat.pid),signal.SIGTERM)
	print('logcat completed')

	onboarding=os.popen("grep -i 'Vold 3.0 (the awakening) firing up' temp.txt")
	home=os.popen("grep -i 'type=device_boot_complete' temp.txt")

	home_time=''
	try:
		onboarding_time=onboarding.readlines()[0][6:18]
	except:
		print('Unable to perform onboarding.readlines')

	try:
		home_time=home.readlines()[0][6:18]
	except:
		print('Unable to perform home.readlines')

	print(onboarding_time)
	print(home_time)

	try:
		print('Onboarding to Homepage')
		ONBOARDING_TO_HOME = timeDifference(onboarding_time,home_time)
		print(ONBOARDING_TO_HOME)
	except:
		print('Unable to perform timeDifference for onboarding_time and home_time')
		ONBOARDING_TO_HOME='NA'
			
	try:
		print('initial_recorded_time to onboarding_time')
		ONBOARDING_PAGE_TIME = timeDifference(initial_recorded_time, onboarding_time)
		print(ONBOARDING_PAGE_TIME)
	except:
		print('Unable to perform timeDifference for initial_recorded_time and onboarding_time')
		ONBOARDING_PAGE_TIME='NA'

	try:
		print('initial_recorded_time to Homepage')
		HOME_PAGE_TIME = timeDifference(initial_recorded_time, home_time)
		print(HOME_PAGE_TIME)
	except:
		print('Unable to perform timeDifference for initial_recorded_time and home_time')
		HOME_PAGE_TIME='NA'
	try:
		WARM_BOOT['ATTEMPTS'].append(i)
		WARM_BOOT['XSTREAM_PAGE'].append('NA')
		WARM_BOOT['ANDROID_PAGE'].append('NA')
		WARM_BOOT['ONBOARDING_PAGE'].append(ONBOARDING_PAGE_TIME)
		WARM_BOOT['HOME_PAGE'].append(HOME_PAGE_TIME)
		WARM_BOOT['ONBOARDING_TO_HOME_PAGE'].append(ONBOARDING_TO_HOME)

	except:
		print('Unable to Add Values')

print(WARM_BOOT)

df = pd.DataFrame(WARM_BOOT)
# df.to_csv('WARMBOOT.csv', index = False, encoding='utf-8')
print('')
print('')
print('')
print(tabulate(df, headers='keys', tablefmt='psql'))
# os.system('open WARMBOOT.csv')