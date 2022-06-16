#! /usr/bin/python3

import csv

with open('NetworkContainer.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        #NC = tmp["Network Container"]
        #desc = tmp["Description"]
        #del tmp["Network Container"]
        #print (NC)
        #print(desc)
        result = {k:tmp[k] for k in ('Network Container','Description') if k in tmp}    
        print (result)

        