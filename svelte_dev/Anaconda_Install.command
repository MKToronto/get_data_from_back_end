#!/bin/sh
dir=${0%/*}
if [ "$dir" = "$0" ]; then
  dir="."
fi
cd "$dir"
# pwd

var=$(pwd)
echo "installing: ""$var/Anaconda3-2022.05-MacOSX-x86_64.sh"
bash "$var/Anaconda3-2022.05-MacOSX-x86_64.sh" 