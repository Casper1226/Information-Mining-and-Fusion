# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:28:09 2019

@author: ASUS
"""

c4=[]
C4=[]
for i in range(0,len(L3)-1):
    for j in range(i+1,len(L3)):
        c4.append(L3[i][0])
        c4.append(L3[i][1])
        c4.append(L3[i][2])
        if L3[j][0] not in L3[i]:
            c4.append(L3[j][0])
        elif L3[j][1] not in L3[i]:
            c4.append(L3[j][1])
        elif L3[j][2] not in L3[i]:
            c4.append(L3[j][2])
        m = 0
        for k in range(0,len(C4)):
            if (c4[0] in C4[k] and c4[1] in C4[k])\
            and (c4[2] in C4[k] and c4[3] in C4[k]):
                m=m+1
        if m == 0:
            C4.append(c4)
        c4=[]
#L3与L3连接得到候选集C4

C_4=[]
for i in range(0,len(C4)):
    m=0
    for j in range(0,len(L3)):
        if (C4[i][0] in L3[j] and C4[i][1] in L3[j])\
        and  C4[i][2] in L3[j]:
            m=m+1
            break
    for j in range(0,len(L3)):
        if (C4[i][0] in L3[j] and C4[i][1] in L3[j])\
        and  C4[i][3] in L3[j]:
            m=m+1
            break
    for j in range(0,len(L3)):
        if (C4[i][2] in L3[j] and C4[i][1] in L3[j])\
        and  C4[i][3] in L3[j]:
            m=m+1
            break
    for j in range(0,len(L3)):
        if (C4[i][0] in L3[j] and C4[i][3] in L3[j])\
        and  C4[i][2] in L3[j]:
            m=m+1
            break
    if m==4:
        C_4.append(C4[i])
#使用先验性质对C4剪枝，结果放在C_4中
        
count4=[]
for i in range(0,len(C_4)):
    c=0
    for j in range(0,len(data)):
        if (C_4[i][0] in data[j] and C_4[i][1] in data[j])\
        and (C_4[i][2] in data[j] and C_4[i][3] in data[j]):
            c=c+1
    count4.append(c)
#对候选4项集计数

L4=[]
countl4=[]
for i in range(0,len(count4)):
    if count4[i]>2 or count4[i]==2:
        L4.append(C_4[i])
        countl4.append(count4[i])
#得到频繁项集L4

c5=[]
C5=[]
for i in range(0,len(L4)-1):
    for j in range(i+1,len(L4)):
        c5.append(L4[i][0])
        c5.append(L4[i][1])
        c5.append(L4[i][2])
        c5.append(L4[i][3])
        if L4[j][0] not in L4[i]:
            c5.append(L4[j][0])
        elif L4[j][1] not in L4[i]:
            c5.append(L4[j][1])
        elif L4[j][2] not in L4[i]:
            c5.append(L4[j][2])
        elif L4[j][3] not in L4[i]:
            c5.append(L4[j][3])
        m = 0
        for k in range(0,len(C5)):
            if (c5[0] in C5[k] and c5[1] in C5[k])\
            and (c5[2] in C5[k] and c5[3] in C5[k])\
            and c5[4] in C5[k]:
                m=m+1
        if m == 0:
            C5.append(c5)
        c5=[]
#连接L4和L4，得到候选5项集C5

C_5=[]
for i in range(0,len(C5)):
    m=0
    for j in range(0,len(L4)):
        if (C5[i][0] in L4[j] and C5[i][1] in L4[j])\
        and  C5[i][2] in L4[j] and C5[i][3] in L4[j]:
            m=m+1
            break
    for j in range(0,len(L4)):
        if (C5[i][0] in L4[j] and C5[i][1] in L4[j])\
        and  C5[i][3] in L4[j] and C5[i][4] in L4[j]:
            m=m+1
            break
    for j in range(0,len(L4)):
        if (C5[i][2] in L4[j] and C5[i][1] in L4[j])\
        and  C5[i][3] in L4[j] and C5[i][4] in L4[j]:
            m=m+1
            break
    for j in range(0,len(L4)):
        if (C5[i][0] in L4[j] and C5[i][3] in L4[j])\
        and  C5[i][2] in L4[j] and C5[i][4] in L4[j]:
            m=m+1
            break
    for j in range(0,len(L4)):
        if (C5[i][0] in L4[j] and C5[i][1] in L4[j])\
        and  C5[i][2] in L4[j] and C5[i][4] in L4[j]:
            m=m+1
            break
    if m==5:
        C_5.append(C5[i])
#对C5进行先验性质剪枝，得到结果C_5
        
count5=[]
for i in range(0,len(C_5)):
    c=0
    for j in range(0,len(data)):
        if (C_5[i][0] in data[j] and C_5[i][1] in data[j])\
        and C_5[i][2] in data[j] and C_5[i][3] in data[j]\
        and C_5[i][4] in data[j]:
            c=c+1
    count5.append(c)
#得到C5的计数

L5=[]
countl5 = []
for i in range(0,len(count5)):
    if count5[i] >min_s or count5[i]==min_s:
        L5.append(C_5[i])
        countl5.append(count5)
#得到频繁5项集L5

print(L5)