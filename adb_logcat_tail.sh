#!/bin/sh

pwd=~./logs
epoch_time=$(date +%s)
file_name=logcat_$epoch_time.txt
echo "Open $pwd/$file_name"
adb logcat -v time > $pwd/$file_name

