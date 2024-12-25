# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:56:24 2019

@author: ASUS
"""
#!/usr/bin/env python3
input_file = "Monday.csv"
output_file =  "Monday4.csv"
import csv
import numpy as np
with open(input_file,'r',newline='') as csv_in_file:       
    with open(output_file,'w',newline='') as csv_out_file:   
        reader = csv.reader(csv_in_file)
        writer1 = csv.writer(csv_out_file)
        header = next(reader,None)
        writer1.writerow(header)
        row_list_output = []
        output = []
        for row in reader:           
            row_list_output.append(float(row[3]))
            output.append(row)
        q1 = np.percentile(row_list_output,25)
        q3 = np.percentile(row_list_output,75)
        iq = q3-q1
        maxs = min(max(row_list_output),q3+iq)
        mins = max(min(row_list_output),q1-iq)
        j=0
        for i in range(0,len(row_list_output)):              
            if row_list_output[i]<mins or row_list_output[i]>maxs:
                del output[i-j]
                j += 1
        writer1.writerows(output)
#wufen("Monday.csv","Monday4.csv")

def zheng(input_file,output_file):
    import csv
    import numpy as np
    with open(input_file,'r',newline='') as csv_in_file:       
        with open(output_file,'w',newline='') as csv_out_file:   
            reader = csv.reader(csv_in_file)
            writer1 = csv.writer(csv_out_file)
            header = next(reader,None)
            writer1.writerow(header)
            row_list_output = []
            output = []
            for row in reader:           
                row_list_output.append(float(row[3]))
                output.append(row)
            j=0
            jun = np.mean(row_list_output)
            fang = np.std(row_list_output)
            for i in range(0,len(row_list_output)-1):              
                if row_list_output[i]<(jun-3*fang) or\
                row_list_output[i]>(jun+3*fang):
                    del output[i-j]
                    j += 1
            writer1.writerows(output)
zheng("Monday.csv","Monday5.csv")