#!/bin/sh

NONE='\033[00m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'

clear

echo "${RED}do you want to record video or capture image${NONE}? v/i"
read input_action

echo "${RED}Please give an alias${NONE}"
read alias

if [ "$input_action" = "v" ]
then
	while [ ]
	adb shell screenrecord /sdcard/"$alias".mp4
	echo "${PURPLE}video captured${NONE}"
	adb pull /sdcard/"$alias".mp4 .
	echo "${CYAN}video pulled${NONE}"
	adb shell rm /sdcard/"$alias".mp4
	echo "${YELLOW}video removed from the device${NONE}"
	echo "\n"
elif [ "$input_action" = "v" ]
then
	adb shell screencap /sdcard/"$alias".png
	echo "${PURPLE}screenshot captured${NONE}"
	adb pull /sdcard/"$alias".png .
	echo "${CYAN}screenshot pulled${NONE}"
	adb shell rm /sdcard/"$alias".mp4
	echo "${YELLOW}screenshot removed from the device${NONE}"
	echo "\n"
fi
	