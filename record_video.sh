#!/bin/sh


echo "${BOLD}Please enter your customized filename${NONE}"
read filename

adb shell screenrecord /sdcard/DCIM/$filename.mp4 &
pid=$(ps aux | grep -i 'adb') &
# &
# adb logcat -v threadtime > adblogs_$filename.txt &

# read -p 'Enter Any character to stop: ' number1
# if [ -z "$number1" ]
# then
#     echo 'Inputs cannot be blank please try again!'
# else
# 	pkill -15 $1
# 	echo "OK"
# fi


adb pull /sdcard/DCIM/$filename.mp4

adb shell rm /sdcard/DCIM/$filename.mp4