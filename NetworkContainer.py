#! /usr/bin/python3

import sys
import re
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

def NetworkContainer_Attribute(nw=str, comm=str, exatt=str):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])
    #ib_network_container.comment = comm
    ea_ex_dict = ib_network_container.extattrs.ea_dict
    if 'Description' not in ea_ex_dict:
        print("No Existing Description")
        ea_ex_dict.update(exatt)
        merged_ea = objects.EA(ea_ex_dict)
        ib_network_container.extattrs = merged_ea
        ib_network_container.update()
        print("Updated EA dictionary is :\n", ea_ex_dict)

    else:
        print("The Description is:\n", ea_ex_dict["Description"])    
          
       
    #RQ_num = ea_ex_dict['Request Number']
    #if ib_network_container.comment == None:
    #    ib_network_container.comment = desc
    #    print('Comment is:\n', ib_network_container.comment)
    #    #ib_network_container.update()
    #elif re.search(r'^SVR|RFC',ib_network_container.comment,re.I):
#
    #    print('Comment is:\n', ib_network_container.comment)
    #ea_dict = ib_network_container.extattrs.ea_dict
    #ea_in = objects.EA(exatt)
    #ea_ex = objects.EA(ea_dict)
    #ea_dict.update(exatt)
    #merged_ea = objects.EA(ea_dict)
    #merged_ea = ea
    #ea = objects.EA(exatt)
    #ea_ex = ib_network_container.extattrs
    #ea_la = ib_network_container.ea
    #ib_network_container.extattrs = ea
    #ib_network_container.update()
    #ib_network_container_update=ib_network_container.update()
    #return ib_network_container_update
    #print ("Searched :\n", ib_network_container)
    #print("Existing EA dictionary :\n", ea_ex_dict)
    #print ("Existing EA type :\n", type(ea_ex_dict))
    #print ("EA Input object format :\n", ea_in)
    #print ("EA Input object format type :\n", type(ea_in))
    #print ("EA Existing object format :\n", ea_ex)
    #print ("EA Existing object format type :\n", type(ea_ex))
    #print ("EA Input :\n", exatt)
    #print ("EA Input type :\n", type(exatt))
    #print("Merged EA Dictionary:\n", ea_dict)
    #print("Merged EA :\n", merged_ea)
    #print("Exisitng description is:\n",desc)
    #print("Request Number is:\n",RQ_num)

NetworkContainer_Attribute('131.226.192.0/18', 'Dev Network Container Used for testing scripts as part of the IPAM Project', {'Description': 'Dev Network Container Used for testing scripts as part of the IPAM Project'})
