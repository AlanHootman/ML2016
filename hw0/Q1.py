#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import glob
import pandas as pd
x = []
y = []
z = []
file = open('/home/jhm/Documents/Git Sources/ML2016/hw0/hw0_data.dat', 'r')  # 改成自己的hw0_data.dat的地址
for line in file:
    trainingSet = line.split(' ')   # 对于每一行,按‘ ’把数据分开
    x.append(trainingSet[3])
x = map(float, x)   # 将x从str转换成float
for i in x:
    y.append(i)
y = sorted(y)   # 升s序排列

outfile = open('/home/jhm/Documents/Git Sources/ML2016/hw0/ans1.txt', 'w')  # 改成自己的ans1.txt的地址
y = map(str, y)    # 将y从float转换成str
for i in y:
    z.append(i)
print(z)

outfile.write(str(z))
outfile.close()
