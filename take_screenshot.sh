#!/bin/sh
pwd=$(pwd)/artefacts
epoch_time=$(date +%s)
filename=$epoch_time
adb shell screencap -p /sdcard/DCIM/$filename.png
adb pull /sdcard/DCIM/$filename.png $pwd/
adb shell rm /sdcard/DCIM/$filename.png
echo "${BOLD}Please enter the filename${NONE}"
read alias
mv $pwd/$filename.png $pwd/$filename_$alias.png
echo "File is in $pwd/$filename_$alias.png"
open $pwd/$filename_$alias.png