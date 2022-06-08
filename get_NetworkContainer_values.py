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

def get_network_container_values(nw=str):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    comment = ib_network_container.comment
    tmp = str(ib_network_container.extattrs)
    EA_NC = tmp.strip("EAs:")
    #using strip() and split()  methods
    EA_dict_NC = dict((a.strip(), b.strip())  
                     for a, b in (element.split('=')  
                                  for element in EA_NC.split(',')))
    return EA_dict_NC , comment

converted_NetworkContainer_data = get_network_container_values('131.226.192.0/18')
print('Network Container Values :\n', converted_NetworkContainer_data)