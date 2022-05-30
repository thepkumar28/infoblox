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

def populate_ExtensibleAttribute_values(connection, place_to_check: str, network_container: str):
    my_args = [
        place_to_check,
        {
            'network': network_container
        }
    ]
    kwargs = {
        'extattrs+': {
            "Description": {
                "value": "This is my test description"
            }
        }
    }

    result = connection.put_object(*my_args, **kwargs)
    return result

connection = default_infoblox_connection()

populate_EA_values = populate_ExtensibleAttribute_values(connection, "networkcontainer", "131.226.192.0/18")

print("Below are the Network Container Values :\n" , populate_EA_values)