#! /usr/bin/python3

import sys

import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector
from infoblox_client import objects
from infoblox_client import object_manager as obm
from obm import *

def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
    conn = Connector(opts)
    return conn

connection = default_infoblox_connection()
ea = objects.EA({'Description': 'This is my test description'})
populate_EA_values = update_network_options(connection, "131.226.192.0/18", ea)

print("Below are the Network Container Values :\n" , populate_EA_values)