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

def search_extensible_attribute(connection, place_to_check: str, extensible_attribute: str, value: str):
    """
    Find extensible attributes.
    :param connection: Infoblox connection
    :param place_to_check: Can be `network`, `networkcontainer` or `record:host` and so on.
    :param extensible_attribute: Which extensible attribute to search for. Can be `CustomerCode`, `Location`
    and so on.
    :param value: The value you want to search for.
    :return: result
    """
    extensible_args = [
        place_to_check,
        {
            f"*{extensible_attribute}:~": value,
        }
    ]
    kwargs = {
        'return_fields': [
            'default',
            'extattrs',
        ]
    }
    result = {"type": f"{place_to_check}", "objects": connection.get_object(*extensible_args, **kwargs, max_results=1)}
    return result

search_network = search_extensible_attribute(connection, "network", "Country", "Australia")
# Print the output:
print("Below is the Search Network :")
#print(search_network)
#for k,v in search_network.items():
#    print("Key Value pair : ")
#    print(k,v)
#for k in search_network.keys():
#    print("Key : ")
#    print(k)
tmp = []
extattrs = []
for v in search_network.values():    
    #print("Value : ")
    #print(v)
    tmp += [v]
print("Values are :\n", tmp)
print("list size of value is:", len(tmp))
extattrs = tmp[1][0]['extattrs']
print("Extensible Attributes :\n", extattrs)
print("list size of Extensible Attributes is:", len(extattrs))
print("Description is :\n", tmp[1][0]['extattrs']['Description']['value'])

#search_host = search_extensible_attribute(connection, "record:host", "Country", "Australia")
## Print the output:
#print("Below is the Search Host :")
#print(search_host)