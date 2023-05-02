#!/bin/sh

echo "Please enter mspid"
read mspid

cd $mspid

echo "Which resolution you want to compare?\nPlease choose from below"
echo "\n1080\n720\n480\n"
read resolution

echo "Do you want to trim? y/n"
read trim_flag

if [ "$trim_flag" = "y" ]
then
	echo "Please enter the end duration in HH:MM:SS format"
	read end_time
	
	ffmpeg -i source.mp4 -ss 00:00:00 -to $end_time -c:v copy -c:a copy original.mp4
	ffmpeg -i "$resolution".mp4 -ss 00:00:00 -to $end_time -c:v copy -c:a copy compressed.mp4
	
	ffmpeg -i compressed.mp4 -i original.mp4 -lavfi libvmaf="model_path='../vmaf_v0.6.1.json'" -f null -
	
	echo "Do you want to remove the files? y/n"
	read remove_files
	if [ "$remove_file" = "y" ]
	then
		rm -r original.mp4
		rm -r compressed.mp4
	fi
else
	ffmpeg -i "$resolution".mp4 -i source.mp4 -lavfi libvmaf="model_path='../vmaf_v0.6.1.json'" -f null -
fi

