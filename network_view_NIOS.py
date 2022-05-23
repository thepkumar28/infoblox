#! /usr/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG)

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from infoblox_client import connector, exceptions, objects

opts = {'host': 'ipam.woolworths.com.au', 'username': 'pkumar28', 'password': 'Welcome@2021'}
conn = connector.Connector(opts)
# get all network_views
network_views = conn.get_object('networkview')
# search network by cidr in specific network view
network = conn.get_object('network', {'network': '10.166.131.32/27', 'network_view': 'default'})
print("get all network_views")
print(network_views)
print("search network by cidr in specific network view")
print(network)