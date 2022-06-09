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

def NetworkContainer_Attribute(nw=str, comm=str, exatt=None):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    #ib_network_container.comment = comm
    ea_dict = ib_network_container.extattrs.ea_dict
    ea_in = objects.EA(exatt)
    ea_ex = objects.EA(ea_dict)
    #ea_dict.update(exatt.ea_dict)
    #merged_ea = objects.EA(ea_dict)
    #merged_ea = ea
    #ea = objects.EA(exatt)
    #ea_ex = ib_network_container.extattrs
    #ea_la = ib_network_container.ea
    #ib_network_container.extattrs = ea
    #ib_network_container.update()
    #ib_network_container_update=ib_network_container.update()
    #return ib_network_container_update
    #print ("Searched :\n", ib_network_container)
    print("Existing EA dictionary :\n", ea_dict)
    print ("Existing EA type :\n", type(ea_dict))
    print ("EA Input object format :\n", ea_in)
    print ("EA Input object format type :\n", type(ea_in))
    print ("EA Existing object format :\n", ea_ex)
    print ("EA Existing object format type :\n", type(ea_ex))
    print ("EA Input :\n", exatt)
    print ("EA Input type :\n", type(exatt))
    #print ("latest EA :\n", ea_la)
    #print ("EA post assigment:\n", ib_network_container.extattrs)
    #print("Existing EA dictionary :\n", ea_dict)
    #print ("Converted EA :\n", ea)
    #print("Merged EA Dictionary:\n", merged_ea)

NetworkContainer_Attribute('131.226.192.0/18', 'Dev Network Container Used for testing scripts as part of the IPAM Project', {'Description': 'Dev Network Container Used for testing scripts as part of the IPAM Project'})

#populate_NetworkContainer_EA = populate_NetworkContainer_ExtensibleAttribute('131.226.192.0/18',{'Description': 'This is my test container description'})

#print("Populated Extensible Attribute for the Network Container is :\n" , populate_NetworkContainer_EA)