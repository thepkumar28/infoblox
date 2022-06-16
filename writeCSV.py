#! /usr/bin/python3

import csv
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

def write_to_CSV(nw=str):

    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])

    ea_ex_dict = ib_network_container.extattrs.ea_dict
    
    print("The EA Dictionary is :\n", ea_ex_dict)

    with open('write.csv', 'w', newline='') as csv_file:
        fieldnames = ['Country', 'Description', 'Environment', 'Operational State', 'Request Number', 'xxx']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(ea_ex_dict)

write_to_CSV('131.226.192.0/18')