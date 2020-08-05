import sys
import time
import os

print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
print('\n')
print(os.getcwd())
print(os.path)
print(os.stat('基本语法.py'))
print('提示操作系统名',os.name)
print(os.sep,"间隔符")

print(os.extsep)

print(repr(os.linesep))
print(time.time())
print(os.path.getatime("基本语法.py"))