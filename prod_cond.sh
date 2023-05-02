#!/bin/sh

NONE='\033[00m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'

clear
echo "${BOLD}Execution started${NONE}"
echo "\n"

echo "${BOLD}Please enter the mspid${NONE}"
read mspid
echo "\n"
echo "${UNDERLINE}${BOLD}do you want to download the source${NONE}? y/n"
read flag_source
echo "\n"
echo "${UNDERLINE}${BOLD}do you want to download the 1080p${NONE}? y/n"
read flag_1080
echo "\n"
echo "${UNDERLINE}${BOLD}do you want to download the 720p${NONE}? y/n"
read flag_720
echo "\n"
echo "${UNDERLINE}${BOLD}do you want to download the 480p${NONE}? y/n"
read flag_480
echo "\n"

rm -rf /${mspid:?}
mkdir $mspid
echo "$mspid directory_created!"
echo "\n"
cd $mspid

if [ "$flag_source" = "y" ]
then
	echo "<<<<<<<<<<<<<<<<<<<<<<<< source_ts processing started >>>>>>>>>>>>>>>>>>>>>>>>>>>"
	mkdir source_ts
	aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/airtelgaming/$mspid/$mspid ./source_ts/ --quiet
	cat ./source_ts/*.ts > ./source_ts/source.ts
	ffmpeg -i ./source_ts/source.ts -acodec copy -vcodec copy source.mp4 -loglevel quiet
	echo "\n"
fi

if [ "$flag_1080" = "y" ]
then
	echo "<<<<<<<<<<<<<<<<<<<<<<<< 1080_ts processing started >>>>>>>>>>>>>>>>>>>>>>>>>>>"
	mkdir 1080_ts
	aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/airtelgaming/$mspid/"$mspid"_1080p ./1080_ts/ --quiet
	cat ./1080_ts/*.ts > ./1080_ts/1080.ts
	ffmpeg -i ./1080_ts/1080.ts -acodec copy -vcodec copy 1080.mp4 -loglevel quiet
	echo "\n"
fi
	
if [ "$flag_720" = "y" ]
then
	echo "<<<<<<<<<<<<<<<<<<<<<<<< 720_ts processing started >>>>>>>>>>>>>>>>>>>>>>>>>>>"
	mkdir 720_ts
	aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/airtelgaming/$mspid/"$mspid"_720p ./720_ts/ --quiet
	cat ./720_ts/*.ts > ./720_ts/720.ts
	ffmpeg -i ./720_ts/720.ts -acodec copy -vcodec copy 720.mp4 -loglevel quiet
	echo "\n"
fi
	
if [ "$flag_480" = "y" ]
then
	echo "<<<<<<<<<<<<<<<<<<<<<<<< 480_ts processing started >>>>>>>>>>>>>>>>>>>>>>>>>>>"
	mkdir 480_ts
	aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/airtelgaming/$mspid/"$mspid"_480p ./480_ts/ --quiet
	cat ./480_ts/*.ts > ./480_ts/480.ts
	ffmpeg -i ./480_ts/480.ts -acodec copy -vcodec copy 480.mp4 -loglevel quiet
	echo "\n"
fi

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ${BOLD}FINAL OUTPUT${NONE} @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

if [ "$flag_source" = "y" ]
then
	echo ""
	echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${PURPLE}source_result${NONE} *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
	ffmpeg -i source.mp4 -hide_banner
fi

if [ "$flag_1080" = "y" ]
then
	echo ""
	echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${CYAN}1080_result${NONE} *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
	ffmpeg -i 1080.mp4 -hide_banner
fi

if [ "$flag_720" = "y" ]
then
	echo ""
	echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${RED}720_result${NONE} *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
	ffmpeg -i 720.mp4 -hide_banner
fi

if [ "$flag_480" = "y" ]
then
	echo ""
	echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${YELLOW}480_result${NONE} *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
	ffmpeg -i 480.mp4 -hide_banner
fi

echo ""
ls -lh *.mp4


	


echo ""
echo ""
echo "${UNDERLINE}${BOLD}do you want to remove the entire directory${NONE}? y/n"
read remove_dir
if [ "$remove_dir" = "y" ]
then
	cd ..
	rm -r $mspid
	echo "directory removed!"
else
	open .
fi