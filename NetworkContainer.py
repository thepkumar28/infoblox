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

with open('UserIntervention.csv', 'w', newline='') as csv_file:
    fieldnames = ['Network Container', 'Comment', 'Description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

def NetworkContainer_Attribute(nw=str, exatt=str):
    ib_network_container = objects.NetworkContainer.search(connection, network=nw, network_view='default', return_fields=['default', 'extattrs'])

    ea_ex_dict = ib_network_container.extattrs.ea_dict

    if 'Description' not in ea_ex_dict:
        print("Description doesn't Exist. Copying the Description from LLD !!!")
        ea_ex_dict.update(exatt)
        merged_ea = objects.EA(ea_ex_dict)
        ib_network_container.extattrs = merged_ea
        ib_network_container.update()
        desc = ea_ex_dict['Description']
        #print("The Description is:\n", desc)
        if ib_network_container.comment == None:
            print("Comment field is Empty for {}. Copying from Description !!!".format(nw))
            ib_network_container.comment = desc
            ib_network_container.update()
            print("The latest EA dictionary is :\n", ea_ex_dict)
            print("The latest comment is :\n", ib_network_container.comment)
        elif re.search(r'^SVR',ib_network_container.comment,re.I):
            print("The existing comment for {} is as below , moving it to the Request number field and Copying the Description to the Comment field.\n{}".format(nw, ib_network_container.comment))
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
            print("The existing comment for {} is as below , User Intervention is required. Moving the values to the UserIntervention.csv file.\n{}".format(nw, ib_network_container.comment))
            my_dict = {'Network Container':nw, 'Comment':ib_network_container.comment, 'Description':desc}
            with open('UserIntervention.csv', 'a', newline='') as csv_file:
                fieldnames = ['Network Container', 'Comment', 'Description']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(my_dict)

    else:
        print("Description Exists , User Intervention is required !!!")
        desc = ea_ex_dict['Description']
        #print("The Description is:\n", desc)
        if ib_network_container.comment == None:
            print("Comment field is Empty for {} , moving the values to the UserIntervention.csv file.".format(nw))
            my_dict = {'Network Container':nw, 'Comment':ib_network_container.comment, 'Description':desc}
            with open('UserIntervention.csv', 'a', newline='') as csv_file:
                fieldnames = ['Network Container', 'Comment', 'Description']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(my_dict)
        elif re.search(r'^SVR',ib_network_container.comment,re.I):
            print("The existing comment for {} is as below , moving it to the Request number field.\nMoving the values to the UserIntervention.csv file.\n{}".format(nw, ib_network_container.comment))
            RQ_num = {'Request Number':ib_network_container.comment}
            #print("Request number dict is :\n", RQ_num)
            ea_ex_dict.update(RQ_num)
            merged_ea = objects.EA(ea_ex_dict)
            ib_network_container.extattrs = merged_ea
            ib_network_container.comment = ""
            ib_network_container.update()
            print("The latest EA dictionary is :\n", ea_ex_dict)
            #print("The latest comment is :\n", ib_network_container.comment)
            my_dict = {'Network Container':nw, 'Comment':ib_network_container.comment, 'Description':desc}
            with open('UserIntervention.csv', 'a', newline='') as csv_file:
                fieldnames = ['Network Container', 'Comment', 'Description']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(my_dict)
        else:
            print("The existing comment for {} is as below , moving the values to the UserIntervention.csv file.\n{}".format(nw, ib_network_container.comment))
            my_dict = {'Network Container':nw, 'Comment':ib_network_container.comment, 'Description':desc}
            with open('UserIntervention.csv', 'a', newline='') as csv_file:
                fieldnames = ['Network Container', 'Comment', 'Description']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(my_dict)

with open('NetworkContainer.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        #NC = tmp["Network Container"]
        #description_key = ['Description']
        #desc = {k:tmp[k] for k in description_key if k in tmp}    
        #print("NC :\n", NC)
        #print("desc :\n", desc)
        for k in 'Description':
            if k in tmp:
                print(k)