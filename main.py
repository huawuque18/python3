import sys
import time
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
print('\n')
import os
print(os.getcwd())
print(os.path)
print(os.stat('main.py'))
print('提示操作系统名',os.name)
print(os.sep,"间隔符")

print(os.extsep)

print(repr(os.linesep))
print(time.time())
print(os.path.getmtime())


'''
if True:
    print ("true")
else:
    print ("False")
'''

#num1=input("shuru:")
#print(num1)
num1=10
num2=12
#total = num1 + num2
#print (total)

#word= input("请输入把：")
#print(word[0:2],word[2])


哈哈哈