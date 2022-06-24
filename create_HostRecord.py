#! /usr/bin/python3

import sys

import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client.connector import Connector
from infoblox_client import objects
from netmiko import ConnectHandler

def default_infoblox_connection():
    opts = {'host': 'ipam.woolworths.com.au', 'wapi_version':'2.10', 'username': sys.argv[1], 'password': sys.argv[2]}
    conn = Connector(opts)
    return conn
connection = default_infoblox_connection()

host_list = [
    {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
    },

    {
        "device_type": "cisco_ios",
        "host": "sandbox-nxos-1.cisco.com",
        "username": "admin",
        "password": "Admin_1234!",
    },

    {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
    }
]

#def connect_to_host():


#def create_Host():

for host in host_list:
    print(host)

#print(host_list)