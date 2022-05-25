#! /usr/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector


def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': 'pkumar28', 'password': 'Welcome@2021'}
    conn = Connector(opts)
    return conn

def get_network_EA(connection, place_to_check: str):
    #args = [
    #    place_to_check,
    #    {
    #        f"*{}:~": value,
    #    }
    #]
    kwargs = {
        'return_fields': [
            'default',
            'extattrs',
            'network',
        ]
    }
    result = {"type": f"{place_to_check}", "objects": connection.get_object(**kwargs, max_results=1)}
    return result

connection = default_infoblox_connection()

search_network = get_network_EA(connection, "network")

print("Below is the Search Network :")
print(search_network)