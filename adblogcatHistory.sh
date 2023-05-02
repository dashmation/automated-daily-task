#!/bin/sh

pwd=$(pwd)
epoch_time=$(date +%s)
file_name=logcat_$epoch_time.txt
echo "Open $pwd/$file_name"
adb logcat -d time > $pwd/$file_name