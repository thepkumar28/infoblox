#! /usr/bin/python3
import logging
logging.basicConfig(level=logging.DEBUG)

from infoblox_client import connector, exceptions, objects

opts = {'host': '100.64.1.5', 'username': 'pkumar28', 'password': 'Welcome@2021'}
conn = connector.Connector(opts)
# get all network_views
network_views = conn.get_object('networkview')
# search network by cidr in specific network view
network = conn.get_object('network', {'network': '10.166.131.32/27', 'network_view': 'default'})
print(network)