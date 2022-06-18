#! /usr/bin/python3

import sys
import csv
#import logging
#logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector
from infoblox_client import objects

def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
    conn = Connector(opts)
    return conn
connection = default_infoblox_connection()

def populate_Network_ExtensibleAttribute(nw=str, desc=str, exatt=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs', 'unmanaged'])
    #ib_network.unmanaged = False
    unmanaged = ib_network.unmanaged
    if unmanaged == True:
        print("The value of Unmanaged for {} is {} hence converting this Unmanaged network to a Managed network".format(nw, unmanaged))
        #ib_network.unmanaged = False
        #ib_network.update()
    else:
        print("The value of Unmanaged for {} is {}".format(nw, unmanaged))
        
    #if ib_network_container.comment == None:
    #    ib_network_container.unmanaged('false')
    #    ib_network_container.comment = desc
    #    ib_network_container.update()
#
    #ea_dict = ib_network_container.extattrs.ea_dict
    #ea_dict.update(exatt)
    #merged_ea = objects.EA(ea_dict)
    #ib_network_container.extattrs = merged_ea
#
    #ib_network_container.update()
    print(ib_network)
    

populate_Network_ExtensibleAttribute('192.0.2.0/24', 'Test comment', {'Description':'Test Description'})

#with open('NetworkContainer.csv', newline='') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    for row in csv_reader:
#        dict_NC = (dict(row))
#        NC = dict_NC["Network Container"]
#        Desc = dict_NC["Description"]
#        del dict_NC["Network Container"]
#        EA_dict_NC = dict_NC
#        populate_NetworkContainer_ExtensibleAttribute(NC,Desc,EA_dict_NC)