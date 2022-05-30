#! /usr/bin/python3

import sys

import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector
from infoblox_client import objects
from infoblox_client import object_manager
from infoblox_client.object_manager import InfobloxObjectManager

def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
    conn = Connector(opts)
    return conn

connection = default_infoblox_connection()
ib_network = objects.Network.search(connection, network='131.226.192.0/18', network_view='default', return_fields=['network', 'extattrs'])
ea = objects.EA({'Description': 'This is my test description'})
ib_network.extattrs = ea
#network.update()
populate_EA_values = InfobloxObjectManager.update_network_options("131.226.192.0/18", ib_network.extattrs)

#print("Below are the Network Container Values :\n" , populate_EA_values)