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

def backup_Network_data(nw=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    with open('backup_Network_data.txt', 'a') as f:
        f.write(str(ib_network) + '\n')
    return ib_network

def backup_NetworkContainer_data(nw=str):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    with open('backup_NetworkContainer_data.txt', 'a') as f:
        f.write(str(ib_network_container) + '\n')
    return ib_network_container

with open('Network_EA.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        NW = tmp["Network Container"]
        print (NW)
        backup_Network_data(NW)

with open('NetworkContainer_EA.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        NC = tmp["Network Container"]
        print (NC)
        backup_NetworkContainer_data(NC)