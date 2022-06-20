#! /usr/bin/python3

import os
import sys
import re
import csv
#import logging
#logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector
from infoblox_client import objects

if os.path.exists('UserIntervention.csv') == True:

    def default_infoblox_connection():
        opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
        conn = Connector(opts)
        return conn
    connection = default_infoblox_connection()

    def NetworkContainer_Attribute_PostIntervention(nw=str, comm=str, desc=str):
        ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs', 'unmanaged'])
        

    with open('UserIntervention.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tmp = (dict(row))
            print(tmp)
            #NC = tmp["Network Container"]
            #description_key = ['Description']
            #desc = {k:tmp[k] for k in description_key if k in tmp}
            #NetworkContainer_Attribute_PostIntervention(NC,desc)    

else:
    print("Please run NetworkContainer.py first , then execute this script !!!")    