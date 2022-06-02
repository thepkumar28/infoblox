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
    with open('backup_Network_data.csv', 'a') as f:
        f.write(str(ib_network) + '\n')
    return ib_network

backup_Network_data('131.226.217.128/27')
print("Backedup Network data")

def backup_NetworkContainer_data(nw=str):
    ib_network_container = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    with open('backup_NetworkContainer_data.csv', 'a') as f:
        f.write(str(ib_network_container) + '\n')
    return ib_network_container

backup_NetworkContainer_data('131.226.217.128/27')
print("Backedup NetworkContainet data")