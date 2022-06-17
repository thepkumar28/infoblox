#! /usr/bin/python3

import os.path

if os.path.exists('backup_NetworkContainer_data.csv') == True:
    print("backup_NetworkContainer_data.csv exists")
else:
    print("backup_NetworkContainer_data.csv doesn't exist")    
