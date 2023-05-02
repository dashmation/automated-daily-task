#!/bin/sh

echo "${RED}Please give an alias${NONE}"
read alias

adb devices
adb shell mkdir -p /sdcard/artifacts/
adb shell screenrecord /sdcard/artifacts/"$alias".mp4