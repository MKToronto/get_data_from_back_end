#!/bin/sh
dir=${0%/*}
if [ "$dir" = "$0" ]; then
  dir="."
fi
cd "$dir"
pwd

echo "Initialising Conda"
conda init bash
source ~/.bash_profile
conda env list
conda activate fastapi
conda info

cd client
pwd
npm install && npm run build 

echo "Set Up Finished" 
echo "Please Close All Terminal Windows"