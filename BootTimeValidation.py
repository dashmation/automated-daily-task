import os
import subprocess
import signal
import time
from datetime import datetime
import pandas as pd
import sys
import statistics
	
#methods
def currentTime():
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S.%m", t)
	print(current_time)
	return current_time
		
def timeDifference(start_time,end_time):
	initial = datetime.strptime(str(start_time), "%H:%M:%S.%f")
	end = datetime.strptime(str(end_time), "%H:%M:%S.%f")
	# get difference
	delta = end - initial
	sec = delta.total_seconds()
	# print(sec,' seconds')
	return sec

def creatingSubProcess(command):
	result = subprocess.Popen(command,stdout=subprocess.PIPE,
                   shell=True, start_new_session=True)
	print('SubProcess Started')
	print("Process ID:", result.pid)
	return result.pid

def killSubProcess(pid):
	os.killpg(os.getpgid(pid),signal.SIGTERM)
	print('SubProcess Killed')

def calculatingAverage():
	ONBOARDING_PAGE_LIST = WARM_BOOT['ONBOARDING_PAGE']
	HOME_PAGE_LIST = WARM_BOOT['HOME_PAGE']
	ONBOARDING_TO_HOME_PAGE_LIST = WARM_BOOT['ONBOARDING_TO_HOME_PAGE']
	MEAN_LIST=[]
	MEAN_LIST.append(statistics.mean(ONBOARDING_PAGE_LIST))
	MEAN_LIST.append(statistics.mean(HOME_PAGE_LIST))
	MEAN_LIST.append(statistics.mean(ONBOARDING_TO_HOME_PAGE_LIST))
	return MEAN_LIST
	
WARM_BOOT = {'ATTEMPTS':[],'XSTREAM_PAGE':[],'ANDROID_PAGE':[],'ONBOARDING_PAGE':[],'HOME_PAGE':[], 'ONBOARDING_TO_HOME_PAGE':[]}

total_iterations = sys.argv[1]

print('running for ',total_iterations,' time(s)')
for i in range(1,int(total_iterations)+1):
	print('')
	print('#################### Iteration ',i, '#######################')
	initial_recorded_time = currentTime()
	print('rebooting...')
	os.system('adb reboot')
	pid = creatingSubProcess('adb logcat -v threadtime > temp.txt')  
	for retry in range(1,15):
		time.sleep(4)
		temp_str = os.popen("grep -i 'type=device_boot_complete' temp.txt").readlines()
		if len(temp_str) == 1 and 'type=device_boot_complete' in temp_str[0]:
			break
	killSubProcess(pid)
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

	# print(onboarding_time)
	# print(home_time)

	try:
		# print('Onboarding to Homepage')
		ONBOARDING_TO_HOME = timeDifference(onboarding_time,home_time)
		# print(ONBOARDING_TO_HOME)
	except:
		print('Unable to perform timeDifference for onboarding_time and home_time')
		ONBOARDING_TO_HOME='NA'
			
	try:
		# print('initial_recorded_time to onboarding_time')
		ONBOARDING_PAGE_TIME = timeDifference(initial_recorded_time, onboarding_time)
		# print(ONBOARDING_PAGE_TIME)
	except:
		print('Unable to perform timeDifference for initial_recorded_time and onboarding_time')
		ONBOARDING_PAGE_TIME='NA'

	try:
		# print('initial_recorded_time to Homepage')
		HOME_PAGE_TIME = timeDifference(initial_recorded_time, home_time)
		# print(HOME_PAGE_TIME)
	except:
		print('Unable to perform timeDifference for initial_recorded_time and home_time')
		HOME_PAGE_TIME='NA'
	try:
		WARM_BOOT['ATTEMPTS'].append(i)
		WARM_BOOT['XSTREAM_PAGE'].append('na')
		WARM_BOOT['ANDROID_PAGE'].append('na')
		WARM_BOOT['ONBOARDING_PAGE'].append(ONBOARDING_PAGE_TIME)
		WARM_BOOT['HOME_PAGE'].append(HOME_PAGE_TIME)
		WARM_BOOT['ONBOARDING_TO_HOME_PAGE'].append(ONBOARDING_TO_HOME)

	except:
		print('Unable to Add Values')

AVERAGE_LIST = calculatingAverage()
WARM_BOOT['ATTEMPTS'].append('AVERAGE')
WARM_BOOT['XSTREAM_PAGE'].append('')
WARM_BOOT['ANDROID_PAGE'].append('')
WARM_BOOT['ONBOARDING_PAGE'].append(AVERAGE_LIST[0])
WARM_BOOT['HOME_PAGE'].append(AVERAGE_LIST[1])
WARM_BOOT['ONBOARDING_TO_HOME_PAGE'].append(AVERAGE_LIST[2])

print(WARM_BOOT)

df = pd.DataFrame(WARM_BOOT)
df.to_csv('WARMBOOT.csv', index = False, encoding='utf-8')
print('')
print('')
print('')
print(df)
os.system('open WARMBOOT.csv')