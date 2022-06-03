#! /usr/bin/python3

import csv

result = {}

with open('NetworkContainer_EA.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for col in csv_reader:
        print (col)

        #for row in col:
#
        #    #result[row['Network Container']] = row['Description']
        #    #print (result)
        #    print (row)




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