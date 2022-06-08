#! /usr/bin/python3

import sys
import re
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

def populate_NetworkContainer_ExtensibleAttribute(nw=str, desc=str, exatt=str):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs', 'comment'])
    if ib_network_container.comment == None:
        ib_network_container.comment = desc
        ib_network_container.update()
    elif re.search("^SVR", ib_network_container.comment):
        ib_network_container.comment = desc
        ib_network_container.update()
        print('Comment is :', ib_network_container.comment)   
    ea = objects.EA(exatt)
    ib_network_container.extattrs = ea
    ib_network_container.update()
    print(ib_network_container)

with open('NetworkContainer_EA.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        dict_NC = (dict(row))
        NC = dict_NC["Network Container"]
        Desc = dict_NC["Description"]
        del dict_NC["Network Container"]
        EA_dict_NC = dict_NC
        print(NC)
        print(Desc)
        print(EA_dict_NC)
        populate_NetworkContainer_ExtensibleAttribute(NC,Desc,EA_dict_NC)