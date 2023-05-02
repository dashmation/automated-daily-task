#!/bin/sh
current_dir=$(pwd)
python_lib_dir=~/Documents/dth/POC/pythonLibrary

# echo $current_dir
# echo $python_lib_dir

echo '#1 ---> RecordVideo'
echo '#2 ---> takeADBLog'
echo '#3 ---> takeADBLogs(filter)'
echo '#4 ---> takeScreenShot'
echo '#5 ---> clearData'
echo '#6 ---> install apk'
echo '#7 ---> Uninstall apk'

read -p "Enter The Action Number To Be Performed: " number

echo $number

if [ $number == 1 ]
then
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.recordVideo()'
	mv ./*.mp4 $current_dir/artefacts/
	
elif [ $number == 2 ]
then
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.takeADBLog()'
	mv ./*.log $current_dir/logs/
 
elif [ $number == 3 ]
then
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.takeADBLogs()'
	mv ./*.log $current_dir/logs/

elif [ $number == 4 ]
then
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.takeScreenShot()'
	mv ./*.png $current_dir/artefacts/
	
elif [ $number == 5 ]
then
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.clearData()'
	
elif [ $number == 6 ]
then
	ls $current_dir/apks/
	read -p "Enter The APK Name To Be Installed: " apk
	apk_file = $current_dir/apks/$apk
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.install('$apk_file')'
	python3 -c 'import ADBAction; ADBAction.clearData()'

elif [ $number == 7 ]
then
	cd $python_lib_dir
	python3 -c 'import ADBAction; ADBAction.uninstall()'
		
else
    echo "Not A Valid Option"
fi
