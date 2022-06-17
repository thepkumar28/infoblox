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
connection = default_infoblox_connection()    

def get_network_container_values(connection, place_to_check: str, network_container: str):
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
    result = connection.get_object(*my_args, **kwargs)
    return result

get_NC_values = get_network_container_values(connection, "networkcontainer", "131.226.192.0/18")

print("Below are the Network Container Values :\n" , get_NC_values)
print(type(get_NC_values))