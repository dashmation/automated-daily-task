#!/bin/sh


echo "${RED}Please give an alias${NONE}"
read alias

adb devices

adb shell mkdir -p /sdcard/artifacts/
adb shell screencap /sdcard/artifacts/"$alias".png

adb pull /sdcard/artifacts/"$alias".png .
echo "pulled....."
adb shell rm /sdcard/artifacts/"$alias".png
echo "removed from device....."