import os
import subprocess
import signal
import time
from datetime import datetime
import sys
import pandas as pd
from tabulate import tabulate


APPLICATION_LOAD_TIME = {'ATTEMPTS':[],'SCENARIO':[], 'TIME_TAKEN':[],'AVERAGE':[]}

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

def findLogCatEventTime(eventname):
    os.system('rm temp.txt')
    event_time = 0
    logcat = subprocess.Popen('adb logcat -v threadtime > temp.txt',stdout=subprocess.PIPE,
                   shell=True, start_new_session=True)
    event_name = "'"+eventname+"'"
    for retry in range(1,51):
        time.sleep(1)
        temp_str = os.popen("grep -i "+event_name+" temp.txt").readlines()
        if len(temp_str) == 1 and event_name in temp_str[-1]:
            break;
    print("Process ID:", logcat.pid)
    os.killpg(os.getpgid(logcat.pid),signal.SIGTERM)
    print('logcat completed')

    event=os.popen("grep -i "+event_name+" temp.txt")

    event_time=''
	
    try:
        event_time=event.readlines()[-1][6:18]
    except:
         print('Unable to perform event.readlines')
                
    return event_time

def launchAPP(appname):
    if appname == 'netflix':
        os.system('adb shell am start -n com.netflix.ninja/com.netflix.ninja.MainActivity')
    elif appname == 'hotstar':
        os.system('adb shell am start -n in.startv.hotstar/com.hotstar.MainActivity')
    elif appname == 'amazonprime':
        os.system('adb shell am start -n com.amazon.amazonvideo.livingroom/com.amazon.ignition.IgnitionActivity')
    elif appname == 'xstream':
        os.system('adb shell am start -n com.netflix.ninja/com.netflix.ninja.MainActivity')


total_iterations = sys.argv[1]

def checkLoadTime(iterations,appPackage,appname,firstEvent,finalEvent):
    os.system('adb shell am force-stop '+appPackage)
    sum = 0
    for counter in range(1,iterations):
        try:
            launchAPP(appname)
            initial_time = findLogCatEventTime(firstEvent)
            final_time = findLogCatEventTime(finalEvent)
            sum = sum + timeDifference(initial_time,final_time)
            os.system('adb shell am force-stop '+appPackage)
            APPLICATION_LOAD_TIME['ATTEMPTS'].append(counter)
            APPLICATION_LOAD_TIME['SCENARIO'].append(appname)
            APPLICATION_LOAD_TIME['TIME_TAKEN'].append(timeDifference(initial_time,final_time))
            if counter == iterations-1:
                APPLICATION_LOAD_TIME['AVERAGE'].append(sum / counter)
            else:
                APPLICATION_LOAD_TIME['AVERAGE'].append('')
        except:
            os.system('adb shell am force-stop '+appPackage)


def main():
    n = int(total_iterations) + 1
    checkLoadTime(n,
                'com.netflix.ninja',
                'netflix',
                'Start app: App(Netflix',
                'AvrcpMediaPlayerList: onActiveSessionsChanged: controller: com.netflix.ninja')
    
    checkLoadTime(n,
                'in.startv.hotstar',
                'hotstar',
                'Fully drawn in.startv.hotstar',
                'AvrcpMediaPlayerList: Name of package changed: in.startv.hotstar')
    
    checkLoadTime(n,
                'com.amazon.amazonvideo.livingroom',
                'amazonprime',
                'addSplashScreen com.amazon.amazonvideo.livingroom',
                'Displayed com.amazon.amazonvideo.livingroom')

    print(APPLICATION_LOAD_TIME)

    df = pd.DataFrame(APPLICATION_LOAD_TIME)
    # df.to_csv('APPLICATION_LOAD_TIME.csv', index = False, encoding='utf-8')
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == '__main__':
    main()