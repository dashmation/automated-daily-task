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

echo "${RED}Please enter the filename to trim${NONE}"
ls
read filename

echo "${RED}Please enter initial time to trim in HH:MM:SS format${NONE}"
read initial

echo "${YELLOW}Please enter final time to trim in HH:MM:SS format${NONE}"
read final

ffmpeg -i $filename -ss $initial -to $final -c:v copy -c:a copy trimmed_"$filename"

echo 'file trimmed'