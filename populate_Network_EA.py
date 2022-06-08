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

def populate_Network_ExtensibleAttribute(nw=str, comm=str, exatt=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    ib_network.comment = comm
    ea = objects.EA(exatt)
    ib_network.extattrs = ea
    ib_network.update()
    #ib_network_update=ib_network.update()
    #return ib_network_update

populate_Network_ExtensibleAttribute('131.226.217.128/27', 'Cisco DevNet Sandbox Range...', {'Description': 'This is my test description', 'Environment': 'Test'})

#populate_Network_EA = populate_Network_ExtensibleAttribute('131.226.217.128/27','Dev Network Used for testing scripts as part of the IPAM Project'{'Description': 'This is my test description', 'Request Number': 'CHG00197378'})

#print("Populated Extensible Attribute for the Network is :\n" , populate_Network_EA)