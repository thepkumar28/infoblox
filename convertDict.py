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

def convert_Network_data_to_dict(nw=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    comment = ib_network.comment
    Ea = ib_network.extattrs
    desc = ib_network.extattrs.Description
    return comment , Ea , desc

converted_data = convert_Network_data_to_dict('131.226.217.128/27')  

print(converted_data)