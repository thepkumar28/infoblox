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

def get_network_values(nw=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    #comment = ib_network.comment
    #EA_dict_N = ib_network.extattrs.ea_dict
    #tmp = str(ib_network.extattrs)
    #EA_N = tmp.strip("EAs:")
    ##using strip() and split()  methods
    #EA_dict_N = dict((a.strip(), b.strip())  
    #                 for a, b in (element.split('=')  
    #                              for element in EA_N.split(',')))
    #return EA_dict_N , comment
    return ib_network

converted_Network_data = get_network_values('10.114.128.0/18')
print("Network Values :\n", converted_Network_data)