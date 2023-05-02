#!/bin/sh

echo "${BOLD}Please enter the filename to pull${NONE}"
echo "\n"
read filename

adb pull /sdcard/DCIM/$filename.mp4