# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:13:17 2019

@author: ASUS
"""
import csv
import datetime


file = '数据集5.csv';
shujuf = [];

with open(file,'r',newline='') as f:
    reader = csv.reader(f,delimiter=',')
    next(reader) #skip header
    for row in reader:
        Time=datetime.datetime.strptime(row[0],"%H:%M")
        series_a = float(row[1])
        series_b =float(row[2])
        series_c= float(row[3])
        sj=[Time,series_a,series_b,series_c]
        shujuf.append(sj)
        
        
def dtw_distance(ts_a,ts_b,d=lambda x,y:abs(x-y),mww=10000):
    import numpy as np
    #Create cost matrix via broadcasting with large int
    ts_a,ts_b=np.array(ts_a),np.array(ts_b)
    M,N=len(ts_a),len(ts_b)
    cost=np.ones((M,N))
    
    #Initialize the first row and column
    cost[0,0]=d(ts_a[0],ts_b[0])
    for i in range(1,M):
        cost[i,0] = cost[i-1,0] + d(ts_a[i],ts_b[0])
        
    for j in range(1,N):
        cost[0,j] = cost[0,j-1] + d(ts_a[0],ts_b[j])
        
    #Populate rest of cost matrix within window
    for i in range(1,M):
        for j in range(max(1,i-mww),min(N,i+mww)):
            choices = cost[i-1,j-1],cost[i,j-1],cost[i-1,j]
            cost[i,j] = min(choices)+d(ts_a[i],ts_b[j])
            
    
    #Return DTW distance given window
    return cost


xl = list(range(1,223))
xl_1 = [x[1] for x in shujuf]
xl_2 = [x[2] for x in shujuf]
xl_3 = [x[3] for x in shujuf]
dtw12 = dtw_distance(xl_1,xl_2)
dtw_13 = dtw_distance(xl_1,xl_3)
dtw_23 = dtw_distance(xl_2,xl_3)

print(dtw12[-1,-1])
print(dtw_13[-1,-1])
print(dtw_23[-1,-1])


def huitu(dtw_12):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from matplotlib import gridspec

    pathx=[]
    pathy=[]
    pathx.append(len(dtw_12)-1)
    pathy.append(len(dtw_12)-1)
    i=len(dtw_12)-1
    j=len(dtw_12)-1
    while i>0 or j>0:
            choices = dtw_12[i-1,j-1],dtw_12[i,j-1],dtw_12[i-1,j]
            if min(choices) == dtw_12[i-1,j-1]:
                i=i-1 
                pathx.append(i)
                j=j-1 
                pathy.append(j)
            elif min(choices) == dtw_12[i,j-1]:
                j=j-1 
                pathx.append(i) 
                pathy.append(j)
            else :
                i=i-1
                pathx.append(i) 
                pathy.append(j)
    pathx.append(0)
    pathy.append(0)
    
    fig = plt.figure()
    gs = gridspec.GridSpec(2,2, width_ratios=[1,10], height_ratios=[10,1])
    ax0 = plt.subplot(gs[0])
    plt.axis('off')
    ax0.plot(xl_2,xl)

    ax3 = plt.subplot(gs[3])
    ax3.plot(xl,xl_1, linewidth=2)
    plt.axis('off')

    ax2 = plt.subplot(gs[2])
    plt.axis('off')

    ax1 = plt.subplot(gs[1])
    heatplt = sns.heatmap(dtw_12, ax=ax1, cmap="viridis", cbar= False)
    ax1.plot(pathx,pathy,'r')

huitu(dtw12)
huitu(dtw_13)
huitu(dtw_23)