#!/bin/sh

clear
command=$(adb devices)
t="$command"
device_name=${t:34:8}
if [ $device_name="devices" ];
then
	adb tcpip 5555
	command_2=$(adb shell ip addr show wlan0)
	t_2="$command_2"
	device_ip=${t_2:160:14}
	echo "$device_ip"
fi

