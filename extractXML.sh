#!/bin/sh
echo 'Enter the filename to be generated'
read filename
adb shell uiautomator dump /sdcard/DCIM/temp.xml
adb pull /sdcard/DCIM/temp.xml ./xmlFiles/
adb shell rm /sdcard/DCIM/temp.xml

mv ./xmlfiles/temp.xml ./xmlfiles/"$filename".xml
