#!/usr/bin/env python
import csv

file = 'mobike_reordered.txt'
bike_list = []

with open(file, newline='') as f:
    reader = csv.reader(f,delimiter=',',quotechar='"')
    next(reader)
    for row in reader:
        order_id = row[2]
        bike_id = row[3]
        user_id = row[4]
        start_time = float(row[0])
        start_time = int(start_time)
        end_time = float(row[1])
        end_time = int(end_time)
        start_lon = float(row[5])
        end_lon = float(row[7])
        start_lat = float(row[6])
        end_lat = float(row[8])
        track = row[9]
        trip_info = [order_id, bike_id, user_id, start_time, end_time, (start_lon, start_lat),(end_lon, end_lat),
                    track]
        bike_list.append(trip_info)  #读入文件

use_time = []

for i in range(len(bike_list)):
    use_time.append(bike_list[i][4] - bike_list[i][3])#计算出行时间,单位为s

from math import radians,cos,sin,asin,sqrt
def haversine(lon1,lat1,lon2,lat2):#定义计算两经纬度之间的距离的函数
    #将十进制数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    #haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 #地球平均半径，单位为km
    return c * r * 1000
  
path = []

for i in range(len(bike_list)):
    track_list = bike_list[i][7].split('#')#将str转为list
    path_t = 0
    for j in range(len(track_list)):
            track_list1 = track_list[j].split(',')
            track_list1 = list(map(float,track_list1))#将字符型转化为数值型
            if j < len(track_list)-1:#防止出现列表调用超出
                track_list2 = track_list[j+1].split(',')
                track_list2 = list(map(float,track_list2))                     
                path_f = haversine(track_list1[0], track_list1[1], track_list2[0], track_list2[1])  #调用函数计算相邻两经纬度之间的距离
                path_t += path_f
    path.append(path_t)           #计算出出发到目的地的距离，单位为m

speed = []

for i in range(len(bike_list)):
    speed_f = (path[i] / use_time[i]) * 3.6  
    speed.append(speed_f)  #计算速度，单位为km/h

mobike_list = [use_time, path, speed]
mobike_list = zip(*mobike_list)  #转置为列

with open("mobike_bike_list.csv", 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(mobike_list)     #写入csv文件                                    