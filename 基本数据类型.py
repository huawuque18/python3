#!/usr/bin/python3.8
import os
import pstats
print(pstats.stats)

import psutil
psutil.cpu_times()
print(os.name)
a, b, c, d = 20, 5.5, True, 4+3j
'''
for n in range(1,10):
    for m in range(n,n+1) :
        print(m,"*",n,'=',m*n,sep='')
        m=m+1
'''


if 3 % 2 == 0:
            print(2)
else:
        # 循环中没有找到元素
        print(4)