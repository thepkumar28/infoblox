#! /usr/bin/python3

import csv

with open('NetworkContainer_EA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row , col in csv_file:
        print(col[0])
        print(row[0])

#with open('NetworkContainer_EA.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            #print(f'{", ".join(row)}')
#            print(row[0])
#            line_count += 1
#        else:
#            #print(f'{", ".join(row)}')
#            print(row[0])
#            line_count += 1
#    print(f'Processed {line_count} lines.')