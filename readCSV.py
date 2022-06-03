#! /usr/bin/python3

import csv

with open('NetworkContainer_EA.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tmp = (dict(row))
        NC = tmp["Network Container"]
        del tmp["Network Container"]
        print (NC)
        print(tmp)
        