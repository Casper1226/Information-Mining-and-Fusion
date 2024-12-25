# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:05:38 2019

@author: ASUS
"""
#!/usr/bin/env python3
def maxmin(input_file,output_file_1):
    import csv
    with open(input_file,'r',newline='') as csv_in_file:       
        with open(output_file_1,'w',newline='') as csv_out_file:   
            reader = csv.reader(csv_in_file)
            writer1 = csv.writer(csv_out_file)
            header = next(reader,None)
            writer1.writerow(header)
            row_list_output = []
            output = []
            for row in reader:           
                row_list_output.append(float(row[3]))
                output.append(row)
            maxs = max(row_list_output)
            mins = min(row_list_output)
            for i in range(0,len(row_list_output)):
                row_list_output[i] = (row_list_output[i]-mins)/\
                (maxs-mins)
                output[i][3]=row_list_output[i]
            writer1.writerows(output)


def junzhi(input_file,output_file_2):
    import csv
    import numpy as np
    with open(input_file,'r',newline='') as csv_in_file:
        with open(output_file_2,'w',newline='') as csv_out_file:
            reader = csv.reader(csv_in_file)
            writer = csv.writer(csv_out_file)
            header = next(reader,None)
            writer.writerow(header)            
            row_list_output = []
            output = []
            for row in reader:           
                row_list_output.append(float(row[3]))
                output.append(row)
            average = np.mean(row_list_output)
            stdo = np.std(row_list_output)
            for i in range(0,len(row_list_output)):
                row_list_output[i] = (row_list_output[i]-average)/\
                stdo
                output[i][3]=row_list_output[i]
            writer.writerows(output)   

def xiaoshu(input_file,output_file):
    import csv
    with open(input_file,'r',newline='') as csv_in_file:
        with open(output_file,'w',newline='') as csv_out_file:
            reader = csv.reader(csv_in_file)
            writer = csv.writer(csv_out_file)
            header = next(reader,None)
            writer.writerow(header)
            row_list_output = []
            output = []
            for row in reader:           
                row_list_output.append(float(row[3]))
                output.append(row)
            import math
            abs_out = []
            for i in range(0,len(row_list_output)):
                abs_out.append(abs(row_list_output[i]))
            maxabs = max(abs_out)
            weishu = math.ceil(math.log(maxabs,10))
            for i in range(0,len(row_list_output)):
                row_list_output[i] = row_list_output[i]/pow(10,weishu)
                output[i][3]=row_list_output[i]
            writer.writerows(output)


def wufen(input_file,output_file):
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

maxmin("Monday.csv","Monday1.csv")
junzhi("Monday.csv","Monday2.csv")
xiaoshu("Monday.csv","Monday3.csv")
wufen("Monday.csv","Monday4.csv")
zheng("Monday.csv","Monday5.csv")
maxmin("Tuesday.csv","Tuesday1.csv")
junzhi("Tuesday.csv","Tuesday2.csv")
xiaoshu("Tuesday.csv","Tuesday3.csv")
wufen("Tuesday.csv","Tuesday4.csv")
zheng("Tuesday.csv","Tuesday5.csv")
maxmin("Wednesday.csv","Wednesday1.csv")
junzhi("Wednesday.csv","Wednesday2.csv")
xiaoshu("Wednesday.csv","Wednesday3.csv")
wufen("Wednesday.csv","Wednesday4.csv")
zheng("Wednesday.csv","Wednesday5.csv")
maxmin("Thursday.csv","Thursday1.csv")
junzhi("Thursday.csv","Thursday2.csv")
xiaoshu("Thursday.csv","Thursday3.csv")
wufen("Thursday.csv","Thursday4.csv")
zheng("Thursday.csv","Thursday5.csv")