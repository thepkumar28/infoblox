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

#with open('write.csv', 'w', newline='') as csv_file:
#    fieldnames = ['Network Container', 'Comment', 'Description']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()

def write_to_CSV(nw=str):

    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])

    ea_ex_dict = ib_network_container.extattrs.ea_dict
    
    print("The EA Dictionary is :\n", ea_ex_dict)
    
    my_dict = {'Network Container':nw, 'Comment':ib_network_container.comment, 'Description':ea_ex_dict['Description']}
    
    with open('write.csv', 'w', newline='') as csv_file:
        fieldnames = ['Network Container', 'Comment', 'Description']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    with open('write.csv', 'a', newline='') as csv_file:
        fieldnames = ['Network Container', 'Comment', 'Description']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(my_dict)       

#write_to_CSV('131.226.192.0/18')
with open('NetworkContainer.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        NC = tmp["Network Container"]
        print (NC)
        write_to_CSV(NC)