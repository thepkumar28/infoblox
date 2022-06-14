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

    ea_ex_dict = ib_network_container.extattrs.ea_dict

    if 'Description' not in ea_ex_dict:
        print("Description doesn't Exist !!!")
        ea_ex_dict.update(exatt)
        merged_ea = objects.EA(ea_ex_dict)
        ib_network_container.extattrs = merged_ea
        ib_network_container.update()
        print("Updated EA dictionary is :\n", ea_ex_dict)
        desc = ea_ex_dict['Description']
        #print("The Description is:\n", desc)
        if ib_network_container.comment == None:
            print("Comment field is Empty !!!")
            ib_network_container.comment = desc
            ib_network_container.update()
            print("The latest EA dictionary is :\n", ea_ex_dict)
            print("The latest comment is :\n", ib_network_container.comment)
        elif re.search(r'^SVR|RFC',ib_network_container.comment,re.I):
            print("The existing comment is as below and it needs to be updated:\n", ib_network_container.comment)
            RQ_num = {'Request Number':ib_network_container.comment}
            #print("Request number dict is :\n", RQ_num)
            ea_ex_dict.update(RQ_num)
            merged_ea = objects.EA(ea_ex_dict)
            ib_network_container.extattrs = merged_ea
            ib_network_container.comment = desc
            ib_network_container.update()
            print("The latest EA dictionary is :\n", ea_ex_dict)
            print("The latest comment is :\n", ib_network_container.comment)

    else:
        print("Description Exists !!!")
        desc = ea_ex_dict['Description']
        #print("The Description is:\n", desc)
        if ib_network_container.comment == None:
            print("Comment field is Empty !!!")
            ib_network_container.comment = desc
            ib_network_container.update()
            print("The latest EA dictionary is :\n", ea_ex_dict)
            print("The latest comment is :\n", ib_network_container.comment)
        elif re.search(r'^SVR|RFC',ib_network_container.comment,re.I):
            print("The existing comment is as below and it needs to be updated:\n", ib_network_container.comment)
            RQ_num = {'Request Number':ib_network_container.comment}
            #print("Request number dict is :\n", RQ_num)
            ea_ex_dict.update(RQ_num)
            merged_ea = objects.EA(ea_ex_dict)
            ib_network_container.extattrs = merged_ea
            ib_network_container.comment = desc
            ib_network_container.update()
            print("The latest EA dictionary is :\n", ea_ex_dict)
            print("The latest comment is :\n", ib_network_container.comment)
        else:
            print("The latest EA dictionary is :\n", ea_ex_dict)
            print("The latest comment is :\n", ib_network_container.comment)
            print("All filelds are correct !!!")       
          
NetworkContainer_Attribute('131.226.192.0/18', 'Dev Network Container Used for testing scripts as part of the IPAM Project', {'Description': 'Dev Network Container Used for testing scripts as part of the IPAM Project'})
