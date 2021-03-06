#! /usr/bin/python3

import sys
import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector
from infoblox_client import objects

def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
    conn = Connector(opts)
    return conn
connection = default_infoblox_connection()

def convert_NetworkContainer_data_to_dict(nw=str):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    comment = ib_network_container.comment
    tmp = str(ib_network_container.extattrs)
    EA_NC = tmp.strip("EAs:")
    #using strip() and split()  methods
    EA_dict_NC = dict((a.strip(), b.strip())  
                     for a, b in (element.split('=')  
                                  for element in EA_NC.split(',')))
    return EA_dict_NC , comment
 
def convert_Network_data_to_dict(nw=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    comment = ib_network.comment
    tmp = str(ib_network.extattrs)
    EA_N = tmp.strip("EAs:")
    #using strip() and split()  methods
    EA_dict_N = dict((a.strip(), b.strip())  
                     for a, b in (element.split('=')  
                                  for element in EA_N.split(',')))
    return EA_dict_N , comment

converted_NetworkContainer_data = convert_NetworkContainer_data_to_dict('131.226.192.0/18') 
converted_Network_data = convert_Network_data_to_dict('131.226.217.128/27')  

print('Network Container Values :\n', converted_NetworkContainer_data)
print("Network Values :\n", converted_Network_data)
