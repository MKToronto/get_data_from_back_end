#!/bin/sh
dir=${0%/*}
if [ "$dir" = "$0" ]; then
  dir="."
fi
cd "$dir"
pwd
# myvariable=$(whoami)
# source /Users/$myvariable/anaconda3/bin/activate base
# echo "$CONDA_PREFIX"
# source activate base

# source ~/.bash_profile
echo "Initialising Conda"
conda init bash
# source ~/.bash_profile
echo "Updating Conda"
conda update conda
echo "Updating Anaconda"
conda update anaconda
echo "Creating FastAPI Environment"
conda env create --file fastapi.yml -n fastapi --force 

echo "Setting Up Node"
open -a Terminal Set_Up_Node.command

echo "Set Up Finished" 
echo "Please Close Terminal Window"