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

def get_network_values(connection, place_to_check: str, network: str):
    my_args = [
        place_to_check,
        {
            'network': network
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

connection = default_infoblox_connection()

get_Network_values = get_network_values(connection, "network", "131.226.217.128/27")

print("Below are the Network Values :\n" , get_Network_values)

print(type(get_Network_values))