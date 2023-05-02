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


echo "${BOLD}Please enter the filename${NONE}"
ls
read filename
echo "\n"

# echo "${BOLD}Enter the keyword to search${NONE}"
# read keyword
# echo "\n"

beginning_of_crash=$(grep -ci 'Beginning of crash' $filename)

fatal_exception=$(grep -ci 'FATAL EXCEPTION' $filename)

echo "${BOLD}Beginning Of Crashes${NONE}	":$beginning_of_crash
echo "${BOLD}FATAL EXCEPTION${NONE}		":$fatal_exception

beginning_dump=$(grep -niA15 'Beginning of crash' $filename | awk 'NR==17 {print " "} {print $0}')

# IFS="--------- beginning of crash" read -a myarray <<< $beginning_dump
# echo "${myarray[1]}"

html_body="<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 2px solid black;
}
</style>
</head>
<body>
<h2>Crashes</h2>
<table style="width:20%">
  <tr>
    <th>Crash Type</th>
    <th>Total</th> 
  </tr>
  <tr>
    <td>Beginning Of Crashes</td>
    <td>$beginning_of_crash</td>
  </tr>
  <tr>
    <td>FATAL EXCEPTION</td>
    <td>$fatal_exception</td>
  </tr>
</table>

<table style="width:100%">
	<tr>
	<td colspan="2">$beginning_dump</th>
	<tr>
</table>

</body>
</html>"

echo $html_body > temp.html
open temp.html
