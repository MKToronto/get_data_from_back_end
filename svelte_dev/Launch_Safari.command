conda init bash
source ~/.bash_profile
conda activate fastapi
conda info
#!/bin/sh
dir=${0%/*}
if [ "$dir" = "$0" ]; then
  dir="."
fi
cd "$dir"

pwd

python server.py &
cd client
pwd
npm run start &
pwd 
cd ..
pwd

pwd 
echo "starting finishing set up"
sleep 5
echo "getting ready to start 60s left"  
sleep 5
echo "55s left"
sleep 5
echo "50s left"
sleep 5
echo "45s left"
sleep 5
echo "40s left"
sleep 5
echo "35s left"
sleep 5
echo "30s left"
sleep 5
echo "25s left"
sleep 5
echo "20s left"
sleep 5
echo "15s left"
sleep 5
echo "10s left"
sleep 5
echo "5s left"
sleep 5
echo finished waiting
open -a Safari http://127.0.0.1:8000/
echo "started in Safari: http://127.0.0.1:8000/"
wait
