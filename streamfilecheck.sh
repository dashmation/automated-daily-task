#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo "Execution started"
echo "Please enter the mspid"
read mspid

if[ -d "$mspid"]
then
	rm -r $mspid
fi
mkdir $mspid
echo "$mspid directory_created!"
cd $mspid

mkdir source_ts 1080_ts 720_ts 480_ts

echo ""
echo ""
echo "<<<<<<<<<<<<<<<<<<<<<<<< downloading started >>>>>>>>>>>>>>>>>>>>>>>>>"

aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/GAMING/$mspid/$mspid ./source_ts/ --quiet

aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/GAMING/$mspid/"$mspid"_1080p ./1080_ts/ --quiet

aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/GAMING/$mspid/"$mspid"_720p ./720_ts/ --quiet

aws s3 cp --recursive s3://wynk-msp-airtelgaming-vod/livestreaming/GAMING/$mspid/"$mspid"_480p ./480_ts/ --quiet

echo "<<<<<<<<<<<<<<<<<<<<<<<< downloading completed >>>>>>>>>>>>>>>>>>>>>>>>>"


echo ""
echo ""
cat ./source_ts/*.ts > ./source_ts/source.ts
echo "######################## ${YELLOW}source.ts_created ########################"
ffmpeg -i ./source_ts/source.ts -acodec copy -vcodec copy source.mp4 -loglevel quiet
echo "######################## ${YELLOW}source.mp4_created ########################"

echo ""
echo ""
cat ./1080_ts/*.ts > ./1080_ts/1080.ts
echo "######################## ${YELLOW}1080.ts_created ########################"
ffmpeg -i ./1080_ts/1080.ts -acodec copy -vcodec copy 1080.mp4 -loglevel quiet
echo "######################## ${YELLOW}1080.mp4_created ########################"

echo ""
echo ""
cat ./720_ts/*.ts > ./720_ts/720.ts
echo "######################## ${YELLOW}720.ts_created ########################"
ffmpeg -i ./720_ts/720.ts -acodec copy -vcodec copy 720.mp4 -loglevel quiet
echo "######################## ${YELLOW}720.mp4_created########################"

echo ""
echo ""
cat ./480_ts/*.ts > ./480_ts/480.ts
echo "######################## ${YELLOW}480.ts_created ########################"
ffmpeg -i ./480_ts/480.ts -acodec copy -vcodec copy 480.mp4 -loglevel quiet
echo "######################## ${YELLOW}480.mp4_created ########################"

echo ""
echo ""
echo ""
echo ""
echo ""
echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${PURPLE}source_result *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
ffmpeg -i source.mp4 -hide_banner

echo ""
echo ""
echo ""
echo ""
echo ""
echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${GREEN}1080_result *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
ffmpeg -i 1080.mp4 -hide_banner

echo ""
echo ""
echo ""
echo ""
echo ""
echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${RED}720_result *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
ffmpeg -i 720.mp4 -hide_banner


echo ""
echo ""
echo ""
echo ""
echo ""
echo "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* ${YELLOW}480_result *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*"
ffmpeg -i 480.mp4 -hide_banner
