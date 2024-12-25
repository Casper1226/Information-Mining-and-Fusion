# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:45:15 2019

@author: ASUS
"""

data = [['T100','M','O','N','K','E','Y'],
        ['T200','D','O','N','K','E','Y'],
        ['T300','M','A','K','E'],
        ['T400','M','U','C','K','Y'],
        ['T500','C','O','O','K','I','E']
         ]

total1 = []
for i in range(0,len(data)):
    for j in range(1,len(data[i])):
        total1.append(data[i][j])
#将所有的购买记录放入集中

C1=[]
for i in range(0,len(total1)):
    c=0
    for j in range(0,len(C1)):
        if C1[j]==total1[i]:
            c=c+1
    if c==0:
        C1.append(total1[i])
#得出候选1项集C1

count1 = []
for i in range(0,len(C1)):
    count1.append(total1.count(C1[i]))
#获取C1每项的个数

min_s = 0.6*5
L1=[]
countl1=[]
for i in range(0,len(count1)):
    if count1[i]>min_s or count1[i]==min_s:
        L1.append(C1[i])
        countl1.append(count1[i])
#设置最小支持度为3，得到频繁1项集及其计数

c2=[]
C2=[]
for i in range(0,len(L1)-1):   
    for j in range(i+1,len(L1)):
        c2.append(L1[i])
        c2.append(L1[j])
        C2.append(c2)
        c2=[]
#连接L1和L1得到候选2项集

count2=[]
for i in range(0,len(C2)):
    c=0
    for j in range(0,len(data)):
        if (C2[i][0] in data[j]) and (C2[i][1] in data[j]):
            c=c+1
    count2.append(c)
#得到候选2项集每项的计数
    
L2=[]
countl2=[]
for i in range(0,len(count2)):
    if count2[i]>min_s or count2[i]==min_s:
        L2.append(C2[i])
        countl2.append(count2[i])
#根据最小分度值2筛选出频繁2项集及其计数

c3=[]
C3=[]
for i in range(0,len(L2)-1):
    for j in range(i+1,len(L2)):
        c3.append(L2[i][0])
        c3.append(L2[i][1])
        if L2[j][0] not in L2[i]:
            c3.append(L2[j][0])
        elif L2[j][1] not in L2[i]:
            c3.append(L2[j][1])
        m = 0
        for k in range(0,len(C3)):
            if (c3[0] in C3[k] and c3[1] in C3[k])\
            and c3[2] in C3[k]:
                m=m+1
        if m == 0:
            C3.append(c3)
        c3=[]
#连接L2和L2，得出候选3项集C3

C_3=[]
for i in range(0,len(C3)):
    m=[0,0,0]
    for j in range(0,len(L2)):
        if C3[i][0] in L2[j] and\
        C3[i][1] in L2[j]:
            m[0]=1
            break
    for j in range(0,len(L2)):
        if C3[i][0] in L2[j] and\
        C3[i][2] in L2[j]:
            m[1]=1
            break
    for j in range(0,len(L2)):
        if C3[i][1] in L2[j] and\
        C3[i][2] in L2[j]:
            m[2]=1
            break
    if m[1]+m[2]+m[0] == 3:
        C_3.append(C3[i])
#使用先验性质剪枝，结果放在C_3中
        
count3=[]
for i in range(0,len(C_3)):
    c=0
    for j in range(0,len(data)):
        if (C_3[i][0] in data[j] and C_3[i][1] in data[j])\
        and (C_3[i][2] in data[j]):
            c=c+1
    count3.append(c)
#计数C_3

L3=[]
countl3=[]
for i in range(0,len(count3)):
    if count3[i]>min_s or count3[i]==min_s:
        L3.append(C_3[i])
        countl3.append(count3[i])
#根据最小分度值，得出频繁3项集及计数

print(L3)