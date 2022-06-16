#! /usr/bin/python3

import csv

with open('NetworkContainer.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        #NC = tmp["Network Container"]
        #desc = tmp["Description"]
        for k,v in tmp.items():
            if k == "Network Container":
                NC = {k:v}
                print(NC)
            elif k == "Description":
                Desc = {k:v}
                print(Desc)    
        #del tmp["Network Container"]
        #print (NC)
        #print(desc)
        