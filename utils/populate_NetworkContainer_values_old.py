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

#def populate_NetworkContainer_ExtensibleAttribute(nw=str, comm=str, exatt=str):
#    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
#    ib_network_container.comment = comm
#    ea = objects.EA(exatt)
#    ib_network_container.extattrs = ea
#    ib_network_container.update()
#    print(ib_network_container)
#
#populate_NetworkContainer_ExtensibleAttribute('131.226.192.0/18', 'Dev Network Container Used for testing scripts as part of the IPAM Project', {'Description': 'This is my test container description', 'Environment': 'Test'})