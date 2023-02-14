import math
import time
import random
"""
1
"""
s=3*math.pi*6
print(s)
"""
例题3.2
"""
speed=563
#25km转换为m
distance=25*1000
g=9.8
sin2A=distance/(speed**2)*g
angle=math.asin(sin2A)
degree=math.degrees(angle)/2
degree=round(degree,2)
print("炮管发射角度为:",degree)

"""
例题3.3
time库的应用
"""
seconds=time.time()
print(seconds)
 #取整
seconds=int(seconds)
print("距离1970年1月1日0点过去了",seconds,"秒")

"""
例题3.4
"""
startTime=time.time()
inputString=input("谁便输入一些字母串:")
print(inputString)
endTime=time.time()
duration=int(endTime-startTime)
print("这个程序用时",duration,"秒")

"""
例题3.5
random库的使用
"""
#import random
print(random.random())
print(random.randint(1,100))

"""
例题3.11
"""
id=input("学号:")
name=input("名字:")
xingxi=id+"\t"+name+"\t"+"\uf0fc"+"\n"
#第二个
id=input("学号:")
name=input("名字:")
xingxi=xingxi+id+"\t"+name+"\t"+"\uf0fc"+"\n"
#第三个
id=input("学号:")
name=input("名字:")
xingxi=xingxi+id+"\t"+name+"\t"+"\uf0fc"+"\n"
title="学号\t姓名\t体温"
print(title)
print(xingxi)
"""

"""