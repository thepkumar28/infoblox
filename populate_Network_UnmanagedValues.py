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

def populate_Network_ExtensibleAttribute(nw=str, exatt=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs', 'unmanaged'])
    # Converting the Unmanaged network to a Managed network and Making sure the Network is always managed.
    ib_network.unmanaged = False
    ea_ex_dict = ib_network.extattrs.ea_dict
    #unmanaged = ib_network.unmanaged
    #if unmanaged == True:
    #    print("The value of Unmanaged for {} is {} hence converting this Unmanaged network to a Managed network".format(nw, unmanaged))
    #    #ib_network.unmanaged = False
    #    #ib_network.update()
    #else:
    #    print("The value of Unmanaged for {} is {}".format(nw, unmanaged))
    #desc = ea_ex_dict['Description']
    if 'Description' not in ea_ex_dict:
        print("Description doesn't Exist for {}. Copying the Description from LLD !!!".format(nw))
        ea_ex_dict.update(exatt)
        merged_ea = objects.EA(ea_ex_dict)
        ib_network.extattrs = merged_ea
        ib_network.update()
        desc = ea_ex_dict['Description']
        if ib_network.comment == None:
            print("Comment field is Empty for {}. Copying from Description !!!".format(nw))
            ib_network.comment = desc
            ib_network.update()
            print("The latest EA dictionary for {} is :\n{}".format(nw, ea_ex_dict))
            print("The latest comment for {} is :\n{}".format(nw, ib_network.comment))

    print(ib_network)
    

populate_Network_ExtensibleAttribute('192.0.2.0/24', {'Description':'Test Description'})

#with open('NetworkContainer.csv', newline='') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    for row in csv_reader:
#        dict_NC = (dict(row))
#        NC = dict_NC["Network Container"]
#        Desc = dict_NC["Description"]
#        del dict_NC["Network Container"]
#        EA_dict_NC = dict_NC
#        populate_NetworkContainer_ExtensibleAttribute(NC,Desc,EA_dict_NC)