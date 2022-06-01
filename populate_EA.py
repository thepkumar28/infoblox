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

def populate_Network_ExtensibleAttribute(nw=str, exatt=str):
    network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    ea = objects.EA({exatt})
    return ea

populate_Network_EA = populate_Network_ExtensibleAttribute('131.226.217.128/27',"'Description': 'This is my updated test description...'")

print("Populated Extensible Attribute for the Network is :\n" , populate_Network_EA)

#ib_network = objects.Network.search(connection, network='131.226.217.128/27', network_view='default', return_fields=['default', 'extattrs'])
#ib_network_container = objects.NetworkContainer.search(connection, network='131.226.192.0/18', network_view='default', return_fields=['default', 'extattrs'])
#ea = objects.EA({'Description': 'This is my test description...'})
#ea_nc = objects.EA({'Description': 'This is my test Container description...'})
#print("ib_network :\n", ib_network)
#print("ib_network_container :\n", ib_network_container)
#print("EA :\n", ea)
#ib_network.extattrs = ea
#ib_network_update=ib_network.update()
#ib_network_container.extattrs = ea_nc
#ib_network_container_update=ib_network_container.update()
#print("Updated Extensible Attribute for Network is :\n", ib_network_update)
#print("Updated Extensible Attribute for Network Container is :\n", ib_network_container_update)