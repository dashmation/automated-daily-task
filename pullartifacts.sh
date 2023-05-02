#!/bin/sh


adb devices

adb pull /sdcard/artifacts/*.* .
echo "pulled....."
adb shell rm /sdcard/artifacts/*.*
echo "removed from device....."