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

def backup_Network_data(nw=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    with open('backup.txt', 'w') as f:
        f.write(str(ib_network) + '\n')
    return ib_network

backedup_Network_data = backup_Network_data('131.226.217.128/27')
print(backedup_Network_data)

#ib_network = objects.Network.search(connection, network='131.226.217.128/27', network_view='default', return_fields=['default', 'extattrs'])
#with open('backup.txt', 'w') as f:
#    f.write(str(ib_network) + '\n')

print(ib_network)
print(type(ib_network))