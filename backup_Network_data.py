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

with open('backup_Network_data.csv', 'w', newline='') as csv_file:
    fieldnames = ['Network', 'Comment', 'Banner', 'Building', 'Country', 'Delivery Channel', 'Description', 'Environment', 'Location-Suburb', 'Operational State', 'Partner', 'Product Owner', 'Region', 'Request Number', 'Service Owner', 'Site', 'Site ID', 'Site Type', 'Source Firewall', 'State', 'VLAN', 'VLAN Name', 'Zone']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

def backup_Network_data(nw=str):
    ib_network = objects.Network.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    ea_ex_dict = ib_network.extattrs.ea_dict
    tmp_dict = {'Comment':ib_network.comment, 'Network':nw}
    ea_ex_dict.update(tmp_dict)
    with open('backup_Network_data.csv', 'a', newline='') as csv_file:
        fieldnames = ['Network', 'Comment', 'Banner', 'Building', 'Country', 'Delivery Channel', 'Description', 'Environment', 'Location-Suburb', 'Operational State', 'Partner', 'Product Owner', 'Region', 'Request Number', 'Service Owner', 'Site', 'Site ID', 'Site Type', 'Source Firewall', 'State', 'VLAN', 'VLAN Name', 'Zone']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(ea_ex_dict)
    print("Backed up {}".format(nw))    

with open('Network.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        NW = tmp["Network"]
        print (NW)
        backup_Network_data(NW)
