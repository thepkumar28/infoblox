#! /usr/bin/python3

import csv

result = {}

with open('NetworkContainer_EA.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print (row)
        for i in row:
            #result[row[0]] = row[i]
            print(i)

        #for row in col:
        #    #result[col[0]] = row[0]
        #    #result[row['Network Container']] = row['Description']
        #    #print (result)
        #    #print (row)




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