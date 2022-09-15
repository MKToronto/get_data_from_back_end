shell_name=$(echo $SHELL)
echo "shell_name: ${shell_name}"
# if ! [ "${shell_name}" = "/bin/bash" ]; then

#!/bin/sh
dir=${0%/*}
if [ "$dir" = "$0" ]; then
  dir="."
fi
cd "$dir"
pwd
echo "Changing Permissions to allow the running of Launch_Chrome.command"
chmod u+x Launch_Chrome.command
sudo xattr -rd com.apple.quarantine Launch_Chrome.command
echo "Changing Permissions to allow the running of Launch_Safari.command"
chmod u+x Launch_Safari.command
sudo xattr -rd com.apple.quarantine Launch_Safari.command
echo "Changing Permissions to allow the running of Set_Up_Env.command"
chmod u+x Set_Up_Env.command
sudo xattr -rd com.apple.quarantine Set_Up_Env.command
echo "Changing Permissions to allow the running of fsevents.node"
chmod u+x client/node_modules/fsevents/fsevents.node
sudo xattr -rd com.apple.quarantine client/node_modules/fsevents/fsevents.node

echo "Changing Permissions to allow the running of server.py"
chmod u+x server.py
sudo xattr -rd com.apple.quarantine server.py

echo "Changing Permissions to allow the running of Set_Up_Node.command"
chmod u+x Set_Up_Node.command
sudo xattr -rd com.apple.quarantine Set_Up_Node.command

# chmod u+x Anaconda_Install.command
# chmod u+x Update_Conda.sh




# sudo xattr -rd com.apple.quarantine Set_Up_Env.command
# sudo xattr -rd com.apple.quarantine Set_Up_Env.command
chip=$(uname -p)
echo "${chip}"



str2="$(which conda)"
# str2="$(which notconda)"
echo "${str2}"
if [ "$str2" ]; then
    if [ "$str2" != "conda not found" ]; then
        CONDA_CHECK="true"
        echo "Found Anaconda. Hooray!"
    else
        CONDA_CHECK="false"
        echo "The message returned: anaconda not found"
    fi
else
  CONDA_CHECK="false"
  echo "Anaconda not found"
fi

echo "CONDA_CHECK:${CONDA_CHECK}"
 
if [ "${CONDA_CHECK}" == "true" ]; then
      
    myvariable=$(whoami)
    conda init bash
    source ~/.bash_profile
    conda activate base
    if [ -d "/Users/$myvariable/anaconda3" ]; then

  
        echo "Found Anaconda Path" "/Users/$myvariable/anaconda3"
        echo "Setting Up Enviroment"
        open -a Terminal Set_Up_Env.command

        
        echo "$CONDA_PREFIX"
        # echo "If Anaconda is already installed please type its path eg /Users/firstnamelastname/anaconda3 "
        # read anaconda_path
        # echo "$anaconda_path"
    elif [ -d "$CONDA_PREFIX" ]; then
    
        echo "Found Anaconda Path" "$CONDA_PREFIX"
        echo "Setting Up Enviroment"

        open -a Terminal Set_Up_Env.command
    else
        echo "Anaconda Path Not Found"
        echo "Anaconda Installation Needed. Might take a few minutes"
        var=$(pwd)
        # if  [ "${chip}" == 'arm' ]; then

        #     echo "installing: ""$var/Anaconda3-2022.05-MacOSX-arm64.sh"
        #     bash "$var/Anaconda3-2022.05-MacOSX-arm64.sh"
            
        # elif [ "${chip}" != 'arm' ]; then

          
        
        
        curl -O https://repo.anaconda.com/archive/Anaconda3-2022.05-MacOSX-x86_64.sh
        hash_answer="$(shasum -a 256 Anaconda3-2022.05-MacOSX-x86_64.sh)"
        substring="1a10c06660ebe1204e538b4e9d810142441af9dfd74b077eee2761ec6e675f39" 
        if [[ "$hash_answer" == *"$substring"* ]]; then
            echo "It's there."
            echo "installing: ""$var/Anaconda3-2022.05-MacOSX-x86_64.sh"
            bash "$var/Anaconda3-2022.05-MacOSX-x86_64.sh"
            echo "Setting Up Enviroment"
            open -a Terminal Set_Up_Env.command 
        else
            echo "It didn't download correctly"
        fi
           
        # fi
        
        # source ~/.bash_profile
        # conda init bash
        # source ~/.bash_profile
        # conda update conda
        # conda update anaconda
        # conda env create --file fastapi.yml -n fastapi --force 
    
    fi
else
    echo "Anaconda Path Not Found"
    echo "Anaconda Installation Needed. Might take a few minutes"
    var=$(pwd)
    curl -O https://repo.anaconda.com/archive/Anaconda3-2022.05-MacOSX-x86_64.sh
    hash_answer="$(shasum -a 256 Anaconda3-2022.05-MacOSX-x86_64.sh)"
    substring="1a10c06660ebe1204e538b4e9d810142441af9dfd74b077eee2761ec6e675f39" 
    if [[ "$hash_answer" == *"$substring"* ]]; then
        echo "It's there."
        echo "installing: ""$var/Anaconda3-2022.05-MacOSX-x86_64.sh"
        bash "$var/Anaconda3-2022.05-MacOSX-x86_64.sh"
        echo "Setting Up Enviroment"
        open -a Terminal Set_Up_Env.command 
    else
        echo "It didn't download correctly"
    fi 
fi
echo "Please Close Terminal Window"
