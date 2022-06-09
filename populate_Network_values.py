#! /usr/bin/python3

import sys
import csv
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

def populate_Network_ExtensibleAttribute(nw=str, desc=str, exatt=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    if ib_network.comment == None:
        ib_network.comment = desc
        ib_network.update()

    ea_dict = ib_network.extattrs.ea_dict
    ea_dict.update(exatt)
    merged_ea = objects.EA(ea_dict)
    ib_network.extattrs = merged_ea
    ib_network.update()
    print(ib_network)

with open('Network.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        dict_NW = (dict(row))
        NW = dict_NW["Network"]
        Desc = dict_NW["Description"]
        del dict_NW["Network"]
        EA_dict_NW = dict_NW
        print(NW)
        print(Desc)
        print(EA_dict_NW)
        populate_Network_ExtensibleAttribute(NW,Desc,EA_dict_NW)