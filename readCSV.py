#! /usr/bin/python3

import csv

with open('NetworkContainer.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        Desc_dict = {}
        #NC = tmp["Network Container"]
        #desc = tmp["Description"]
        for k,v in tmp.items():
            if k == "Network Container":
                NC_dict = {k:v}
                NC = NC_dict["Network Container"]
                print(NC_dict)
                print(NC)
            elif k == "Description":
                Desc_dict = {k:v}
                print(Desc_dict)    
        #del tmp["Network Container"]
        #print (NC)
        #print(desc)
        