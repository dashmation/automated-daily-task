#!/bin/sh
echo 'Enter Your Location'

echo 'Enter 1 if Connected To DeviceHacked'
echo 'Enter 2 if Connected To ACT-Home'
echo 'Enter 3 if Connected To One Plus Mobile Hotspot'
echo 'Enter 5 if connected to Sercomm-2.4'

read input

adb devices
adb disconnect

if [ "$input" = "1" ]
then
    adb connect 192.168.1.4

elif [ "$input" = "2" ]
then
    adb connect 192.168.0.103

elif [ "$input" = "3" ]
then
    adb connect 192.168.109.146

elif [ "$input" = "4" ]
then
    adb connect 192.168.10.12

elif [ "$input" = "5" ]
then
    adb connect 192.168.0.102
fi
