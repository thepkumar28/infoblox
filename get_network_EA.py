#! /usr/bin/python3

import sys

import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector


def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
    conn = Connector(opts)
    return conn

def get_network_EA(connection, place_to_check: str, network_container: str):
    my_args = [
        place_to_check,
        {
            'network': network_container
        }
    ]
    kwargs = {
        'return_fields': [
            'default',
            'extattrs',
        ]
    }
    #result = {"type": f"{place_to_check}", "objects": connection.get_object(*my_args, **kwargs)}
    result = connection.get_object(*my_args, **kwargs)
    return result

connection = default_infoblox_connection()

get_EA = get_network_EA(connection, "networkcontainer", "10.1.0.0/16")

print("Below is the Extensible Attribute :")
print(get_EA)