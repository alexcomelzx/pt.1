"""
例题3.5
random库的使用
"""
import random
print(random.random())
print(random.randint(1,100))

"""
例题3.6
随机生成一个大写字母
"""
randValue=random.randint(0,25)
charValue=ord("A")
newCharvalue=charValue+randValue
print("随机生成的字母是:",chr(newCharvalue))

"""
ord()函数
unicode与文本的翻译
"""
A=input("输入随便一个字母:")
print(ord(A))
"""
chr()函数
随便一个字的Unicode+9的字母是哪个
"""
ch=input("unicode里的随便一段数字:")
chValue=ord(ch)
newCh=chr(chValue+9)
print(newCh)

"""
例题3.9
"""
cnm=input("随便一个英语字母:")
chValue=ord(cnm)
ri=chr(chValue+32)
print(ri)

"""
连接字符串
"""
hao=input("请输入学号:")
ming=input("请输入名字:")
message="学号为"+hao+"的"+ming+"你好"
print(message)

"""
例题3.12
"""
print("hello")
print("world")
print("hello",end="")
print("world")
print("hello",end="***")
print("world")

"""
例题3.13
连接字符串与数字
"""
celcius=eval(input("请输入摄氏温度:"))
fahrenheit=round(32+celcius*(9/5),2)
message="转换为华氏温度为:"+str(fahrenheit)
print(message)





"""
课后1
"""
str1="Hello"
str2="worldeer"
message=str1+str2
print(message)

"""
2
"""
G=input("输入一个字符:")
print(ord(G))

"""
3
"""
unicode_div="\u00F7"
print(unicode_div)
"""
4
"""
ch=input("unicode里的随便一段数字:")
chValue=ord(ch)
newCh=chr(chValue+7)
print(newCh)

"""
5
"""
a=input("输入单价:")
b=input("输入总量:")
total=int(str(a*b))
print("总价格为:",total)

"""
7
"""
num1=float(input("输入第一个数:"))
num2=float(input("输入第二个数:"))
result=num1/num2
print("两数相除的结果为:",result)