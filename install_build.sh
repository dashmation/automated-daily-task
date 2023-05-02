#!/bin/sh

echo "${BOLD}Please enter the filename${NONE}"
ls
echo "\n"
read filename

status=$(adb install $filename)
sleep 20s
if [ $status == "Success"  ]
then
	adb shell pm clear com.airtel.tv
fi

